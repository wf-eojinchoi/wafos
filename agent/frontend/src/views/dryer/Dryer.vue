<template>
  <v-layout wrap>
    <v-flex xs12>
      <v-stepper v-model="steps" alt-labels class="wt-stepper elevation-0">
        <v-stepper-header>
          <!-- <v-stepper-step
            :class="$i18n.locale != 'ko' ? 'title' : $store.getters.isV2 ? 'headline': 'display-1'"
            :complete="steps > 1"
            step="1"
          >{{ $t('dryer.step1.title') }}</v-stepper-step>
          <v-divider/> -->
          <v-stepper-step
            :class="$i18n.locale != 'ko' ? 'title' : $store.getters.isV2 ? 'headline': 'display-1'"
            :complete="steps > 1"
            step="1"
          >{{ $t('dryer.step2.title') }}</v-stepper-step>
          <v-divider/>
          <v-stepper-step
            :class="$i18n.locale != 'ko' ? 'title' : $store.getters.isV2 ? 'headline': 'display-1'"
            :complete="steps === 2"
            step="2"
          >{{ $t('dryer.step3.title') }}</v-stepper-step>
          <!-- <v-divider/> -->
          <!-- <v-stepper-step
            :class="$i18n.locale != 'ko' ? 'title' : $store.getters.isV2 ? 'headline': 'display-1'"
            :complete="steps === 2"
            step="2"
          >{{ $t('dryer.step4.title') }}</v-stepper-step> -->
        </v-stepper-header>
        <v-stepper-items>
          <!-- <v-stepper-content step="1">
            <step1 :steps.sync="steps"/>
            <v-layout justify-space-between>
              <v-flex xs3 class="text-xs-center">
                <v-btn
                  flat
                  round
                  class="wt-prev-bg white--text wt-btn"
                  :class="$store.getters.isV2 ? 'display-1': 'display-2'"
                >{{ $t('app.prev') }}</v-btn>
              </v-flex>
              <v-flex xs3 class="text-xs-center">
                <img :src="require('@/assets/logo2.png')" class="wt-bottom-logo">
              </v-flex>
              <v-flex xs3 class="text-xs-center">
                <v-btn
                  flat
                  round
                  class="wt-next-bg white--text wt-btn"
                  :class="$store.getters.isV2 ? 'display-1': 'display-2'"
                  @click="steps = 2"
                >{{ $t('app.next') }}</v-btn>
              </v-flex>
            </v-layout>
          </v-stepper-content> -->
          <v-stepper-content step="1">
            <step2 :selected.sync="selected" :steps.sync="steps"/>
            <v-layout justify-space-between>
              <!-- <v-flex xs3 class="text-xs-center">
                <v-btn
                  flat
                  round
                  class="wt-prev-bg white--text wt-btn"
                  :class="$store.getters.isV2 ? 'display-1': 'display-2'"
                  @click="steps = 1"
                >{{ $t('app.prev') }}</v-btn>
              </v-flex>
              -->
              <v-flex xs3 class="text-xs-center"></v-flex>
              <v-flex xs3 class="text-xs-center">
                <img :src="require('@/assets/logo2.png')" class="wt-bottom-logo">
              </v-flex>
              <v-flex xs3></v-flex>
            </v-layout>
          </v-stepper-content>
          <v-stepper-content step="2">
            <step3 :price.sync="price" :selected="selected" :minutes.sync="minutes"/>
            <v-layout justify-space-around>
              <v-flex xs3 class="text-xs-center">
                <v-btn
                  flat
                  round
                  class="wt-prev-bg white--text wt-btn"
                  :class="$store.getters.isV2 ? 'display-1': 'display-2'"
                  @click="steps = 1"
                >{{ $t('app.prev') }}</v-btn>
              </v-flex>
              <v-flex xs3 class="text-xs-center">
                <img :src="require('@/assets/logo2.png')" class="wt-bottom-logo">
              </v-flex>
              <v-flex xs3 class="text-xs-center">
                <v-btn
                  flat
                  round
                  class="wt-next-bg white--text wt-btn"
                  :class="$store.getters.isV2 ? 'display-1': 'display-2'"
                  :disabled="(!price || price === 0)"
                  @click="dialog = true"
                >{{ $t('app.next') }}</v-btn>
              </v-flex>
            </v-layout>
          </v-stepper-content>
          <!-- <v-stepper-content step="2">
            <step2 :bounce.sync="bounce"/>
            <v-layout justify-space-around>
              <v-flex xs3 class="text-xs-center">
                <v-btn
                  flat
                  round
                  class="wt-prev-bg white--text wt-btn"
                  :class="$store.getters.isV2 ? 'display-1': 'display-2'"
                  @click="steps = 2"
                >{{ $t('app.prev') }}</v-btn>
              </v-flex>
              <v-flex xs3 class="text-xs-center">
                <img :src="require('@/assets/logo2.png')" class="wt-bottom-logo">
              </v-flex>
              <v-flex xs3 class="text-xs-center">
                <v-btn
                  flat
                  round
                  class="wt-next-bg white--text wt-btn"
                  :class="$store.getters.isV2 ? 'display-1': 'display-2'"
                  @click="dialog = true"
                >{{ $t('app.next') }}</v-btn>
              </v-flex>
            </v-layout>
          </v-stepper-content> -->
        </v-stepper-items>
      </v-stepper>
    </v-flex>
    <v-dialog v-model="dialog" lazy :persistent="paymentSteps >= 5 ? true : false">
      <v-card height="800px">
        <v-card-title>
          <v-spacer/>
          <v-btn flat icon @click="clearDialog()" v-if="paymentSteps < 5">
            <v-icon class="fa fa-times fa-4x"></v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <!-- 코스 확인하기 -->
          <v-layout wrap justify-center align-center v-if="paymentSteps === 1" mt-5>
            <v-flex xs12 class="text-xs-center" mt-5>
              <p>
                <span class="display-2">{{ $t('payment.dryer') }}</span>
                <span class="display-2 wt-primary-font">({{ minutes }} {{ $t('app.minute') }})</span>
                <br>
                <!-- <span class="display-2">{{ $t('app.bounce') }}</span>
                <span class="display-2 wt-primary-font">({{ bounce }} {{ $t('app.unit') }})</span>
                <br> -->
                <span class="display-2">{{ $t('payment.use-price') }}:</span>
                <span
                  class="display-2 wt-primary-font"
                >({{ bounce * 500 + price }} {{ $t('app.money-unit') }})</span>
                <br>
                <span class="display-2">{{ $t('payment.desc2-3') }}</span>
                <br><br>
                <span class="display-2 mt-5" mt-3 v-show="!canPayment()">
                  "{{ $t('payment.cant-payment') }}"
                </span>
              </p>
            </v-flex>
            <v-flex xs6 class="text-xs-center mt-5">
              <v-btn
                round
                class="display-2 wt-wave-bg wt-btn white--text py-5"
                :disabled="!canPayment()"
                @click="$store.state.user.hasOwnProperty('phone') ? trigger() : paymentSteps = 2"
              >
              <span v-if="!canPayment()">{{ $t('payment.no-payment') }}</span>
              <span v-else>{{ $t('app.buy') }}</span>
              </v-btn>
            </v-flex>
          </v-layout>
          <!-- 결제 방법 선택 -->
          <v-layout wrap justify-center align-center v-else-if="paymentSteps === 2" mt-5>
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
                @click="paymentSteps = 4; payment = 'cash'"
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
                @click="paymentSteps = 3; payment = 'card'"
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
          <v-layout wrap justify-center align-center v-else-if="paymentSteps === 3" mt-5>
            <v-flex xs12 class="text-xs-center" mb-5>
              <p>
                <span class="display-2">{{ $t('payment.desc5') }}</span>
              </p>
            </v-flex>
            <v-flex xs5 class="text-xs-center mt-1" v-for="p in prices" :key="p">
              <v-btn
                round
                class="display-1 wt-payment-btn"
                @click="paymentSteps = 4; paymentPrice = p"
              >
                <span>{{ p }} {{ $t('app.money-unit') }}</span>
              </v-btn>
            </v-flex>
          </v-layout>
          <!-- 결제 선택후 -->
          <v-layout
            wrap
            justify-center
            align-center
            v-else-if="paymentSteps === 4 && $i18n.locale === 'ko'"
            mt-5
          >
            <v-flex xs8 class="text-xs-left">
              <span class="display-2">{{ $t('payment.product-price') }}:&nbsp;</span>
              <span class="display-2 wt-primary-font">{{ price + bounce * 500 }}</span>
              <span class="display-2">{{ $t('app.money-unit') }}</span>
            </v-flex>
            <v-flex xs8 class="text-xs-left" mt-3>
              <span class="display-2">{{ $t('payment.payment-price') }}:&nbsp;</span>
              <span class="display-2 wt-primary-font">{{ paymentPrice }}</span>
              <span class="display-2">{{ $t('app.point-unit') }}</span>
            </v-flex>
            <v-flex xs9 class="text-xs-left" my-2>
              <v-divider/>
            </v-flex>
            <v-flex xs8 class="text-xs-left" mt-3>
              <span class="display-2">{{ $t('payment.total-saved-money') }}:&nbsp;</span>

              <span class="display-2 wt-primary-font">0</span>
              <span class="display-2">
                {{ $t('app.money-unit') }}
                <br>
                {{ $t('payment.cant-save') }}
              </span>
            </v-flex>
            <v-flex xs6 class="text-xs-center" mt-4>
              <v-btn
                round
                class="display-2 wt-wave-bg wt-btn white--text py-5"
                :disabled="payment === 'card' && paymentPrice < (price + bounce * 500)"
                @click="requestPayment(); paymentSteps = 5"
              >
                <span v-if="payment === 'card'">{{ $t('payment.card') }}</span>
                <span v-else>{{ $t('payment.cash') }}</span>
              </v-btn>
            </v-flex>
          </v-layout>
          <!-- 결제 선택후 -->
          <v-layout
            wrap
            justify-center
            align-center
            v-else-if="paymentSteps === 4 && $i18n.locale !== 'ko'"
            mt-5
          >
            <v-flex xs8 class="text-xs-left">
              <span class="display-1">{{ $t('payment.product-price') }}:&nbsp;</span>
              <span class="display-1 wt-primary-font">{{ price + bounce * 500 }}</span>
              <span class="display-1">{{ $t('app.money-unit') }}</span>
            </v-flex>
            <v-flex xs8 class="text-xs-left" mt-3>
              <span class="display-1">{{ $t('payment.payment-price') }}:&nbsp;</span>
              <span class="display-1 wt-primary-font">{{ paymentPrice }}</span>
              <span class="display-1">{{ $t('app.point-unit') }}</span>
            </v-flex>
            <v-flex xs9 class="text-xs-left" my-2>
              <v-divider/>
            </v-flex>
            <v-flex xs8 class="text-xs-left" mt-3>
              <span class="display-1">{{ $t('payment.total-saved-money') }}:&nbsp;</span>
              <span class="display-1 wt-primary-font">0</span>
              <span class="display-1">
                {{ $t('app.money-unit') }}
                <br>
                {{ $t('payment.cant-save') }}
              </span>
            </v-flex>
            <v-flex xs6 class="text-xs-center" mt-4>
              <v-btn
                round
                class="display-1 wt-wave-bg wt-btn white--text py-5"
                :disabled="payment === 'card' && paymentPrice < (price + bounce * 500)"
                @click="requestPayment(); paymentSteps = 5"
              >
                <span v-if="payment === 'card'">{{ $t('payment.card') }}</span>
                <span v-else>{{ $t('payment.cash') }}</span>
              </v-btn>
            </v-flex>
          </v-layout>
          <v-layout wrap justify-center align-center v-else-if="paymentSteps === 5" mt-5>
            <v-flex xs8 class="text-xs-left" mt-3 v-if="payment === 'cash'">
              <span class="display-2">{{ $t('payment.cash-warning') }}</span>
            </v-flex>
            <v-flex xs8 class="text-xs-left" mt-3>
              <span class="display-2">{{ $t('payment.payment-price') }}:&nbsp;</span>
              <span class="display-2 wt-primary-font">{{ price + bounce * 500 }}</span>
              <span class="display-2">{{ $t('app.money-unit') }}</span>
            </v-flex>
            <v-flex xs8 class="text-xs-left" mt-3>
              <span class="display-2">{{ $t('payment.insert-money') }}:&nbsp;</span>
              <span class="display-2 wt-primary-font">{{ insertMoney }}</span>
              <span class="display-2">{{ $t('app.money-unit') }}</span>
            </v-flex>
            <v-flex xs8 class="text-xs-left" mt-3>
              <span class="display-2">{{ $t('payment.limit-time') }}:&nbsp;</span>
              <span class="display-2 wt-primary-font">{{ 120 - insertCount }}</span>
              <span class="display-2">{{ $t('app.second') }}</span>
            </v-flex>
          </v-layout>
          <!-- 실패 알림 -->
          <v-layout wrap justify-center align-center v-else-if="paymentSteps === 6" mt-5>
            <v-flex xs8 class="text-xs-center" mt-3>
              <span class="display-2">{{ $t('payment.failure') }}</span>
            </v-flex>
            <v-flex xs8 class="text-xs-center" mt-3>
              <span class="display-1">{{ $t('payment.close') }}</span>
            </v-flex>
          </v-layout>
          <!-- 성공 알림 -->
          <v-layout wrap justify-center align-center v-else-if="paymentSteps === 7" mt-5>
            <v-flex xs8 class="text-xs-center" mt-3>
              <span class="display-1">{{ $t('payment.dryer-success') }}</span>
            </v-flex>
            <v-flex xs8 class="text-xs-center" mt-3>
              <span class="display-1">{{ $t('payment.close') }}</span>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
// import Step1 from '@/views/dryer/steps/Step1'
import Step2 from '@/views/dryer/steps/Step2'
import Step3 from '@/views/dryer/steps/Step3'
// import Step4 from '@/views/dryer/steps/Step4'

export default {
  name: 'Dryer',
  components: {
    // Step1,
    Step2,
    Step3,
    // Step4
  },
  data () {
    return {
      selected: null,
      bounce: 0,
      price: 0,
      minutes: 0,
      steps: 1,
      dialog: false,
      payment: null,
      paymentSteps: 1,
      paymentPrice: 0,
      prices: [
        1000, 5000, 10000, 20000, 30000, 40000, 50000
      ],
      interval: null,
      insertMoney: 0,
      insertCount: 0
    }
  },
  destroyed () {
    this.clearDialog()
    if (this.interval) {
      clearInterval(this.interval)
    }
  },
  methods: {
    canPayment () {
      if (!this.$store.state.user.hasOwnProperty('phone')) {
        return true
      }

      // 필요한 돈 만큼 사용자가 가진지 확인
      if (this.$store.state.agency.use_point !== 0 &&
        this.$store.state.user.point >= this.$store.state.agency.use_point) {
        if (this.$store.state.user.point + this.$store.state.user.money >= (this.price)) {
          return true
        }
      } else {
        if (this.$store.state.user.money >= (this.price)) {
          return true
        }
      }

      return false
    },
    trigger () {
      this.$store.commit('statePause', true)
      if (this.interval) {
        clearInterval(this.interval)
      }
      if (this.insertMoney < this.paymentPrice) {
        this.paymentSteps = 6
        setTimeout(this.clearDialog, 2000)
        return
      }
      // let deviceId = this.$store.state.devices.supplies[0].controller_id
      let deviceId = this.$store.state.devices.dryer[this.selected].controller_id
      this.$axios.post('/trigger', {
        price: this.price,
        target: deviceId
      })
        .then((res) => {
          // setTimeout(this.triggerDryer, 1500)
          if (this.$store.state.user.hasOwnProperty('phone')) {
            let usePoint = 0
            let useMoney = 0
            let userid = this.$store.state.user.id
            if (this.$store.state.user.point < this.$store.state.agency.use_point) {
              usePoint = 0
            } else {
              if (this.$store.state.user.point >= (this.price)) {
                usePoint = this.price
              } else {
                usePoint = this.$store.state.user.point
              }
            }

            if (this.$store.state.user.money >= (this.price) - usePoint) {
              useMoney = (this.price) - usePoint
            } else {
              this.paymentSteps = 6
              setTimeout(this.clearDialog, 2000)
              return
            }
            console.log(usePoint, useMoney)
            this.$store.state.user.point -= usePoint
            this.$store.state.user.money -= useMoney
            setTimeout(function () {
              this.$axios.post('/server', {
                method: 'POST',
                path: '/payment',
                args: {
                  agency_id: this.$store.state.agency.id,
                  member_id: userid,
                  amount: useMoney,
                  use_point: usePoint,
                  pay_type: 3, // 적립금 사용
                  device_type: 1
                }
              })
            }.bind(this), 1500)

          } else {
            setTimeout(function () {
              this.$axios.post('/server', {
                method: 'POST',
                path: '/payment',
                args: {
                  agency_id: this.$store.state.agency.id,
                  member_id: 0,
                  amount: this.insertMoney,
                  pay_type: this.payment === 'cash' ? 0 : 2,
                  device_type: 1
                }
              })
            }.bind(this), 1500)
          }
          this.paymentSteps = 7
          setTimeout(function () {
            this.$router.push('/first')
            this.clearDialog()
          }.bind(this), 5000)
        })
        .catch((res) => {
          this.paymentSteps = 6
          setTimeout(this.clearDialog, 2000)
        })
    },
    triggerDryer () {
      let deviceId = this.$store.state.devices.dryer[this.selected].controller_id
      this.$axios.post('/trigger', {
        price: this.price,
        target: deviceId
      })
    },
    clearDialog () {
      this.$store.commit('stateNoAction', 60)
      this.$store.commit('statePause', false)
      this.dialog = false
      this.paymentSteps = 1
      this.paymentPrice = 0
      this.insertMoney = 0
      this.insertCount = 0
    },
    requestPayment () {
      this.$store.commit('statePause', true)
      if (this.payment === 'cash') {
        this.$axios.post('/cash/call')
          .then((res) => {
            this.insertMoney = res.data.money
          })
          .catch((res) => {
            if (this.interval) {
              clearInterval(this.interval)
            }
            this.$socket.emit('cancel-payment')
          })
        this.interval = setInterval(function () {
          this.$axios.get('/cash/status')
            .then((res) => {
              if (res.data.money >= (this.price + this.bounce * 500)) {
                this.trigger()
                this.$socket.emit('cancel-payment')
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
            this.trigger()
          })
          .catch((res) => {
          })
          .finally(() => {
            if (this.interval) {
              clearInterval(this.interval)
            }
          })
        this.interval = setInterval(function () {
          this.$axios.get('/card/status')
            .then((res) => {
              if (res.data.money < this.paymentPrice) {
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
  margin: 40px 20px 0 !important;
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
