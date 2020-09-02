<template>
  <div class="login">
    <h3>Formulário de login (WIP)</h3>
    <div class="row justify-content-center mt-3">
      <div class="col-2 text-left">
        <FormLogin />
      </div>
    </div>
  </div>
</template>

<script>
import FormLogin from "@/components/FormLogin.vue";

export default {
  components: { FormLogin }
};
</script>

<style lang="scss">
.login {
  padding-top: 30px;
}
</style>