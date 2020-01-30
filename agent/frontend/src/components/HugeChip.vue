<template>
  <v-chip
    class="wt-chip display-2"
    :color="color"
    text-color="white"
  >
    <slot />
  </v-chip>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: 'primary'
    }
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
.wt-chip >>> .v-chip__content {
  height: auto;
  padding: 20px 40px 20px 40px;
}
</style>
