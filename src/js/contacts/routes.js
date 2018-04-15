import List from './components/List.vue'
import Create from './components/Create.vue'
import Detail from './components/Detail.vue'

export const routes = [
    { 
        path: '',
        component: List,
        name: 'list'
     },
    { 
        path: '/create',
        component: Create,
        name: 'create'
     },
    { 
        path: '/detail/:id',
        component: Detail,
        name: 'detail'
     }
];