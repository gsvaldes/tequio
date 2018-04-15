import Vue from 'vue'
import VueRouter from 'vue-router';
import App from './App.vue'
import { ClientTable, Event } from 'vue-tables-2';
import { routes } from './routes';

Vue.use(VueRouter);

const router = new VueRouter({
    routes
});

Vue.use(ClientTable, { theme: 'bootstrap4' });

Vue.prototype.initial_data = window.initial_data;

new Vue({
    el: '#app',
    router,
    render: h => h(App)
})