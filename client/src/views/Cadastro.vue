<template>
  <div class="cadastro">
    <h1>Formulário de cadastro (WIP)</h1>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <b-form :novalidate="true" validated="true" @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group
            id="input-group-usuario"
            label="Nome de usuário:"
            label-for="input-usuario"
            invalid-feedback="Nome de usuário deve ter pelo menos 3 caracteres"
          >
            <b-form-input
              id="input-usuario"
              v-model="form.usuario"
              required
              minlength="3"
              placeholder="Usuário"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-senha"
            label="Senha:"
            label-for="input-senha"
            invalid-feedback="Senha deve ter pelo menos 8 caracteres"
          >
            <b-form-input
              id="input-senha"
              v-model="form.senha"
              type="password"
              required
              minlength="8"
              placeholder="Senha"
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Enviar</b-button>&nbsp;
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      form: {
        usuario: "",
        senha: ""
      },
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      axios
        .post("/api/cadastro", {
          usuario: this.form.usuario,
          senha: this.form.senha
        })
        .then(resposta => {
          alert(JSON.stringify(resposta));
        })
        .catch(erro => {
          alert(erro);
        });
    },
    onReset(evt) {
      evt.preventDefault();
      this.form.usuario = "";
      this.form.senha = "";
    }
  }
};
</script>

<style lang="scss">
.cadastro {
  padding-top: 30px;
}
</style>