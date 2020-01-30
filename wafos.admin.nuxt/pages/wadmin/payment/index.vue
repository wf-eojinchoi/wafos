<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12>
        <v-card>
          <v-card-title>
            <v-layout wrap>
              <v-flex xs12>
                <v-layout row pa-2>
                  <v-flex xs12>
                    <table width="100%">
                      <tbody>
                        <td>
                          <v-layout row>
                            <v-flex xs3 sm3 d-flex>
                              <v-select :items="agencyList" v-model="selectAgency" label="가맹점 선택"></v-select>
                            </v-flex>
                          </v-layout>
                        </td>
                        <td width="30%">
                          <v-flex xs12 >
                            <v-text-field
                              label="전화번호 검색"
                              type="text"
                              clearable
                              hide-details
                              v-model="inputPhone"
                            ></v-text-field>
                          </v-flex>
                        </td>
                        <td>
                          <!-- <v-layout row>
                            <v-flex text-xs-right pt-1>
                              <v-btn color="primary" @click="onRegister()">가맹점 추가</v-btn>
                            </v-flex>
                          </v-layout>-->
                          <v-layout row>
                            <v-flex text-xs-right pt-1>
                              <v-btn color="success" @click="dnDialog.show = true">엑셀다운받기</v-btn>
                            </v-flex>
                          </v-layout>
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
            :pagination.sync="pagination"
            :rows-per-page-items="[20,{'text':'All','value':-1}]"
            :total-items="totalitems"
            :loading="loading"
            no-data-text="등록된 데이터가 없습니다"
            no-results-text="검색 결과가 없습니다"
            light
          >
            <template slot="items" slot-scope="props">
              <tr style="cursor: pointer;">
                <td class="text-xs-center">{{ props.item.agency.agency_name }}</td>
                <td class="text-xs-center">
                  <span
                    style="font-size: 10px;"
                  >{{ props.item.tran_dttm ? props.item.tran_dttm.substr(0,10) : '-' }}</span>
                  <br>
                  <span
                    style="font-size: 8px; color: #999999;"
                  >{{ props.item.tran_dttm ? props.item.tran_dttm.substr(10,18) : '-' }}</span>
                </td>
                <td class="text-xs-center">{{ props.item.member ? props.item.member.tel ? props.item.member.tel : '-' : '-' }}</td>
                <td
                  class="text-xs-center"
                  v-if="props.item.type != null"
                >{{ typeArr[props.item.type] }}</td>
                <td class="text-xs-center" v-else-if="props.item.tran_type != null">
                  {{ getWafos1Type(props.item.tran_type) }}
                </td>
                <td class="text-xs-center" v-else>
                  {{ props.item.memo }}
                </td>
                <td class="text-xs-center">{{ add_comma(props.item.save_money) }}</td>
                <td class="text-xs-center">{{ add_comma(props.item.used_money) }}</td>
                <td class="text-xs-center">{{ add_comma(props.item.save_point) }}</td>
                <td class="text-xs-center">{{ add_comma(props.item.used_point) }}</td>
                <td class="text-xs-center">{{ add_comma(props.item.balance_money) }}</td>
                <td class="text-xs-center">{{ add_comma(props.item.balance_point) }}</td>
              </tr>
            </template>
            <template slot="footer"></template>
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="dnDialog.show" max-width="50%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-select :items="selData" v-model="selDataItem" label="기간선택"></v-select>
          <v-layout row v-if="selDataItem === '기간선택'">
            <v-flex xs6>
              <v-menu
                :close-on-content-click="false"
                v-model="dnDialog.menu1"
                :nudge-right="40"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="dnDialog.date1"
                  label="시작날짜"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="dnDialog.date1" @input="dnDialog.menu1 = false"></v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs6>
              <v-menu
                :close-on-content-click="false"
                v-model="dnDialog.menu2"
                :nudge-right="40"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="dnDialog.date2"
                  label="종료날짜"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="dnDialog.date2" @input="dnDialog.menu2 = false"></v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="requestExcel(dnDialog)">다운받기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="dnDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
      <v-btn dark flat @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'PaymentMgr',
  methods: {
    add_comma (x) {
      // 2018.07.23 _ 소숫점 삭제 반올림 하도록 변경
      var data = Math.round(x)
      return data.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
    },
    // API
    loadAgencyList () {
      this.$store.dispatch('AgencyListAll', {})
        .then((result) => {
          for (const idx in result.results) {
            if (result.results.hasOwnProperty(idx)) {
              const element = result.results[idx];
              console.log(element)
              this.agencyList.push(element.agency_name)
            }
          }
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    loadPayList () {
      this.loading = true
      this.$store.dispatch('PaymentList', {
        page: this.pagination.page,
        agency_name: this.selectAgency,
        tel: this.inputPhone
      })
        .then((result) => {
          this.loading = false
          this.items = result.results
          this.totalitems = result.count
        })
        .catch((result) => {
          this.error = '리스트를 가져오는데 실패했습니다'
        })
    },
    requestExcel (item) {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      var params = {
        agency_name: this.selectAgency,
        // agency_id: null,
        st_date: item.date1,
        et_date: item.date2,
        type: this.selDataItem === '전체' ? 0 : 1
      }
      console.log(params)
      this.$store.dispatch('PayDownload', params)
        .then((result) => {
          console.log(result)
          if (result.success) {
            this.dnDialog = { show: false }
            // console.log(result.path)
            window.location.href = result.path
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.error = result.msg
        })
    },
    getWafos1Type (item) {
      if (item === '110002') {
        return '현금입금(W1)'
      } else if (item === '110003') {
        return '세탁기(W1)'
      } else if (item === '110004') {
        return '건조기(W1)'
      } else if (item === '110005') {
        return '운동화세탁기(W1)'
      } else if (item === '110006') {
        return '운동화건조기(W1)'
      } else if (item === '110007') {
        return '멀티자판기(W1)'
      } else if (item === '110008') {
        return '냉난방기(W1)'
      } else if (item === '110011') {
        return '에어드레셔(W1)'
      } else if (item === '110012') {
        return '포인트증액(W1)'
      } else if (item === '110013') {
        return '포인트감액(W1)'
      } else if (item === '110014') {
        return '현금감액(W1)'
      } else if (item === '110015') {
        return '카드입금(W1)'
      } else {
        return '-'
      }
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '매출 관리')
    this.loadPayList()
    this.loadAgencyList()
  },
  watch: {
    pagination: {
      handler () {
        this.loadPayList()
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
    inputPhone: {
      handler () {
        this.loadPayList()
      }
    }
  },
  data () {
    return {
      selData: ['전체', '기간선택'],
      selDataItem: '전체',
      dnDialog: { show: false },
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      error: null,
      search: null,
      loading: false,
      inputPhone: null,
      pagination: {},
      totalitems: 0,
      selectAgency: '전체',
      agencyList: ['전체'],
      items: [],
      selected: [],
      typeArr: ['세탁기', '건조기', '트롬스타일러', '운동화세탁기', '운동화건조기', '냉난방', '세탁용품'],
      headers: [
        {
          text: '가맹점',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '이용일시',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '전화번호',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '서비스종류',
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
          text: '현금잔액',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '포인트잔액',
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
