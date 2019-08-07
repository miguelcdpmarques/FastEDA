import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        result: 'empty',
        filename: ''
    },
    actions: {
        upload({state, commit}, payload) {
            axios.post('http://0.0.0.0:8000/app/upload_csv', payload.formData, payload.config)
            .then(function (response) {
                console.log('SUCCESS!!');
                console.log(response.data)
                commit('updateFilename', response.data)
            })
            .catch(function () {
                console.log('FAILURE!!');
            });
        }
    },
    mutations: {
        updateData({state}, payload){
            state.result = payload
            console.log('Updated data')
        },
        updateFilename({state}, payload) {
            console.log('Running mutation')
            this.state.filename = payload
        }
    }   
})

export default store