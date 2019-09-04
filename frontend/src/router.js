import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  { path: '/slide', component: () => import('./components/Slide.vue') },
  { path: '/new', component: () => import('./components/Create.vue') },
  { path: '*', component: () => import('./components/Index.vue') }
]

export default new VueRouter({
  mode: 'history',
  routes
})
