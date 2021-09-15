import {createStore} from "vuex"
import axios from "axios";
import * as util from '../util/constants'

const state = {
    images: [],
    image: {},
    error: null,
    success: null,
}, mutations = {
    SET_IMAGES(state, images) {
        state.images = images;
    },
    SET_ERROR(state, error) {
        state.error = error;
    }
}, actions = {
    loadImages({commit}) {
        axios.get(util.API_URL).then(response => {
            commit('SET_IMAGES', response.data);
        }).catch(err => {
            commit('SET_ERROR', err);
        });
    },
    async updateScore({commit}, data) {
        await axios.post(util.API_URL, data).then(response => {
            console.log(response);
            commit('SET_SUCCESS', response.data)
        }).catch(err => {
            commit('SET_ERROR', err);
        })
    }
};


export default createStore({
    state,
    actions,
    mutations
});
