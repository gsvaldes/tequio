import Vue from 'vue'
import App from './App.vue'
import { ClientTable, Event } from 'vue-tables-2';

// TODO move vue-tables import and Vue.use to App component
// Vue.use(ClientTable);
Vue.use(ClientTable, { theme: 'bootstrap4' });

Vue.prototype.initial_data = window.initial_data;

new Vue({
  el: '#app',
  render: h => h(App)
})
