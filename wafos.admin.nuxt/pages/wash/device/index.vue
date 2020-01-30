<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn
         icon
         @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-toolbar-title>기기 관리</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>
    </v-layout>
    <v-container fluid grid-list-md>
      <v-data-iterator
        :items="items"
        :rows-per-page-items="[20,{'text':'All','value':-1}]"
        :pagination.sync="pagination"
        content-tag="v-layout"
        row
        wrap
      >
          <v-flex
            slot="item"
            slot-scope="props"
            xs12
            sm6
            md4
            lg3>
            <v-card>
              <v-card-title class="font-weight-bold">
                <v-flex xs4>
                  {{ '컨트롤러 ID : ' + props.item.controller_id }}
                </v-flex>
                <v-spacer></v-spacer>
                <v-flex xs4 v-if="props.item.device" text-xs-right>
                  <div class="indigo--text">{{ getTypeStr(props.item.device.type) + '(' + props.item.device.kg + 'kg)' }}</div>
                </v-flex>
                <v-flex xs4 v-if="props.item.etcDevice" text-xs-right>
                  <div class="indigo--text">{{ getTypeStr(props.item.etcDevice.type) }}</div>
                </v-flex>
              </v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <!-- <v-list-tile>
                  <v-list-tile-content>기기종류:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.calories }}</v-list-tile-content>
                </v-list-tile> -->
                <!-- <v-list-tile>
                  <v-list-tile-content>용량:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.iron }}</v-list-tile-content>
                </v-list-tile> -->
                <v-list-tile>
                  <v-list-tile-content class="font-weight-bold black--text">기준금액:</v-list-tile-content>
                  <v-list-tile-content class="align-end indigo--text text-xs-right">{{ props.item.current_coin + '원' }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content class="font-weight-bold black--text">최소금액:</v-list-tile-content>
                  <v-list-tile-content class="align-end indigo--text" text-xs-right>{{ props.item.min_coin + '원' }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content class="font-weight-bold black--text">최대금액:</v-list-tile-content>
                  <v-list-tile-content class="align-end indigo--text">{{ props.item.max_coin + '원' }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content class="font-weight-bold black--text">기준시간(분):</v-list-tile-content>
                  <v-list-tile-content class="align-end indigo--text">{{ props.item.min_etc_coin + '분' }}</v-list-tile-content>
                </v-list-tile>
              </v-list>
              <v-divider></v-divider>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="green darken-1" flat @click="onModify(props.item)">요금수정</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
      </v-data-iterator>
    </v-container>
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
    <v-dialog v-model="device_register_dialog.show" max-width="90%" lazy persistent>
      <v-card>
        <v-card-title class="font-weight-bold">
          장비 요금 수정
        </v-card-title>
        <v-card-text>
          <v-layout row wrap>
            <v-flex xs12>
              <table width="100%">
                <tr>
                  <td class="text-xs-left">
                    <div v-if="device_register_dialog.device">
                      {{ '기기종류 : ' + getTypeStr(device_register_dialog.device.type) }}
                    </div>
                    <div v-if="device_register_dialog.etcDevice">
                      {{ '기기종류 : ' + getTypeStr(device_register_dialog.etcDevice.type) }}
                    </div>
                  </td>
                  <td class="text-xs-left">
                    <div v-if="device_register_dialog.device">
                      {{ '용량 : ' + device_register_dialog.device.kg + ' kg' }}
                    </div>
                  </td>
                </tr>
                <tr v-if="device_register_dialog.device">
                  <td class="text-xs-left">{{ '제조사 : ' + device_register_dialog.device.brand.name }}</td>
                  <td class="text-xs-left">{{ '모델 : ' + device_register_dialog.device.model.name }}</td>
                </tr>
              </table>
            </v-flex>
            <v-flex xs12 mt-4>
              <v-layout row wrap>
                <v-flex xs6>
                  <v-text-field
                    color="primary lighten-2"
                    type="number"
                    v-model="device_register_dialog.controller_id"
                    :disabled="true"
                    label="컨트롤러 ID"></v-text-field>
                </v-flex>
                <v-flex xs6 pl-2>
                  <v-text-field
                    color="primary lighten-2"
                    type="text"
                    :disabled="true"
                    :value="device_register_dialog.used?'사용중':'사용안함'"
                    label="사용여부"></v-text-field>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="number"
                suffix="원"
                v-model="device_register_dialog.current_coin"
                label="기준금액"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="number"
                suffix="원"
                v-model="device_register_dialog.min_coin"
                label="최소금액"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="number"
                suffix="원"
                v-model="device_register_dialog.max_coin"
                label="최대금액"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="number"
                suffix="분"
                :disabled="true"
                v-model="device_register_dialog.min_etc_coin"
                label="기준시간"></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="modifyData(device_register_dialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="device_register_dialog = { show: false, agency: {} }">닫기</v-btn>
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
  name: 'AgencyDetail',
  // props: [
  //   'rid', 'mode'
  // ],
  watch: {
    pagination: {
      handler () {
        this.loadDeviceData()
      },
      deep: true
    }
  },
  methods: {
    // API
    loadDeviceData () {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      this.$store.dispatch('AgencyDeviceList', this.$store.state.adminAgency.wash)//this.$store.state.adminAgency.wash)
        .then((result) => {
          this.items = result.results
        })
        .catch((result) => {
          this.error = '삭제에 실패했습니다'
        })
    },
    // COMPONENT FUNC
    onBack () {
      this.$router.go(-1)
    },
    getTypeStr (item) {
      if (item != null) {
        return this.selTypes[item]
      } else {
        return '-'
      }
    },
    onModify (item) {
      console.log(item)
      this.device_register_dialog = item
      this.device_register_dialog.show = true
    },
    modifyData (item) {
      console.log(item.current_coin)
      if (item.current_coin.length === 0) {
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '기준금액을 입력해주세요.'
        this.loadDeviceData()
        return
      }
      var params = {
        agency: item,
        device: item.device,
        id: item.agency.id,
        adInfo_id: item.id
      }
      console.log(item)
      this.$store.dispatch('AgencyDeviceModify', params)
        .then((result) => {
          this.device_register_dialog = { show: false, agency: {} }
          this.loadDeviceData()
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '가맹점 상세보기')
    this.loadDeviceData()
  },
  data () {
    return {
      // [[ Select Device Dialog
      pagination: {},
      search: null,
      loading: false,
      totalitems: 0,
      standardCourseDialog: { show: false },
      selTypes: [ '세탁기', '건조기', '트롬스타일러', '운동화세탁기', '운동화건조기', '냉난방', '세탁용품' ],
      deviceItems: [],
      deviceHeaders: [
        {
          text: '제조사',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '모델',
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
          text: '용량(kg)',
          value: '',
          align: 'center',
          sortable: false
        }
      ],
      items: [],
      headers: [
        {
          text: '컨트롤러ID',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '기기종류',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '용량(Kg)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '기준코인(요금)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '최소코인(요금)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '최대코인(요금)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '분당요금',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '상태',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '',
          value: '',
          align: 'center',
          sortable: false
        }
      ],
      actionItems: [ '코스 설정', '장비 수정'],
      setCtrl: [],
      selectCtrlItem: null,
      selUsed: ['사용', '사용안함'],
      selectUsedItem: '사용',
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      // dialog
      device_register_dialog: {
        show: false,
        mode: false,
        agency: {}
      },
      alertDialog: { show: false },
      select_device_dialog: { show: false },
      select_etc_device_dialog: { show: false }
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
