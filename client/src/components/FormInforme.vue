<template>
    <div class="form-informe">
        <b-form @submit.prevent="showMsgBoxSave">
            <b-form-group 
                id="input-group-titulo"
                label-for="input-titulo"
            >
                <b-form-input
                    id="input-titulo"
                    v-model="form.titulo"
                    required
                    placeholder="Título"
                ></b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-corpo"
                label-for="input-corpo"
            >
                <b-form-textarea
                    id="input-corpo"
                    v-model="form.corpo"
                    rows="12"
                    no-resize
                    required
                    placeholder="Texto"
                ></b-form-textarea>
            </b-form-group>
            <b-button type="submit" variant="primary">Postar</b-button>&nbsp;
            <b-button @click="showMsgBoxCancel" variant="danger">Cancelar</b-button>
        </b-form>
    </div>
</template>

<script>
const axios = require("axios");

export default {
   name: "FormInforme", 
   data() {
        return {
            form: {
            titulo: '',
            corpo: ''
            }
        }
    },
    methods: {
        showMsgBoxSave() {
            this.$bvModal.msgBoxConfirm('Deseja publicar o informe?')
            .then(value => {
                if(value==true){
                    axios
                        .post("/api/publicar", this.form)
                        .then(resposta => {
                            if(resposta.status == 200){
                                this.$bvModal.msgBoxOk("Informe publicado com sucesso")
                                .then(_ => {
                                    this.$router.go(-1);
                                });
                            }
                        })
                        .catch(erro => {
                            alert(erro);
                        });
                }    
            });
        },
        showMsgBoxCancel() {
            this.$bvModal.msgBoxConfirm('Deseja abandonar esta página?')
            .then(value => {
                if(value==true){
                    this.$router.go(-1);
                }    
            });
        }
    }
}
</script>