<template>
  <div class="profile">
    <h3>Perfil do usuário</h3>
    <div class="row justify-content-center">
      <div class="col-4 text-left">
        <p>Nome de usuário: {{ name }}</p>
        <p>ID: {{ id }}</p>
      </div>
    </div>
    <b-button size="sm" variant="outline-danger" v-on:click="logout">Logout</b-button>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      name: "",
      id: "",
    };
  },
  methods: {
    logout() {
      axios
        .post("/api/logout")
        .then(_response => {
          this.$router.push("/");
        })
        .catch(error => {
          alert(error);
        });
    }
  },
  beforeMount() {
    axios
      .get("/api/profile")
      .then(response => {
        this.name = response.data.data.username;
        this.id = response.data.data.id;
      })
      .catch(error => {
        if (error.response && error.response.status === 401) {
          this.$router.push("login");
        }
      });
  }
};
</script>

<style lang="scss">
.profile {
  padding-top: 30px;
}
</style>
