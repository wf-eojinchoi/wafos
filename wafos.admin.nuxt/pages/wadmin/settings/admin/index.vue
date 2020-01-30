<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-card-title>
            <v-layout row>
              <v-flex xs12 >
                <table width="100%">
                  <tbody>
                    <td >
                      <v-layout row>
                        <v-flex text-xs-right pt-1>
                          <v-btn color="primary" @click="onRegister()">계정 추가</v-btn>
                        </v-flex>
                      </v-layout>
                    </td>
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
            v-model="table_selected"
            no-data-text="등록된 데이터가 없습니다"
            no-results-text="검색 결과가 없습니다"
            select-all
            light>

            <template slot="items" slot-scope="props">
              <tr >
                <td>
                  <v-checkbox
                    v-model="props.selected"
                    primary
                    hide-details
                  ></v-checkbox>
                </td>
                <td class="text-xs-center">{{ props.item.id }}</td>
                <td class="text-xs-center indigo--text" style="cursor: pointer;" @click="onDetail(props.item)">{{ props.item.login_id }}</td>
                <td class="text-xs-center indigo--text" style="cursor: pointer;" @click="onDetail(props.item)">{{ props.item.name }}</td>
                <td class="text-xs-center">{{ props.item.reg_dttm }}</td>
                <td class="text-xs-center">
                  <v-icon class="red--text" @click.stop="onDeleteDialog(props.item.id)">delete_forever</v-icon>
                </td>
              </tr>
            </template>
          </v-data-table>
          <!-- <v-layout row pa-2>
            <tr >
              <td class="text-xs-center">
                <v-btn color="primary" small :disabled="!table_selected.length > 0" @click="selectDeleteDialog()">삭제</v-btn>
              </td>
              <td class="text-xs-center"></td>
              <td class="text-xs-center"></td>
              <td class="text-xs-center"></td>
              <td class="text-xs-center"></td>
              <td class="text-xs-center"></td>
            </tr>
          </v-layout> -->
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="model_delete_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">선택한 계정을 삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="deleteData(model_delete_dialog.id)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_delete_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_register_dialog.show" max-width="50%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="아이디"
                v-model="model_register_dialog.login_id"
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="이름"
                v-model="model_register_dialog.name"
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row v-if="!model_register_dialog.mode">
            <v-flex xs12>
              <v-form v-model="valid">
                <v-text-field
                  color="primary lighten-2"
                  label="비밀번호"
                  type="password"
                  v-model="model_register_dialog.pwd"
                  ></v-text-field>
              </v-form>
            </v-flex>
          </v-layout>
          <v-layout row v-else>
            <v-flex xs12>
              <v-btn color="info" block @click="onInitPWD(model_register_dialog)">비밀번호 초기화</v-btn>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              접근권한설정
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs6>
              <v-switch
                v-model="model_register_dialog.enterMember"
                label="고객관리"
              ></v-switch>
              <v-switch
                v-model="model_register_dialog.enterDevice"
                label="장비관리"
              ></v-switch>
              <v-switch
                v-model="model_register_dialog.enterHoliday"
                label="휴일관리"
              ></v-switch>
            </v-flex>
            <v-flex xs6>
              <v-switch
                v-model="model_register_dialog.enterAgency"
                label="가맹점관리"
              ></v-switch>
              <v-switch
                v-model="model_register_dialog.enterPayment"
                label="매출관리"
              ></v-switch>
              <v-switch
                v-model="model_register_dialog.enterAccount"
                label="관리자계정관리"
              ></v-switch>
            </v-flex>
          </v-layout>
          <!-- <v-layout row>
                <v-subheader>권한 설정</v-subheader>
            </v-layout>
            <v-layout row>
                <v-flex xs12 ml-1>
                <v-data-table
                  :items="admin_prop"
                  hide-actions
                  hide-headers
                >
                  <template slot="items" slot-scope="props">
                    <td>{{ props.item.name }}</td>
                    <td class="text-xs-center"><v-switch v-model="props.item.swich"></v-switch></td>
                  </template>
                </v-data-table>
              </v-flex>
            </v-layout> -->
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" v-if="!model_register_dialog.mode" flat @click="registerData(model_register_dialog)">등록하기</v-btn>
          <v-btn color="primary darken-1" v-if="model_register_dialog.mode" flat @click="modifyData(model_register_dialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_register_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="selectedDeleteDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">선택하신 관리자 계정을 삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="onDeleteSelecteList(selectedDeleteDialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="selectedDeleteDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="snackbar"
      :color="'error'"
      :multi-line="snackbar_mode === 'multi-line'"
      :timeout="2500"
      :vertical="snackbar_mode === 'vertical'"
      >
      {{ errMessage }}
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
  name: 'SettingsAdmin',
  methods: {
    // API
    reloadDatas () {
      this.loading = true
      this.$store.dispatch('adminUserList')
        .then((result) => {
          this.loading = false
          this.items = result.results
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    // COMPONENT FUNC
    onDeleteDialog (user) {
      this.model_delete_dialog.id = user
      this.model_delete_dialog.show = true
    },
    registerData (item) {
      this.$store.dispatch('adminUserRegister', item)
        .then((result) => {
          this.reloadDatas()
          this.model_register_dialog = { show: false }
        })
        .catch((result) => {
          this.error = '관리자 계정 등록에 실패했습니다'
        })
    },
    modifyData (item) {
      this.$store.dispatch('adminUserModify', item)
        .then((result) => {
          this.reloadDatas()
          this.model_register_dialog = { show: false }
        })
        .catch((result) => {
          this.error = '관리자 계정 수정에 실패했습니다'
        })
    },
    deleteData (aId) {
      this.$store.dispatch('adminUserDelete', aId)
        .then((result) => {
          this.reloadDatas()
          this.model_delete_dialog = { show: false }
        })
        .catch((result) => {
          this.error = '관리자 계정 삭제에 실패했습니다'
        })
    },
    onRegister (user) {
      // this.$router.push('/config/admin/register')
      this.model_register_dialog.show = true
    },
    onDetail (item) {
      this.model_register_dialog = item
      this.model_register_dialog.mode = true
      this.model_register_dialog.show = true
    },
    selectDeleteDialog () {
      this.selectedDeleteDialog = this.table_selected
      this.selectedDeleteDialog.show = true
    },
    onDeleteSelecteList (item) {
      // 주문 상태를 변경
      item.sel_data = []
      this.table_selected.forEach(f => {
        item.sel_data.push(f.id)
      })
      this.$store.dispatch('selectDeleteAdminUserList', item)
        .then((result) => {
          this.selectedDeleteDialog = { show: false }
          this.reloadDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
        })
    },
    onInitPWD (item) {
      this.$store.dispatch('adminInitPWD', item)
        .then((result) => {
          this.errMessage = '비밀번호가 0000 으로 초기화 되었습니다.'
          this.snackbar = true
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
        })
    }
  },
  mounted () {
    if (this.$cookie.get('admin-id')  > 2) {
      this.$router.go(-1)
      return
    }
    this.$store.dispatch('updateTitle', '관리자계정 관리')
    this.reloadDatas()
  },
  data () {
    return {
      snackbar_mode: '',
      errMessage: null,
      snackbar: false,
      table_selected: [],
      selectedDeleteDialog: { show: false },
      model_delete_dialog: { show: false },
      model_register_dialog: { show: false, mode: false },
      userSwitch: false,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      items: [],
      selected: [],
      valid: false,
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || '메일 형식이 올바르지 않습니다.'
      ],
      headers: [
        {
          text: 'ID',
          value: 'id',
          align: 'center',
          sortable: true
        },
        {
          text: 'ID',
          value: 'login_id',
          align: 'center',
          sortable: true
        },
        {
          text: '이름',
          value: 'name',
          align: 'center',
          sortable: true
        },
        {
          text: '등록일',
          value: 'reg_dttm',
          align: 'center',
          sortable: true
        },
        {
          text: '',
          value: '',
          align: 'center',
          sortable: false
        }
      ],
      admin_prop: [
        {
          name: '조리관리',
          swich: false
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
