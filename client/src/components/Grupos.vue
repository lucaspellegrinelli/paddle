<template>
	<div>
    <b-table striped hover :items="items"></b-table>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "Grupos",
  data() {
    return {
      items: []
    }
  },
  created() {
    this.get_vitorias();
  },
  methods: {
    get_vitorias() {
      var payload = {
        id_camp: 2
      }
      axios.post("/api/classificacao_camp", payload).then(response => {
      this.items = response.data.conteudo;
      for(let i = 0; i < this.items.length; i++){
        this.items[i].classificacao = (i + 1);
      }
      });
    }    
  }

}
</script>

<style lang="scss">
.row > [class^=col-], .row > .col{
	border: 1px solid #000;
}
</style>
