import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    phone: null,
    agency: {},
    devices: {},
    user: {},
    kiosk: null,
    youtube: '',
    noaction: 0,
    pause: false,
    noActionInterval: null
  },
  mutations: {
    statePhone (state, value) {
      state.phone = value
    },
    stateAgency (state, value) {
      state.agency = value
    },
    stateUser (state, value) {
      state.user = value
    },
    stateDevices (state, value) {
      state.devices = value
    },
    stateKiosk (state, _value) {
      state.kiosk = _value
    },
    stateYoutube (state, _value) {
      state.youtube = _value
    },
    stateNoAction (state, _value) {
      state.noaction = _value
    },
    statePause (state, _value) {
      state.pause = _value
    },
    noActionInterval (state, _value) {
      state.noActionInterval = _value
    }
  },
  actions: {},
  getters: {
    isV2 (state) {
      return state.kiosk === 'v2'
    },
    isNoAction (state) {
      return state.noaction <= 0
    }
  }
})
