<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 >
        <v-card>
          <v-card-title>
            <v-flex xs6>
              <v-breadcrumbs flat>
                <v-icon slot="divider">chevron_right</v-icon>
                <v-breadcrumbs-item
                  v-for="item in bread_items"
                  :key="item.text"
                  :disabled="item.disabled"
                  @click.native="onBack(item.path)"
                  >
                    {{ item.text }}
                </v-breadcrumbs-item>
              </v-breadcrumbs>
            </v-flex>
            <v-flex xs6 text-xs-right>
              <v-btn color="primary" round @click="onRegisterDialog()">등록</v-btn>
            </v-flex>
            <v-layout row>
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="search"
                label="Search"
                single-line
                hide-details></v-text-field>
            </v-layout>
          </v-card-title>
          <v-card-text>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="model_delete_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">'{{ model_delete_dialog.name }}' 재료를 삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="deleteData(model_delete_dialog.id)">삭제하기</v-btn>
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
                :value="model_register_dialog.upd_date"
                disabled
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="재료명"
                :value="model_register_dialog.name"
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs4>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="무게"
                :value="model_register_dialog.weight"
                suffix="g"
                ></v-text-field>
            </v-flex>
            <v-flex xs8 ml-3>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="가격"
                :value="model_register_dialog.price"
                suffix="원"
                ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" v-if="!model_register_dialog.mode" flat @click="registerData(model_register_dialog.id)">등록하기</v-btn>
          <v-btn color="primary darken-1" v-if="model_register_dialog.mode" flat @click="modifyData(model_register_dialog.id)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_register_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'SettingsAdmin',
  methods: {
    toggleAll () {
      if (this.selected.length) this.selected = []
      else this.selected = this.data.slice()
    },
    changeSort (column) {
      if (this.pagination.sortBy === column) {
        this.pagination.descending = !this.pagination.descending
      } else {
        this.pagination.sortBy = column
        this.pagination.descending = false
      }
    },
    onDeleteDialog (user) {
      this.model_delete_dialog.show = true
    },
    onRegisterDialog (user) {
      this.model_register_dialog.show = true
    },
    onDetail (item) {
      this.model_register_dialog = item
      this.model_register_dialog.mode = true
      this.model_register_dialog.show = true
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', 'Capacity 관리')
  },
  data () {
    return {
      model_delete_dialog: { show: false },
      model_register_dialog: { show: false, mode: false },
      userSwitch: false,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      items: [
        {
          id: '1',
          email: 'sunkyu.yun@moreum.co.kr',
          name: '윤순규',
          ins_date: '2018-06-27'
        },
        {
          id: '2',
          email: 'sunkyu.yun@moreum.co.kr',
          name: '윤',
          ins_date: '2018-06-27'
        }
      ],
      selected: [],
      headers: [
        {
          text: 'ID',
          value: 'id',
          align: 'center',
          sortable: true
        },
        {
          text: 'EMAIL',
          value: 'email',
          align: 'center',
          sortable: true
        },
        {
          text: '이름',
          value: 'name',
          align: 'left',
          sortable: true
        },
        {
          text: '등록일',
          value: 'upd_date',
          align: 'center',
          sortable: true
        },
        {
          text: '삭제',
          value: '',
          align: 'center',
          sortable: false
        }
      ],
      bread_items: [
        {
          text: '관리자계정 관리',
          path: true,
          disabled: false
        },
        {
          text: '관리자계정 상세보기',
          path: false,
          disabled: true
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
