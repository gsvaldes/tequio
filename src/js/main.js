import Vue from 'vue'
import App from './App.vue'

Vue.prototype.vue_data = window.vue_data;

new Vue({
  el: '#app',
  render: h => h(App)
})
