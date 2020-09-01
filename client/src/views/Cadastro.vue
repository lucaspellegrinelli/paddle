<template>
  <div class="cadastro">
    <h1>Formulário de cadastro (WIP)</h1>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <FormCadastro />
      </div>
    </div>
  </div>
</template>

<script>
import FormCadastro from "@/components/FormCadastro.vue";

export default {
  components: { FormCadastro }
};
</script>

<style lang="scss">
.cadastro {
  padding-top: 30px;
}
</style>