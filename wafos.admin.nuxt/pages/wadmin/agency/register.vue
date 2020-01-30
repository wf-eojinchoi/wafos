<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 >
        <v-layout row pa-2>
          <v-flex xs12 >
            <table width="100%">
              <tbody>
                <td >
                  <v-layout row>
                    <v-flex text-xs-right pt-1>
                      <v-btn color="primary" @click="onRegister()">등록</v-btn>
                    </v-flex>
                  </v-layout>
                </td>
              </tbody>
            </table>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-subheader class="black--text">가맹점 정보 입력</v-subheader>
          <v-layout wrap pa-4>
            <v-flex xs12>
              <v-layout wrap>
                <v-flex xs3>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="가맹점 ID"
                    hint="기본 비밀번호 - 전화번호 뒷자리"
                    persistent-hint></v-text-field>
                </v-flex>
                <v-flex xs3 pl-2>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="가맹점 코드"></v-text-field>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex xs12>
              <v-layout wrap>
                <v-flex xs3>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="가맹점 이름"></v-text-field>
                </v-flex>
                <v-flex xs3 pl-2>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="점주 이름"></v-text-field>
                </v-flex>
                <v-flex xs3 pl-2>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="사업자등록번호"></v-text-field>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex xs12>
              <v-layout wrap>
                <v-flex xs3>
                  <v-text-field
                    color="primary lighten-2"
                    type="number"
                    label="가맹점 전화번호"></v-text-field>
                </v-flex>
                <v-flex xs3 pl-2>
                  <v-text-field
                    color="primary lighten-2"
                    type="number"
                    label="휴대폰번호"></v-text-field>
                </v-flex>
                <v-flex xs3 pl-2>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="IP 주소"></v-text-field>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex xs12>
              <v-layout wrap>
                <v-flex xs5>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="가맹점 주소"></v-text-field>
                </v-flex>
                <v-flex xs4 pl-2>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    label="상세주소"></v-text-field>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex xs12>
              <v-layout wrap>
                <v-flex xs5>
                  <v-textarea
                    color="primary lighten-2"
                    type="text"
                    label="비고"></v-textarea>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
    <!-- Dialog Area -->
    <v-dialog v-model="capacityDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>

          <v-flex xs12>
            <v-select
              :items="temp_items"
              v-model="sel_model"
              label="Select"
              item-text="name"
              item-value="id"
              multiple
              chips
              return-object
              max-height="200"
              scrollable
              autocomplete
            >
              <template slot="selection" slot-scope="data">
                <v-chip
                  :selected="data.selected"
                  :key="JSON.stringify(data.item)"
                  close
                  class="chip--select-multi"
                  @input="data.parent.selectItem(data.item)"
                >
                  {{ data.item.name }}
                </v-chip>
              </template>
              <template slot="item" slot-scope="data">
                <template v-if="typeof data.item !== 'object'">
                  <v-list-tile-content v-text="data.item"></v-list-tile-content>
                </template>
                <template v-else>
                  <v-list-tile-content>
                    <v-list-tile-title v-html="data.item.name"></v-list-tile-title>
                  </v-list-tile-content>
                </template>
              </template>
            </v-select>
          </v-flex>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="addCapacity(sel_model)">추가하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="capacityDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="alertDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">변경된 데이터를 저장하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="modifyData(recipeDetailData)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="alertDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="snackbar"
      :color="'success'"
      :multi-line="snackbar_mode === 'multi-line'"
      :timeout="2500"
      :vertical="snackbar_mode === 'vertical'"
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
  name: 'AgencyRegister',
  // props: [
  //   'rid', 'mode'
  // ],
  methods: {
    // API
    loadDetailData () {
      this.loading = true
      this.$store.dispatch('recipeDetail', this.$route.params.rid)
        .then((result) => {
          this.loading = false
          this.sel_model = result.capacities
          this.recipeDetailData = result
          this.ori_capacities = result.capacities
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    isValidation () {
      // if(this.registData.)
      var percent = 0
      this.recipeDetailData.capacities.forEach(f => {
        percent += ~~f.percent
      })
      if (percent !== 100) {
        return false
      }
      return true
    },
    modifyData (item) {
      if (!this.isValidation()) {
        this.alertDialog = { show: false }
        this.snackbar = true
        return
      }

      let args = Object.assign({}, item)
      args.capacities = this.recipeDetailData.capacities.map(v => {
        return `${v.id},${v.percent}`
      }).join('|')

      // if (JSON.stringify(this.recipeDetailData.capacities) !== JSON.stringify(this.ori_capacities)) {
      //   for (let o of this.ori_capacities) {
      //     console.log(o['id'])
      //     // console.log('%s : %o', key, value)
      //   }
      // }
      this.$store.dispatch('recipeModify', args)
        .then((result) => {
          this.loadDetailData()
          this.isModify = !this.isModify
          this.alertDialog = { show: false }
        })
        .catch((result) => {
          alert(result.detail)
          this.alertDialog = { show: false }
          // this.error = 'recipe 수정에 실패했습니다'
        })
    },
    deleteData (item) {
      this.$store.dispatch('recipeDelete', item.id)
        .then((result) => {
          this.loadDetailData()
          this.deleteDialog = { }
        })
        .catch((result) => {
          this.error = 'recipe 삭제에 실패했습니다'
        })
    },
    // COMPONENT FUNC
    onBack (_path) {
      if (_path) {
        this.$router.go(-1)
      }
    },
    onModify () {
      if (this.isModify) {
        this.alertDialog.show = true
      } else {
        // 상태 전환
        this.isModify = !this.isModify
      }
    },
    addCapacity (_selectitem) {
      console.log('CAPA : %o', _selectitem)
      this.recipeDetailData.capacities = _selectitem
      this.capacityDialog = { show: false }
    },
    showDialog () {
      console.log('sel_model : %o', this.sel_model)

      this.$store.dispatch('capacityList')
        .then((result) => {
          console.log(result)
          this.temp_items = result.results
          this.capacityDialog.show = true
        })
        .catch((result) => {
          this.error = 'Capacity 불러오는데 실패했습니다'
        })
    },
    initCapacityData () {
      this.recipeDetailData.capacities = []
      this.temp_items = []
      this.sel_model = []
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
    onRegister () {
      this.snackbar = true
      this.snackbar_msg = '등록'
    }
  },
  mounted () {
    this.$store
      .dispatch('updateTitle', '가맹점 등록')
  },
  data () {
    return {
      snackbar: false,
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
      mode: this.$route.params.mode,
      alertDialog: { show: false },
      capacityDialog: {
        show: false
      },
      isModify: false,
      max3chars: (v) => ~~v <= 100 || '값이 너무 큽니다.',
      recipeDetailData: {},
      ori_capacities: [],
      sel_model: [],
      temp_items: [],
      headers: [
        {
          text: '가맹점',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '이름',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '사용일',
          value: '',
          align: 'center',
          sortable: true
        },
        {
          text: '이용금액',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '타입',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '이용시간',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: 'reserved',
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
