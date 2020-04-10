<template>
  <div class="home">
    <b-container>
      <b-container>
        <h1 class="titulo"> Informes </h1>
        <b-card-group deck>
          <Informe v-for="post in ultimos_posts" :key="post.id" :post_info="post"/>
        </b-card-group>
        <b-button href="#" size="sm" variant="outline-dark" style="margin-top: 20px">
          Ver todos
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
      ultimos_posts: []
    }
  },
  created(){
    this.get_recent_posts();
  },
  methods: {
    get_recent_posts() {
      axios.get("/api/home")
      .then(response => {
        this.ultimos_posts = response.data.ultimos_3_posts;
      })
      //.catch(function(error) {
      //  alert(error);
      //});
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

