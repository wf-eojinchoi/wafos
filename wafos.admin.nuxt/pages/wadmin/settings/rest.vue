<template>
  <v-content>
    <v-layout>
      <v-flex>
        <v-sheet height="500">
          <v-calendar
            :now="today"
            :value="today"
            color="primary"
          >
            <template
              slot="day"
              slot-scope="{ date }"
            >
              <template v-for="event in eventsMap[date]">
                <v-menu
                  :key="event.title"
                  v-model="event.open"
                  full-width
                  offset-x
                >
                  <div
                    v-if="!event.time"
                    slot="activator"
                    v-ripple
                    class="my-event"
                    v-html="event.title"
                  ></div>
                  <v-card
                    color="grey lighten-4"
                    min-width="350px"
                    flat
                  >
                    <v-toolbar
                      color="primary"
                      dark
                    >
                      <v-btn icon>
                        <v-icon>edit</v-icon>
                      </v-btn>
                      <v-toolbar-title v-html="event.title"></v-toolbar-title>
                      <v-spacer></v-spacer>
                      <v-btn icon>
                        <v-icon>favorite</v-icon>
                      </v-btn>
                      <v-btn icon>
                        <v-icon>more_vert</v-icon>
                      </v-btn>
                    </v-toolbar>
                    <v-card-title primary-title>
                      <span v-html="event.details"></span>
                    </v-card-title>
                    <v-card-actions>
                      <v-btn
                        flat
                        color="secondary"
                      >
                        Cancel
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-menu>
              </template>
            </template>
          </v-calendar>
        </v-sheet>
      </v-flex>
    </v-layout>
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
                          <v-btn color="primary" @click="onRegister()">휴일 추가</v-btn>
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
  layout: 'wadmin',
  name: 'SettingsHolidayList',
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
    registerData (item) {
      this.$store.dispatch('holidayRegister', item)
        .then((result) => {
          this.reloadDatas()
          this.model_register_dialog = { show: false }
        })
        .catch((result) => {
          this.error = 'Holiday 등록에 실패했습니다'
        })
    },
    modifyData (item) {
      this.$store.dispatch('holidayModify', item)
        .then((result) => {
          this.reloadDatas()
          this.model_register_dialog = { show: false }
        })
        .catch((result) => {
          this.error = 'Holiday 수정에 실패했습니다'
        })
    },
    deleteData (item) {
      this.$store.dispatch('holidayDelete', item.id)
        .then((result) => {
          this.reloadDatas()
          this.model_delete_dialog = { show: false }
        })
        .catch((result) => {
          this.error = 'Holiday 수정에 실패했습니다'
        })
    },
    // COMPONENT FUNC
    onDeleteDialog (item) {
      this.model_delete_dialog = item
      this.model_delete_dialog.show = true
    },
    onRegister () {
      this.model_register_dialog.show = true
    },
    onDetail (index, item) {
      this.model_register_dialog = item
      this.model_register_dialog.mode = true
      this.model_register_dialog.show = true
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '휴일 관리')
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
          text: 'ID',
          value: 'id',
          align: 'center',
          sortable: false
        },
        {
          text: '날짜',
          value: 'h_date',
          align: 'center',
          sortable: true
        },
        {
          text: '메모',
          value: 'memo',
          align: 'center',
          sortable: false
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
.font_color {
  color: darkblue;
}
.my-event {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-radius: 2px;
    background-color: #1867c0;
    color: #ffffff;
    border: 1px solid #1867c0;
    width: 100%;
    font-size: 12px;
    padding: 3px;
    cursor: pointer;
    margin-bottom: 1px;
  }
</style>
