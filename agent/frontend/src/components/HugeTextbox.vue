<template>
  <v-text-field
    v-model="inputModel"
    class="wt-textfield"
    :type="type"
    single-line
    hide-details
    outline
    readonly
  />
</template>

<script>
export default {
  props: {
    model: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: 'text'
    }
  },
  data () {
    return {
      inputModel: null
    }
  },
  watch: {
    model () {
      this.inputModel = this.model
    }
  }
}
</script>

<style scoped>
.wt-textfield >>> .v-input__slot {
  border: 1px solid #ea68a2 !important;
  border-radius: 20px !important;
  background: rgba(255, 255, 255, 0.5) !important;
}
.wt-textfield >>> .v-text-field__slot {
  font-size: 4rem;
}
.wt-textfield >>> input {
  max-height: 100% !important;
  text-align: center;
  color: #fff !important;
}
</style>
