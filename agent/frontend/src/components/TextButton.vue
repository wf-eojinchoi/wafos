<template>
  <v-btn
    :round="round"
    :color="color"
    :class="classObject"
    :to="to"
    :disabled="disable"
    @click="handleClick()"
  >
    <slot />
  </v-btn>
</template>

<script>
export default {
  props: {
    click: Function,
    color: {
      type: String,
      default: 'primary'
    },
    size: {
      type: String,
      default: 'huge' // full, huge, large, normal, small
    },
    fontsize: {
      type: String,
      default: '' // full, huge, large, normal, small
    },
    round: {
      type: Boolean,
      default: false
    },
    to: String,
    disable: Boolean
  },
  data () {
    return {
      classObject: {
      }
    }
  },
  computed: {
    real_fontsize () {
      if (this.fontsize) {
        return this.fontsize
      }
      return this.size
    }
  },
  created () {
    this.classObject['wt-' + this.size + '-btn'] = true
    this.classObject['wt-font-' + this.real_fontsize + '-btn'] = true
  },
  methods: {
    handleClick () {
      this.$emit('click')
    }
  }
}
</script>

<style scoped>
.v-btn {
  font-weight: 700;
}
.wt-full-btn {
  padding: 50px;
  width: 100%;
  height: 100%;
}
.wt-huge-btn {
  padding: 30px;
  width: 90%;
  height: 90%;
}
.wt-large-btn {
  width: 40%;
  height: 30%;
}
.wt-normal-btn {
  width: 30%;
  height: 20%;
}
.wt-small-btn {
  width: 20%;
  height: 15%;
}
.wt-font-full-btn {
  font-size: 6rem;
}
.wt-font-huge-btn {
  font-size: 5rem;
}
.wt-font-large-btn {
  font-size: 3rem;
}
.wt-font-normal-btn {
  font-size: 2rem;
}
.wt-font-small-btn {
  font-size: 1.5rem;
}
</style>
