<template>
  <div class="informe-novo">
    <b-container>
      <div class="row justify-content-center">
        <div class="col-9 p-4">
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
  },
  created() {
    if (!this.$root.admin) {
      this.$router.push("login");
    }
  }
}
</script>

<style lang="scss">
.informe-novo {
  padding-top: 30px;
}
</style>