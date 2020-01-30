<template>
  <v-content >
    <v-layout row pa-2>
      <v-flex xs12>
        <v-card>
          <v-card-text>
            <v-flex xs12 sm6>
              <v-text-field
                label="현재 비밀번호 입력"
                color="primary lighten-2"
                type="password"
                v-model="password1"
              ></v-text-field>
            </v-flex>
            <v-flex xs12 sm6>
              <v-text-field
                label="변경 할 비밀번호 입력"
                color="primary lighten-2"
                type="password"
                v-model="password2"
              ></v-text-field>
            </v-flex>
            <v-flex xs12 sm6>
              <v-text-field
                label="비밀번호 확인"
                color="primary lighten-2"
                type="password"
                v-model="confirm_password2"
              ></v-text-field>
            </v-flex>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary darken-1" flat @click="pwd()">비밀번호 변경</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
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
  layout: 'wadmin',
  name: 'passwordChange',
  methods: {
    reloadDatas () {
      // this.loading = true
      // this.$store.dispatch('dashboardInfo')
      //   .then((result) => {
      //     this.loading = false
      //     this.weeklyData = result.results
      //     this.todayData = result.today
      //     this.dayEtcData = result.day_etc
      //     this.smsData = result.sms_info
      //   })
      //   .catch((result) => {
      //     this.error = '사용자 리스트를 가져오는데 실패했습니다'
      //     this.loading = false
      //   })
    },
    onBack () {
      this.$router.go(-1)
    },
    pwd () {
      if (this.$cookie.get('admin-id') == null) {
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '다시 로그인해주세요.'
        return
      }
      if (this.password2 === this.confirm_password2) {
        var params = {
          id: this.$cookie.get('admin-id'),
          pwd: this.password1,
          pwd2: this.password2
        }
        this.$store.dispatch('adminChangePWD', params)
          .then((result) => {
            if(result.success) {
              this.$router.go(-1)
            }
          })
          .catch((result) => {
            this.error = '사용자 리스트를 가져오는데 실패했습니다'
            this.loading = false
          })
      } else {
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '비밀번호를 확인해주세요.'
      }
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', 'Login')
    // this.reloadDatas()
  },
  data () {
    return {
      smsData: {},
      weeklyData: [],
      todayData: [],
      dayEtcData: [],
      show3: false,
      password1: null,
      password2: null,
      confirm_password2: null,
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
