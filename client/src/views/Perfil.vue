<template>
  <div class="perfil">
    <h3>Perfil do usuário</h3>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <p><b>Nome de usuário:</b> {{ dados.usuario }}</p>
        <p><b>ID:</b> {{ dados.id }}</p>
        <div v-if="dados.dados_atleta">
          <h4>Dados de atleta</h4>
          <b-alert v-if="dados.dados_atleta.federado" show>Esse atleta é federado</b-alert>
          <b-alert v-if="!dados.dados_atleta.federado" show>Esse atleta não é federado</b-alert>

          <p><b>Nome:</b> {{ dados.dados_atleta.nome }}</p>
          <p><b>Data de nascimento:</b> {{ dados.dados_atleta.nascimento }}</p>
          <p><b>Sexo:</b> {{ dados.dados_atleta.sexo == "F" ? "Feminino" : "Masculino" }}</p>
          
          <p><b>Categoria:</b> {{ dados.dados_atleta.categoria }}</p>
          <p v-if="dados.dados_atleta.pontuacao"><b>Pontuação:</b> {{ dados.dados_atleta.pontuacao }}</p>
        </div>

      </div>
    </div>
    <b-button size="sm" variant="outline-danger" v-on:click="logout">Logout</b-button>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      dados: {
        id: null,
        usuario: "",
        email: "",
        dados_atleta: null
      }
    };
  },
  methods: {
    logout() {
      axios
        .post("/api/logout")
        .then(_resposta => {
          this.$root.logado = false;
          this.$root.admin = false;
          this.$router.push("/");
        })
        .catch(erro => {
          alert(erro);
        });
    }
  },
  beforeMount() {    
    if (!this.$root.logado) {
      this.$router.push("login");
      return;
    }

    axios
      .get("/api/perfil")
      .then(resposta => {
        this.dados = resposta.data.conteudo;
      })
      .catch(_ => {
        this.$router.push("login");
      });
  }
};
</script>

<style lang="scss">
.perfil {
  padding-top: 30px;
}
</style>
