<template>
  <div>
    <b-navbar toggleable="md" type="dark" variant="dark" id="navbar">
      <b-navbar-brand href="/">
        <img src="../assets/images/navicon.svg" alt="Paddle" />
        <img src="../assets/images/navicon-hover.svg" class="hover" alt="Paddle" />
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/sobre">Sobre</b-nav-item>
          <b-nav-item to="/informes">Informes</b-nav-item>
          <b-nav-item to="/atletas">Atletas</b-nav-item>
          <b-nav-item to="/campeonatos">Campeonatos</b-nav-item>
          <b-nav-item to="/ranking">Ranking</b-nav-item>
          <b-nav-item v-b-modal.modal-login  v-if="!this.$root.logado">Login</b-nav-item>
          <b-nav-item to="/cadastro" v-if="this.$root.logado && this.$root.admin">Cadastro</b-nav-item>
          <b-nav-item to="/campeonato" v-if="this.$root.logado && this.$root.admin">Criar Campeonato</b-nav-item>          
          <b-nav-item to="/partidas" v-if="this.$root.logado && this.$root.admin">Adicionar Partida</b-nav-item>      
          <b-nav-item-dropdown right v-if="this.$root.logado">
            <template v-slot:button-content>
              <b-icon icon="person-fill"></b-icon>
            </template>
            <b-dropdown-item to="/perfil">Perfil</b-dropdown-item>
            <b-dropdown-item v-on:click="logout">Sair</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <b-modal id="modal-login" size="sm" :hide-footer="true" title="Login">
      <FormLogin />
    </b-modal>
  </div>
</template>

<script>
import FormLogin from "@/components/FormLogin.vue";
const axios = require("axios");

export default {
  name: "Navbar",
  components: { FormLogin },
  methods: {
    logout() {
      axios
        .post("/api/logout")
        .then(_resposta => {
          this.$root.logado = false;
          this.$root.admin = false;
          this.$router.push("/");
        })
        .catch(erro => {
          alert(erro);
        });
    }
  }
};
</script>

<style lang="scss">
@import "../assets/style/custom.scss";

a {
  outline: 0;
}

.navbar {
  -webkit-box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.3);
  -moz-box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.3);
  box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.3);
  height: $nav-height;
}

.navbar-brand .hover {
  transition: 0.5s;
  position: absolute;
  opacity: 0;
  left: 16px;
}

.navbar-brand:hover .hover {
  opacity: 100%;
}

.nav-item {
  top: 50%;
  outline: none;
  padding: 5px;
  height: $nav-height;

  a:hover,
  a:active {
    color: white;
    transition: 0.3s;
  }
}

.navbar,
.nav-item,
.navbar-brand {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.nav-item .dropdown-menu a:hover,
a:active {
  color: black;
}
</style>
