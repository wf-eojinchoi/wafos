<template>
  <v-layout wrap justify-space-around>
    <v-flex xs12 pa-5 class="text-xs-center"></v-flex>
    <v-card height="800px" width="100%">
      <v-card-text>
        <!-- 결제 방법 선택 -->
        <v-layout wrap justify-center align-center v-if="paymentSteps === 1" mt-5>
          <v-flex xs12 class="text-xs-center">
            <p>
              <span class="display-2">{{ $t('payment.way') }}</span>
            </p>
          </v-flex>
          <v-flex xs6 class="text-xs-center mt-5">
            <v-btn
              color="#ea68a2"
              round
              class="display-3 huge-btn white--text"
              @click="paymentSteps = 3; payment = 'cash'; requestPayment();"
            >
              <p>
                <img :src="require('@/assets/cash.png')">
                <br>
                <span>{{ $t('payment.cash') }}</span>
              </p>
            </v-btn>
          </v-flex>
          <v-flex xs6 class="text-xs-center mt-5">
            <v-btn
              color="#ea68a2"
              round
              class="display-3 huge-btn white--text"
              @click="paymentSteps = 2; payment = 'card'"
              v-show="$store.state.agency.menu_card === true"
            >
              <p>
                <img :src="require('@/assets/card.png')">
                <br>
                <span>{{ $t('payment.card') }}</span>
              </p>
            </v-btn>
          </v-flex>
        </v-layout>
        <!-- 결제 선택후 -->
        <v-layout wrap justify-center align-center v-else-if="paymentSteps === 2" mt-5>
          <v-flex xs12 class="text-xs-center" mb-5>
            <p>
              <span class="display-2">{{ $t('payment.desc5') }}</span>
            </p>
          </v-flex>
          <v-flex xs5 class="text-xs-center mt-1" v-for="p in prices" :key="p">
            <v-btn
              round
              class="display-1 wt-payment-btn"
              @click="paymentPrice = p;requestPayment();paymentSteps = 3"
            >
              <span>{{ p }} {{ $t('app.money-unit') }}</span>
            </v-btn>
          </v-flex>
        </v-layout>
        <v-layout wrap justify-center align-center v-else-if="paymentSteps === 3 " mt-5>
          <v-flex xs8 class="text-xs-left" mt-3 v-if="payment === 'cash'">
            <span class="display-2">{{ $t('payment.cash-warning') }}</span>
          </v-flex>
          <v-flex xs8 class="text-xs-left" mt-3 v-if="payment === 'card'">
            <span class="display-2">{{ $t('payment.payment-price') }}:&nbsp;</span>
            <span class="display-2 wt-primary-font">{{ paymentPrice }}</span>
            <span class="display-2">{{ $t('app.money-unit') }}</span>
          </v-flex>
          <v-flex xs8 class="text-xs-left" mt-3>
            <span class="display-2">{{ $t('payment.insert-money') }}:&nbsp;</span>
            <span class="display-2 wt-primary-font">{{ insertMoney }}</span>
            <span class="display-2">{{ $t('app.money-unit') }}</span>
          </v-flex>
          <v-flex xs8 class="text-xs-left" mt-3 v-if="payment === 'card'">
            <span class="display-1 wt-primary-font">{{ $t('payment.card-warning') }}</span>
          </v-flex>
          <v-flex xs8 class="text-xs-left" mt-3>
            <span class="display-2">{{ $t('payment.limit-time') }}:&nbsp;</span>
            <span class="display-2 wt-primary-font">{{ 120 - insertCount }}</span>
            <span class="display-2">{{ $t('app.second') }}</span>
          </v-flex>
          <v-flex xs12>
            <v-layout warp justify-center>
              <v-flex xs4 class="text-xs-left" mt-3>
                <v-btn
                  round
                  class="display-1 wt-payment-btn"
                  @click="updateServer(true)"
                >{{ $t('app.back') }}</v-btn>
              </v-flex>
              <v-flex xs4 class="text-xs-left" mt-3 v-if="payment === 'cash'">
                <v-btn
                  color="#ea68a2"
                  round
                  class="display-1 white--text wt-payment-btn"
                  @click="updateServer(false)"
                >{{ $t('app.do-save') }}</v-btn>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
        <!-- 실패 알림 -->
        <v-layout wrap justify-center align-center v-else-if="paymentSteps === 4" mt-5>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="display-1">{{ $t('payment.failure') }}</span>
          </v-flex>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="display-1">{{ $t('payment.close') }}</span>
          </v-flex>
        </v-layout>
        <!-- 성공 알림 -->
        <v-layout wrap justify-center align-center v-else-if="paymentSteps === 5" mt-5>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="display-1">{{ $t('payment.success') }}</span>
          </v-flex>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="display-1">{{ $t('payment.close') }}</span>
          </v-flex>
        </v-layout>
        <!-- 실패 알림 -->
        <v-layout wrap justify-center align-center v-else-if="paymentSteps === 6" mt-5>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="display-1">{{ $t('payment.payment-result', {number: insertMoney}) }}</span>
          </v-flex>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="display-1">{{ $t('payment.close') }}</span>
          </v-flex>
        </v-layout>
        <!-- 실패, 재시도 알림 -->
        <v-layout wrap justify-center align-center v-else-if="paymentSteps === 7" mt-5>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="headline">{{ $t('payment.alert-retry') }}</span>
          </v-flex>
          <v-flex xs12 class="text-xs-center" mt-3>
            <span class="display-1">{{ $t('payment.close') }}</span>
          </v-flex>
        </v-layout>
      </v-card-text>
    </v-card>
    <v-dialog v-model="dialog">
      <v-card height="800px">
        <v-card-text>
          <!-- 코스 확인하기 -->
          <v-layout wrap justify-center align-center mt-5>
            <v-flex xs12 class="text-xs-center" mt-5>
              <p>
                <span class="display-2">{{ $t('payment.pending') }}</span>
              </p>
            </v-flex>
            <v-flex xs6 class="text-xs-center mt-5">
              <v-btn
                round
                class="display-2 wt-wave-bg wt-btn white--text py-5"
                @click="dialog = false"
              >{{ $t('app.close') }}</v-btn>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-dialog>
    <full-loading :value="payloading" message="결제 처리 중입니다"/>
  </v-layout>
</template>

<script>
import FullLoading from '@/components/FullLoading'

export default {
  name: 'Charge',
  components: {
    FullLoading
  },
  beforeRouteLeave (to, from, next) {
    if (!this.flagRequest) {
      this.dialog = true
    } else {
      return next()
    }
  },
  data () {
    return {
      dialog: false,
      payment: null,
      paymentSteps: 1,
      paymentPrice: 0,
      prices: [
        1000, 5000, 10000, 20000, 30000, 40000, 50000
      ],
      interval: null,
      insertMoney: 0,
      insertCount: 0,
      flagRequest: true,
      cancel: false,
      payloading: false
    }
  },
  beforeDestroy () {
    this.clearPayment()
    if (this.interval) {
      clearInterval(this.interval)
    }
  },
  mounted () {
    this.flagRequest = true
  },
  methods: {
    clearPayment () {
      this.$store.commit('stateNoAction', 60)
      this.$store.commit('statePause', false)
      this.paymentSteps = 1
      this.insertMoney = 0
      this.insertCount = 0
      this.flagRequest = true
    },
    updateServer (cancel) {
      if (this.payment === 'cash') {
        this.payloading = true
        this.$socket.emit('cancel-payment')
        setTimeout(function () {
          this.payloading = false
          if (this.interval) {
            clearInterval(this.interval)
          }
          this.cancel = cancel
        }.bind(this), 5000)
      } else {
        if (this.interval) {
          clearInterval(this.interval)
        }
        this.cancel = cancel
        this.$socket.emit('cancel-payment')
      }
    },
    requestPaymentReal () {
      this.$store.commit('statePause', true)
      if (this.insertMoney > 0) {
        this.$axios.post('/server', {
          method: 'POST',
          path: '/payment',
          args: {
            agency_id: this.$store.state.agency.id,
            member_id: this.$store.state.user.hasOwnProperty('phone') ? this.$store.state.user.id : 0,
            amount: this.insertMoney,
            pay_type: this.payment === 'cash' ? 0 : 2
          }
        }).then(() => {
          this.$axios.post('/server', {
            method: 'POST',
            path: '/login',
            args: {
              tel: this.$store.state.user.phone.replace('-', '').replace('-', ''),
              pwd: this.$store.state.user.pwd
            }
          })
            .then(res => {
              let data = res.data
              data.phone = this.$store.state.user.phone
              this.$store.commit('stateUser', data)
              this.$router.push('/washer')
            })
            .catch(res => {
              console.log(res)
            })
          if (this.cancel) {
            this.paymentSteps = 6
            setTimeout(this.clearPayment, 3000)
          } else {
            this.paymentSteps = 5
            setTimeout(this.clearPayment, 3000)
          }
        }).catch(() => {
          this.paymentSteps = 4
          setTimeout(this.clearPayment, 3000)
        })
      } else if (this.insertMoney === -1) {
        this.paymentSteps = 7
        setTimeout(this.clearPayment, 4000)
      } else {
        this.paymentSteps = 6
        setTimeout(this.clearPayment, 3000)
      }
    },
    requestPayment () {
      this.$store.commit('statePause', true)
      this.flagRequest = false
      if (this.payment === 'cash') {
        this.$axios.post('/cash/call')
          .then((res) => {

            console.log('cach already called')
            this.insertMoney = res.data.money
          })
          .catch((res) => {
            this.insertMoney = -1
          })
          .finally(() => {
            this.flagRequest = true
            console.log('requestPaymentReal()')
            this.requestPaymentReal()
            if (this.interval) {
              clearInterval(this.interval)
            }
          })
        this.interval = setInterval(function () {
          this.$axios.get('/cash/status')
            .then((res) => {
              if (res.insertMoney >= this.paymentPrice) {
                if (this.interval) {
                  clearInterval(this.interval)
                }
              } else {
                if (res.data.money) {
                  this.insertMoney = res.data.money
                }
                if (res.data.t) {
                  this.insertCount = res.data.t
                }
              }
            })
            .catch((res) => {
            })
        }.bind(this), 500)
      } else if (this.payment === 'card') {
        this.$axios.post('/card/call', {
          money: this.paymentPrice
        })
          .then((res) => {
            this.insertMoney = res.data.money
          })
          .catch((res) => {
            console.log(res)
          })
          .finally(() => {
            if (this.interval) {
              clearInterval(this.interval)
            }
            this.payloading = true
            setTimeout(function () {
              this.payloading = false
              this.flagRequest = true
              this.requestPaymentReal()
            }.bind(this), 15000)
          })
        this.interval = setInterval(function () {
          this.$axios.get('/card/status')
            .then((res) => {
              if (res.insertMoney >= this.paymentPrice) {
                if (this.interval) {
                  clearInterval(this.interval)
                }
              } else {
                if (res.data.money) {
                  this.insertMoney = res.data.money
                }
                if (res.data.t) {
                  this.insertCount = res.data.t
                }
              }
            })
            .catch((res) => {
            })
        }.bind(this), 500)
      }
    }
  }
}
</script>

<style scoped>
.wt-stepper {
  border: 0;
}
.wt-stepper >>> .v-stepper__items,
.wt-stepper >>> .v-stepper__content,
.wt-stepper >>> .v-stepper__wrapper {
  height: 100%;
}
.wt-stepper >>> .v-stepper__step {
  padding: 20px 0 20px 0 !important;
}
.wt-stepper >>> .v-stepper__step__step {
  border-radius: 15% !important;
  font-size: 2rem;
  padding: 20px 30px 20px 30px !important;
}

.v-divider {
  border-color: #000 !important;
  margin: 40px 30px 0 !important;
}
.wt-point-box {
  border: 1px solid #42b2ec;
  border-radius: 30px;
}
.wt-payment-btn {
  width: 50%;
  height: 100px;
}
.wt-btn {
  width: 90%;
  height: 80%;
}
</style>
