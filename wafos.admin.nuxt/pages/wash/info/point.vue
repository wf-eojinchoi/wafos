<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn icon @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-toolbar-title>적립금 설정</v-toolbar-title>

        <v-spacer></v-spacer>
      </v-toolbar>
    </v-layout>
    <div>
      <v-layout wrap>
        <v-flex xs12 ma-2>
          <v-card>
            <v-layout row wrap>
              <v-subheader class="black--text">적립금 설정</v-subheader>
              <v-icon
                color="primary"
                style="cursor: pointer;"
                @click="onPointModify()"
              >settings_applications</v-icon>
              <v-layout row pt-1 ml-4 v-if="isPointModify">
                <v-btn color="success" @click="alertPointDialog.show = true" small>수정</v-btn>
              </v-layout>
            </v-layout>
            <v-layout wrap>
              <v-flex xs12 ma-2>
                <v-layout wrap pa-2>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="사용가능 포인트"
                          v-model="pointData.use_point"
                          :disabled="!isPointModify"
                          persistent-hint
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12 ma-2>
          <v-card>
            <v-subheader class="black--text">현금 기본 포인트</v-subheader>
            <v-layout wrap pa-2>
              <v-flex xs6>
                <v-layout wrap pa-2>
                  <v-flex xs12>주중</v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="적립 포인트"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_day_new"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_day_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_day_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_day_shoes_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_day_shoes_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                </v-layout>
              </v-flex>
              <v-flex xs6>
                <v-layout wrap pa-2>
                  <v-flex xs12>주말</v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="적립 포인트"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_weekend_new"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_weekend_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_weekend_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_weekend_shoes_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_weekend_shoes_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12 ma-2>
          <v-card>
            <v-subheader class="black--text">카드 기본 포인트</v-subheader>
            <v-layout wrap pa-2>
              <v-flex xs6>
                <v-layout wrap pa-2>
                  <v-flex xs12>주중</v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="적립 포인트"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_day_new"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_day_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_day_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_day_shoes_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_day_shoes_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                </v-layout>
              </v-flex>
              <v-flex xs6>
                <v-layout wrap pa-2>
                  <v-flex xs12>주말</v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="적립 포인트"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_weekend_new"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_weekend_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_weekend_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_weekend_shoes_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.def_card_weekend_shoes_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12 ma-2>
          <v-card>
            <v-subheader class="black--text">이벤트 포인트</v-subheader>
            <v-layout wrap pa-2>
              <v-flex xs12>
                <v-layout wrap pa-2>
                  <v-flex xs6>
                    <v-menu
                      :close-on-content-click="false"
                      v-model="menu1"
                      :nudge-right="40"
                      lazy
                      transition="scale-transition"
                      offset-y
                      full-width
                      :disabled="!isPointModify"
                      min-width="290px"
                    >
                      <v-text-field
                        slot="activator"
                        v-model="pointData.evt_st_date"
                        label="시작날짜"
                        prepend-icon="event"
                        readonly
                      ></v-text-field>
                      <v-date-picker v-model="pointData.evt_st_date" @input="menu1 = false"></v-date-picker>
                    </v-menu>
                  </v-flex>
                  <v-flex xs6 pl-2>
                    <v-menu
                      :close-on-content-click="false"
                      v-model="menu2"
                      :nudge-right="40"
                      lazy
                      transition="scale-transition"
                      offset-y
                      full-width
                      :disabled="!isPointModify"
                      min-width="290px"
                    >
                      <v-text-field
                        slot="activator"
                        v-model="pointData.evt_et_date"
                        label="종료날짜"
                        prepend-icon="event"
                        readonly
                      ></v-text-field>
                      <v-date-picker v-model="pointData.evt_et_date" @input="menu2 = false"></v-date-picker>
                    </v-menu>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
            <v-layout wrap pa-2>
              <v-flex xs6>
                <v-layout wrap pa-2>
                  <v-flex xs12>주중</v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="적립 포인트"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_day_new"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_day_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_day_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_day_shoes_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_day_shoes_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                </v-layout>
              </v-flex>
              <v-flex xs6>
                <v-layout wrap pa-2>
                  <v-flex xs12>주말</v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="적립 포인트"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_weekend_new"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_weekend_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_weekend_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 세탁"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_weekend_shoes_wash"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      color="primary lighten-2"
                      type="number"
                      label="운동화 건조"
                      suffix="%"
                      :disabled="!isPointModify"
                      v-model="pointData.evt_weekend_shoes_dry"
                      persistent-hint
                    ></v-text-field>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
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
    <v-dialog v-model="alertPointDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">변경된 데이터를 저장하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestPointModify(pointData)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="alertPointDialog = { show: false }">닫기</v-btn>
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
  name: 'AgencyDetail',
  // props: [
  //   'rid', 'mode'
  // ],
  methods: {
    // API
    loadDetailData () {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      this.$store.dispatch('AgencyPointInfo', this.$store.state.adminAgency.wash)
        .then((result) => {
          this.pointData = result
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
        })
    },
    modifyData (item) {
      console.log('#')
    },
    // COMPONENT FUNC
    onBack () {
      this.$router.go(-1)
    },
    onPointModify () {
      // 상태 전환
      this.isPointModify = !this.isPointModify
    },
    requestPointModify (item) {
      if (item.evt_st_date > item.evt_et_date) {
        this.alertPointDialog = { show: false }
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '시작일이 종료일보다 클 수 없습니다. 이벤트 날짜를 다시 선택해주세요.'
      } else {
        this.$store.dispatch('AgencyPointModify', item)
          .then((result) => {
            this.alertPointDialog = { show: false }
            this.isPointModify = !this.isPointModify
            this.snackbar = true
            this.snackbar_color = 'success'
            this.snackbar_msg = '수정되었습니다.'
          })
          .catch((result) => {
            this.error = result.msg
          })
      }
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '가맹점 상세보기')
    this.loadDetailData()
  },
  data () {
    return {
      // [[ Select Device Dialog
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      pointData: {},
      //
      date1: null,
      menu1: false,
      date2: null,
      menu2: false,
      isPointModify: false,
      alertPointDialog: { show: false },
      alertDialog: { show: false }
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
