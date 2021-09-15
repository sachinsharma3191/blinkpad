import {createApp} from 'vue'
import App from './App.vue'
import Vuetify from "vuetify";
import store from "./store/Image";

createApp(App).use(store).use(Vuetify).mount("#app");
