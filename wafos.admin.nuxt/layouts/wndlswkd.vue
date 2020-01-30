<template>
  <v-app>
    <o-header :title="currentTitle" width="200px"></o-header>
    <transition name="slide-fade" mode="out-in">
      <nuxt />
    </transition>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'
import OHeader from '@/components/OHeader'

export default {
  name: 'App',
  components: {
    OHeader
  },
  computed: {
    ...mapGetters([
      'currentTitle'
    ])
  }
}
</script>

<style>
pre {
  word-break: break-all;
  white-space: pre-line;
}

.slide-fade-enter-active {
  transition: all .3s ease;
}

.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-enter, .slide-fade-leave-to {
  transform: translateX(50px);
  opacity: 0;
}
</style>
