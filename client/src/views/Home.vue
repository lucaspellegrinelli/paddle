<template>
  <div class="home">
    <b-container>
      <b-container>
        <h1 class="titulo"> Informes </h1>
        <b-card-group deck>
          <Informe v-for="post in ultimos_posts" :key="post.id" :post_info="post" :esconder_texto="esconder_texto"/>
        </b-card-group>
        <b-button :to="'informes'" size="sm" variant="outline-dark" style="margin-top: 20px">
          Ver todos
        </b-button>
      </b-container>
      <b-container>
        <h1 class="titulo"> Ranking </h1>
        <img src="../assets/images/podio.png" alt="podio" width=360 height=240>
        <h2 class="posicao"> 1&ordm; lugar </h2>

        <template>
          <div class="table1">
            <b-table ref="table1" striped hover :fields="campos" :items="items1"></b-table>
          </div>
        </template>

        <h2 class="posicao"> 2&ordm; lugar </h2>

        <template>
          <div class="table2">
            <b-table ref="table2" striped hover :fields="campos" :items="items2"></b-table>
          </div>
        </template>

        <h2 class="posicao"> 3&ordm; lugar </h2>

        <template>
          <div class="table3">
            <b-table ref="table3" striped hover :fields="campos" :items="items3"></b-table>
          </div>
        </template>
    
        <b-button :to="'ranking'" size="sm" variant="outline-dark" style="margin-top: 20px">
          Ver todos
        </b-button>
      </b-container>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Informe from '@/components/Informe.vue'

const axios = require("axios");

export default {
  name: 'Home',
  components: {
    Informe
  },
  data() {
    return {
      atletas: [],

      ultimos_posts: [],
      esconder_texto: true,
        
        campos: ['nome'],

        items1: [],

        items2:[],

        items3:[]
    }
  },

  created(){
    this.getPostsRecentes();
  
    this.getTodosAtletas();
  },
  methods: {
    getPostsRecentes() {
      axios.get("/api/informes", {
        params: {
          limite: 3
        }
      })
      .then(response => {
        this.ultimos_posts = response.data.conteudo;
      })
      .catch(function(error) {
        alert(error);
      });
    },
        getTodosAtletas() {
      //TODO? Pegar somente atletas da pag atual em uma requisição e fazer uma req por pag?
      axios.get("/api/atletas")
      .then(resposta => {
        this.atletas = resposta.data.conteudo;
        this.atletas.sort((a, b) => { return b.pontuacao - a.pontuacao});
        this.items1 = [this.atletas[0]];
        this.items2 = [this.atletas[1]];
        this.items3 = [this.atletas[2]];
      })
      .catch(function(erro) {
        alert(erro);
      });
    },

  }

}
</script>

<style scoped lang="scss">
@import '../assets/style/app.scss';

.home {
  padding-top: 30px;
  padding-bottom: 30px;
}
</style>

