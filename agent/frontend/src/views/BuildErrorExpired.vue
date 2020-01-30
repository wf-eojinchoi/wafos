<template>
  <v-container wrap fill-height fluid>
    <v-layout id="bg" wrap justify-center align-center>
      <v-flex xs8>
        <v-card height="700" class="elevation-2">
          <v-card-text class="text-xs-center">
            <v-layout wrap>
              <v-flex xs12>
                <span class="display-3">Expired</span>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'BuildErrorExpired',
  data () {
    return {}
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
