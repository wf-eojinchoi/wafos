<template>
  <v-content >
    <!-- 주간 정보 -->
    <v-layout row pa-2 justify-center mt-5>
      <v-flex xs6>
        <v-card>
          <v-card-title>
            <v-subheader class="title">WAFOS 관리자 로그인</v-subheader>
          </v-card-title>
          <v-card-text >
            <v-flex xs12 sm12 pl-3 pr-3>
              <v-text-field
                label="ID"
                color="primary lighten-2"
                type="text"
                v-model="login_id"
              ></v-text-field>
            </v-flex>
            <v-flex xs12 sm12 pl-3 pr-3>
              <v-text-field
                :append-icon="show3 ? 'visibility_off' : 'visibility'"
                :rules="[rules.required, rules.min]"
                :type="show3 ? 'text' : 'password'"
                name="input-10-2"
                label="비밀번호"
                hint="At least 4 characters"
                v-model="pwd"
                class="input-group--focused"
                @click:append="show3 = !show3"
                v-on:keyup.enter="login()"
              ></v-text-field>
            </v-flex>
          </v-card-text>
          <v-card-actions>
            <v-flex xs12 pa-3>
              <v-btn color="primary darken-1" block @click="login()">로그인</v-btn>
            </v-flex>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
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
  layout: 'nomenu',
  name: 'WALogin',
  methods: {
    login () {
      console.log('##')
      var item = {
        login_id: this.login_id,
        pwd: this.pwd
      }
      this.$cookie.delete('auth-token')
      this.$store.dispatch('doLogin', item)
        .then((result) => {
          if (result.success) {
            this.$cookie.set('admin-id', result.admin_id, { expires: '2h' })
            var member = result.enterMember
            if (member) {
              var path = '/wadmin/members/'
              this.$router.push(path)
            } else {
              var path = '/wadmin/main'
              this.$router.push(path)
            }
            // this.$store.dispatch('TokenRegister', item)
            //   .then((result) => {
            //     if (result.access) {
            //       if (member) {
            //         var path = '/wadmin/members/'
            //         this.$router.push(path)
            //       } else {
            //         var path = '/wadmin/main'
            //         this.$router.push(path)
            //       }
            //     } else {
            //       this.errMessage = result.msg
            //       this.snackbar = true
            //     }
            //   })
            //   .catch((result) => {
            //     this.error = 'TOKEN 생성에 실패했습니다'
            //   })
          } else {
            this.errMessage = result.msg
            this.snackbar = true
          }
          // TokenRegister
          // if (result.success) {
          //   var path = '/wadmin/members/'
          //   this.$router.push(path)
          // } else {
          //   this.errMessage = result.msg
          //   this.snackbar = true
          // }
        })
        .catch((result) => {
          this.error = '관리자 계정 로그인에 실패했습니다'
        })
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', 'Login')
  },
  data () {
    return {
      snackbar_mode: '',
      errMessage: null,
      snackbar: false,
      // Page Data
      login_id: null,
      pwd: null,
      show3: false,
      password: 'Password',
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
