<template>
  <v-app>
    <!--  v-touch="{tap:actionDown}" or v-touch="{press:actionDown}" -->
    <v-container pa-0 my-0 fluid fill-height v-on="{mousedown:actionDown}">
      <v-layout wrap>
        <v-flex xs12 v-if="$store.state.kiosk === 'v2'">
            <div class="video-cover"></div>
            <div class="video-container">
              <iframe
                width="100%"
                :src="'https://www.youtube.com/embed/' + $store.state.youtube + '?controls=0&origin=http://127.0.0.1:4000&autoplay=1&loop=1&playlist='+$store.state.youtube"
                frameborder="0"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
              ></iframe>
          </div>
        </v-flex>
        <v-flex xs12 fill-height>
          <menubar :class="{ nodisplay: noMenubar }" />
          <v-container align-center justify-content-center px-0 pa-0 my-0 fluid :class="{ 'wt-container': !noMenubar }" fill-height>
            <v-layout wrap>
              <v-flex xs12>
                <v-layout
                  wrap
                  :class="{ nodisplay: noTopbar }"
                  pa-3
                  class="white--text text-xs-center wt-topbar-bg"
                >
                  <v-flex xs4 v-if="$store.state.user.hasOwnProperty('phone')">
                    <span class="headline">{{ $store.state.user.phone.slice(0, -4) + '****' }}</span>
                  </v-flex>
                  <v-flex xs4 v-if="$store.state.user.hasOwnProperty('money')">
                    <span
                      class="headline"
                    >{{ add_comma($store.state.user.money) }}{{ $t('app.money-unit') }} {{ $t('app.have') }}</span>
                  </v-flex>
                  <v-flex xs4 v-if="$store.state.user.hasOwnProperty('point')">
                    <span
                      class="headline"
                    >{{ add_comma($store.state.user.point) }}{{ $t('app.point-unit') }} {{ $t('app.have') }}</span>
                  </v-flex>
                  <v-flex xs4 v-if="$store.state.user.hasOwnProperty('point')">
                    <v-btn
                      class="wt-top-btn headline white--text"
                      color="#b70501"
                      to="/charge"
                    >{{ $t('app.do-save') }}</v-btn>
                  </v-flex>
                  <v-flex xs4 v-if="$store.state.user.hasOwnProperty('point')">
                    <v-btn
                      class="wt-top-btn headline white--text"
                      color="#b70501"
                      to="/history"
                    >{{ $t('app.usage') }}</v-btn>
                  </v-flex>
                  <v-flex xs4 v-if="$store.state.user.hasOwnProperty('point')">
                    <v-btn
                      class="wt-top-btn headline white--text clockdiv"
                      color="#b70501"
                    >{{ $t('menu.autologout') }} {{ $store.state.noaction }}{{$t('app.second')}}</v-btn>
                  </v-flex>
                  <v-flex xs12 v-if="!$store.state.user.hasOwnProperty('phone')">
                    <span class="display-1">{{ $t('app.guest') }}</span>
                  </v-flex>
                </v-layout>
              </v-flex>
              <v-flex xs12 fill-height>
                <v-layout wrap :class="noTopbar ? 'height-without-menu' : 'height-with-menu'">
                  <v-flex xs12 v-if="loading">
                    <v-layout class="text-xs-center" align-center justify-center row fill-height>
                      <v-flex xs12>
                        <v-progress-circular indeterminate color="primary"></v-progress-circular>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12 v-else>
                    <router-view/>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import Menubar from '@/components/Menubar'

export default {
  components: {
    Menubar
  },
  data () {
    return {
      noMenubar: false,
      noTopbar: false,
      noMenuViews: [
        'home', 'login-phone', 'login-password', 'language',
        'register-phone', 'register-password', 'info', 'init'
      ],
      noTopbarViews: [
        'home', 'login-phone', 'login-password', 'language',
        'register-phone', 'register-password', 'info', 'init'
      ],
      loading: false,
      noaction: 60,
      interval: null,
      tab: false
    }
  },
  created () {
    this.loading = true
    if (this.$router.currentRoute.name === null ||
      this.noMenuViews.includes(this.$router.currentRoute.name)) {
      this.noMenubar = true
    } else {
      this.noMenubar = false
    }

    if (this.$router.currentRoute.name === null ||
      this.noTopbarViews.includes(this.$router.currentRoute.name)) {
      this.noTopbar = true
    } else {
      this.noTopbar = false
    }
    console.log(window.screen.availHeight)
    if (window.screen.availHeight >= 1850) {
      this.$store.commit('stateKiosk', 'v2')
      console.log('use for v2')
    } else {
      this.$store.commit('stateKiosk', 'v1')
      console.log('use for v1')
    }

    this.$axios.get('/init')
      .then(() => {
        this.$axios.get('/build')
          .then((res) => {
            this.$store.commit('stateAgency', res.data.agency)
            this.$store.commit('stateDevices', res.data.devices)
            this.$store.commit('stateYoutube', res.data.youtube)    

            this.$router.beforeEach((to, from, next) => {
              if (to.name === 'home' || to.name === 'language') {
                this.$store.commit('stateUser', {})
              }
              if (this.noMenuViews.includes(to.name)) {
                this.noMenubar = true
              } else {
                this.noMenubar = false
              }
              if (this.noTopbarViews.includes(to.name)) {
                this.noTopbar = true
              } else {
                this.noTopbar = false
              }
              return next()
            })
            this.loading = false
          })
          .catch((res) => {
            if (res.response.data.err === 'expired') {
              this.$router.replace('/build-error-expired')
            } else {
              this.$router.replace('/build-error')
            }
            this.loading = false
          })
      })
      .catch(() => {
        this.$router.replace('/init')
        this.loading = false
      })
  }
  ,
  mounted () {
    this.$store.commit('stateNoAction', 60)
    this.$store.commit('statePause', false)
  },
  methods: {
    add_comma (x) {
      var data = Math.round(x)
      return data.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
    },
    actionDown (e) {
      this.$store.state.noaction = 60
    }
  }
}
</script>

<style>
#app {
  background: #fff;
  overflow-y: hidden;
  font-family: GoyangDeogyang !important;
}
#app * {
  user-select: none !important;
  -webkit-user-drag: none !important;
}
.wt-topbar-bg {
  background: #282828;
  /* position: absolute;
  left:0!important;
  bottom:0!important;
  z-index:9999; */
  /* min-width:100%!important; */
  /* width:100%!important */
}
.height-with-menu {
  height: 80%;
}
.height-without-menu {
  height: 100%;
}
.nodisplay {
  display: none !important;
}
img {
  height: 100%;
}
.wt-container {
  padding-left: 200px !important;
}
.wt-primary-font {
  color: #e4007f;
}
.wt-opacity-80 {
  opacity: 0.8;
}
.wt-opacity-50 {
  opacity: 0.5;
}
.wt-wave-bg {
  background-color: transparent !important;
  background: url("./assets/wave_bg_btn.png") no-repeat;
  background-position: center;
  background-size: cover;
}
.wt-prev-bg {
  background: #a9a9a9 !important;
}
.wt-btn {
  width: 90%;
  height: 80%;
}
.wt-top-btn {
  width: 90%;
  height: 50px;
}
.huge-btn {
  width: 90%;
  height: 300px;
}
/* .huge-btn img {
  width: 100% !important;
  height: auto;
} */
.wt-next-bg {
  background-color: transparent !important;
  background: url("./assets/wave_bg_btn.png") no-repeat;
  background-position: center;
  background-size: cover;
}
.wt-font-deogyang {
  font-family: GoyangDeogyang, sans-serif;
}

.wt-font-ilsan {
  font-family: GoyangIlsan, sans-serif;
}
.single-stepper {
  flex-basis: 100% !important;
}
@font-face {
  font-family: "GoyangIlsan";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/GoyangIlsan.woff")
    format("woff");
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: "GoyangDeogyang";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/GoyangDeogyang.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
.display-1 {
  font-family: GoyangIlsan !important;
}
.subheading,
.headline,
.display-2,
.display-3 {
  font-family: GoyangDeogyang !important;
}
.video-cover {
  position: absolute;
  z-index: 2000;
  top: 0;
  left: 0;
  width: 100%;
  padding-bottom: 56.25%;
}
.video-container {
  float: none;
  clear: both;
  width: 100%;
  position: relative;
  padding-bottom: 56.25%;
}
.video-container > iframe {
  pointer-events: none;
}
.wt-bottom-logo {
  width: 100%;
  height: auto;
}
iframe {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
}
</style>
