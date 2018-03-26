import Vue from 'vue'
import App from './App.vue'


Vue.prototype.initialData = window.initialData;

new Vue({
    el: '#app',
    render: h => h(App)
})
