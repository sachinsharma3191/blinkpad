import {createWebHistory, createRouter} from "vue-router";
import Images from '../components/Images';
import Image from '../components/Image';

const routes = [
    {
        path: "/",
        name: "Home",
        component: Images,
        children: [{
            path: "/:id",
            name: "About",
            component: Image,
        }]
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
