<template>
  <b-form :novalidate="true" @submit.prevent="onSubmit" @reset.prevent="onReset">
    <b-form-group
      id="input-group-usuario"
      label="Nome de usuário:"
      label-for="input-usuario"
      invalid-feedback="Nome de usuário deve ter pelo menos 3 caracteres"
    >
      <b-form-input
        id="input-usuario"
        v-model="$v.form.usuario.$model"
        placeholder="Usuário"
        :state="validar('usuario')"
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-email"
      label="Email:"
      label-for="input-email"
      invalid-feedback="Insira um endereço de email válido"
    >
      <b-form-input
        id="input-email"
        v-model="$v.form.email.$model"
        type="email"
        placeholder="Email"
        :state="validar('email')"
      ></b-form-input>
    </b-form-group>

    <div class="row">
      <div class="col-md-6">
        <b-form-group
          id="input-group-senha"
          label="Senha:"
          label-for="input-senha"
          invalid-feedback="Senha deve ter pelo menos 8 caracteres"
        >
          <b-form-input
            id="input-senha"
            v-model="$v.form.senha.$model"
            type="password"
            placeholder="Senha"
            :state="validar('senha')"
          ></b-form-input>
        </b-form-group>
      </div>
      <div class="col-md-6">
        <b-form-group
          id="input-group-confirmar-senha"
          label="Confirmar senha:"
          label-for="input-confirmar-senha"
          invalid-feedback="Senhas não coincidem"
        >
          <b-form-input
            id="input-confirmar-senha"
            v-model="$v.form.confirmar_senha.$model"
            type="password"
            placeholder="Confirmar"
            :state="validar('confirmar_senha')"
          ></b-form-input>
        </b-form-group>
      </div>
    </div>
    <b-form-group id="input-group-admin">
      <b-form-checkbox v-model="form.admin">Esta conta é uma conta de administrador</b-form-checkbox>
    </b-form-group>

    <b-form-group id="input-group-atleta">
      <b-form-checkbox v-model="form.dados_atleta.atleta">Esta conta representa um atleta</b-form-checkbox>
    </b-form-group>

    <b-form-group
      id="input-group-dados-atleta"
      label="Dados do atleta"
      label-size="lg"
      label-class="font-weight-bold"
      v-if="form.dados_atleta.atleta"
    >
      <b-form-group
        id="input-group-atleta-nome"
        label="Nome completo:"
        label-for="input-atleta-nome"
        invalid-feedback="Insira um nome"
      >
        <b-form-input
          id="input-atleta-nome"
          v-model="$v.form.dados_atleta.nome.$model"
          placeholder="Nome"
          :state="validar('dados_atleta.nome')"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-atleta-nascimento"
        label="Data de nascimento:"
        label-for="input-atleta-nascimento"
        invalid-feedback="Insira uma data de nascimento"
      >
        <b-form-datepicker
          id="input-atleta-nascimento"
          v-model="$v.form.dados_atleta.nascimento.$model"
          placeholder="Escolha uma data"
          :state="validar('dados_atleta.nascimento')"
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group id="input-group-atleta-federado">
        <b-form-checkbox v-model="form.dados_atleta.federado">Este atleta é federado</b-form-checkbox>
      </b-form-group>
    </b-form-group>

    <b-button type="submit" variant="primary">Enviar</b-button>&nbsp;
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-form>
</template>

<script>
import {
  required,
  requiredIf,
  minLength,
  maxLength,
  email,
  sameAs
} from "vuelidate/lib/validators";
const axios = require("axios");

export default {
  name: "FormCadastro",
  data() {
    return {
      form: {
        usuario: "",
        email: "",
        senha: "",
        confirmar_senha: "",
        admin: false,
        dados_atleta: {
          atleta: false,
          nome: "",
          nascimento: "",
          federado: false
        }
      },
      show: true
    };
  },
  validations: {
    form: {
      usuario: {
        required,
        minLength: minLength(3)
      },
      email: {
        required,
        email
      },
      senha: {
        required,
        minLength: minLength(8),
        maxLength: maxLength(64)
      },
      confirmar_senha: {
        required,
        igualSenha: sameAs("senha")
      },
      dados_atleta: {
        nome: {
          required: requiredIf("atleta")
        },
        nascimento: {
          required: requiredIf("atleta")
        }
      }
    }
  },
  methods: {
    validar(nome) {
      // Caso `nome` seja uma propriedade aninhada (e.g. "dados_atleta.nascimento"), precisamos
      // separá-lo em partes e aprofundar no objeto usando essas partes.
      let raiz = this.$v.form;
      let prop = nome.split(".").reduce((acc, parte) => acc[parte], raiz);
      const { $dirty, $error } = prop;
      return $dirty ? !$error : null;
    },
    onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }

      // Estou criadno uma cópia do objeto `this.form` e deletando campos desnecessários
      const payload = { ...this.form };
      delete payload.confirmar_senha;
      if (this.form.dados_atleta.atleta) {
        delete payload.dados_atleta.atleta;
      } else {
        delete payload.dados_atleta;
      }

      alert(JSON.stringify(payload));
      axios
        .post("/api/cadastro", payload)
        .then(resposta => {
          alert(JSON.stringify(resposta));
        })
        .catch(erro => {
          alert(erro);
        });
    },
    onReset() {
      this.form = {
        usuario: "",
        email: "",
        senha: "",
        confirmar_senha: "",
        admin: false,
        dados_atleta: {
          atleta: false,
          nome: "",
          nascimento: "",
          federado: false
        }
      };
      this.$nextTick(() => {
        this.$v.$reset();
      });
    }
  }
};
</script>
