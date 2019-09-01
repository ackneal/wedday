import Vue from 'vue'
import store from './store'
import router from './router'
import App from './App.vue'
import './styles/app.css'
import socket from './socket'

Vue.config.productionTip = false
Vue.prototype.$socket = socket

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
