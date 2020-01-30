<template>
  <v-container wrap fill-height fluid>
    <v-layout id="bg" wrap justify-center>
      <v-flex xs8 mt-5>
        <v-card height="700" class="elevation-2">
          <v-card-text class="text-xs-center">
            <v-layout wrap>
              <v-flex xs12>
                <v-text-field v-model="kid" label="아이디"/>
              </v-flex>
              <v-flex xs12>
                <v-text-field v-model="seckey" label="seckey"/>
              </v-flex>
              <v-flex xs12>카드 단말기를 사용할 경우 단말기 TID를 입력</v-flex>
              <v-flex xs12>
                <v-text-field v-model="cardkey" label="cardkey"/>
              </v-flex>
              <v-flex xs12>
                <v-btn class="font-weight-bold display-2" @click="submit()">{{ $t('app.confirm') }}</v-btn>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="dialog" width="600">
      <v-card>
        <v-card-text class="display-2 text-xs-center mt-2">{{ dialogText }}</v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn color="grey" class="display-1" @click="dialog = false">{{ $t('app.close') }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: 'Info',
  data () {
    return {
      kid: null,
      seckey: null,
      cardkey: null,
      dialog: false,
      dialogText: ''
    }
  },
  methods: {
    submit () {
      this.$axios.post('/init', {
        kid: this.kid,
        seckey: this.seckey,
        cardkey: this.cardkey
      })
        .then(() => {
          this.dialogText = this.$t('init.complete')
          this.dialog = true
        })
        .catch(() => {
          this.dialogText = this.$t('init.noentry')
          this.dialog = true
        })
    }
  }
}
</script>

<style scoped>
.v-card {
  border: none !important;
}
.v-btn {
  height: 100px;
  width: 100%;
}
</style>
