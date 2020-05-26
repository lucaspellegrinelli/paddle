<template>
  <div class="informe_item">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
            <Informe :post_info="post" :esconder_texto="esconder_texto" v-if="this.post!=undefined"/>
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
  name: 'InformeItem',
  components: {
    Informe
  },
  props: ['id','post'],
  data() {
    return {
      esconder_texto: false
    }
  },
  created() {
    if (this.post == undefined)
      this.get_post();
  },
  methods: {
    get_post() {
      axios.get(`/api/informes/${this.id}`)
      .then(resposta => {
        this.post = resposta.data.conteudo;
      })
      .catch(erro => {
        if(erro.response.status == 404){
          //TODO: Exibir view de NotFound sem redirecionar
          this.$router.replace({ name: 'NotFound' });
        }
        else{
          alert(erro);
        }
      });
    }
  }
}
</script>

<style lang="scss">
.informe {
  padding-top: 30px;
}
</style>
