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
    component: () => import('../views/InformesLista.vue')
  },
  //Tem que vir antes da rota 'Informe' para /novo nao ser entendido como uma id
  {
    path: '/informes/novo',
    name: 'InformeNovo',
    component: () => import('../views/InformeNovo.vue')
  },
  {
    path: '/informes/:id',
    name: 'Informe',
    component: () => import('../views/InformeItem.vue'),
    props: true
  },
  {
    path: '/informes/editar/:id',
    name: 'InformeEditar',
    component: () => import('../views/InformeEditar.vue'),
    props: true
  },
  {
    path: '/atletas',
    name: 'Atletas',
    component: () => import('../views/Atletas.vue')
  },
  {
    path: '/campeonatos',
    name: 'Campeonatos',
    component: () => import('../views/Campeonatos.vue')
  },
  {
    path: '/campInfo',
    name: 'CampInfo',
    component: () => import('../views/CampInfo.vue')
  },
  {
    path: '/ranking',
    name: 'Ranking',
    component: () => import('../views/Ranking.vue')
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
    path: '/campeonato',
    name: 'Campeonato',
    component: () => import('../views/Campeonato.vue')
  },
  {
    path: '/visualizarcampeonato',
    name: 'VisualizarCamp',
    component: () => import('../views/VisualizarCamp.vue')
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
