<template>
  <v-content >
    <v-layout row wrap>
      <v-toolbar>
        <v-btn
         icon
         @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-toolbar-title>경고 방송 및 기기 제어 관리</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>
    </v-layout>
    <v-layout row pa-2>
      <v-layout row>
        <v-flex xs12 ma-2>
          <v-card>
            <v-card-title>
              경고 방송
            </v-card-title>
            <v-flex pa-2>
              <v-btn color="primary" block @click="onBroadcast(0)">퇴출요청</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="primary" block @click="onBroadcast(1)">장난금지</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="primary" block @click="onBroadcast(2)">동물퇴출</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="primary" block @click="onBroadcast(3)">사이렌</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="primary" block @click="onBroadcast(10)">새 알람</v-btn>
            </v-flex>
          </v-card>
        </v-flex>
      </v-layout>
    </v-layout>
    <v-layout row pa-2>
      <v-layout row>
        <v-flex xs12 ma-2>
          <v-card>
            <v-card-title>
              기기 제어
            </v-card-title>
            <v-flex pa-2>
              <v-btn color="success" block @click="onCtrlBroadcast(4)">냉난방기 켜기</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="success" block @click="onCtrlBroadcast(5)">장비전원 재시작</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="success" block @click="onCtrlBroadcast(6)">PC 재부팅</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="success" block @click="onCtrlBroadcast(7)">코인 신호 보내기</v-btn>
            </v-flex>
            <v-flex pa-2>
              <v-btn color="success" block @click="onCtrlBroadcast(8)">업데이트 신호보내기</v-btn>
            </v-flex>
          </v-card>
        </v-flex>
      </v-layout>
    </v-layout>
    <v-dialog v-model="broadCastDialog.show" max-width="80%">
      <v-card>
        <v-card-text>
          <v-layout row wrap>
            <v-flex xs12 v-if="broadCastDialog.index === 0">
              불청객 퇴출방송입니다.
            </v-flex>
            <v-flex xs12 v-if="broadCastDialog.index === 1">
              장난금지 방송입니다.
            </v-flex>
            <v-flex xs12 v-if="broadCastDialog.index === 2">
              애완동물 퇴출 방송입니다.
            </v-flex>  
            <v-flex xs12 v-if="broadCastDialog.index === 3">
              사이렌 경고 방송입니다.
            </v-flex> 
            <v-flex xs12 v-if="broadCastDialog.index === 10">
              새로운 경고 방송입니다.
            </v-flex>   
            <v-flex xs12>
              1분 이내에 점포에서 경고방송이 작동됩니다.
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestData(broadCastDialog)">전송</v-btn>
          <v-btn color="grey darken-1" flat @click.native="broadCastDialog = { show: false }">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="controlBroadCastDialog.show" max-width="80%">
      <v-card>
        <v-card-text v-if="controlBroadCastDialog.index === 5"><!-- if문 시작 -->
          <v-layout row wrap>
            <v-flex xs12>
              신호가 기계에 전달되기까지 최장 30초 걸립니다.<br>
              전송하시고 30초 후에 확인 해주세요.<br>
              (다른 고객이 계속 사용하고 있으면 더 지연 될 수 있으며, 신호는 최대 12회까지 보낼 수 있습니다.)<br>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              <v-select
                :items="setCtrl"
                v-model="controlBroadCastDialog.ctrl_id"
                label="컨트롤러 ID 선택"
              ></v-select>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              <v-select
                :items="setOnoff"
                v-model="controlBroadCastDialog.onoff"
                label="명령어 선택"
              ></v-select>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-text v-else-if="controlBroadCastDialog.index < 7"><!-- elseif문 index<7 -->
          <v-layout row wrap>
            <v-flex xs12 v-if="controlBroadCastDialog.index === 4">
              냉난방기를 가동합니다.<br>
              1분 이내에 점포에서 냉난방기가 작동됩니다.
            </v-flex>
            <v-flex xs12 v-if="controlBroadCastDialog.index === 5">
              리셋 신호가 기계에 전달되기까지 최장 1분 걸립니다.<br>
              전송하시고 1분 후에 확인해주세요.<br>
              (다른 고객이 사용하고 있으면 더 지연됩니다.)<br>
              <span style="color: #0000ff;">*리셋 기능이 연결된 장비에만 작동됩니다.</span>
            </v-flex>
            <v-flex xs12 v-if="controlBroadCastDialog.index === 6">
              시스템 재부팅까지 3분 소요됩니다.<br>
              <span style="color: #ff0000;">
                * 주의 : 키오스크가 재시작됩니다.<br>
                고객 사용유무 확인 후 시도하세요.
              </span>
            </v-flex>  
          </v-layout>
        </v-card-text>
        <v-card-text v-else-if="controlBroadCastDialog.index === 7"> <!-- 동전신호 -->
          <v-layout row wrap>
            <v-flex xs12>
              동전 신호 수동 전송은 기계에 전달되기까지 최장 30초 걸립니다.<br>
              전송하시고 30초 후에 확인 해주세요.<br>
              (다른 고객이 계속 사용하고 있으면 더 지연됨)
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              <v-select
                :items="setCtrl"
                v-model="controlBroadCastDialog.ctrl_id"
                label="컨트롤러 ID 선택"
              ></v-select>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs12>
              <v-text-field
                label="코인 수량 입력"
                color="primary lighten-2"
                type="number"
                v-model="controlBroadCastDialog.coin"
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-text v-else> <!-- else  업데이트신호   -->
          <v-layout row wrap>
            <v-flex xs12>
              업데이트 신호 주는 명령입니다.<br>
              실행시 해당점포는 단말기서비스를 이용할 수 없습니다.<br>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestControlData(controlBroadCastDialog)">전송</v-btn>
          <v-btn color="grey darken-1" flat @click.native="controlBroadCastDialog = { show: false }">취소</v-btn>
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
  name: 'Alert',
  methods: {
    onBack () {
      this.$router.go(-1)
    },
    onBroadcast (index) {
      this.broadCastDialog.index = index
      this.broadCastDialog.show = true
    },
    requestData (item) {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      var params = {
        agency_id: this.$store.state.adminAgency.wash,
        cmd: item.index
      }
      this.$store.dispatch('AgencyAlertReg', params)
        .then((result) => {
          if (result.success) {
            this.broadCastDialog = { show: false }
            console.log("success")
          } else {
            console.log("failure")
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = '서비스가 정상적이지 않습니다. 지속적으로 발생하면 관리자에게 문의해주세요.'
          }
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    onCtrlBroadcast (index) {
      if (index === 7 || index === 5) { //장비전원 재시작, 코인신호보내기
        if (this.$store.state.adminAgency.wash == null) {
          this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
        }
        var params = {
          agency_id: this.$store.state.adminAgency.wash
        }
        console.log("onCtrlBroadCast에서 AgencyAllowControllerID dispatch 진입 직전")
        this.$store.dispatch('AgencyAllowControllerID', params)
          .then((result) => {
            if (result.success) {
              this.setCtrl = result.id_list
              this.controlBroadCastDialog.index = index
              this.controlBroadCastDialog.show = true
            } else {
              this.snackbar = true
              this.snackbar_color = 'error'
              this.snackbar_msg = '서비스가 정상적이지 않습니다. 지속적으로 발생하면 관리자에게 문의해주세요.'
            }
          })
          .catch((result) => {
            this.error = '실패했습니다'
          })
      } else { // 냉난방기,PC재부팅, 업데이트 신호
        this.controlBroadCastDialog.index = index
        this.controlBroadCastDialog.show = true
      }
    },
    requestControlData (item) {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      var params = {
        agency_id: this.$store.state.adminAgency.wash,
        cmd: item.index
      }
      if (item.index === 7) {
        console.log(item)
        params.ctrl_id = item.ctrl_id
        if (item.coin > 12 || item.coin == 0) {
          this.snackbar = true
          this.snackbar_color = 'error'
          this.snackbar_msg = '코인 신호는 최대 1~12회까지 보낼 수 있습니다. 값을 확인해주세요.'
          return
        }
        params.coin = item.coin
      }
      else if (item.index === 5) {
        console.log(item)
        params.ctrl_id = item.ctrl_id
        if (item.onoff === '전원리셋') {
          params.onoff = 0
        } else if (item.onoff === '전원OFF') {
          params.onoff = 1
        } else {
          params.onoff = 2
        }
        // params.onoff = item.onoff === '전원리셋' ? 0 : 1
      }

      if(item.index === 8){
        console.log("업데이트신호주기");
      }
      this.$store.dispatch('AgencyAlertReg', params)
        .then((result) => {
          if (result.success) {
            if (item.index < 4) {
              this.broadCastDialog = { show: false }
            } else {
              this.controlBroadCastDialog = { show: false }
            }
            this.snackbar = true
            this.snackbar_color = 'success'
            this.snackbar_msg = '정상 처리 되었습니다.'
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.snackbar = true
          this.snackbar_color = 'error'
          this.snackbar_msg = '서비스가 정상적이지 않습니다. 지속적으로 발생하면 관리자에게 문의해주세요.'
          // window.location.href = '/wash'
        })
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', 'Login')
    // this.reloadDatas()
  },
  data () {
    return {
      broadCastDialog: { show: false },
      controlBroadCastDialog: { show: false },
      setCtrl: [],
      setOnoff: ['전원리셋', '전원ON', '전원OFF'],
      selectCtrlItem: null,
      show3: false,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 4 || 'Min 4 characters',
        emailMatch: () => ('The email and password you entered don\'t match')
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.or-table {
  width: 100%;
  background-color: #ffffff;
  /* border: 1px solid #444444; */
  border-collapse: collapse;
  box-shadow: 0 2px 1px -1px rgba(0,0,0,.2), 0 1px 1px 0 rgba(0,0,0,.14), 0 1px 3px 0 rgba(0,0,0,.12);
}
.or-table th {
  width: 20%;
  padding: 10px;
  border-bottom: 1px solid #f1f1f1;
}
.or-table-item {
  /* border: 1px; */
  border-color: black;
}
.or-table-item td {
  border-right: 1px solid #f1f1f1;
  text-align: center;
}
.or-table-foot td {
  border-top: 1px solid #f1f1f1;
  padding-top: 20px;
  padding-bottom: 20px;
  text-align: center;
}
.or-table-foot-w {
  color: #7a7308;
}
.or-table-foot-e {
  color: #b30000;
}
.or-table-foot-n {
  color: #00ff00
}
.cursor-st {
  cursor: pointer;
}
.cursor-st:hover {
  text-decoration: underline;
}
</style>