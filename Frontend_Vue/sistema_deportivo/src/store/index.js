import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    partidos: [],
    equipos: [],
    partidoSeleccionado: {},
    datosCargados: false,
  },
  mutations: {
    updatePartidos(state, payload) {
      state.partidos = payload.newPartidos
    },
    updateEquipos(state, payload) {
      state.equipos = payload.newEquipos
    },
  },
  actions: {
  },
  modules: {
  }
})
