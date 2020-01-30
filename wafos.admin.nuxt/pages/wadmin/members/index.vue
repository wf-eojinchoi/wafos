<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-card-title>
            <v-layout wrap>
              <v-flex xs12 >
                <v-layout row pa-2>
                  <v-flex xs12 >
                    <table width="100%">
                      <tbody>
                        <td style="padding-top: 20px;">
                          <v-flex xs3>
                            <v-select
                              :items="agencyList"
                              v-model="selectAgency"
                              label="가맹점 선택"
                            ></v-select>
                          </v-flex>
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
                        <td >
                        </td>
                        <td >
                          <v-layout row>
                            <v-flex text-xs-right pt-1>
                              <v-btn
                              color="success"
                              @click="dnDialog.show = true">
                                엑셀다운받기
                              </v-btn>
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
            :rows-per-page-items="[10,{'text':'All','value':-1}]"
            :total-items="totalitems"
            :loading="loading"
            no-data-text="등록된 데이터가 없습니다"
            no-results-text="검색 결과가 없습니다"
            light>

            <template slot="items" slot-scope="props">
              <tr style="cursor: pointer;" @click="onDetail(props.item)">
                <td class="text-xs-center">{{ props.item.agency.agency_name }}</td>
                <td class="text-xs-center">{{ props.item.tel }}</td>
                <td class="text-xs-center">{{ props.item.money }}</td>
                <td class="text-xs-center">{{ props.item.point }}</td>
                <td class="text-xs-center">{{ props.item.use_count }}</td>
                <td class="text-xs-center">
                  {{ props.item.last_use_dttm ? props.item.last_use_dttm.substr(0,10) : '-' }}
                  <br>
                  <span style="font-size: 8px; color: #999999;">{{ props.item.last_use_dttm ? props.item.last_use_dttm.substr(10,18) : '-' }}</span>
                </td>
                <td class="text-xs-center">
                  {{ props.item.reg_dttm ? props.item.reg_dttm.substr(0,10) : '-' }}
                  <br>
                  <span style="font-size: 8px; color: #999999;">{{ props.item.reg_dttm ? props.item.reg_dttm.substr(10,18) : '-' }}</span>
                </td>
                <td class="text-xs-center">{{ props.item.memo }}</td>
              </tr>
            </template>
            <template slot="footer">
            </template>
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="model_delete_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">'{{ model_delete_dialog.memo }}' 삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="deleteData(model_delete_dialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_delete_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_register_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row v-if="model_register_dialog.mode">
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="등록일"
                :value="model_register_dialog.ins_date"
                disabled
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-menu
                ref="h_date_model"
                :close-on-content-click="false"
                v-model="h_date_model"
                :nudge-right="40"
                :return-value.sync="h_date"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="150px" >
                <v-text-field
                  slot="activator"
                  v-model="model_register_dialog.h_date"
                  label="휴일 선택"
                  class="body-1"
                  prepend-icon="event"
                  :value="model_register_dialog.h_date"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="model_register_dialog.h_date" @input="$refs.h_date_model.save(model_register_dialog.h_date)"></v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                v-model="model_register_dialog.memo"
                type="text"
                label="메모"
                :value="model_register_dialog.memo"
                ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" v-if="!model_register_dialog.mode" flat @click="registerData(model_register_dialog)">등록하기</v-btn>
          <v-btn color="primary darken-1" v-if="model_register_dialog.mode" flat @click="modifyData(model_register_dialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_register_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dnDialog.show" max-width="50%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-select
            :items="selData"
            v-model="selDataItem"
            label="기간선택"
          ></v-select>
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
  layout: 'wadmin',
  name: 'Members',
  methods: {
    // API
    loadAgencyList () {
      this.$store.dispatch('AgencyListAll', {})
        .then((result) => {
          for (const idx in result.results) {
            if (result.results.hasOwnProperty(idx)) {
              const element = result.results[idx];
              //console.log('member index.vue element :', element)
              this.agencyList.push(element.agency_name)
            }
          }
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    reloadDatas () {
      this.loading = true
      this.$store.dispatch('MemberList', {
        page: this.pagination.page,
        sortby: this.pagination.sortBy,
        descending: this.pagination.descending,
        query: this.search,
        agency_name: this.selectAgency,
        tel: this.inputPhone
      })
        .then((result) => {
          this.loading = false
          this.items = result.results
          this.totalitems = result.count
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    onDetail (memberInfo) {
      console.log(memberInfo)
      var path = '/wadmin/members/detail/' + memberInfo.id
      this.$router.push(path)
    },
    requestExcel (item) {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      var params = {
        // agency_id: this.$store.state.adminAgency.wash,
        st_date: item.date1,
        et_date: item.date2,
        type: this.selDataItem === '전체' ? 0 : 1
      }
      console.log(params)
      this.$store.dispatch('MemberDownload', params)
        .then((result) => {
          console.log(result)
          if (result.success) {
            this.dnDialog = { show: false }
            console.log(result.path)
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
    }
  },
  created () {
    console.log('#created#')
    this.loadAgencyList()
    this.reloadDatas()
  },
  mounted () {
    this.$store.dispatch('updateTitle', '고객 관리')
    // this.reloadDatas()
  },
  watch: {
    pagination: {
      handler () {
        this.reloadDatas()
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
        this.reloadDatas()
      }
    },
    inputPhone: {
      handler () {
        this.reloadDatas()
      }
    }
  },
  data () {
    return {
      table_selected: [],
      h_date: null,
      h_date_model: false,
      inputPhone: null,
      model_register_dialog: { show: false, mode: false },
      model_delete_dialog: { show: false },
      userSwitch: false,
      selData: [ '전체', '기간선택' ],
      selDataItem: '전체',
      dnDialog: { show: false },
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
      items: [
        {
          agency: '강서점',
          name: '테스트',
          tel: '01056701114',
          amount: '25,000',
          amount2: '5,000',
          reg_dttm: '2019-02-11 12:00:00',
          last_use_dttm: '2019-02-11 12:00:00'
        }
      ],
      selected: [],
      headers: [
        {
          text: '가맹점',
          value: 'adsf',
          align: 'center',
          sortable: true
        },
        {
          text: '전화번호',
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
        },
        {
          text: '이용횟수',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '최종 이용일',
          value: 'last_use_dttm',
          align: 'center',
          sortable: true
        },
        {
          text: '가입일',
          value: 'reg_dttm',
          align: 'center',
          sortable: true
        },
        {
          text: '메모',
          value: 'memo',
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
