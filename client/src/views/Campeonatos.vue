<template>
  <div class="campeonatos">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-12 p-4">
          <h1 class="titulo"> Campeonatos </h1>
          <div style="text-align: left">

            <b-button size="sm" variant="dark" :pressed.sync="show_filtros">
              <b-icon icon="funnel-fill"></b-icon> Filtrar
            </b-button>

            <b-form @reset.prevent="onReset" v-if="show_filtros" class="justify-content-between" inline>
              <b-form-input v-model="filtros.nome" placeholder="Nome" class="my-2 col-sm-7"></b-form-input>
            </b-form>

          </div>
          <div class="tabela">
            <b-table
              striped
              hover 
              outlined
              :items="campeonatos"
              :fields="campos"
              :current-page="pagina_atual"
              :per-page="por_pagina"
              :sort-by.sync="ordenar_por"
              :sort-desc.sync="ordem_decresc"
              :filter="filtros.nome"
              @filtered="onFiltered"
            > 
            </b-table>
          </div>

          <b-pagination class="justify-content-center" v-model="pagina_atual" :total-rows="total_campeonatos" :per-page="por_pagina"/>
        
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
      campeonatos: [],
      ordenar_por: 'Nome',
      ordem_decresc: false,
      pagina_atual: 1,
      por_pagina: 10,
      filtros: {
          nome: null
      },
      show_filtros: false
    }
  },
  computed: {
    total_campeonatos(){
      return this.campeonatos.length;
    }
  },
  created() {
    this.getTodosCampeonatos();
  },
  methods: {
    onReset(){
      this.filtros = {
        nome: null
      }
    },
    getTodosCampeonatos() {
      axios.get("/api/campeonatos")
      .then(resposta => {

        let format_date = function(date){
          let day = date.getDate().toString().padStart(2, '0');
          let month = (date.getMonth()+1).toString().padStart(2, '0');
          let year = date.getFullYear();
          return day + "/" + month + "/" + year;
        }

        const estilos = [
          "Estilo A", "Estilo B", "Estilo C"
        ]

        this.campeonatos = [];
        resposta.data.conteudo.forEach(camp => {
          let formatted_date = format_date(new Date(camp.data));

          this.campeonatos.push({
            "nome": camp.nome,
            "data": formatted_date,
            "capacidade": camp.capacidade,
            "estilo": estilos[camp.estilo],
            "comentarios": camp.comentarios
          });
        });
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

<style lang="scss"></style>

