<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn
         icon
         @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-toolbar-title>회원 상세정보</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>
    </v-layout>
    <div>
      <v-tabs
        v-model="active"
        dark
        slider-color="blue"
        fixed-tabs
      >
        <v-tab
          ripple
        >
          회원정보
        </v-tab>
        <v-tab
          ripple
        >
          사용내역
        </v-tab>
        <v-tab
          ripple
        >
          관리
        </v-tab>
        <v-tabs-items touchless>
          <v-tab-item >
            <v-layout row>
              <v-flex xs12 mt-2 ml-2 mr-2>
                <v-card pa-4>
                  <v-layout wrap pa-4>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs6>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="전화번호"
                            v-model="memberDetail.tel"
                            readonly></v-text-field>
                        </v-flex>
                        <v-flex xs6 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="가맹점명"
                            v-model="memberDetail.agency.agency_name"
                            readonly></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs6>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="현금잔액"
                            v-model="memberDetail.money"
                            readonly></v-text-field>
                        </v-flex>
                        <v-flex xs6 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="포인트잔액"
                            v-model="memberDetail.point"
                            readonly></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs6>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="마지막 사용일"
                            v-model="memberDetail.last_use_dttm"
                            readonly></v-text-field>
                        </v-flex>
                        <v-flex xs6 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="가입일"
                            v-model="memberDetail.reg_dttm"
                            readonly></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs6>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="특별포인트율"
                            suffix="%"
                            v-model="memberDetail.special_point"
                            readonly></v-text-field>
                        </v-flex>
                        <v-flex xs6 pl-2>
                          <v-text-field
                            color="primary lighten-2"
                            type="text"
                            label="SMS 수신여부"
                            :value="memberDetail.use_sms?'수신동의':'동의안함'"
                            readonly></v-text-field>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex xs12>
                      <v-layout wrap>
                        <v-flex xs12>
                          <v-textarea
                            color="primary lighten-2"
                            type="text"
                            label="MEMO"
                            v-model="memberDetail.memo"
                            @click="onAddMemo()"
                            readonly></v-textarea>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                  </v-layout>
                </v-card>
              </v-flex>
            </v-layout>
          </v-tab-item>
          <v-tab-item>
            <v-layout row>
              <v-flex xs12 mt-2 mr-2>
                <v-card>
                  <v-card-title>
                    <v-flex xs12>
                      <span style="color: #0000ff;">
                      <b>사용된 현금</b>00원/<b>사용된 포인트</b>00이고 
                      사용된 현금에 대한 <b>적립된포인트</b>는 00입니다.
                      <b>현금 잔액</b>은 00원, <b>포인트 잔액</b>은 00입니다.
                      </span>
                    </v-flex>
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
                      <tr style="cursor: pointer;">
                        <td class="text-xs-center">
                          <span style="font-size: 10px;">{{ props.item.tran_dttm ? props.item.tran_dttm.substr(0,10) : '-' }}</span>
                          <br>
                          <span style="font-size: 8px; color: #999999;">{{ props.item.tran_dttm ? props.item.tran_dttm.substr(10,18) : '-' }}</span>
                        </td>
                        <td class="text-xs-center" v-if="props.item.type != null">{{ typeArr[props.item.type] }}</td>
                        <td class="text-xs-center" v-else-if="props.item.tran_type != null">
                          {{ getWafos1Type(props.item.tran_type) }}
                        </td>
                        <td class="text-xs-center" v-else>
                          {{ props.item.memo }}
                        </td>
                        <td class="text-xs-center">{{ props.item.save_money }}</td>
                        <td class="text-xs-center">{{ props.item.used_money }}</td>
                        <td class="text-xs-center">{{ props.item.save_point }}</td>
                        <td class="text-xs-center">{{ props.item.used_point }}</td>
                        <td class="text-xs-center">{{ props.item.balance_money }}</td>
                        <td class="text-xs-center">{{ props.item.balance_point }}</td>
                      </tr>
                    </template>
                    <template slot="footer">
                    </template>
                  </v-data-table>
                </v-card>
              </v-flex>
            </v-layout>
          </v-tab-item>
          
          <v-tab-item >
            <v-layout row>
              <v-flex xs12 ma-2>
                <v-card>
                  <v-flex pa-2>
                    <v-btn color="primary" block @click="onPoint()">포인트 증액(+)</v-btn>
                  </v-flex>
                  <v-flex pa-2>
                    <v-btn color="primary" block @click="onMinusPoint()">포인트 감액(-)</v-btn>
                  </v-flex>
                  <v-flex pa-2>
                    <v-btn color="primary" block @click="onMinusMoney()">현금잔액 감액(-)</v-btn>
                  </v-flex>
                  <v-flex pa-2>
                    <v-btn color="primary" block @click="onInitPassword()">비밀번호 초기화</v-btn>
                  </v-flex>
                  <v-flex pa-2>
                    <v-btn color="primary" block @click="onAddMemo()">메모 등록</v-btn>
                  </v-flex>
                </v-card>
              </v-flex>
            </v-layout>
          </v-tab-item>
        </v-tabs-items>
        
      </v-tabs>
    </div>
    <!-- Dialog Area -->
    <v-dialog v-model="pointDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-flex xs12>
            <v-text-field
              color="primary lighten-2"
              type="number"
              label="포인트 입력"
              v-model="pointDialog.point"
              hint="증액 할 포인트를 입력 하세요"
              persistent-hint></v-text-field>
          </v-flex>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" flat @click.native="pointDialog = { show: false }">닫기</v-btn>
          <v-btn color="primary darken-1" flat @click="addPoint(pointDialog)">포인트 증액</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="pointDialog2.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-flex xs12>
            <v-text-field
              color="primary lighten-2"
              type="number"
              label="포인트 입력"
              v-model="pointDialog2.point"
              hint="감액 할 포인트를 입력 하세요"
              persistent-hint></v-text-field>
          </v-flex>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" flat @click.native="pointDialog2 = { show: false }">닫기</v-btn>
          <v-btn color="primary darken-1" flat @click="minusPoint(pointDialog2)">포인트 감액</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="minusMoneyDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-flex xs12>
            <v-text-field
              color="primary lighten-2"
              type="number"
              label="현금 입력"
              v-model="minusMoneyDialog.money"
              hint="감액 할 현금를 입력 하세요"
              persistent-hint></v-text-field>
          </v-flex>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" flat @click.native="minusMoneyDialog = { show: false }">닫기</v-btn>
          <v-btn color="primary darken-1" flat @click="minusMoney(minusMoneyDialog)">현금 감액</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="initPasswordDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-flex xs12>
            <v-text-field
              color="primary lighten-2"
              type="number"
              counter="4"
              label="변경할 비밀번호 입력"
              v-model="initPasswordDialog.pwd"
              hint="초기화 할 비밀번호 4자리를 입력하세요."
              persistent-hint></v-text-field>
          </v-flex>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" flat @click.native="initPasswordDialog = { show: false }">닫기</v-btn>
          <v-btn color="primary darken-1" flat @click="initPassword(initPasswordDialog)">초기화</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="addMemoDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-flex xs12>
            <v-text-field
              color="primary lighten-2"
              type="text"
              label="메모 입력"
              v-model="addMemoDialog.memo"
              hint="참고 사항을 입력 하세요"
              persistent-hint></v-text-field>
          </v-flex>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" flat @click.native="addMemoDialog = { show: false }">닫기</v-btn>
          <v-btn color="primary darken-1" flat @click="changeMemo(addMemoDialog)">메모 입력</v-btn>
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
  layout: 'nomenu',
  name: 'UserDetail',
  // props: [
  //   'rid', 'mode'
  // ],
  watch: {
    pagination: {
      handler () {
        this.loadPayList()
      },
      deep: true
    }
  },
  methods: {
    // API
    loadDetailData () {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      console.log('#')
      var params = {
        agency_id: this.$store.state.adminAgency.wash,
        id: this.$route.params.id
      }
      this.$store.dispatch('AgencyMemberDetail', params)
        .then((result) => {
          this.memberDetail = result
          this.totalitems = result.count
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
        })
    },
    loadPayList () {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      this.$store.dispatch('MemberPaymentList', {
        agency_id: this.$store.state.adminAgency.wash,
        id: this.$route.params.id,
        sortby: this.pagination.sortBy,
        descending: this.pagination.descending,
        page: this.pagination.page
      })
        .then((result) => {
          this.items = result.results
          this.totalitems = result.count
        })
        .catch((result) => {
          this.error = '리스트를 가져오는데 실패했습니다'
        })
    },
    // COMPONENT FUNC
    onBack () {
      this.$router.go(-1)
    },
    onModify () {
      if (this.isModify) {
        this.alertDialog.show = true
      } else {
        // 상태 전환
        this.isModify = !this.isModify
      }
    },
    changeLayout (index) {
      this.uiChange = index
      for (let i = 0; i < this.links.length; i++) {
        if (index === i) {
          this.links[i].active = true
        } else {
          this.links[i].active = false
        }
      }
    },
    onPoint () {
      this.pointDialog.show = true
    },
    onMinusPoint () {
      this.pointDialog2.show = true
    },
    onMinusMoney () {
      this.minusMoneyDialog.show = true
    },
    onInitPassword () {
      this.initPasswordDialog.show = true
    },
    onAddMemo () {
      this.addMemoDialog.memo = this.memberDetail.memo
      this.addMemoDialog.show = true
    },
    addPoint (item) {
      console.log(item)
      var params = {
        id: this.$route.params.id,
        point: item.point,
        minus: false
      }
      this.$store.dispatch('MemberChangePoint', params)
        .then((result) => {
          console.log(result, params.point)
          this.pointDialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'info'
          this.snackbar_msg = params.point + '포인트를 증액하였습니다.'
          this.loadDetailData()
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    minusPoint (item) {
      console.log(item)
      var params = {
        id: this.$route.params.id,
        point: item.point,
        minus: true
      }
      this.$store.dispatch('MemberChangePoint', params)
        .then((result) => {
          console.log(result, params.point)
          this.pointDialog2 = { show: false }
          this.snackbar = true
          this.snackbar_color = 'info'
          this.snackbar_msg = params.point + '포인트를 감액하였습니다.'
          this.loadDetailData()
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    minusMoney (item) {
      var params = {
        id: this.$route.params.id,
        money: item.money,
        minus: true
      }
      this.$store.dispatch('MemberChangeMoney', params)
        .then((result) => {
          console.log(result, params.point)
          this.minusMoneyDialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'info'
          this.snackbar_msg = '현금 잔액 ' + params.money +'원을 감액하였습니다.'
          this.loadDetailData()
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    initPassword (item) {
      var params = {
        id: this.$route.params.id,
        pwd: item.pwd
      }
      if (item.pwd.length === 4) {
        this.$store.dispatch('MemberInitPassword', params)
          .then((result) => {
            this.initPasswordDialog = { show: false }
            this.snackbar = true
            this.snackbar_color = 'info'
            this.snackbar_msg = '비밀번호가 초기화되었습니다.'
            this.loadDetailData()
          })
          .catch((result) => {
            this.error = '실패했습니다'
          })
      } else {
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '비밀번호를 잘못 입력하셨습니다. 비밀번호는 4자리 숫자로 입력하세요.'
      }
    },
    changeMemo (item) {
      var params = {
        id: this.$route.params.id,
        memo: item.memo
      }
      this.$store.dispatch('MemberChangeMemo', params)
        .then((result) => {
          this.addMemoDialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'info'
          this.snackbar_msg = '메모가 변경되었습니다.'
          this.loadDetailData()
        })
        .catch((result) => {
          this.error = '실패했습니다'
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
    this.$store.dispatch('updateTitle', '고객 상세보기')
    this.loadDetailData()
    this.loadPayList()
  },
  data () {
    return {
      active: null,
      pagination: {},
      search: null,
      loading: false,
      totalitems: 0,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      uiChange: 0,
      links: [
        {
          title: '회원정보',
          active: true
        },
        {
          title: '사용내역',
          active: false
        }
      ],
      pointDialog: { show: false },
      memoDialog: { show: false },
      pointDialog2: { show: false },
      minusMoneyDialog: { show: false },
      initPasswordDialog: { show: false },
      addMemoDialog: { show: false },
      isModify: false,
      memberDetail: {
        agency: {}
      },
      items: [],
      typeArr: [ '세탁기', '건조기', '트롬스타일러', '운동화세탁기', '운동화건조기', '냉난방', '세탁용품' ],
      headers: [
        {
          text: '이용일시',
          value: 'tran_dttm',
          align: 'center',
          sortable: true
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
          text: '사용된현금',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '적립된포인트',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '사용된포인트',
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
      ],
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length === 4 || '비밀번호는 4자리입니다.',
        emailMatch: () => ('The email and password you entered don\'t match')
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .tile {
    margin: 5px;
    border-radius: 4px;
  }
  .tile:hover {
    background: green;
  }
  .tile:active {
    background: yellow;
  }
</style>
