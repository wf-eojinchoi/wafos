<template>
  <v-btn
    block
    :class="`elevation-0 wt-btn ${textcolor}--text ${size}--text`"
    :color="color"
    :to="to"
    @click="handleClick()"
  ><slot></slot></v-btn>
</template>

<script>
export default {
  name: 'WiseButton',
  props: {
    color: String,
    textcolor: {
      type: String,
      default: 'white'
    },
    size: {
      type: String,
      default: 'normal' /* small / normal / big / huge */
    },
    to: String
  },
  methods: {
    handleClick () {
      this.$emit('click')
    }
  },
  data () {
    return {
    }
  }
}
</script>

<style>
.wt-btn {
  min-height: 40px;
  border-radius: 10px 0 10px 0 !important;
  font-size: 16px !important;
}

.small--text {
  font-size: 12px !important;
}

.normal--text {
  font-size: 16px !important;
}

.big--text {
  font-size: 20px !important;
}

.huge--text {
  font-size: 24px !important;
}
</style>
