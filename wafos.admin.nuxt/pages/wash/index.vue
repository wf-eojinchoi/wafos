<template>
  <v-content >
    <v-layout row pa-2>
      <v-flex xs12>
        <v-card>
          <v-card-title>
            <v-flex xs12 text-xs-center>
              <img src="/logo.png" alt="(주)워시홀딩스 셀프빨래방" style="width: 80%;">
            </v-flex>
          </v-card-title>
          <v-card-text>
            <v-flex xs12 >
              <span class="title" justify-center >WAFOS 가맹점 로그인</span>
            </v-flex>
            <v-flex xs12 sm6 mt-4>
              <v-text-field
                label="점포코드"
                color="primary lighten-2"
                type="text"
                v-model="login_id"
              ></v-text-field>
            </v-flex>
            <v-flex xs12 sm6>
              <v-text-field
                :append-icon="show3 ? 'visibility_off' : 'visibility'"
                :type="show3 ? 'text' : 'password'"
                name="input-10-2"
                label="비밀번호"
                hint="At least 4 characters"
                v-model="pwd"
                class="input-group--focused"
                @click:append="show3 = !show3"
              ></v-text-field>
            </v-flex>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary darken-1" block @click="loginSubmit()">로그인</v-btn>
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
  layout: 'nomenu',
  name: 'ALogin',
  methods: {
    loginSubmit () {
      let item = {
        login_id: this.login_id,
        pwd: this.pwd
      }
      this.$cookie.delete('auth-token')
      this.$store.dispatch('doWashLogin', item)
        .then((result) => {
          if (result.success) {
            this.$cookie.set('expire-date', result.expire)
            item.username = this.login_id
            item.password = this.pwd
            var path = '/wash/main'
            this.$router.push(path)
            // this.$store.dispatch('TokenRegister', item)
            //   .then((res2) => {
            //     if (res2.access) {
            //       var path = '/wash/main'
            //       this.$router.push(path)
            //     } else {
            //       this.errMessage = res2.msg
            //       this.snackbar = true
            //     }
            //   })
            //   .catch((res2) => {
            //     this.snackbar = true
            //     this.snackbar_color = 'error'
            //     this.snackbar_msg = 'TOKEN 생성에 실패했습니다'
            //   })
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.snackbar = true
          this.snackbar_color = 'error'
          if (result.msg) {
            this.snackbar_msg = result.msg
          } else {
            this.snackbar_msg = '관리자 계정 로그인에 실패했습니다'
          }
        })
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', 'Login')
  },
  data () {
    return {
      login_id: null,
      pwd: null,
      show3: false,
      password: null,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null
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
