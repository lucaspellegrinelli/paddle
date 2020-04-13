import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sobre',
    name: 'Sobre',
    component: () => import('../views/Sobre.vue')
  },
  {
    path: '/informes',
    name: 'Informes',
    component: () => import('../views/Informes.vue'),
  },
  {
    path: '/informes/:id',
    name: 'Informe',
    component: () => import('../views/InformeItem.vue'),
    props: true
  },
  {
    path: '/campeonatos',
    name: 'Campeonatos',
    component: () => import('../views/Campeonatos.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/cadastro',
    name: 'Cadastro',
    component: () => import('../views/Cadastro.vue')
  },
  {
    path: '/perfil',
    name: 'Perfil',
    component: () => import('../views/Perfil.vue')
  },
  {
    path: '*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
