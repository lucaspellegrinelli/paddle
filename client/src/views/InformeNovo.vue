<template>
  <div class="informe-novo">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
          <h3> Teste </h3>
          <h5> Futuramente rota protegida </h5>
          <FormInforme />
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
  }
}
</script>

<style lang="scss">
.informe-novo {
  padding-top: 30px;
}
</style>