<template>
  <v-content >
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>로그인</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-progress-circular
                v-if="loading"
                indeterminate
                color="white"
              ></v-progress-circular>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                v-model="uid"
                color="primary"
                prepend-icon="person"
                name="email"
                label="Email"
                type="text"
                v-on:keyup.enter="requestKey()"></v-text-field>
              <v-text-field
                v-if="waiting"
                v-model="password"
                color="primary"
                prepend-icon="lock"
                name="password"
                label="Password"
                type="password"
                v-on:keyup.enter="doLogin()"></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" v-on:click="requestKey()" v-if="!waiting">Request</v-btn>
              <v-btn color="primary" v-on:click="doLogin()" v-else-if="waiting">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
export default {
  name: 'Login',
  layout: 'nomenu',
  mounted () {
    this.$store
      .dispatch('updateTitle', '로그인')
  },
  methods: {
    requestKey () {
      this.loading = true
      this.$store
        .dispatch('requestKey', this.uid)
        .then(() => {
          this.waiting = true
          this.loading = false
        })
        .catch(() => {
          this.loading = false
          this.waiting = false
        })
    },
    doLogin () {
      this.loading = true
      this.$store
        .dispatch('doLogin', {
          uid: this.uid,
          password: this.password
        })
        .then(() => {
          this.loading = false
          this.$router.push({ name: 'Dashboard' })
        })
        .catch(() => {
          this.loading = false
          this.waiting = false
        })
    }
  },
  data () {
    return {
      uid: null,
      waiting: false,
      passwod: false,
      loading: false
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
  box-shadow: 0 2px 1px -1px rgba(0,0,0,.2), 0 1px 1px 0 rgba(0,0,0,.14), 0 1px 3px 0 rgba(0,0,0,.12);
}
.or-table th {
  width: 20%;
  border-bottom: 1px solid #f1f1f1;
}
.or-table-item {
  border: 1px;
  border-color: black;
}
.or-table-item td {
  border-right: 1px solid #f1f1f1;
  text-align: center;
}
.or-table-foot td {
  border-top: 1px solid #f1f1f1;
  text-align: center;
}

</style>
