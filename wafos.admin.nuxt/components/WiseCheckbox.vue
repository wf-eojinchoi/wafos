<template>
  <v-checkbox
    height="1"
    v-model="inputChecked[pkey]"
    @change="handleInput"
    hide-details
    class="wt-checkbox-noscoped"
    :label="label"
  ></v-checkbox>
</template>

<script>
export default {
  name: 'WisePopup',
  props: [ 'model', 'label', 'pkey' ],
  methods: {
    handleInput (val) {
      this.inputChecked.selected = this.pkey
      this.inputChecked[this.pkey] = val
      if (this.pkey) {
        this.$emit('update:model', this.inputChecked.selected)
      } else {
        this.$emit('update:model', val)
      }
    }
  },
  watch: {
    inputChecked: {
      handler: function (val, old) {
        for (let key in val) {
          if (key !== this.inputChecked.selected && key !== 'selected') {
            if (this.inputChecked[this.inputChecked.selected] && this.inputChecked[key]) {
              this.inputChecked[key] = false
            }
          }
        }
      },
      deep: true
    }
  },
  computed: {
    inputChecked: {
      get () {
        return this.$store.state.radio
      },
      set (val) {
        this.$emit('update:model', val)
        this.$store.dispatch('setRadio', val)
      }
    },
    checked: {
      get () {
        return this.inputChecked[this.pkey]
      },
      set (val) {
        this.inputChecked[this.pkey] = val
      }
    }
  },
  data () {
    return {
    }
  }
}
</script>

<style>
.v-label {
  color: #aaaaaa !important;
}

.v-icon {
  font-size: 15px !important;
  color: #aaaaaa !important;
}

.v-input--selection-controls__input {
  margin: 0 !important;
}

.wt-checkbox-noscoped {
  max-width: 100px !important;
}
</style>
