<template>
  <div class="ranking">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <h1 class="titulo"> Ranking </h1>
          <p class="sobre"> Veja a classificação dos Atletas da Federação Mineira de Tênis de Mesa </p> 
          <div style="text-align: left">

            <b-button size="sm" variant="dark" :pressed.sync="show_filtros">
              <b-icon icon="funnel-fill"></b-icon> Filtrar
            </b-button>

            <b-form @reset.prevent="onReset" v-if="show_filtros" class="justify-content-between" inline>
              <b-form-input v-model="filtros.nome" placeholder="Nome" class="my-2 col-sm-7"></b-form-input>
              <b-form-select v-model="filtros.categoria" :options="categorias" placeholder="categoria" class="my-2 col-sm-4">
                <template v-slot:first>
                  <b-form-select-option :value="null" disabled>Categoria</b-form-select-option>
                </template>
              </b-form-select>
              <b-form-checkbox v-model="filtros.federado" :unchecked-value="null"> Apenas federados </b-form-checkbox>
              <b-form-radio-group v-model="filtros.sexo">
                <spam>Sexo </spam> 
                <b-form-radio value="M">Masculino</b-form-radio>
                <b-form-radio value="F">Feminino</b-form-radio>
              </b-form-radio-group>
              <div class="botoes">
                <b-button type="reset" variant="danger" size="sm">Reset</b-button>
              </div>
            </b-form>

          </div>
          <div class="tabela">
            <b-table ref="table"
              striped
              hover 
              outlined
              :items="atletas_filtrados"
              :fields="campos"
              :current-page="pagina_atual"
              :per-page="por_pagina"
              :sort-by.sync="ordenar_por"
              :sort-desc.sync="ordem_decresc"
            >
            <template v-slot:cell(index)="data">
              {{ data.index + 1 }}
            </template>
            </b-table>
          </div>

          <b-pagination class="justify-content-center" v-model="pagina_atual" :total-rows="total_atletas" :per-page="por_pagina"/>
        
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  components: {},
  data() {
    return {
      atletas: [],
      categorias: [{ text: "Carregando categorias...", value: null, disabled: true }],
      campos: [{key: 'index', label:"Classificação"}, 'nome', 'sexo', 'categoria', 'federado', {key: 'pontuacao', label:"Pontuação"}],

      ordenar_por: 'pontuacao',
      ordem_decresc: true,
      pagina_atual: 1,
      por_pagina: 10,
      filtros: {
          nome: null,
          federado: null,
          sexo: null,
          categoria: null
      },
      show_filtros: false
    }
  },
  computed: {
    total_atletas(){
      return this.atletas.length;
    },
    atletas_filtrados(){
      let atletas = this.atletas;
      if (this.filtros.federado) {
         atletas = atletas.filter((a) => a.federado == true);
      }
      if (this.filtros.nome){
         atletas = atletas.filter((a) => a.nome.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").includes(this.filtros.nome));
      }
      if (this.filtros.sexo) {
         atletas = atletas.filter((a) => a.sexo == this.filtros.sexo);
      }
      if (this.filtros.categoria) {
         atletas = atletas.filter((a) => a.categoria == this.filtros.categoria);
      }
      return atletas;
    }
  },
  created() {
    this.getTodosAtletas();
    this.getCategorias();
  },
  watch: {
      filtros: {
          handler: function () {
            this.$refs.table.refresh()
          },
          deep: true
      }
  },
  methods: {
    onReset(){
      this.filtros = {
        nome: null,
        categoria: null,
        federado: null,
        sexo: null
      }
    },
    getTodosAtletas() {
      //TODO? Pegar somente atletas da pag atual em uma requisição e fazer uma req por pag?
      axios.get("/api/atletas")
      .then(resposta => {
        this.atletas = resposta.data.conteudo;
      })
      .catch(function(erro) {
        alert(erro);
      });
    },
    getCategorias() {
      axios
        .get("/api/categorias")
        .then(resposta => {
          var cats = resposta.data.conteudo;
          this.categorias = cats.map((cat_json) => cat_json.text)
        })
        .catch(erro => {
          alert(erro);
        });
    }      
  }
}
</script>

<style lang="scss">
.atletas {
  padding-top: 30px;
}

.tabela {
  margin-top: 30px;
}
</style>

