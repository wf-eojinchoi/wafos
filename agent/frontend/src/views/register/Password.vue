<template>
  <v-layout id="bg" wrap fill-height justify-center>
    <v-flex xs7>
      <v-layout wrap class="text-xs-center">
        <v-flex xs12 mt-5>
          <span class="display-3 white--text">{{ $t('register.password.title') }}</span>
        </v-flex>
        <v-flex xs12 mt-2>
          <span class="display-1 wt-primary-font">{{ phone }}</span>
          <span class="display-1 white--text">{{ $t('register.password.desc1') }}&nbsp;</span>
        </v-flex>
        <v-flex xs12>
          <span class="display-1 wt-primary-font">{{ $t('register.password.desc2') }}</span>
          <span class="display-1 white--text">{{ $t('register.password.desc3') }}</span>
        </v-flex>
      </v-layout>
      <v-layout wrap mt-4>
        <v-flex xs12 px-5>
          <huge-textbox :model="number" type="password"/>
        </v-flex>
      </v-layout>
      <v-layout wrap justify-center pa-0 mt-3>
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
            :class="$i18n.locale === 'ko' ? 'display-2' : 'display-1'"
            class="elevation-0 grey--text"
            @click="goBack()"
          >{{ $t('app.back') }}</v-btn>
        </v-flex>
        <v-flex xs6 pl-1>
          <v-btn
            color="blue"
            :round="true"
            :disabled="number.length <= 3"
            :class="$i18n.locale === 'ko' ? 'display-2' : 'display-1'"
            class="elevation-0 white--text wt-wave-bg"
            @click="submit()"
          >{{ $t('app.confirm') }}</v-btn>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-dialog v-model="dialog" width="600">
      <v-card>
        <v-card-text class="display-2 text-xs-center mt-2">{{ dialogText }}</v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn color="grey" class="display-2" @click="dialog = false">{{ $t('app.close') }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import HugeTextbox from '@/components/HugeTextbox'

export default {
  name: 'LoginPassword',
  components: {
    HugeTextbox
  },
  data () {
    return {
      number: '',
      phone: '',
      dialog: false,
      dialogText: this.$t('register.password.fail')
    }
  },
  created () {
    this.phone = this.$store.state.phone
  },
  methods: {
    pushNumber (number) {
      if (this.number.length <= 4) {
        if (number === '<') {
          if (this.number.length !== 0) {
            this.number = this.number.substr(0, this.number.length - 1)
          }
        } else if (this.number.length <= 3) {
          this.number += number
        }
      }
    },
    clearNumber () {
      this.number = ''
    },
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    submit () {
      this.$axios.post('/server', {
        method: 'POST',
        path: '/signup',
        args: {
          tel: this.phone.replace('-', '').replace('-', ''),
          pwd: this.number
        }
      })
        .then(res => {
          this.$router.push('/login/password')
        })
        .catch(res => {
          if (res.response.status === 403) {
            this.dialogText = this.$t('register.password.already')
          } else {
            this.dialogText = this.$t('register.password.fail')
          }
          this.dialog = true
        })
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
