<template>
  <div class="informes">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <div class="row-2 my-3" v-for="post in posts_atuais" :key="post.id">
            <Informe :post_info="post" :esconder_texto="esconder_texto"/>
          </div>
          <b-pagination class="justify-content-center" v-model="pagina_atual" :total-rows="total_posts" :per-page="por_pagina">
          </b-pagination>
        </div>
      </div>
    </b-container>
    <router-view/>
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
      posts:[],
      pagina_atual: 1,
      por_pagina: 5,
      esconder_texto: true
    }
  },
  computed: {
    total_posts(){
      return this.posts.length;
    },
    posts_atuais() {
      return this.posts.slice((this.pagina_atual - 1) * this.por_pagina,
      this.pagina_atual * this.por_pagina);
    }
  },
  created() {
    this.get_posts();
  },
  methods: {
    get_posts() {
      axios.get("/api/informes")
      .then(response => {
        this.posts = response.data.conteudo;
      })
      .catch(function(error) {
        alert(error);
      });
    }
  }
}
</script>

<style lang="scss">
.informes {
  padding-top: 30px;
}
</style>

