<template>
  <b-card :header="post_info.data">
    <b-card-title><a href="#" class="card-link"> {{post_info.titulo}} </a></b-card-title>
    <b-card-text> {{post_info.corpo}} </b-card-text>
  </b-card>
</template>

<script>
export default {
  name: 'Informe',
  props: ['post_info']
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
