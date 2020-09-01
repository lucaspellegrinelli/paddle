import Vue from 'vue'
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import Vuelidate from 'vuelidate'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/style/custom.scss'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(Vuelidate)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

