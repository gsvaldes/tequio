import List from './components/List.vue'
import Create from './components/Create.vue'
import Detail from './components/Detail.vue'
import Edit from './components/Edit.vue'
import Tags from './components/Tags.vue'

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
    },
    {
        path: '/edit/:id',
        component: Edit,
        name: 'edit'
     },
     {
        path: '/tags',
        component: Tags,
        name: 'tags'
    },
    {
        path: '*',
        redirect: { name: 'list'}
    },
];