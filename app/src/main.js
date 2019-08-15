import Vue from 'vue'
import App from './App.vue'
import './styles/app.css'
import 'material-design-lite/material'
import 'material-design-lite/material.css'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
