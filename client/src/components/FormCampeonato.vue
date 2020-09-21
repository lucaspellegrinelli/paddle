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
         placeholder="Escolha uma data"
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

    <b-button type="submit" variant="primary">Enviar</b-button>&nbsp;
    <b-button type="reset" variant="danger">Reset</b-button>
    
  </b-form>
</template>

<script>
import {
  required,
  minLength
} from "vuelidate/lib/validators";
const axios = require("axios");

export default {
  name: "FormCampeonato",
  data() {
    return {
      form: {
        campeonato: "",
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
          { value: '2', text: '2 competidores' },
        ],        
        comentarios: ""
      },
      show: true
    };
  },
  validations: {
    form: {
      nome: {
        required,
        minLength: minLength(1)
      },
      data: {
        required: ("data")
      }
    }
  },

  created(){
    this.getEstilo();
  },

  methods: {
    validar(nome) {
      let raiz = this.$v.form;
      let prop = nome.split(".").reduce((acc, parte) => acc[parte], raiz);
      const { $dirty, $error } = prop;
      return $dirty ? !$error : null;
    },
    getEstilo() {
      axios.get("/api/estilos").then(response => {
        this.estilos = response.data.conteudo;
        for(let i = 0; i < this.estilos.length; i++){
          this.estilos[i].value = this.estilos[i].id;
          this.estilos[i].text = this.estilos[i].estilo;
          delete this.estilos[i].id;
          delete this.estilos[i].estilo;
        }
        this.optionse = this.estilos;            
      })       
      .catch(function(error) {
        alert(error);
      });
    },
    // onSubmit() {
    //   this.$v.form.$touch();
    //   if (this.$v.form.$anyError) {
    //     return;
    //   }

    //   const payload = { ...this.form };

    //   alert(JSON.stringify(payload));
    //   axios
    //     .post("/api/campeonato", payload)
    //     .then(resposta => {
    //       alert(JSON.stringify(resposta));
    //     })
    //     .catch(erro => {
    //       alert(erro);
    //     });
    // },
    // onReset() {
    //   this.form = {
    //     nome: "",
    //     data: "",
    //     capacidade: null,
    //     optionsc: [
    //       { value: '0', text: 'Escolha uma opção' },
    //       { value: '2', text: '2 competidores' },
    //       { value: '4', text: '4 competidores' },
    //       { value: '8', text: '8 competidores' },
    //       { value: '16', text: '16 competidores'}
    //     ],
    //     estilo: null,
    //     optionse:
    //     comentarios: ""
    //     };
    //   this.$nextTick(() => {
    //     this.$v.$reset();
    //   });
    // }
  }
};
</script>
