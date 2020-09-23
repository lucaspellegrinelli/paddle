<template>
  <b-form>


    <b-form-group
      id="input-partida"
      label="Número do capeonato:"
      label-for="input-partida"
      invalid-feedback="A partida deve ter um campeonato correspondente"
    >

     <b-form-input
        id="input-partida"
        v-model="form.partida"
        :options="form.optionsp"
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-jogador1"
      label="Jogador 1:"
      label-for="jogador1"
    >

     <b-form-input
        id="jogador1"
        v-model="form.jogador1"
        :options="form.optionsj1"
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-jogador2"
      label="Jogador 2:"
      label-for="jogador2"
    >

     <b-form-input
        id="jogador2"
        v-model="form.jogador2"
        :options="form.optionsj2"
      ></b-form-input>
    </b-form-group>

    
    <b-form-group
      id="input-vencedor"
      label="Vencedor:"
      label-for="vencedor"
    >

     <b-form-select
        id="vencedor"
        v-model="form.vencedor"
        :options="form.optionsv"
      ></b-form-select>
    </b-form-group>      

    <b-button variant="primary" @click="salvar">Salvar</b-button>&nbsp;
    <b-alert show variant="primary" v-model="salvo">Partida salva</b-alert>
    
  </b-form>
</template>


<script>

export default {
  name: "FormPartida",
  data() {
    return {
      form: {
        partida: "",
        jogador1: "",
        jogador2: "",
        vencedor: "",
        optionsv: [
            {value: 1, text: "Jogador 1"}, {value: -1, text: "Jogador 2"} 
        ],
        },
      show: true
    };
  },
    
    salvar() {
      var payload = {};

      payload.id_camp = this.form.partida;
      payload.id_atleta1 = this.form.jogador1;
      payload.id_atleta2 = this.form.jogador2;
      payload.resultado = this.form.vencedor;
      
      var ctx = this;
      axios 
        .post("/api/criar_partida", payload)
        .then(_ => {
          ctx.salvo = true;
        })
        .catch(erro => {
          alert(erro);
        });
    }
};

</script>