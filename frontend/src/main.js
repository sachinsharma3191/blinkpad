import {createApp} from 'vue'
import App from './App.vue'
import Vuetify from "vuetify";
import router from "./router/index";
import store from "./store/Image";

createApp(App).use(router).use(store).use(Vuetify).mount("#app");
