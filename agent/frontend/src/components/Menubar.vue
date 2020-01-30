<template>
  <v-navigation-drawer absolute touchless permanent value="true" :height="menuHeight">
    <v-layout align-center column fill-height>
      <v-flex
        v-for="item in items"
        :key="item.title"
        class="wt-flex v-btn pa-0 mt-0 primary"
        @click="$router.push(item.link)"
      >
        <div class="text-xs-center">
          <div v-if="item.icon">
            <img :src="item.icon" :alt="item.title" :class="img_class">
            <br>
          </div>
          <span :class="font_class" class="white--text">{{ item.title }}</span>
        </div>
      </v-flex>
    </v-layout>
  </v-navigation-drawer>
</template>

<script>

export default {
  data () {
    return {
      items: [
      ],
      img_class: 'wt-img',
      font_class: 'wt-menu-font',
      agency: null,
      menuHeight: '100%'
    }
  },
  watch: {
    agency () {
      this.refreshMenu()
    },
    '$i18n.locale': {
      handler () {
        this.refreshMenu()
      }
    }
  },
  beforeMount () {
    if (this.$store.state.kiosk === 'v2') {
      this.menuHeight = 1920 - 675
    }

    this.$store.watch(
      (state) => {
        return this.$store.state.agency // could also put a Getter here
      },
      (newValue, oldValue) => {
        this.agency = newValue
      },
      {
        deep: true
      }
    )
    this.refreshMenu()
  },
  methods: {
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    refreshMenu () {
      if (!this.agency) {
        return
      }
      this.items = []
      if (this.agency.menu_wash) {
        this.items.push({
          title: this.$t('menu.washer'),
          icon: require('@/assets/washer-reverse.png'),
          link: '/washer'
        })
      }
      if (this.agency.menu_dry) {
        this.items.push({
          title: this.$t('menu.dryer'),
          icon: require('@/assets/dryer-reverse.png'),
          link: '/dryer'
        })
      }
      if (this.agency.menu_shoes_wash) {
        this.items.push({
          title: this.$t('menu.shoes-washer'),
          icon: require('@/assets/washer-reverse.png'),
          link: '/shoes-washer'
        })
      }
      if (this.agency.menu_shoes_dry) {
        this.items.push({
          title: this.$t('menu.shoes-dryer'),
          icon: require('@/assets/dryer-reverse.png'),
          link: '/shoes-dryer'
        })
      }
      if (this.agency.menu_tromm) {
        this.items.push({
          title: this.$t('menu.airdresser'),
          icon: require('@/assets/washer-reverse.png'),
          link: '/styler'
        })
      }
      if (this.agency.menu_item) {
        this.items.push({
          title: this.$t('menu.supplies'),
          icon: require('@/assets/supplies-reverse.png'),
          link: '/supplies'
        })
      }
      if (this.agency.menu_air) {
        this.items.push({
          title: this.$t('menu.airconditioner'),
          icon: require('@/assets/airconditioner-reverse.png'),
          link: '/airconditioner'
        })
      }
      this.items.push({
        title: this.$t('menu.home'),
        link: '/'
      })
      if (this.items.length < 5) {
        this.img_class = 'wt-img-large'
        this.font_class = 'wt-menu-font-large'
      } else {
        this.img_class = 'wt-img'
        this.font_class = 'wt-menu-font'
      }
      if (this.$i18n.locale !== 'ko') {
        this.font_class += ' title'
      }
    }
  }
}
</script>

<style scoped>
.wt-flex {
  width: 100%;
  background: #b70501;
}
.v-navigation-drawer {
  width: 200px !important;
  top: auto !important;
}
.wt-img {
  width: 50%;
}
.wt-img-large {
  width: 80%;
}
.v-btn {
  width: 100%;
}
.wt-bottom-link {
  width: 100%;
}
.wt-menu-font {
  font-size: 2.2rem;
}
.wt-menu-font-large {
  font-size: 3rem;
}
</style>
