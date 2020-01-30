<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn
         icon
         @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-toolbar-title>매출현황관리</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>
    </v-layout>
    <!-- <v-layout wrap>
      <v-flex xs12 >
        <v-card>
          <v-layout row pa-2>
            <table>
              <tbody>
                <td>
                  <v-layout row>
                    <v-flex xs4>
                      <v-select
                        :items="selItems"
                        v-model="selectItem"
                        label="기간 선택"
                      ></v-select>
                    </v-flex>
                    <v-flex xs3>
                      <v-menu
                        :close-on-content-click="false"
                        v-model="menu1"
                        :nudge-right="40"
                        lazy
                        transition="scale-transition"
                        offset-y
                        full-width
                        min-width="290px"
                      >
                        <v-text-field
                          slot="activator"
                          v-model="date1"
                          label="시작날짜"
                          prepend-icon="event"
                          readonly
                        ></v-text-field>
                        <v-date-picker v-model="date1" @input="menu1 = false"></v-date-picker>
                      </v-menu>
                    </v-flex>
                    <v-flex xs3>
                      <v-menu
                        :close-on-content-click="false"
                        v-model="menu2"
                        :nudge-right="40"
                        lazy
                        transition="scale-transition"
                        offset-y
                        full-width
                        min-width="290px"
                      >
                        <v-text-field
                          slot="activator"
                          v-model="date2"
                          label="종료날짜"
                          prepend-icon="event"
                          readonly
                        ></v-text-field>
                        <v-date-picker v-model="date2" @input="menu2 = false"></v-date-picker>
                      </v-menu>
                    </v-flex>
                  </v-layout>
                </td>
                <td width="5%">&nbsp;</td>
                <td>
                  <v-layout row>
                    <v-flex xs4 sm4 d-flex>
                      <v-select
                        :items="selStatusItems"
                        v-model="selectStatusItem"
                        label="Status"
                      ></v-select>
                    </v-flex>
                    <v-flex xs6 sm6 pl-2>
                      <v-text-field
                        :disabled="inputEnabled"
                        v-model="inputKeyword"
                        label="검색어 입력"
                        single-line
                      ></v-text-field>
                    </v-flex>
                    <v-flex xs2 text-xs-center pt-2>
                      <v-btn color="primary" @click="onSearch()">검색</v-btn>
                    </v-flex>
                  </v-layout>
                </td>
              </tbody>
            </table>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout> -->
    <v-layout wrap>
      <v-flex xs12 >
        <v-card>
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
                <td class="text-xs-center">{{ props.item.id }}</td>
                <td class="text-xs-center">{{ props.item.h_date }}</td>
                <td class="text-xs-center">{{ props.item.memo }}</td>
                <td class="text-xs-center">
                  <v-icon class="red--text" @click.stop="onDeleteDialog(props.item)">delete_forever</v-icon>
                </td>
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
  </v-content>
</template>

<script>
export default {
  layout: 'nomenu',
  name: 'PaymentMgr',
  methods: {
    // API
    reloadDatas () {
      this.loading = true
      this.$store.dispatch('holidayList', {
        page: this.pagination.page,
        sortby: this.pagination.sortBy,
        descending: this.pagination.descending,
        query: this.search
      })
        .then((result) => {
          this.loading = false
          this.items = result.results
          console.log(result)
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
    this.$store.dispatch('updateTitle', '매출 관리')
    // this.reloadDatas()
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
    }
  },
  data () {
    return {
      table_selected: [],
      h_date: null,
      h_date_model: false,
      model_register_dialog: { show: false, mode: false },
      model_delete_dialog: { show: false },
      userSwitch: false,
      snackbar: false,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      items: [],
      selected: [],
      headers: [
        {
          text: '사용자',
          value: '',
          align: 'center',
          sortable: true
        },
        {
          text: '장비명',
          value: '',
          align: 'center',
          sortable: true
        },
        {
          text: '코스',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '이용가격',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '결제일',
          value: '',
          align: 'center',
          sortable: true
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
