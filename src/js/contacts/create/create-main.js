import Vue from 'vue'
import App from './App.vue'


Vue.prototype.initial_data = window.initial_data;

new Vue({
    el: '#app',
    render: h => h(App)
})
