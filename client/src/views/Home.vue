<template>
  <div class="home">
    <b-container>
      <b-container>
        <h1 class="titulo"> Informes </h1>
        <b-card-group deck>
          <Informe v-for="post in ultimos_posts" :key="post.id" :post_info="post"/>
        </b-card-group>
        <b-button href="/informes" size="sm" variant="outline-dark" style="margin-top: 20px">
          Ver todos
        </b-button>&nbsp;
        <b-button v-on:click="publica_post" size="sm" variant="outline-dark" style="margin-top: 20px">
          Teste: Publicar post
        </b-button>
      </b-container>
      <b-container>
        <h1 class="titulo"> Ranking </h1>
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
      ultimos_posts: [],
      esconder_texto: true
    }
  },
  created(){
    this.get_posts_recentes();
  },
  methods: {
    get_posts_recentes() {
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
    publica_post() {
      axios.get("/api/publicar")
        .then(function(response) {
          alert(JSON.stringify(response));
        })
      .catch(function(error) {
        alert(error);
      });
    }
  }
}
</script>

<style scoped lang="scss">
@import '../assets/style/app.scss';

.home {
  padding-top: 30px;
}
</style>

