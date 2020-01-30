<template>
  <v-card class="mb-5 elevation-0" height="640px">
    <v-layout wrap justify-center align-center fill-height>
      <v-flex xs12 pa-1 class="text-xs-center" v-if="$i18n.locale === 'ko'">
        <span class="display-2">{{ $t('washer.step3.desc1') }}&nbsp;</span>
        <span class="display-2 font-weight-bold wt-primary-font">{{ $t('washer.step3.desc2') }}</span>
        <span class="display-2">{{ $t('washer.step3.desc3') }}</span>
      </v-flex>
      <v-flex xs12 pa-1 class="text-xs-center" v-else>
        <span class="display-1">{{ $t('washer.step3.desc1') }}&nbsp;</span>
        <span class="display-1">{{ $t('washer.step3.desc2') }}</span>
        <span class="display-1">{{ $t('washer.step3.desc3') }}</span>
      </v-flex>
      <v-flex v-for="(item, idx) in items" :key="item.id" xs4 pa-1 class="text-xs-center">
        <v-btn
          :class="idx == selected ? 'selected-washer' : 'not-selected-washer'"
          class="washer"
          flat
          top
          @click="selectWasher(idx)"
        >
          <v-layout wrap mb-5>
            <v-flex xs12>
              <span
                class="display-1"
              >{{ $t('washer.step3.select', { number: item.controller_id }) }}</span>
            </v-flex>
          </v-layout>
        </v-btn>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: 'WasherStep3',
  props: {
    selected: Number,
    steps: Number
  },
  data () {
    return {
    }
  },
  computed: {
    items () {
      return this.$store.state.devices.washer
    }
  },
  methods: {
    selectWasher (id) {
      this.$emit('update:selected', id)
      this.$emit('update:steps', this.steps + 1)
    }
  }
}
</script>

<style scoped>
.selected-washer {
  background-color: transparent !important;
  background: url("../../../assets/washer_on.gif") no-repeat;
  background-position: center;
  background-size: cover;
  color: #72cef4 !important;
}

.not-selected-washer {
  background-color: transparent !important;
  background: url("../../../assets/washer_off.png") no-repeat;
  background-position: center;
  background-size: cover;
  color: #b2b2b2 !important;
}
.washer {
  width: 280px;
  height: 280px;
}
</style>
