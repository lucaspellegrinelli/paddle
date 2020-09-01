<template>
  <div class="cadastro">
    <h1>Formulário de cadastro (WIP)</h1>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <b-form :novalidate="true" @submit="onSubmit" @reset="onReset" v-if="show">
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
            id="input-group-email"
            label="Email:"
            label-for="input-email"
          >
            <b-form-input
              id="input-email"
              v-model="form.email"
              type="email"
              placeholder="Email"
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

          <b-form-group id="input-group-admin">
            <b-form-checkbox v-model="form.admin">Esta conta é uma conta de administrador</b-form-checkbox>
          </b-form-group>

          <b-form-group id="input-group-atleta">
            <b-form-checkbox v-model="form.atleta">Esta conta representa um atleta</b-form-checkbox>
          </b-form-group>

          <b-form-group id="input-group-dados-atleta" label="Dados do atleta" label-size="lg" label-class="font-weight-bold"
 v-if="form.atleta">
            <b-form-group
              id="input-group-atleta-nome"
              label="Nome completo:"
              label-for="input-atleta-nome"
            >
              <b-form-input
                id="input-atleta-nome"
                v-model="form.dados_atleta.nome"
                required
                placeholder="Nome"
              ></b-form-input>
            </b-form-group>

            <b-form-group
              id="input-group-atleta-nascimento"
              label="Data de nascimento:"
              label-for="input-atleta-nascimento"
            >
              <b-form-datepicker
                id="input-atleta-nascimento"
                v-model="form.dados_atleta.nascimento"
                placeholder="Escolha uma data"
              ></b-form-datepicker>
            </b-form-group>

            <b-form-group id="input-group-atleta-federado">
              <b-form-checkbox
                v-model="form.dados_atleta.federado"
                :state="null"
              >Este atleta é federado</b-form-checkbox>
            </b-form-group>
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
        email: "",
        senha: "",
        admin: false,
        atleta: false,
        dados_atleta: {
          nome: "",
          nascimento: "",
          federado: false
        }
      },
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
      axios
        .post("/api/cadastro", this.form)
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