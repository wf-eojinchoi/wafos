<template>
  <div>
    <v-layout wrap pt-2 class="hidden-md-and-down">
      <v-flex xs4>
        <div class="logo_area">
          <router-link to="/"><img src="/logo.png" alt="헤더로고"></router-link>
        </div>
      </v-flex>
      <v-flex xs8>
        <v-toolbar :class="toolbarClass" height="40">
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
              v-for="menu in menus"
              :key="menu.to"
              flat :to="menu.to" :class="toolbarItemClass">{{ menu.showtext }}</v-btn>
            <wise-button
              to="/start"
              color="#ee8537"
              textcolor="white">
              시작하기
            </wise-button>
          </v-toolbar-items>
        </v-toolbar>
      </v-flex>
    </v-layout>
    <v-layout wrap pt-2 class="hidden-lg-and-up" justify-space-between>
      <v-flex xs1 ma-4>
        <v-btn
          flat
          icon
          @click.stop="drawer = !drawer"
        >
          <v-icon x-large>menu</v-icon>
        </v-btn>
        <v-navigation-drawer
          v-model="drawer"
          absolute
          temporary>
          <v-list class="pt-0" dense>
            <v-divider light></v-divider>
            <v-list-tile
              v-for="menu in menus"
              :key="menu.to"
              :to="menu.to">
              <v-list-tile-content>
                <v-list-tile-title
                  class="black--text">{{ menu.showtext }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
      </v-flex>
      <v-flex xs4 sm3 md2>
        <router-link to="/"><v-img src="/logo.png" alt="헤더로고"></v-img></router-link>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import WiseButton from '@/components/WiseButton'

export default {
  name: 'WiseTopMenu',
  components: {
    WiseButton
  },
  props: {
    inverted: {
      type: Boolean,
      default: false
    }
  },
  mounted () {
    if (this.inverted) {
      this.toolbarClass = 'nav--inverted'
      this.toolbarItemClass = 'nav_menu--inverted'
    }
  },
  data () {
    return {
      drawer: false,
      menus: [
        { showtext: '브랜드', to: '/brand' },
        { showtext: '레시피', to: '/recipe' },
        { showtext: '리뷰', to: '/review' },
        { showtext: '커뮤니티', to: '/community' },
        { showtext: '뉴스', to: '/news' },
        { showtext: '블로그', to: '/blog' },
        { showtext: '로그인', to: '/login' }
      ],
      toolbarClass: 'nav',
      toolbarItemClass: 'nav_menu'
    }
  }
}
</script>

<style scoped>
.logo_area {
  float:left;
}

.logo_area img {
  width:150px;
  margin-left:100px;
}

.nav {
  background-color:#fede57 !important;
  box-shadow:none;
  padding-top:20px;
}

.nav_menu {
  font-size:18px;
  font-weight:bold;
  background:#fede57;
  color:#000;
}

.nav--inverted {
  background-color:#fff !important;
  box-shadow:none;
  padding-top:20px;
}

.nav_menu--inverted {
  font-size:18px;
  font-weight:bold;
  background:#fff;
  color:#000;
}

</style>
