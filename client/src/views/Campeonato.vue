<template>
  <div class="campeonato">
    <h1>Formulário de criação de campeonatos</h1>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <FormCampeonato />
      </div>
    </div>
  </div>
</template>

<script>
import FormCampeonato from "@/components/FormCampeonato.vue";

export default {
  components: { FormCampeonato },
  beforeMount() {
    // Essa rota é protegida, e requer conta de administrador
    if (!this.$root.logado || !this.$root.admin) {
      this.$router.push("login");
    }
  }
};
</script>

<style lang="scss">
.campeonato {
  padding-top: 30px;
}
</style>