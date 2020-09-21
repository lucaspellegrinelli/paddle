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
      <p v-if="camp_info.inscrito">Status inscrição: {{ camp_info.inscr_aprovada ? "Aprovada" : "Em espera" }}</p>

      <b-row>
        <b-col v-if="this.$root.logado && this.$root.admin">
          <b-button class="mt-3" variant="outline-secondary" block @click="gerenciar_camp">Gerenciar</b-button>
        </b-col>
        <b-col>
          <b-button class="mt-3" variant="outline-secondary" block @click="visualizar_camp">Visualizar</b-button>
        </b-col>
        <b-col v-if="this.$root.logado && camp_info['participantes'] < camp_info['capacidade']">
          <b-button class="mt-3" variant="outline-success" block @click="inscrever_camp">{{ camp_info.inscrito ? "Desinscrever-se" : "Inscrever-se" }}</b-button>
        </b-col>
        <b-col>
          <b-button class="mt-3" variant="outline-danger" block @click="fechar_model">Fechar</b-button>
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
        estilo: "",
        comentarios: "",
        participantes: 0,
        inscrito: false,
        inscr_aprovada: false
      },
      campeonatos: [],
      campos: ["nome", "data"]
    }
  },
  created() {
    this.getTodosCampeonatos();
    this.getInscricoes();
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
    getTodosCampeonatos() {
      axios.get("/api/campeonatos")
      .then(resposta => {
        let format_date = function(date){
          let day = date.getDate().toString().padStart(2, '0');
          let month = (date.getMonth() + 1).toString().padStart(2, '0');
          let year = date.getFullYear();
          return day + "/" + month + "/" + year;
        }

        this.campeonatos = [];
        resposta.data.conteudo.forEach(camp => {
          let formatted_date = format_date(new Date(camp.data));

          this.campeonatos.push({
            "id": camp.id,
            "nome": camp.nome,
            "data": formatted_date,
            "capacidade": camp.capacidade,
            "estilo": camp.estilo,
            "comentarios": camp.comentarios,
            "participantes": camp.participantes
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
    }
  }
}
</script>

<style lang="scss">
  .table td{
    cursor: pointer;
  }
</style>

