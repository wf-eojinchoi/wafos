<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn icon @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>
        <v-toolbar-title>고객정보관리</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="success" flat @click="dnDialog.show = true">엑셀다운받기</v-btn>
      </v-toolbar>
    </v-layout>
    <v-layout wrap row ma-2>
      <v-flex xs12>
        <v-text-field
          label="전화번호 검색"
          single-line
          type="text"
          solo
          clearable
          hide-details
          v-model="inputPhone"
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-data-table
            :search="search"
            :headers="headers"
            :items="items"
            :pagination.sync="pagination"
            :rows-per-page-items="[20]"
            :total-items="totalitems"
            :loading="loading"
            no-data-text="등록된 데이터가 없습니다"
            no-results-text="검색 결과가 없습니다"
            light
          >
            <template slot="items" slot-scope="props">
              <tr style="cursor: pointer;" @click="onDetail(props.item)">
                <td class="text-xs-center">{{ props.item.tel }}</td>
                <td class="text-xs-center">{{ props.item.money }}</td>
                <td class="text-xs-center">{{ props.item.point }}</td>
                <td class="text-xs-center">{{ props.item.use_count }}</td>
                <td class="text-xs-center">
                  <span
                    style="font-size: 10px;"
                  >{{ props.item.last_use_dttm ? props.item.last_use_dttm.substr(0,10) : '-' }}</span>
                  <br>
                  <span
                    style="font-size: 8px; color: #999999;"
                  >{{ props.item.last_use_dttm ? props.item.last_use_dttm.substr(10,18) : '-' }}</span>
                </td>
                <td class="text-xs-center">
                  <span
                    style="font-size: 10px;"
                  >{{ props.item.reg_dttm ? props.item.reg_dttm.substr(0,10) : '-' }}</span>
                  <br>
                  <span
                    style="font-size: 8px; color: #999999;"
                  >{{ props.item.reg_dttm ? props.item.reg_dttm.substr(10,18) : '-' }}</span>
                </td>
                <td class="text-xs-center">{{ props.item.memo }}</td>
              </tr>
            </template>
            <template slot="footer"></template>
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
                min-width="150px"
              >
                <v-text-field
                  slot="activator"
                  v-model="model_register_dialog.h_date"
                  label="휴일 선택"
                  class="body-1"
                  prepend-icon="event"
                  :value="model_register_dialog.h_date"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="model_register_dialog.h_date"
                  @input="$refs.h_date_model.save(model_register_dialog.h_date)"
                ></v-date-picker>
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
          <v-btn
            color="primary darken-1"
            v-if="!model_register_dialog.mode"
            flat
            @click="registerData(model_register_dialog)"
          >등록하기</v-btn>
          <v-btn
            color="primary darken-1"
            v-if="model_register_dialog.mode"
            flat
            @click="modifyData(model_register_dialog)"
          >수정하기</v-btn>
          <v-btn
            color="grey darken-1"
            flat
            @click.native="model_register_dialog = { show: false }"
          >닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dnDialog.show" max-width="80%" lazy persistent>
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
  layout: 'nomenu',
  name: 'Members',
  methods: {
    // API
    reloadDatas () {
      // console.log(this.$store.state.adminAgency)
      // console.log(this.$cookie.get('agency-info'))
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      // console.log('pagination', this.pagination)
      // console.log('descending', this.pagination.descending, this.pagination.sortBy, this.search)
      this.loading = true
      this.$store.dispatch('AgencyMemberList', {
        id: this.$store.state.adminAgency.wash,
        page: this.pagination.page,
        sortby: this.pagination.sortby, //'last_use_dttm'
        descending: this.pagination.descending,
        query: this.search,
        tel: this.inputPhone
      })
        .then((result) => {
          this.loading = false
          this.items = result.results
          this.totalitems = result.count
          console.log(result)
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    onDetail (memberInfo) {
      var path = '/wash/members/detail/' + memberInfo.id
      this.$router.push(path)
    },
    onBack () {
      this.$router.go(-1)
    },
    requestExcel (item) {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      var params = {
        agency_id: this.$store.state.adminAgency.wash,
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
    }
  },
  created () {
    console.log('#created#')
    this.reloadDatas()
  },
  mounted () {
    console.log('#mounted#')
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
      selData: ['전체', '기간선택'],
      selDataItem: '전체',
      dnDialog: { show: false },
      model_register_dialog: { show: false, mode: false },
      model_delete_dialog: { show: false },
      userSwitch: false,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      error: null,
      search: null,
      loading: false,
      pagination: {descending: true},
      totalitems: 0,
      selectAgency: '전체',
      agencyList: ['전체'],
      items: [],
      selected: [],
      headers: [
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
