import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import VueWebsocket from 'vue-websocket'
Vue.use(VueWebsocket, 'ws://localhost:4000')

Vue.use(Vuetify, {
  iconfont: 'fa',
  theme: {
    primary: '#b70501',
    secondary: '#C9E6FB'
  }
})
