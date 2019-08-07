import Import from './components/app/Import/Import.vue'
import Visualization from './components/app/Visualization/Visualization.vue'

export const routes = [
    {path: '/', redirect: '/import'},
    {path: '/import', component: Import, name: 'import'},
    {path: '/visualization', component: Visualization, name: 'visualization'},
]
