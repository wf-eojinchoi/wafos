<template>
  <v-text-field
    v-model="inputModel"
    @input="handleInput"
    :type="type"
    background-color="#f2f2f2"
    :placeholder="placeholder"
    :readonly="readonly"
    flat
    solo
    hide-details
    single-line
  ></v-text-field>
</template>

<script>
export default {
  name: 'WiseTextField',
  props: [
    'model', 'placeholder', 'type',
    'readonly'
  ],
  watch: {
    model (val) {
      this.inputModel = val
      this.handleInput()
    }
  },
  methods: {
    handleInput () {
      this.$emit('update:model', this.inputModel)
    }
  },
  data () {
    return {
      inputModel: null
    }
  }
}
</script>

<style>
.v-text-field {
  border: none !important;
  overflow: hidden !important;
  border-radius: 5px !important;
}

.v-text-field .v-input__slot {
  padding: 0 20px !important;  
}

.v-input--is-focused {
  border: 1px solid #fede57 !important; 
}

</style>
