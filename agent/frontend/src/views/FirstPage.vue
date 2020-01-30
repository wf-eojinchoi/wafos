<template>
  <v-layout wrap justify-space-around fill-height align-center>
    <v-flex xs12 pa-5 class="text-xs-center">
      <v-layout wrap>
        <v-flex xs6>
          <v-btn
            color="#ea68a2"
            round
            class="display-3 huge-btn white--text"
            @click="$router.push('/charge')"
          >{{ $t('app.do-save') }}</v-btn>
        </v-flex>
        <v-flex xs6>
          <v-btn
            color="#ea68a2"
            round
            class="display-3 huge-btn white--text"
            @click="$router.push('/history')"
          >{{ $t('app.usage') }}</v-btn>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'FirstPage',
  data () {
    return {
      history: [],
      currentHistory: [],
      count: 0,
      pageUnits: 10,
      page: 1
    }
  },
  destroyed () {
  },
  mounted () {
    this.$store.commit('statePause', false)
  },
  methods: {
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

.wt-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid black;
  min-height: 700px;
}

.wt-table-header {
  height: 50px;
}

.wt-table > tr,
.wt-table > tr > td,
.wt-table > tr > th {
  border: 1px solid black;
  padding: 2px;
}
</style>
