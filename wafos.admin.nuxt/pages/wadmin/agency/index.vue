<template>
  <v-content>
    <v-layout wrap>
      {{ addrResult }}
    </v-layout>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-card-title>
            <v-layout row pa-2>
              <v-flex xs12 >
                <table width="100%">
                  <tbody>
                    <td >
                      <v-layout row>
                        <v-flex xs3 d-flex>
                          <v-select
                            :items="selLocationItems"
                            v-model="selectLocationItem"
                            label="지역 검색"
                          ></v-select>
                        </v-flex>
                      </v-layout>
                    </td>
                    <td width="30%">
                      <v-flex xs12 >
                        <v-text-field
                          label="지점 검색"
                          type="text"
                          clearable
                          hide-details
                          v-model="inputName"
                        ></v-text-field>
                      </v-flex>
                    </td>
                    <td >
                      <v-layout row>
                        <v-flex text-xs-right pt-1>
                          <v-btn color="primary" @click="onRegister()">가맹점 추가</v-btn>
                        </v-flex>
                      </v-layout>
                    </td>
                    <!-- <td >
                      <v-layout row>
                        <v-flex text-xs-right pt-1>
                          <v-btn color="info" @click="onUpdateAllClick()">전체 업데이트</v-btn>
                        </v-flex>
                      </v-layout>
                    </td> -->
                  </tbody>
                </table>
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
              <tr style="cursor: pointer;" @click="onDetail(props.index, props.item)">
                <td class="text-xs-center">{{ props.item.agency_code }}</td>
                <td class="text-xs-center">{{ props.item.agency_name }}</td>
                <td class="text-xs-center">{{ props.item.agency_owner }}</td>
                <td class="text-xs-center">{{ props.item.addr1 }}</td>
                <td class="text-xs-center">{{ props.item.tel }}</td>
                <td class="text-xs-center">
                  <v-icon class="green--text" @click.stop="onUpdateClick(props.item)">update</v-icon>
                </td>
              </tr>
            </template>
            <template slot="footer">
            </template> 
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="model_update_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">
            가맹점 와포스2의 업데이트를 진행하시겠습니까?<br>
            업데이트는 약 5~15분 진행되며 완료 후 자동으로 재부팅됩니다.
          </span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="updateAgency(model_update_dialog)">업데이트 진행</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_update_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_update_all_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">
            모든 가맹점 와포스2의 업데이트를 진행하시겠습니까?<br>
            업데이트는 약 5~15분 진행되며 완료 후 자동으로 재부팅됩니다.
          </span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="updateAll()">업데이트 진행</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_update_all_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_delete_dialog.show" max-width="430" lazy persistent>
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
    <v-dialog v-model="model_addr_dialog.show" max-width="430" lazy>
      <v-card>
        <vue-daum-postcode @complete="onPostComplete($event)"/>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_register_dialog.show" max-width="50%" lazy persistent>
      <v-card>
        <v-subheader class="black--text">가맹점 정보 입력</v-subheader>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-layout wrap pa-4>
                <v-flex xs12>
                  <v-layout wrap>
                    <!-- <v-flex xs3>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="가맹점 ID"
                        hint="기본 비밀번호 - 전화번호 뒷자리"
                        v-model="model_register_dialog.id"
                        persistent-hint></v-text-field>
                    </v-flex> -->
                    <v-flex xs3>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="가맹점 코드"
                        v-model="model_register_dialog.agency_code"
                        ></v-text-field>
                    </v-flex>
                  </v-layout>
                </v-flex>
                <v-flex xs12>
                  <v-layout wrap>
                    <v-flex xs3>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="가맹점 이름"
                        v-model="model_register_dialog.agency_name"
                        ></v-text-field>
                    </v-flex>
                    <v-flex xs3 pl-2>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="점주 이름"
                        v-model="model_register_dialog.agency_owner"
                        ></v-text-field>
                    </v-flex>
                    <v-flex xs3 pl-2>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="사업자등록번호"
                        v-model="model_register_dialog.cor_number"
                        ></v-text-field>
                    </v-flex>
                  </v-layout>
                </v-flex>
                <v-flex xs12>
                  <v-layout wrap>
                    <v-flex xs3>
                      <v-text-field
                        color="primary lighten-2"
                        type="number"
                        label="가맹점 전화번호"
                        v-model="model_register_dialog.tel"
                        ></v-text-field>
                    </v-flex>
                    <v-flex xs3 pl-2>
                      <v-text-field
                        color="primary lighten-2"
                        type="number"
                        label="휴대폰번호"
                        v-model="model_register_dialog.phone"
                        ></v-text-field>
                    </v-flex>
                    <v-flex xs3 pl-2>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="IP 주소"
                        v-model="model_register_dialog.ip_addr"
                        ></v-text-field>
                    </v-flex>
                  </v-layout>
                </v-flex>
                <v-flex xs12>
                  <v-layout wrap>
                    <v-flex xs2>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="우편번호"
                        readonly
                        v-model="model_register_dialog.zipcode"
                        ></v-text-field>
                    </v-flex>
                    <v-flex xs6 pl-2>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="가맹점 주소"
                        readonly
                        v-model="model_register_dialog.addr1"
                        ></v-text-field>
                    </v-flex>
                    <v-flex xs4 pl-2>
                      <v-btn @click="onPostcode()">우편번호검색</v-btn>
                    </v-flex>
                  </v-layout>
                </v-flex>
                <v-flex xs12>
                  <v-layout wrap>
                    <v-flex xs8>
                      <v-text-field
                        color="primary lighten-2"
                        type="text"
                        label="상세주소"
                        v-model="model_register_dialog.addr2"
                        ></v-text-field>
                    </v-flex>
                  </v-layout>
                </v-flex>
                <v-flex xs12>
                  <v-layout wrap>
                    <v-flex xs12>
                      <v-textarea
                        color="primary lighten-2"
                        type="text"
                        label="비고"
                        v-model="model_register_dialog.memo"
                        ></v-textarea>
                    </v-flex>
                  </v-layout>
                </v-flex>
                <v-flex xs12>
                  <v-layout wrap>
                    <v-flex xs3>
                      <v-menu
                        :close-on-content-click="false"
                        v-model="menu"
                        :nudge-right="40"
                        lazy
                        transition="scale-transition"
                        offset-y
                        full-width
                        min-width="290px"
                      >
                        <v-text-field
                          slot="activator"
                          v-model="model_register_dialog.expire_date"
                          label="유지보수 만료일"
                          prepend-icon="event"
                          readonly
                        ></v-text-field>
                        <v-date-picker v-model="model_register_dialog.expire_date" @input="menu = false"></v-date-picker>
                      </v-menu>
                    </v-flex>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" v-if="!model_register_dialog.mode" flat @click="registerData(model_register_dialog)">등록하기</v-btn>
          <v-btn color="primary darken-1" v-if="model_register_dialog.mode" flat @click="modifyData(model_register_dialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_register_dialog = { show: false }">닫기</v-btn>
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
  name: 'AgencyMgr',
  methods: {
    // API
    reloadDatas () {
      console.log('reloadDatas called')
      this.loading = true
      this.$store.dispatch('AgencyList', {
        page: this.pagination.page,//undefined(페이지번호)
        sortby: this.pagination.sortBy,//undefined(정렬기준)
        descending: this.pagination.descending,//undefined
        query: this.search,//undefined
        location: this.selectLocationItem,//undefined (지역검색)
        name: this.inputName//undefined (지점검색)
      })
        .then((result) => {
          this.loading = false
          this.items = result.results
          this.totalitems = result.count
          console.log('dispatch AgencyList result : ', result)
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    onRegister () {
      // var path = '/wadmin/agency/register/'
      // this.$router.push(path)
      this.model_register_dialog.show = true
    },
    registerData (item) {
      this.$store.dispatch('AgencyRegister', item)
        .then((result) => {
          this.model_register_dialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '등록되었습니다.'
          this.reloadDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
          console.log(result)
        })
    },
    onDetail (index, item) {
      var path = '/wadmin/agency/detail/' + item.id
      this.$router.push(path)
    },
    onPostcode () {
      this.model_addr_dialog.show = true
    },
    onPostComplete (event) {
      // this.addrResult = event
      console.log(event)
      this.model_register_dialog.zipcode = event.zonecode
      this.model_register_dialog.addr1 = event.address
      this.model_addr_dialog = { show: false }
    },
    onUpdateClick (item) {
      this.model_update_dialog = item
      this.model_update_dialog.show = true
    },
    updateAgency (item) {
      console.log(item)
      let params = {
        agency_id: item.id,
        cmd: 8
      }
      this.$store.dispatch('AgencyAlertReg', params)
        .then((result) => {
          if (result.success) {
            this.model_update_dialog = { show: false }
            this.snackbar = true
            this.snackbar_color = 'success'
            this.snackbar_msg = item.agency_name + ' 와포스2에 업데이트 스케줄을 등록하였습니다.'
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = '서비스가 정상적이지 않습니다. 지속적으로 발생하면 관리자에게 문의해주세요.'
          }
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    onUpdateAllClick () {
      this.model_update_all_dialog.show = true
    },
    updateAll () {
      this.$store.dispatch('AgencyUpdateAll')
        .then((result) => {
          if (result.success) {
            this.model_update_all_dialog = { show: false }
            this.snackbar = true
            this.snackbar_color = 'success'
            this.snackbar_msg = '모든 가맹점 와포스2에 업데이트 스케줄을 등록하였습니다.'
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = '서비스가 정상적이지 않습니다. 지속적으로 발생하면 관리자에게 문의해주세요.'
          }
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    }
  },
  created () {
    console.log('###agency-index.vue created###')
    //pagination deep true 이기 때문에 reloadDatas() 하지말것
  },
  mounted () {
    this.$store.dispatch('updateTitle', '가맹점 관리')
  },
  watch: {
    pagination: {
      handler () {
        console.log('watch pagination called')
        console.log('watch pagination.page :', this.pagination.page)
        this.reloadDatas()
      },
    },
    search: {
      handler () {
        console.log('watch search called')
        console.log('search :', this.search)
        this.reloadDatas()
      }
    },
    selectLocationItem: {//지역검색
      handler () {
        console.log('watch selectLocationItem called')
        console.log('지역선택 : ', this.selectLocationItem)
        this.pagination.page = 1
        this.reloadDatas()
      }
    },
    inputName: {//지점검색
      handler () {
        console.log('watch inputName called')
        console.log('지점검색 :', this.inputName)
        this.pagination.page = 1
        this.reloadDatas()
      }
    }
  },
  data () {
    return {
      selLocationItems: [ '전체', '서울', '경기', '인천', '충남', '충북', '경남', '경북', '강원', '부산', '대전', '대구', '광주'],
      selectLocationItem: '전체',
      table_selected: [],
      h_date: null,
      h_date_model: false,
      date: null,
      menu: false,
      model_addr_dialog: { show: false },
      addrResult: null,
      model_register_dialog: { show: false, mode: false },
      model_delete_dialog: { show: false },
      model_update_dialog: { show: false },
      model_update_all_dialog: { show: false },
      userSwitch: false,
      inputName: null,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      items: [],
      selected: [],
      headers: [
        {
          text: '가맹점코드',
          value: 'agency_code',
          align: 'center',
          sortable: true
        },
        {
          text: '가맹점명',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '점주명',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '지역',
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
          text: '업데이트',
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
body {
  font-family: 'Spoqa Han Sans', 'Open Sans', sans-serif;
}
h1 {
  font-size: 2rem;
}
h2 {
  font-size: 1.2rem;
  font-weight: 400;
}
p {
  font-weight: 300;
}
.source {
  padding: .5rem;
  background: #f8f8f8;
}
.source pre {
  margin-bottom: 0;
}
.source + .source,
.source + .result {
  margin-top: 1rem;
}
section + section {
  margin-top: 2rem;
}
.vue-daum-postcode {
  border: 1px solid #000;
}
.vue-daum-postcode-container {
  transition: all 500ms ease;
}
</style>
