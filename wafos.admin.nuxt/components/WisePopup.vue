<template>
  <v-dialog
    v-model="dialog"
    max-width="600"
  >
    <v-card class="wt-card">
      <v-card-title class="headline wt-card-title">
        <v-spacer></v-spacer>
        <v-btn small round icon color="#f8db6c" class="elevation-0">
          <v-icon>clear</v-icon>
        </v-btn>
      </v-card-title>
      <v-card-text>
        <slot></slot>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'WisePopup',
  props: [ 'model' ],
  watch: {
    model (val) {
      this.dialog = val
    }
  },
  methods: {
  },
  data () {
    return {
      dialog: false
    }
  }
}
</script>

<style>
.v-dialog .v-icon {
  color: #fff !important;
}
.v-dialog.v-dialog--active {
  border-radius: 30px 0 30px 0 !important;
  box-shadow: 0 !important;
} 

.wt-card {
  border-radius: 30px 0 30px 0 !important;
}

.wt-card-title {
  border-radius: 30px 0 0 0 !important;
  background-color: #f8db6c !important;
  padding: 0 !important;
}
/* 2f4f8c */

</style>
