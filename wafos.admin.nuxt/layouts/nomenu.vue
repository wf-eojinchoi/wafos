<template>
  <v-app>
    <transition name="slide-fade" mode="out-in">
      <router-view/>
    </transition>
  </v-app>
</template>

<script>
export default {
  name: 'App'
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
