<template>
  <v-card class="mb-5 elevation-0" height="640px">
    <v-layout wrap justify-center align-center fill-height>
      <v-flex xs12 pa-1 class="text-xs-center" v-if="$i18n.locale === 'ko'">
        <span class="display-2">{{ $t('dryer.step2.desc1') }}&nbsp;</span>
        <span class="display-2 font-weight-bold wt-primary-font">{{ $t('dryer.step2.desc2') }}</span>
        <span class="display-2">{{ $t('dryer.step2.desc3') }}</span>
      </v-flex>
      <v-flex xs12 pa-1 class="text-xs-center" v-else>
        <span class="display-1">{{ $t('dryer.step2.desc1') }}&nbsp;</span>
        <span class="display-1">{{ $t('dryer.step2.desc2') }}</span>
        <span class="display-1">{{ $t('dryer.step2.desc3') }}</span>
      </v-flex>
      <v-flex v-for="(item, idx) in items" :key="item.id" xs4 pa-1 class="text-xs-center">
        <v-btn
          :class="idx == selected ? 'selected-dryer' : 'not-selected-dryer'"
          class="dryer"
          flat
          top
          @click="selectWasher(idx)"
        >
          <v-layout wrap ml-5>
            <v-flex xs12 ml-5>
              <span class="display-1">{{ $t('dryer.step2.select', { number: item.controller_id }) }}</span>
            </v-flex>
          </v-layout>
        </v-btn>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>

export default {
  name: 'DryerStep2',
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
      return this.$store.state.devices.dryer
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
.selected-dryer {
  background-color: transparent !important;
  background: url("../../../assets/dryer_on.gif") no-repeat;
  background-position: center;
  background-size: cover;
  color: #72cef4 !important;
}

.not-selected-dryer {
  background-color: transparent !important;
  background: url("../../../assets/dryer_off.png") no-repeat;
  background-position: center;
  background-size: cover;
  color: #b2b2b2 !important;
}
.dryer {
  width: 280px;
  height: 280px;
}
</style>
