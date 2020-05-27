<template>
  <div class="informe-editar">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <h3> Teste: Editar informe </h3>
          <h3> Futuramente rota protegida </h3>
          <FormInforme :post_edicao="this.post"/>
        </div>
      </div>
    </b-container>
  </div>
</template>


<script>
import FormInforme from "@/components/FormInforme.vue";

export default {
  components: { 
    FormInforme
  },
  props: ['post'],
  created() {
    if (!this.$root.admin) {
      this.$router.push("login");
    }
  }
}
</script>

<style lang="scss">
.informe-editar {
  padding-top: 30px;
}
</style>