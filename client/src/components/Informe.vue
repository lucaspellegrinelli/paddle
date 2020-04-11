<template>
  <b-card :header="post_info.data">
    <b-card-title><a href="#" class="card-link"> {{post_info.titulo}} </a></b-card-title>
    <b-card-text> {{corpo_post}} </b-card-text>
  </b-card>
</template>

<script>
export default {
  name: 'Informe',
  props: ['post_info', 'esconder_texto'],
  computed: {
     corpo_post() {
      if (this.post_info.corpo.length > 170)
        return this.post_info.corpo.slice(0,170)+"...";
      return this.post_info.corpo;
    }
  }
  /*methods: {
    redireciona_post(){
      this.$router.push({ path: "informes", params: { id: this.post_info.id }});
    }
  }*/
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import '../assets/style/custom.scss';
  
  .card-text{
    text-align: justify;
  }

  .card-header {
    padding: 0;
    color: $gray-600;
  }

  .card-link, .card-link:hover{
    color: inherit;
    text-decoration: inherit;
  }
  
</style>
