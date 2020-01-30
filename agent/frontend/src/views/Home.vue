<template>
  <v-layout wrap fill-height justify-center>
    <v-flex id="bg" xs12>
      <v-layout wrap justify-center mt-5 mb-3>
        <v-flex xs8 class="text-xs-center wt-headline" align-self-center>
          <span class="display-3 font-weight-bold white--text">{{ $t('home.header') }}</span>
        </v-flex>
        <v-flex xs12 class="text-xs-center" align-self-center mt-5>
          <span class="display-2 font-weight-bold">{{ $t('home.title1') }}</span>
        </v-flex>
        <v-flex xs12 class="text-xs-center" align-self-center mt-3>
          <span class="display-1">{{ $t('home.title2') }}</span>
        </v-flex>
        <v-flex xs12 class="text-xs-center" align-self-center>
          <span
            class="display-1"
            :class="$i18n.locale === 'ko' ? 'wt-primary-font' : ''"
          >{{ $t('home.title3') }}</span>
          <span class="display-1">{{ $t('home.title4') }}</span>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center class="start-contents">
        <v-flex xs6 class="text-xs-center">
          <v-btn
            to="/login/phone"
            :round="true"
            color="#ea68a2"
            :class="$i18n.locale === 'vi' ? 'headline' : 'display-3'"
            class="elevation-0 white--text wt-opacity-80"
          >
            {{ $t('home.btn1') }}
            <v-icon class="fa fa-angle-right fa-1x"/>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center v-show="$store.state.agency.menu_signup">
        <v-flex xs6 class="text-xs-center" mt-2>
          <v-btn
            to="/washer"
            :round="true"
            color="#e88f0c"
            :class="$i18n.locale === 'vi' ? 'headline' : 'display-3'"
            class="elevation-0 white--text wt-opacity-80"
          >
            {{ $t('home.btn2') }}
            <v-icon class="fa fa-angle-right fa-1x"/>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center>
        <v-flex xs6 class="text-xs-center" mt-2>
          <v-btn
            to="/register/phone"
            :round="true"
            color="#b0ad08"
            :class="$i18n.locale === 'vi' ? 'headline' : 'display-3'"
            class="elevation-0 white--text wt-opacity-50"
          >
            {{ $t('home.btn3') }}
            <v-icon class="fa fa-angle-right fa-1x"/>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center>
        <v-flex xs6 class="text-xs-center" my-2>
          <v-btn
            to="/info"
            color="#00a0e9"
            :round="true"
            :class="$i18n.locale === 'vi' ? 'headline' : 'display-3'"
            class="elevation-0 white--text wt-opacity-50"
          >
            {{ $t('home.btn4') }}
            <v-icon class="fa fa-angle-right fa-1x"/>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center>
        <v-flex xs6 class="text-xs-center" my-2>
          <v-btn
            @click="$router.go(-1)"
            color="grey"
            :round="true"
            :class="$i18n.locale === 'vi' ? 'headline' : 'display-3'"
            class="elevation-0 white--text wt-opacity-50"
          >
            <v-icon class="fa fa-angle-left fa-1x"/>
            {{ $t('home.btn5') }}
          </v-btn>
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
  name: 'Home',
  components: {
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
#bg {
  background: url("../assets/main_background.png") no-repeat;
  background-position: center;
  background-size: cover;
}
.start-contents {
  margin: 80px 0 0 0 !important;
}
.v-btn {
  width: 100%;
  height: 70px;
  opacity: 0.65;
}
.go-bottom {
  margin: 50px 0 0 0;
}
.wt-headline {
  background: #b70501;
  padding: 10px 0 10px 0;
}
</style>
