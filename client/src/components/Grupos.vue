<template>
	<div>
    <b-table striped hover :items="items"></b-table>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "Grupos",
  props: ['id'],
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
      axios.get(`/api/classificacao_camp/${this.id}`, ).then(response => {
        this.items = response.data.conteudo;

        this.items.sort(function(a, b){
          if(a.vitorias == b.vitorias) return 0;
          return a.vitorias < b.vitorias ? 1 : -1;
        });

        for(let i = 0; i < this.items.length; i++){
          this.items[i].classificacao = (i + 1);
        }
      });
    }    
  }

}
</script>