import Vue from 'vue'
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import Vuelidate from 'vuelidate'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/style/custom.scss'

const axios = require("axios");

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(Vuelidate)

Vue.config.productionTip = false

new Vue({
  router,
  data: {
    logado: null,
    admin: null,
  },
  methods: {
    atualizarSessao() {
      return axios
        .get("/api/sessao")
        .then(resposta => {
          if (resposta.data.conteudo) {
            this.logado = resposta.data.conteudo.logado;
            this.admin = resposta.data.conteudo.admin;
          }
        });
    }
  },
  beforeMount() {
    this.atualizarSessao();
  },
  render: h => h(App),
}).$mount('#app')
