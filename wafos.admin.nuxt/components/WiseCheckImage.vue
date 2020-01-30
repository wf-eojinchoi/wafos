<template>
  <v-card
    :class="cardClasses"
    @click="toggleBox()"
  >
    <v-badge v-if="badge" :color="badgecolor">
      <v-icon
        slot="badge"
        color="white"
      >
        done
      </v-icon>
    </v-badge>
    <slot>내용이 없습니다. <br/> 내용을 확인해주세요</slot>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'WiseCheckImage',
  props: [
    'badge', 'badgecolor', 'pkey', 'model'
  ],
  watch: {
    inputChecked: {
      handler: function (val, old) {
        if (this.reloadFlag) {
          this.updateBox()
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
    }
  },
  methods: {
    ...mapGetters(['currentRadio']),
    updateBox () {
      if (this.inputChecked[this.pkey]) {
        this.cardClasses['wt-checkbox--active'] = true
      } else {
        this.cardClasses['wt-checkbox--active'] = false
      }
      this.$store.dispatch('setRadio', this.inputChecked)
    },
    toggleBox () {
      this.reloadFlag = false
      this.inputChecked = this.currentRadio()
      if (!this.inputChecked[this.pkey]) {
        this.inputChecked[this.pkey] = false
      }
      if (this.inputChecked[this.pkey]) {
        this.inputChecked[this.pkey] = false
      } else {
        this.inputChecked[this.pkey] = true
        this.inputChecked.selected = this.pkey
      }
      for (let key in this.inputChecked) {
        if (key !== this.inputChecked.selected && key !== 'selected') {
          if (this.inputChecked[this.inputChecked.selected] && this.inputChecked[key]) {
            this.inputChecked[key] = false
          }
        }
      }
      this.updateBox()
      this.reloadFlag = true
    }
  },
  data () {
    return {
      cardClasses: {
        'wt-checkbox': true,
        'wt-checkbox--active': false
      },
      reloadFlag: true
    }
  }
}
</script>

<style scoped>
.v-badge {
  position: absolute !important;
  top: 0;
  left: calc( 100% - 10px ) !important;
}

.wt-checkbox {
  padding: 30px 15px 30px 15px;
  border-bottom: 2px solid #f9f9f9;
  border-radius: 30px 0 30px 0;
}

.wt-checkbox--active {
  border-left: 2px solid #f9df6e;
  border-top: 2px solid #f9df6e;
  border-right: 2px solid #ee8537;
  border-bottom: 2px solid #ee8537;
  border-radius: 30px 0 30px 0;
}
</style>
