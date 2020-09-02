<template>
  <div class="perfil">
    <h3>Perfil do usuário</h3>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <p>Nome de usuário: {{ nome_usuario }}</p>
        <p>ID: {{ id }}</p>
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
      nome_usuario: "",
      id: "",
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
        this.id = resposta.data.conteudo.id;
        this.nome_usuario = resposta.data.conteudo.usuario;
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
