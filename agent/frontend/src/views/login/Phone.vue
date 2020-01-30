<template>
  <v-layout id="bg" wrap fill-height justify-center>
    <v-flex xs7>
      <v-layout wrap class="text-xs-center">
        <v-flex xs12 mt-5>
          <span class="display-3 font-weight-bold white--text">{{ $t('login.phone.title') }}</span>
        </v-flex>
        <v-flex xs12 mt-2 v-if="$i18n.locale === 'ko'">
          <span class="display-1 white--text">{{ $t('login.phone.desc1') }}&nbsp;</span>
          <span class="display-1 wt-primary-font">{{ $t('login.phone.desc2') }}</span>
          <span class="display-1 white--text">{{ $t('login.phone.desc3') }}</span>
        </v-flex>
        <v-flex xs12 mt-2 v-else>
          <span class="display-1 white--text">{{ $t('login.phone.desc1') }}&nbsp;</span>
          <span class="display-1 white--text">{{ $t('login.phone.desc2') }}</span>
          <span class="display-1 white--text">{{ $t('login.phone.desc3') }}</span>
        </v-flex>
      </v-layout>
      <v-layout wrap mt-4>
        <v-flex xs12 px-5>
          <huge-textbox :model="number"/>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center pa-0 mt-5>
        <v-flex v-for="n in 9" :key="n" xs4 pa-1>
          <v-btn
            color="#787878"
            :round="true"
            class="elevation-0 white--text display-3"
            @click="pushNumber(n)"
          >{{ n }}</v-btn>
        </v-flex>
        <v-flex xs4 pa-1>
          <v-btn
            color="#787878"
            :round="true"
            class="elevation-0 white--text display-3"
            @click="clearNumber()"
          >
            <v-icon class="fa fa-trash fa-1x"/>
          </v-btn>
        </v-flex>
        <v-flex xs4 pa-1>
          <v-btn
            color="#787878"
            :round="true"
            class="elevation-0 white--text display-3"
            @click="pushNumber('0')"
          >0</v-btn>
        </v-flex>
        <v-flex xs4 pa-1>
          <v-btn
            color="#787878"
            :round="true"
            class="elevation-0 white--text display-3"
            @click="pushNumber('<')"
          >
            <v-icon class="fa fa-backspace fa-1x"/>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-layout wrap mt-1>
        <v-flex xs6 pr-1>
          <v-btn
            :round="true"
            class="elevation-0 grey--text"
            :class="$i18n.locale === 'ko' ? 'display-2' : 'display-1'"
            @click="goBack()"
          >{{ $t('app.back') }}</v-btn>
        </v-flex>
        <v-flex xs6 pl-1>
          <v-btn
            :round="true"
            :disabled="number.length <= 11"
            :class="$i18n.locale === 'ko' ? 'display-2' : 'display-1'"
            class="elevation-0 white--text wt-wave-bg"
            @click="submit()"
          >{{ $t('app.confirm') }}</v-btn>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
import HugeTextbox from '@/components/HugeTextbox'

export default {
  name: 'LoginPhone',
  components: {
    HugeTextbox
  },
  data () {
    return {
      number: ''
    }
  },
  mounted () {
    this.number = '010-'
  },
  methods: {
    pushNumber (number) {
      let num = this.number.replace(/-/g, '')

      if (num.length >= 3 && num.length <= 11) {
        if (number === '<') {
          if (num.length !== 3) {
            num = num.substr(0, num.length - 1)
          }
        } else {
          num += number
        }
      }
      this.number = this.formatNumber(num)
    },
    formatNumber (number) {
      let len = number.length
      let _str = ''
      if (len === 3) {
        _str = '010-'
      } else if (len > 3 && len < 6) {
        _str = number.substr(0, 3) + '-' + number.substr(3, len - 3)
      } else if (len >= 6 && len < 11) {
        _str = number.substr(0, 3) + '-' + number.substr(3, 3) + '-' + number.substr(6, len - 6)
      } else if (len >= 11) {
        _str = number.substr(0, 3) + '-' + number.substr(3, 4) + '-' + number.substr(7, 4)
      }
      return _str
    },
    clearNumber () {
      this.number = '010-'
    },
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    submit () {
      this.$store.commit('statePhone', this.number)
      this.$router.push('/login/password')
    }
  }
}
</script>

<style scoped>
#bg {
  background: url("../../assets/number_background.png") no-repeat;
  background-position: center;
  background-size: cover;
}
.start-contents {
  margin: 100px 0 0 0 !important;
}
button {
  width: 100%;
  height: 100px;
}
</style>
