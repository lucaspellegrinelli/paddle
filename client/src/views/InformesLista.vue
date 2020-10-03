<template>
  <div class="informes-lista">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <h1 class="titulo"> Informes </h1>
          <b-button class='novo-informe' :to="'informes/novo'" size="sm" variant="dark" v-if="this.$root.logado && this.$root.admin">
            <b-icon icon="plus"></b-icon> Novo informe
          </b-button>
          <div class="row-2 my-3" v-for="post in posts_atuais" :key="post.id">
            <Informe :post_info="post" :esconder_texto="esconder_texto"/>
          </div>
          <b-pagination class="justify-content-center" v-model="pagina_atual" :total-rows="total_posts" :per-page="por_pagina"/>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Informe from '@/components/Informe.vue'

const axios = require("axios");

export default {
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
    this.getPosts();
  },
  methods: {
    getPosts() {
      axios.get("/api/informes")
      .then(resposta => {
        this.posts = resposta.data.conteudo;
      })
      .catch(function(erro) {
        alert(erro);
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

