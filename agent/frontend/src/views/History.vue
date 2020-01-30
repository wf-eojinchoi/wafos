<template>
  <v-layout wrap justify-space-around>
    <v-flex xs12 pa-5 class="text-xs-center">
      <table class="wt-table">
        <tr class="subheading wt-table-header">
          <th>{{ $t('app.history-service') }}</th>
          <th>{{ $t('app.history-payment') }}</th>
          <th>{{ $t('app.history-save-cash') }}</th>
          <th>{{ $t('app.history-use-cash') }}</th>
          <th>{{ $t('app.history-save-point') }}</th>
          <th>{{ $t('app.history-use-point') }}</th>
          <th>{{ $t('app.history-balance-cash') }}</th>
          <th>{{ $t('app.history-balance-point') }}</th>
          <th>{{ $t('app.history-when') }}</th>
        </tr>
        <template v-if="loading">
          <tr>
            <td colspan="9">
              <v-progress-circular indeterminate color="primary"></v-progress-circular>
            </td>
          </tr>
        </template>
        <template v-else-if="count">
          <tr class="subheading" v-for="item in currentHistory" :key="item.id">
            <td>{{ typeName(item.type) }}</td>
            <td class="body-1">{{ paytypeName(item.pay_type) }}</td>
            <td>{{ add_comma(item.save_money) }}</td>
            <td>{{ add_comma(item.used_money) }}</td>
            <td>{{ add_comma(item.save_point) }}</td>
            <td>{{ add_comma(item.used_point) }}</td>
            <td>{{ add_comma(item.balance_money) }}</td>
            <td>{{ add_comma(item.balance_point) }}</td>
            <td class="body-1">{{ item.pay_dttm }}</td>
          </tr>
        </template>
        <template v-else>
          <tr>
            <td colspan="9" class="headline">사용내역이 없습니다</td>
          </tr>
        </template>
      </table>
    </v-flex>
    <v-flex xs3 class="text-xs-center">
      <v-btn
        flat
        round
        class="wt-prev-bg white--text wt-btn"
        :class="$store.getters.isV2 ? 'display-1': 'display-2'"
        @click="prevPage()"
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
        @click="nextPage()"
      >{{ $t('app.next') }}</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'History',
  data () {
    return {
      loading: true,
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
    this.loading = true
    this.reloadHistory()
  },
  methods: {
    typeName (tid) {
      if (tid === 0) {
        return this.$t('app.washer')
      } else if (tid === 1) {
        return this.$t('app.dryer')
      } else if (tid === 2) {
        return this.$t('app.air-dresser')
      } else if (tid === 3) {
        return this.$t('app.shoes-washer')
      } else if (tid === 4) {
        return this.$t('app.shoes-dryer')
      } else if (tid === 5) {
        return this.$t('app.air-conditioner')
      } else if (tid === 6) {
        return this.$t('app.supplies')
      } else {
        return this.$t('app.save')
      }
    },
    paytypeName (tid) {
      if (tid === 0) {
        return this.$t('app.cash')
      } else if (tid === 1) {
        return this.$t('app.saved-point')
      } else if (tid === 2) {
        return this.$t('app.card')
      } else if (tid === 3) {
        return this.$t('app.use-cash')
      } else {
        return 'Unknown'
      }
    },
    nextPage () {
      if (this.page * this.pageUnits < this.history.length) {
        this.currentHistory = this.history.slice(this.page * this.pageUnits, (this.page + 1) * this.pageUnits)
        this.page += 1
      }
    },
    prevPage () {
      if (this.page > 1) {
        this.currentHistory = this.history.slice((this.page - 2) * this.pageUnits, (this.page - 1) * this.pageUnits)
        this.page -= 1
      }
    },
    reloadHistory () {
      this.$axios.post('/server', {
        method: 'GET',
        path: '/payment-member/' + this.$store.state.user.id
      })
        .then((res) => {
          this.history = res.data
          this.count = res.data.length
          if (this.count > this.pageUnits) {
            this.currentHistory = this.history.slice(0, this.pageUnits)
          } else {
            this.currentHistory = this.history
          }
        })
        .catch((res) => {
          console.log(res)
        })
        .finally(() => {
          this.loading = false
        })
    },
    add_comma (x) {
      var data = Math.round(x)
      return data.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
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
