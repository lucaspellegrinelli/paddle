<template>
  <b-card :header="post_info.data">
    <div class="text-right my-2">
      <b-button :to="{ name: 'InformeEditar', params: { id: this.post_info.id, post: this.post_info }}" 
      size="sm" variant="light" v-if="this.$root.logado && this.$root.admin">
        <b-icon icon="pencil"></b-icon> Editar
      </b-button>&nbsp;
      <b-button @click="showMsgBoxDelete" size="sm" variant="light" v-if="this.$root.logado && this.$root.admin">
        <b-icon icon="trash"></b-icon> Excluir
      </b-button>
    </div>
    <b-card-title>
      <b-link :to="{ name: 'Informe', params: { id: this.post_info.id, post: this.post_info }}" class="card-link">
        {{post_info.titulo}}
      </b-link>
    </b-card-title>
    <b-card-text> {{corpo_post}} </b-card-text>
    <div class="text-right" v-if="this.esconder_texto">
      <b-link :to="{ name: 'Informe', params: { id: this.post_info.id, post: this.post_info }}">
        Leia Mais
      </b-link>
    </div>
  </b-card>
</template>

<script>
const axios = require("axios");

export default {
  name: 'Informe',
  props: ['post_info', 'esconder_texto'],
  computed: {
    corpo_post() {
      if (this.esconder_texto && this.post_info.corpo.length > 170)
        return this.post_info.corpo.slice(0,170)+"...";
      return this.post_info.corpo;
    }
  },
  methods: {
    showMsgBoxDelete() {
      if (!this.$root.admin) {
        this.$router.push("login");
        return;
      }
      this.$bvModal.msgBoxConfirm('Deseja deletar o seguinte informe? \n' + this.post_info.titulo)
      .then(value => {
        if(value==true){
          axios
            .delete(`/api/informes/${this.post_info.id}`)
            .then(resposta => {
              if(resposta.status == 200){
                this.$bvModal.msgBoxOk("Informe deletado com sucesso")
                .then(_ => {
                  this.$router.go();
                });
              }
            })
            .catch(erro => {
              alert(erro);
            });
        }    
      });
    }
  }
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
