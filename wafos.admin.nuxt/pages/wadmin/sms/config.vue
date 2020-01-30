<template>
  <v-content>
    <v-layout row>
      <v-flex xs12>
        <v-card>
          <v-card-text>
            <v-flex xs12 text-xs-right>
              <v-btn color="primary" round small @click="onSMSDialog()">이벤트 문자 등록</v-btn>
            </v-flex>
            <!-- SMS LIST -->
            <v-data-table
              :items="items"
              :headers="headers"
              :pagination.sync="pagination"
              :rows-per-page-items="[10,{'text':'All','value':-1}]"
              :total-items="totalitems"
              :loading="loading"
              no-data-text="등록된 이벤트 문자가 없습니다"
              light
            >
              <template slot="items" slot-scope="props">
                <tr style="cursor: pointer;">
                  <td class="text-xs-center green--text" v-if="props.item.stat === 0">{{ getStatus(props.item.stat) }}</td>
                  <td class="text-xs-center blue--text" v-else-if="props.item.stat === 1">{{ getStatus(props.item.stat) }}</td>
                  <td class="text-xs-center red--text" v-else-if="props.item.stat >= 2">{{ getStatus(props.item.stat) }}</td>
                  <td class="text-xs-center">{{ props.item.rvd_date }}</td>
                  <td class="indigo--text" style="cursor: pointer;" @click="onDetail(props.index, props.item)"><div class="title-overflow">{{ props.item.title }}</div></td>
                  <td class="indigo--text" style="cursor: pointer;" @click="onDetail(props.index, props.item)"><div class="content-overflow" >{{ props.item.contents }}</div></td>
                  <!-- <td class="text-xs-center">{{ props.item.ins_date }}</td> -->
                  <td class="text-xs-center">
                    <v-icon class="red--text" @click.stop="onDeleteDialog(props.item)">delete_forever</v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="smsDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="제목"
                counter="120"
                v-model="smsDialog.title"
                single-line></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="내용"
                counter="1000"
                v-model="smsDialog.contents"
                multi-line></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <v-flex xs12>
              <v-menu
                ref="date_model"
                :close-on-content-click="false"
                v-model="date_model"
                :nudge-right="40"
                :return-value.sync="smsDialog.date"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px" >
                <v-text-field
                  slot="activator"
                  v-model="smsDialog.date"
                  label="발송 날짜"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="smsDialog.date" @input="$refs.date_model.save(smsDialog.date)"></v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs12>
              <v-menu
                ref="time_model"
                :close-on-content-click="false"
                v-model="time_model"
                :nudge-right="40"
                :return-value.sync="smsDialog.time"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px" >
                <v-text-field
                  slot="activator"
                  v-model="smsDialog.time"
                  label="발송 시간"
                  prepend-icon="access_time"
                  readonly
                ></v-text-field>
                <v-time-picker v-model="smsDialog.time" @change="$refs.time_model.save(smsDialog.time)"></v-time-picker>
              </v-menu>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="registerData(smsDialog)" v-if="!smsDialog.mode">등록하기</v-btn>
          <v-btn color="primary" flat @click="modifyData(smsDialog)" v-if="smsDialog.mode">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="smsDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_delete_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">'{{ model_delete_dialog.title }}' 문자를 삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="deleteData(model_delete_dialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_delete_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'SMSMgr',
  methods: {
    // API
    reloadDatas () {
      this.loading = true
      this.$store.dispatch('smsList', {
        page: this.pagination.page,
        sortby: this.pagination.sortBy,
        descending: this.pagination.descending,
        query: this.search
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
    registerData (item) {
      console.log('reg data : %o', item)
      item.rvd_date = item.date + ' ' + item.time
      this.$store.dispatch('smsRegister', item)
        .then((result) => {
          this.reloadDatas()
          this.smsDialog = { show: false }
        })
        .catch((result) => {
          this.error = 'sms 등록에 실패했습니다'
        })
    },
    modifyData (item) {
      item.rvd_date = item.date + ' ' + item.time
      this.$store.dispatch('smsModify', item)
        .then((result) => {
          this.reloadDatas()
          this.smsDialog = { show: false }
        })
        .catch((result) => {
          this.error = 'sms 수정에 실패했습니다'
        })
    },
    deleteData (item) {
      this.$store.dispatch('smsDelete', item.id)
        .then((result) => {
          this.reloadDatas()
          this.model_delete_dialog = { show: false }
        })
        .catch((result) => {
          this.error = 'sms 삭제가 실패했습니다'
        })
    },
    // COMPONENT FUNC
    onDeleteDialog (item) {
      this.model_delete_dialog = item
      this.model_delete_dialog.show = true
    },
    onSMSDialog () {
      this.smsDialog.show = true
    },
    onCookModify () {
      this.isCookModify = !this.isCookModify
    },
    onDeliveryModify () {
      this.isDeliveryModify = !this.isDeliveryModify
    },
    onDetail (index, item) {
      this.smsDialog = item
      this.smsDialog.mode = true
      this.smsDialog.date = item.rvd_date.slice(0, 10)
      this.smsDialog.time = item.rvd_date.slice(11, 16)
      this.smsDialog.show = true
    },
    getStatus (param) {
      if (param === 0) {
        return '발송 대기'
      } else if (param === 1) {
        return '발송 완료'
      } else if (param === 2) {
        return '발송 실패'
      } else if (param === 3) {
        return 'NightBlock'
      }
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', 'SMS 관리')
    this.reloadDatas()
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
    }
  },
  data () {
    return {
      model_delete_dialog: { show: false },
      smsDialog: { show: false, mode: false, time: '12:00', date: new Date().toISOString().slice(0, 10) },
      time: null,
      date: null,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      date_model: false,
      time_model: false,
      isCookModify: false,
      isDeliveryModify: false,
      items: [],
      headers: [
        {
          text: '발송상태',
          value: 'stat',
          align: 'center',
          sortable: true
        },
        {
          text: '예약일',
          value: 'rvd_date',
          align: 'center',
          sortable: true
        },
        {
          text: '제목',
          value: 'price',
          align: 'center',
          sortable: false
        },
        {
          text: '내용',
          value: 'discount',
          align: 'center',
          sortable: false
        },
        // {
        //   text: '등록일',
        //   value: 'ins_date',
        //   align: 'center',
        //   sortable: false
        // },
        {
          text: '삭제',
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
.title-overflow {
  width: 100px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.content-overflow {
  width: 200px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
</style>
