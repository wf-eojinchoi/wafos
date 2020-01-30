<template>
  <v-content>
    <v-layout row>
      <v-flex xs12>
        <v-card>
          <v-card-text>
            <v-flex xs12 text-xs-right>
              <v-btn color="primary" round small @click="onSMSDialog()">하트 등록</v-btn>
            </v-flex>
            <!-- SMS LIST -->
            <v-data-table
              :items="items"
              :headers="headers"
              :pagination.sync="pagination"
              :rows-per-page-items="[10,{'text':'All','value':-1}]"
              :total-items="totalitems"
              :loading="loading"
              no-data-text="등록된 내용이 없습니다"
              light
            >
              <template slot="items" slot-scope="props">
                <tr style="cursor: pointer;">
                  <td class="text-xs-center">{{ props.item.id }}</td>
                  <td class="indigo--text" style="cursor: pointer;" @click="onDetail(props.index, props.item)"><div class="content-overflow">{{ props.item.title }}</div></td>
                  <td class="indigo--text" style="cursor: pointer;" @click="onDetail(props.index, props.item)">{{ props.item.point }}</td>
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
                type="number"
                label="하트"
                v-model="smsDialog.point"
                single-line></v-text-field>
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
          <span class="subheading">삭제하시겠습니까?</span>
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
  name: 'PointMgr',
  methods: {
    // API
    reloadDatas () {
      this.loading = true
      this.$store.dispatch('HeartList', {
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
      this.$store.dispatch('HeartRegister', item)
        .then((result) => {
          this.reloadDatas()
          this.smsDialog = { show: false }
        })
        .catch((result) => {
          this.error = '등록에 실패했습니다'
        })
    },
    modifyData (item) {
      this.$store.dispatch('HeartModify', item)
        .then((result) => {
          this.reloadDatas()
          this.smsDialog = { show: false }
        })
        .catch((result) => {
          this.error = '수정에 실패했습니다'
        })
    },
    deleteData (item) {
      this.$store.dispatch('HeartDelete', item.id)
        .then((result) => {
          this.reloadDatas()
          this.model_delete_dialog = { show: false }
        })
        .catch((result) => {
          this.error = '삭제가 실패했습니다'
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
      this.smsDialog.point = item.point
      this.smsDialog.show = true
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '하트 지급 관리')
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
      smsDialog: { show: false, mode: false, point: 0 },
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
          text: 'id',
          value: 'id',
          align: 'center',
          sortable: false
        },
        {
          text: '제목',
          value: 'title',
          align: 'center',
          sortable: true
        },
        {
          text: '하트',
          value: 'point',
          align: 'center',
          sortable: true
        },
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
