<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn
         icon
         @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-toolbar-title>월별 매출 현황</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>
    </v-layout>
    <v-layout wrap>
      <v-flex xs12 >
        <v-card>
          <v-card-title>
            <v-layout wrap>
              <v-flex xs12 >
                <v-layout row pa-2>
                  <v-flex xs12 >
                    <table width="100%">
                      <tbody>
                        <td >
                          <v-layout row>
                            <v-flex xs12>
                              <v-select
                                :items="yearList"
                                v-model="yearItem"
                                label="년도 선택"
                              ></v-select>
                            </v-flex>
                          </v-layout>
                        </td>
                        <td >
                          <!-- <v-layout row>
                            <v-flex text-xs-right pt-1>
                              <v-btn color="primary" @click="onRegister()">가맹점 추가</v-btn>
                            </v-flex>
                          </v-layout> -->
                        </td>
                      </tbody>
                    </table>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card-title>
          <v-data-table
            :search="search"
            :headers="headers"
            :items="items"
            :loading="loading"
            :rows-per-page-items="[31,{'text':'All','value':-1}]"
            hide-actions
            no-data-text="등록된 데이터가 없습니다"
            no-results-text="검색 결과가 없습니다"
            light>

            <template slot="items" slot-scope="props">
              <td class="text-xs-center">{{ props.item.date }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.save_money) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.used_money) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.save_point) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.used_point) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.first) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.type0) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.type1) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.type2) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.type3) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.type4) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.type5) }}</td>
              <td class="text-xs-center">{{ add_comma(props.item.type6) }}</td>
            </template>
            <template slot="footer">
              <td class="text-xs-center font-weight-bold indigo--text">합계</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.save_money) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.used_money) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.save_point) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.used_point) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.first) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.type0) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.type1) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.type2) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.type3) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.type4) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.type5) }}</td>
              <td class="text-xs-center font-weight-bold indigo--text">{{ add_comma(total.type6) }}</td>
            </template>
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
    <v-snackbar
      v-model="snackbar"
      :color="snackbar_color"
      :left="true"
      :top="true"
      :multi-line="true"
      :timeout="3000"
      :vertical="true"
      >
      {{ snackbar_msg }}
      <v-btn
        dark
        flat
        @click="snackbar = false"
        >
        Close
      </v-btn>
    </v-snackbar>
  </v-content>
</template>

<script>
export default {
  layout: 'nomenu',
  name: 'PaymentMonthMgr',
  methods: {
    add_comma (x) {
      // 2018.07.23 _ 소숫점 삭제 반올림 하도록 변경
      var data = Math.round(x)
      return data.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
    },
    // API
    loadPayList () {
      console.log(this.date)
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      this.loading = true
      this.$store.dispatch('PaymentMonthList', {
        page: this.pagination.page,
        agency_id: this.$store.state.adminAgency.wash,
        year: this.yearItem,
        month: this.date?this.date.substr(5, 7):null
      })
        .then((result) => {
          this.loading = false
          this.items = result.results
          this.total = result.total
        })
        .catch((result) => {
          this.error = '리스트를 가져오는데 실패했습니다'
        })
      this.$store.dispatch('YearList')
        .then((result) => {
          this.yearList = result.results
          this.yearItem = result.now
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    onBack () {
      this.$router.go(-1)
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '월별 매출 관리')
    this.loadPayList()
  },
  watch: {
    pagination: {
      handler () {
        // this.reloadDatas()
      },
      deep: true
    },
    search: {
      handler () {
        this.pagination.page = 1
        this.reloadDatas()
      }
    },
    selectAgency: {
      handler () {
        this.loadPayList()
      }
    },
    date: {
      handler () {
        this.loadPayList()
      }
    },
    yearItem: {
      handler () {
        this.loadPayList()
      }
    }
  },
  data () {
    return {
      date: new Date().toISOString().substr(0, 7),
      menu: null,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      selectAgency: '전체',
      agencyList: ['전체'],
      yearList: [],
      yearItem: null,
      items: [],
      total: {},
      selected: [],
      typeArr: [ '세탁기', '건조기', '트롬스타일러', '운동화세탁기', '운동화건조기', '냉난방', '세탁용품' ],
      headers: [
        {
          text: '일자',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '현금적립',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '현금사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '포인트부여',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '포인트사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '신규고객',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '세탁사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '건조사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '에어드레셔사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '운동화세탁사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '운동화건조사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '냉난방사용',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '세탁용품사용',
          value: '',
          align: 'center',
          sortable: false
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.font_color {
  color: darkblue;
}
</style>
