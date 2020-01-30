<template>
  <v-layout wrap fill-height justify-center>
    <v-flex id="bg" xs12>
      <v-layout wrap justify-center my-5 class="start-contents">
        <v-flex
          xs12
          class="text-xs-center"
          align-self-center
          mt-5
          v-show="$store.state.agency.menu_lang_ko"
        >
          <span class="display-2">언어를 선택해주세요</span>
        </v-flex>
        <v-flex
          xs12
          class="text-xs-center"
          align-self-center
          mt-2
          v-show="$store.state.agency.menu_lang_en"
        >
          <span class="display-2">Choose your language</span>
        </v-flex>
        <v-flex
          xs12
          class="text-xs-center"
          align-self-center
          mt-2
          v-show="$store.state.agency.menu_lang_vn"
        >
          <span class="display-2">Vui lòng chọn một ngôn ngữ</span>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center v-for="lang in langs" :key="lang.i18n" v-show="lang.show">
        <v-flex xs6 class="text-xs-center">
          <v-btn
            :round="true"
            :color="lang.color"
            class="elevation-0 white--text display-3 wt-opacity-80"
            @click="setLanguage(lang.i18n)"
          >{{ lang.title }}</v-btn>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center class="go-bottom">
        <v-flex xs12 class="text-xs-center" align-self-center>
          <img :src="require('@/assets/logo.png')">
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'Language',
  components: {
  },
  data () {
    return {
      langs: [
        { i18n: 'ko', title: '한국어', color: '#ea68a2', show: this.$store.state.agency.menu_lang_ko },
        { i18n: 'en', title: 'English', color: '#e88f0c', show: this.$store.state.agency.menu_lang_en },
        { i18n: 'vi', title: 'Tiếng việt', color: '#00a0e9', show: this.$store.state.agency.menu_lang_vn }
      ]
    }
  },
  methods: {
    setLanguage (key) {
      this.$i18n.locale = key
      this.$router.push('/home')
    }
  },
  mounted () {
    if (this.$store.state.noActionInterval) {
      clearInterval(this.$store.state.noActionInterval)
    }
  },
  beforeDestroy(){
    this.$store.state.noActionInterval = setInterval(()=> {
      if (!this.$store.state.pause) {
        if (this.$store.state.noaction <= 0) {
          this.$store.commit('stateNoAction', 60)
          this.$store.commit('stateUser', {})
          this.$router.replace('/')
        }
        this.$store.state.noaction--
      }
    }, 1000);
  }
}
</script>

<style scoped>
#bg {
  background: url("../assets/main_background.png") no-repeat;
  background-position: center;
  background-size: cover;
}

.v-btn {
  width: 100%;
  height: 120px;
  opacity: 0.65;
}
.start-contents {
  margin-bottom: 50px;
}
.go-bottom {
  width: 100%;
  position: absolute;
  top: calc(100% - 120px);
}
.wt-headline {
  background: #b70501;
  padding: 10px 0 10px 0;
}
</style>
