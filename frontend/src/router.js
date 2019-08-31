import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from './components/Index.vue'
import Slide from './components/Slide.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/slide', component: Slide },
  { path: '*', component: Index }
]

export default new VueRouter({
  mode: 'history',
  routes
})
