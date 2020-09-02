<template>
  <b-form :novalidate="true" @submit="onSubmit">
    <b-form-group id="input-group-usuario">
      <b-form-input id="input-usuario" v-model="form.usuario" required placeholder="Usuário"></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-senha">
      <b-form-input
        id="input-senha"
        v-model="form.senha"
        type="password"
        required
        placeholder="Senha"
      ></b-form-input>
    </b-form-group>
    <div style="text-align: right">
      <b-button block type="submit" variant="primary">Enviar</b-button>
    </div>
  </b-form>
</template>

<script>
const axios = require("axios");

export default {
  name: "FormLogin",
  data() {
    return {
      form: {
        usuario: "",
        senha: ""
      }
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      axios
        .post("/api/login", {
          usuario: this.form.usuario,
          senha: this.form.senha
        })
        .then(_resposta => {
          // TODO: retornar dados de sessão (logado, admin) do endpoint "/api/login"
          // para que essa chamada a `atualizarSessao` não seja necessária
          this.$root
            .atualizarSessao()
            .then(() => {
              this.$router.push("perfil");
            });
        })
        .catch(erro => {
          alert(erro);
        });
    }
  }
};
</script>

<style lang="scss">
.login {
  padding-top: 30px;
}
</style>