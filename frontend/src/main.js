import Vue from 'vue'
import store from './store'
import router from './router'
import App from './App.vue'
import './styles/app.css'
import 'material-design-lite/material'

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
