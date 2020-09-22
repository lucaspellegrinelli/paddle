<template>
  <div class="campeonatos">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-12 p-4">
          <h1 class="titulo"> Campeonatos </h1>
          <div style="text-align: left">
          </div>
          <div class="tabela">
            <b-table striped hover outlined
            :items="campeonatos"
            :fields="campos"
            @row-clicked="row_click_handler"></b-table>
          </div>      
        </div>
      </div>
    </b-container>

    <b-modal hide-footer size="lg" ref="campeonato-info-modal" v-bind:title="camp_info.titulo">
      <p>Data: {{ camp_info.data }}</p>
      <p>Participantes: {{ camp_info.participantes }} / {{ camp_info.capacidade }}</p>
      <p>Estilo: {{ camp_info.estilo }}</p>
      <p>Comentários: {{ camp_info.comentarios }}</p>
      <p v-if="camp_info.inscrito">Status inscrição: {{ camp_info.inscr_aprovada ? "Aprovada" : "Aprovação pendente" }}</p>

      <b-row>
        <b-col v-if="this.$root.logado && this.$root.admin">
          <b-button class="mt-3" variant="outline-secondary" block @click="gerenciar_camp">Gerenciar</b-button>
        </b-col>
        <b-col>
          <b-button class="mt-3" variant="outline-secondary" block @click="visualizar_camp">Visualizar</b-button>
        </b-col>
        <b-col v-if="this.$root.logado && camp_info.participantes < camp_info.capacidade">
          <b-button class="mt-3" variant="outline-success" block @click="inscrever_camp">{{ camp_info.inscrito ? "Desinscrever-se" : "Inscrever-se" }}</b-button>
        </b-col>
        <b-col>
          <b-button class="mt-3" variant="outline-danger" block @click="fechar_model">Fechar</b-button>
        </b-col>
      </b-row>
    </b-modal>

    <b-modal hide-footer size="md" ref="campeonato-edit-modal" title="Editar campeonato">
      <b-form>
        <b-form-group label="Nome do campeonato:">
          <b-form-input
            ref="edit-nome-camp"
            v-model="edit_info.titulo"
            type="text"
            placeholder="Digite um título"
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Data:">
          <b-form-datepicker
            ref="edit-data-camp"
            v-model="edit_info.data"
            class="mb-2"
            value-as-date
          ></b-form-datepicker>
        </b-form-group>

        <b-form-group label="Capacidade:">
          <b-form-select
            ref="edit-estilo-camp"
            v-model="edit_info.capacidade"
            :options="capacidades"
          ></b-form-select>
        </b-form-group>

        <b-form-group label="Estilo:">
          <b-form-select
            ref="edit-estilo-camp"
            v-model="edit_info.estilo"
            :options="estilos"
          ></b-form-select>
        </b-form-group>

        <b-form-group label="Comentários:">
          <b-form-textarea
            ref="edit-comentario-camp"
            v-model="edit_info.comentarios"
            placeholder="Digite algum comentário..."
            rows="3"
            max-rows="6"
          ></b-form-textarea>
        </b-form-group>

        <b-row>
          <b-col>
            <b-button class="mt-3" variant="outline-danger" block @click="close_editar">Fechar</b-button>
          </b-col>
          <b-col>
            <b-button class="mt-3" variant="outline-secondary" block @click="inscricoes_editar">Inscrições</b-button>
          </b-col>
          <b-col>
            <b-button class="mt-3" variant="outline-success" block @click="submit_editar">Salvar</b-button>
          </b-col>
        </b-row>
      </b-form>
    </b-modal>

    <b-modal hide-footer size="md" ref="gerenciar-inscricoes-modal" title="Gerenciar inscrições">
      <b-form-checkbox-group
        v-model="selected_subscriptions"
        :options="pending_subscriptions"
        stacked
      ></b-form-checkbox-group>

      <b-row>
        <b-col>
          <b-button class="mt-3" variant="outline-danger" block @click="fechar_inscricoes">Fechar</b-button>
        </b-col>
        <b-col>
          <b-button class="mt-3" variant="outline-success" block @click="salvar_inscricoes">Aprovar</b-button>
        </b-col>
      </b-row>
    </b-modal>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      camp_info: {
        id: 0,
        titulo: "",
        data: "",
        capacidade: 0,
        estilo: 0,
        comentarios: "",
        participantes: 0,
        inscrito: false,
        inscr_aprovada: false
      },
      edit_info: {
        titulo: "",
        data: "",
        capacidade: 0,
        estilo: 0,
        comentarios: ""
      },
      selected_subscriptions: [],
      pending_subscriptions: [],
      estilos: [
        { value: 1, text: "Mata-Mata" },
        { value: 2, text: "Grupos" },
      ],
      capacidades: [
        { value: 2, text: "2 competidores" },
        { value: 4, text: "4 competidores" },
        { value: 8, text: "8 competidores" },
        { value: 16, text: "16 competidores" }
      ],
      campeonatos: [],
      campos: ["nome", "data", "lotacao"]
    }
  },
  created() {
    this.getInscricoes();
    this.getTodosCampeonatos();
  },
  methods: {
    row_click_handler(_, index){
      this.$refs['campeonato-info-modal'].show();
      this.popular_modal(this.campeonatos[index]);
    },
    popular_modal(info){
      this.camp_info.id = info["id"];
      this.camp_info.titulo = info["nome"];
      this.camp_info.data = info["data"];
      this.camp_info.capacidade = info["capacidade"];
      this.camp_info.estilo = info["estilo"];
      this.camp_info.comentarios = info["comentarios"];
      this.camp_info.participantes = info["participantes"];
      this.camp_info.inscrito = false;
      
      this.inscricoes.forEach(insc => {
        if(this.camp_info.id == insc.id){
          this.camp_info.inscrito = true;
          this.camp_info.inscr_aprovada = insc.aprovado == 1;
          return;
        }
      });

      this.getParticipantes(info["id"]);
    },
    fechar_model(){
      this.$refs['campeonato-info-modal'].hide();
    },
    inscrever_camp(){
      axios.get("/api/perfil").then(resposta => {
        let payload = {
          "id_atleta": resposta.data.conteudo.id,
          "id_camp": this.camp_info.id,
        }

        if(this.camp_info.inscrito){
          axios.post("/api/desinscricao", payload).then(_ => {
            this.inscricoes = this.inscricoes.filter(i => i.id !== this.camp_info.id);
            this.camp_info.participantes--;
            this.fechar_model();
          }).catch(erro => {
            alert(erro);
          });
        }else{
          axios.post("/api/inscricao", payload).then(_ => {
            this.inscricoes.push({ "id": this.camp_info.id, "aprovado": 0 });
            this.camp_info.participantes++;
            this.fechar_model();
          }).catch(erro => {
            alert(erro);
          });
        }
      });
    },
    close_editar() {
      this.$refs['campeonato-edit-modal'].hide();
      this.$refs['campeonato-info-modal'].show();
    },
    submit_editar() {
      let payload = {
        "id": this.camp_info.id,
        "nome": this.edit_info.titulo,
        "data": this.edit_info.data.getTime(),
        "capacidade": this.edit_info.capacidade,
        "estilo": this.edit_info.estilo,
        "comentarios": this.edit_info.comentarios,
      }

      axios.post("/api/atualizar_campeonato", payload).then(() => {
        this.$refs['campeonato-edit-modal'].hide();
        this.getTodosCampeonatos();
      });
    },
    inscricoes_editar() {
      this.$refs['campeonato-edit-modal'].hide();
      this.$refs['gerenciar-inscricoes-modal'].show();
    },
    fechar_inscricoes() {
      this.$refs['gerenciar-inscricoes-modal'].hide();
      this.$refs['campeonato-edit-modal'].show();
    },
    salvar_inscricoes() {
      this.$refs['gerenciar-inscricoes-modal'].hide();

      let payload = {
        "ids": this.selected_subscriptions
      }

      axios.post("/api/aprovar_participantes", payload).then(() => {
        
      });
    },
    gerenciar_camp() {
      this.$refs['campeonato-info-modal'].hide();
      this.$refs['campeonato-edit-modal'].show();

      this.edit_info.titulo = this.camp_info.titulo;
      this.edit_info.data = this.camp_info.data;
      this.edit_info.capacidade = this.camp_info.capacidade;
      this.edit_info.estilo = this.camp_info.estilo;
      this.edit_info.comentarios = this.camp_info.comentarios;
    },
    getParticipantes(id_camp){
      let payload = {
        "id_camp": id_camp
      };

      axios.post("/api/participantes", payload).then(response => {
        this.pending_subscriptions = [];
        response.data.conteudo.forEach(item => {
          if(item.aprovado == 0){
            this.pending_subscriptions.push({
              value: item.id_atleta,
              text: item.nome_atleta
            });
          }
        });
      });
    },
    getTodosCampeonatos() {
      axios.get("/api/campeonatos").then(resposta => {
        this.campeonatos = [];
        resposta.data.conteudo.forEach(camp => {
          let date = new Date(0);
          date.setSeconds(camp.data + 24 * 60 * 60);

          this.campeonatos.push({
            "id": camp.id,
            "nome": camp.nome,
            "data": date,
            "capacidade": camp.capacidade,
            "estilo": camp.estilo,
            "comentarios": camp.comentarios,
            "participantes": camp.participantes,
            "lotacao": camp.participantes + "/" + camp.capacidade
          });
        });
      })
      .catch(function(erro) {
        alert(erro);
      });
    },
    getInscricoes(){
      axios.get("/api/perfil").then(resposta => {
        let payload = { "id_atleta": resposta.data.conteudo.id }
        axios.post("/api/inscricoes", payload).then(response => {
          this.inscricoes = response.data.conteudo;
        });
      });
    },
    // format_date(date){
    //   let day = date.getDate().toString().padStart(2, '0');
    //   let month = (date.getMonth() + 1).toString().padStart(2, '0');
    //   let year = date.getFullYear();
    //   return day + "/" + month + "/" + year;
    // }
  }
}
</script>

<style lang="scss">
  .table td{
    cursor: pointer;
  }
</style>

