import Vue from 'vue'
import VueRouter from 'vue-router';
import App from './App.vue'
import { ClientTable, Event } from 'vue-tables-2';
import { routes } from './routes';
import './filters.js';

Vue.use(VueRouter);

const router = new VueRouter({
    routes
});

Vue.use(ClientTable, { theme: 'bootstrap4' });

Vue.prototype.initialData = window.initialData;

new Vue({
    el: '#app',
    router,
    render: h => h(App)
})