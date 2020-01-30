<template>
  <v-card class="mb-5 elevation-0" height="640px">
    <v-layout
      id="bg"
      wrap
      justify-center
      fill-height
      align-center
      @click="$emit('update:steps', steps + 1)"
    >
      <v-flex xs12 class="text-xs-center">
        <span
          :class="$i18n.locale != 'ko' ? 'display-1' : 'display-3'"
        >{{ $t('washer.step1.desc') }}</span>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: 'WasherStep1',
  props: {
    steps: Number
  },
  components: {
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
#bg {
  background: url("../../../assets/water.gif") no-repeat;
  background-position: center;
  background-size: 650px;
}
</style>
