<template>
  <div class="atletas">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <h1 class="titulo"> Atletas </h1>
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
            <b-table
              striped
              hover 
              outlined
              :items="atletas"
              :fields="campos"
              :current-page="pagina_atual"
              :per-page="por_pagina"
              :sort-by.sync="ordenar_por"
              :sort-desc.sync="ordem_decresc"
              :filter="filtros.nome"
              :filterIncludedFields="filtros.categoria"
              @filtered="onFiltered"
            > 
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
      ordenar_por: 'Nome',
      ordem_decresc: false,
      pagina_atual: 1,
      por_pagina: 10,
      filtros: {
          nome: null,
          categoria: null,
          federado: null,
          sexo: null
      },
      show_filtros: false
    }
  },
  computed: {
    total_atletas(){
      return this.atletas.length;
    }
  },
  created() {
    this.getTodosAtletas();
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
    onFiltered(_) {
      this.pagina_atual = 1
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

