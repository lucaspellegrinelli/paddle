<template>
  <b-form>
    <b-form-group
      id="input-group-nome"
      label="Nome do campeonato:"
      label-for="input-nome"
      invalid-feedback="O nome do Campeonato não deve ser vazio"
    >
    <b-form-input
        id="input-nome"
        v-model="form.nome"
        placeholder="Nome"
      ></b-form-input>
    </b-form-group>

   <b-form-group
       id="input-group-data"
       label="Data:"
       label-for="input-data"
       invalid-feedback="Selecione uma data"
     >
      <b-form-datepicker
         id="input-data"
         v-model="form.data"
         placeholder="Escolha uma data"
         value-as-date
       ></b-form-datepicker>
     </b-form-group>

    <b-form-group
      id="input-group-capacidade"
      label="Número máximo de inscrições permitidas:"
      label-for="input-capacidade"
    >

     <b-form-select
        id="input-capacidade"
        v-model="form.capacidade"
        :options="form.optionsc"
      ></b-form-select>
    </b-form-group>

    <b-form-group
      id="input-group-estilo"
      label="Estilo da competição:"
      label-for="input-estilo"
    >

     <b-form-select
        id="input-estilo"
        v-model="form.estilo"
        :options="form.optionse"
      ></b-form-select>
    </b-form-group>    

    <b-form-group
      id="input-group-comentarios"
      label="Comentários:"
      label-for="input-comentarios"
    >

    <b-form-input
        id="input-comentarios"
        v-model="form.comentarios"
        placeholder="texto"
      ></b-form-input>
    </b-form-group>

    <b-button variant="primary" @click="salvar">Salvar</b-button>&nbsp;
    <b-alert show variant="primary" v-model="salvo">Campeonato salvo</b-alert>
    
  </b-form>
</template>

<script>
// import {
//   required,
//   minLength
// } from "vuelidate/lib/validators";

const axios = require("axios");

export default {
  name: "FormCampeonato",
  data() {
    return {
      form: {
        nome: "",
        data: "",
        capacidade: null,
        optionsc: [
          { value: '2', text: '2 competidores' },
          { value: '4', text: '4 competidores' },
          { value: '8', text: '8 competidores' },
          { value: '16', text: '16 competidores'}
        ],
        estilo: null,
        optionse: [
          { value: '0', text: 'Grupos' },
          { value: '1', text: 'Mata-mata' },
        ],        
        comentarios: "",
      },
      salvo: false,
      show: true
    };
  },
  // validations: {
  //   form: {
  //     nome: {
  //       required,
  //       minLength: minLength(1)
  //     },
  //     data: {
  //       required: ("data")
  //     }
  //   }
  // },

  methods: {
    validar(nome) {
      let raiz = this.$v.form;
      let prop = nome.split(".").reduce((acc, parte) => acc[parte], raiz);
      const { $dirty, $error } = prop;
      return $dirty ? !$error : null;
    },
    salvar() {
      var payload = {};

      payload.nome = this.form.nome;
      payload.data = this.form.data.getTime();
      payload.capacidade = this.form.capacidade;
      payload.estilo = this.form.estilo;
      payload.comentarios = this.form.comentarios;
      
      var ctx = this;
      axios 
        .post("/api/criar_camp", payload)
        .then(_ => {
          ctx.salvo = true;
        })
        .catch(erro => {
          alert(erro);
        });
    }
  }
};
</script>
