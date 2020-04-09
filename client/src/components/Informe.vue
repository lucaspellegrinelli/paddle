<template>
  <b-card :title="postData.title" :header="postData.date">
    <b-card-text> {{postData.body}} </b-card-text>
  </b-card>
</template>

<script>
export default {
  name: 'Informe',
  props: ['postData']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap.scss';
  
  .card-text{
    text-align: justify;
  }

  .card-header {
    padding: 0;
    color: $gray-600;
  }
  
</style>
