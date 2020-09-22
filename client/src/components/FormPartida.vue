<template>
  <b-form>


    <b-form-group
      id="input-partida"
      label="Número da partida:"
      label-for="input-partida"
    >

     <b-form-select
        id="input-partida"
        v-model="form.partida"
        :options="form.optionsp"
      ></b-form-select>
    </b-form-group>

    <b-form-group
      id="input-jogador1"
      label="Jogador 1:"
      label-for="jogador1"
    >

     <b-form-select
        id="jogador1"
        v-model="form.jogador1"
        :options="form.optionsj1"
      ></b-form-select>
    </b-form-group>

    <b-form-group
      id="input-jogador2"
      label="Jogador 2:"
      label-for="jogador2"
    >

     <b-form-select
        id="jogador2"
        v-model="form.jogador2"
        :options="form.optionsj2"
      ></b-form-select>
    </b-form-group>

    <p>
    <input
      v-model.number="placar1"
      type="number"
      name="placar1"
    > Placar 1 <br/>
    <input
      v-model.number="placar2"
      type="number"
      name="placar2"
    > Placar 2 <br/>
    </p>
      
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

    <b-button type="submit" variant="primary">Enviar</b-button>&nbsp;
    <b-button type="reset" variant="danger">Reset</b-button>
    
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
        optionsp: [
          { value: '1', text: 'Partida 1' },
          { value: '2', text: 'Partida 2' },
          { value: '3', text: 'Partida 3' },
          { value: '4', text: 'Partida 4' },
          { value: '5', text: 'Partida 5' },
          { value: '6', text: 'Partida 6' },
          { value: '7', text: 'Partida 7' },
          { value: '8', text: 'Partida 8' },
          { value: '9', text: 'Partida 9' },
          { value: '10', text: 'Partida 10' },
          { value: '11', text: 'Partida 11' },
          { value: '12', text: 'Partida 12' },
          { value: '13', text: 'Partida 13' },
          { value: '14', text: 'Partida 14' },
          { value: '15', text: 'Partida 15' }
        ],
        optionsj1: [
            {text: "Ana"}, {text: "Carlos"}, {text: "Barbara"}, {text: "Daniel"} 
        ],
        optionsj2: [
            {text: "Ana"}, {text: "Carlos"}, {text: "Barbara"}, {text: "Daniel"} 
        ],
        optionsv: [
            {text: "Ana"}, {text: "Carlos"}, {text: "Barbara"}, {text: "Daniel"} 
        ],
        placar1: 0,
        placar2: 0,
        },
      show: true
    };
  },}
</script>