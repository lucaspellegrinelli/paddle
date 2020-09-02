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
  components: { FormCadastro },
  beforeMount() {
    // Essa rota é protegida, e requer conta de administrador
    if (!this.$root.logado || !this.$root.admin) {
      this.$router.push("login");
    }
  }
};
</script>

<style lang="scss">
.cadastro {
  padding-top: 30px;
}
</style>