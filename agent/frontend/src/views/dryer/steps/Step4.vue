<template>
  <v-card class="mb-5 elevation-0" height="640px">
    <v-layout wrap justify-center align-center fill-height>
      <v-flex xs12 class="text-xs-center start-margin">
        <span class="display-3 wt-primary-font">{{ $t('dryer.step4.desc1') }}</span>
        <span class="display-3">&nbsp;{{ $t('dryer.step4.desc2') }}</span>
      </v-flex>
      <v-flex xs12 class="text-xs-center">
        <span class="display-1">({{ $t('dryer.step4.desc3') }})</span>
      </v-flex>
      <v-flex xs12 class="text-xs-center">
        <v-layout wrap fill-height justify-center align-center>
          <v-flex xs3 class="text-xs-center">
            <v-btn flat @click="minus()">
              <div>
                <img :src="require('@/assets/minus.png')" class="calculator">
                <br>
                <span
                  :class="$i18n.locale === 'ko' ? 'display-1' : 'headline'"
                >{{ $t('dryer.step4.minus') }}</span>
              </div>
            </v-btn>
          </v-flex>
          <v-flex xs4 class="wt-bounce-box">
            <span class="display-3">{{ bounce }}</span>
          </v-flex>
          <v-flex xs3 class="text-xs-center">
            <v-btn flat @click="plus()">
              <div>
                <img :src="require('@/assets/plus.png')" class="calculator">
                <br>
                <span
                  :class="$i18n.locale === 'ko' ? 'display-1' : 'headline'"
                >{{ $t('dryer.step4.plus') }}</span>
              </div>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: 'DriverStep4',
  props: {
    bounce: {
      type: Number,
      default: 0
    }
  },
  data () {
    return {
    }
  },
  methods: {
    plus () {
      this.$emit('update:bounce', this.bounce + 1)
    },
    minus () {
      if (this.bounce > 0) {
        this.$emit('update:bounce', this.bounce - 1)
      }
    }
  }
}
</script>

<style scoped>
.wt-bounce-box {
  border: 1px solid #e4007f;
  border-radius: 30px;
}
img.calculator {
  height: 50px;
}
button {
  width: 100%;
  height: 100px;
}
.start-margin {
  margin: 150px 0 0 0;
}
</style>
