<template>
  <v-container wrap fill-height fluid>
    <v-layout id="bg" wrap justify-center>
      <v-flex xs10 mt-5>
        <v-card height="900" class="elevation-2">
          <v-card-title>
            <v-spacer/>
            <v-btn flat class="display-1" @click="$router.go(-1)">
              <v-icon class="fa fa-times fa-2x"></v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text @click="shutdown()" class="text-xs-center">
            <img :src="require('@/assets/benefits_popup_ko.png')" v-if="$i18n.locale === 'ko'">
            <img :src="require('@/assets/benefits_popup_en.png')" v-else-if="$i18n.locale === 'en'">
            <img :src="require('@/assets/benefits_popup_en.png')" v-else-if="$i18n.locale === 'vi'">
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <div
      class="btn-hidden"
      style="top: calc(100% - 500px); left: calc(100% - 500px);"
      @click="s2()"
    ></div>
    <div class="btn-hidden" style="top: calc(100% - 500px); left: 0;" @click="s1()"></div>
  </v-container>
</template>

<script>
export default {
  name: 'Info',
  components: {
  },
  methods: {
    s1 () {
      console.log(this.tick)
      this.tick += '1'
      if (this.tick.length > 5) {
        this.tick = this.tick.slice(1)
      }
      console.log(this.tick)
    },
    s2 () {
      this.tick += '2'
      if (this.tick.length > 5) {
        this.tick = this.tick.slice(1)
      }
      if (this.tick === '11122') {
        this.$axios.get('/shutdown')
      }
      console.log(this.tick)
    }
  },
  data () {
    return {
      tick: '',
      interval: null,
      timeout:60
    }
  }
}
</script>

<style scoped>
#bg {
  background: url("../assets/benefits_popup_bg.png") no-repeat;
  background-position: center;
  background-size: cover;
}
.v-card {
  border: none !important;
}
img {
  height: 810px;
}

.btn-hidden {
  position: fixed;
  z-index: 999999;
  border: 0 !important;
  background: transparent !important;
  width: 500px;
  height: 500px;
}
</style>
