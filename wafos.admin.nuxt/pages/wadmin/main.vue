<template>
  <v-content >
    <!-- 주간 정보 -->
    <v-layout row pa-2 justify-center mt-5>
      <v-flex xs6>
        <v-card>
          <v-card-title>
            <v-flex xs12 text-xs-center>
              <img src="/logo.png" alt="(주)워시홀딩스 셀프빨래방" style="width: 80%;">
            </v-flex>
          </v-card-title>
          <v-card-text>
            <v-flex xs12 text-xs-center>
              WAFOS 관리자 페이지
            </v-flex>
          </v-card-text>
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
  layout: 'wadmin',
  name: 'WAMain',
  methods: {
  },
  mounted () {
    this.$store.dispatch('updateTitle', '')
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
