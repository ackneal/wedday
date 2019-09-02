import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from './components/Index.vue'
import Slide from './components/Slide.vue'
import Create from './components/Create.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/slide', component: Slide },
  { path: '/new', component: Create },
  { path: '*', component: Index }
]

export default new VueRouter({
  mode: 'history',
  routes
})
