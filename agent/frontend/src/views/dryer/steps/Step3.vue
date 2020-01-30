<template>
  <v-card class="mb-5 elevation-0" height="640px">
    <v-layout wrap justify-center align-center fill-height>
      <v-flex xs12 pa-1 class="text-xs-center" v-if="$i18n.locale === 'ko'">
        <span class="display-2 font-weight-bold wt-primary-font">{{ $t('dryer.step3.desc1') }}</span>
        <span class="display-2">{{ $t('dryer.step3.desc2') }}</span>
      </v-flex>
      <v-flex xs12 pa-1 class="text-xs-center" v-else>
        <span class="display-1">{{ $t('dryer.step3.desc1') }}</span>
        <span class="display-1">{{ $t('dryer.step3.desc2') }}</span>
      </v-flex>
      <v-flex xs12 class="text-xs-center">
        <img :src="require('@/assets/dryer_icon.png')">
      </v-flex>
      <v-flex xs8 mb-5>
        <v-layout wrap fill-height justify-center align-center>
          <v-flex xs6 class="text-xs-center">
            <v-btn flat @click="minus()">
              <div>
                <img :src="require('@/assets/minus.png')" class="calculator">
                <br>
                <span class="display-1">{{ $t('dryer.step3.minus-time') }}</span>
              </div>
            </v-btn>
          </v-flex>
          <v-flex xs6 class="text-xs-center">
            <v-btn flat @click="plus()">
              <div>
                <img :src="require('@/assets/plus.png')" class="calculator">
                <br>
                <span class="display-1">{{ $t('dryer.step3.plus-time') }}</span>
              </div>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex xs10 class="wt-dryer-timebox" mt-5>
        <v-layout wrap justify-space-between pa-4 v-if="$i18n.locale === 'ko'">
          <v-flex xs4 class="display-2 text-xs-center">{{ $t('dryer.step3.desc3') }}</v-flex>
          <v-flex xs4 class="display-2 text-xs-right font-weight-bold wt-primary-font">{{ minutes }}</v-flex>
          <v-flex xs4 class="display-2 text-xs-center">{{ $t('app.minute') }}</v-flex>
          <v-flex xs4 mt-3 class="display-2 text-xs-center">{{ $t('payment.use-price') }}</v-flex>
          <v-flex
            xs4
            mt-3
            class="display-2 text-xs-right font-weight-bold wt-primary-font"
          >{{ price }}</v-flex>
          <v-flex xs4 mt-3 class="display-2 text-xs-center">{{ $t('app.money-unit') }}</v-flex>
        </v-layout>
        <v-layout wrap justify-space-between pa-4 v-else>
          <v-flex xs6 class="display-1 text-xs-center">{{ $t('dryer.step3.desc3') }}</v-flex>
          <v-flex xs3 class="display-1 text-xs-right font-weight-bold wt-primary-font">{{ minutes }}</v-flex>
          <v-flex xs3 class="display-1 text-xs-center">{{ $t('app.minute') }}</v-flex>
          <v-flex xs6 mt-3 class="display-1 text-xs-center">{{ $t('payment.use-price') }}</v-flex>
          <v-flex
            xs3
            mt-3
            class="display-1 text-xs-right font-weight-bold wt-primary-font"
          >{{ price }}</v-flex>
          <v-flex xs3 mt-3 class="display-1 text-xs-center">{{ $t('app.money-unit') }}</v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>

export default {
  name: 'DryerStep3',
  components: {
  },
  props: {
    minutes: Number,
    selected: Number,
    price: Number
  },
  data () {
    return {
      unitPrice: 0,
      maxPrice: 0,
      minPrice: 0,
      unit: 0
    }
  },
  watch: {
    selected (val) {
      if (val !== null) {
        let dryer = this.$store.state.devices.dryer[this.selected]
        this.unit = dryer.min_etc_coin
        this.unitPrice = dryer.min_coin
        this.maxPrice = dryer.max_coin
        this.minPrice = dryer.current_coin
        this.$emit('update:minutes', this.unit * (this.minPrice / this.unitPrice))
        this.$emit('update:price', this.minPrice)
      }
    }
  },
  mounted () {
    if (this.selected !== null) {
      let dryer = this.$store.state.devices.dryer[this.selected]
      this.unit = dryer.min_etc_coin
      this.unitPrice = dryer.min_coin
      this.maxPrice = dryer.max_coin
      this.minPrice = dryer.current_coin
      this.$emit('update:minutes', this.unit * (this.minPrice / this.unitPrice))
      this.$emit('update:price', this.minPrice)
    }
  },
  methods: {
    plus () {
      if (this.price < this.maxPrice) {
        this.$emit('update:minutes', this.minutes + this.unit)
        this.$emit('update:price', this.price + this.unitPrice)
      }
    },
    minus () {
      if (this.price > this.unitPrice) {
        this.$emit('update:minutes', this.minutes - this.unit)
        this.$emit('update:price', this.price - this.unitPrice)
      }
    }
  }
}
</script>

<style scoped>
.wt-dryer-timebox {
  border: 1px solid #42b2ec;
  border-radius: 30px;
}
img.calculator {
  height: 50px;
}
</style>
