<template>
  <v-card class="mb-5 elevation-0" height="640px">
    <v-layout wrap justify-center fill-height>
      <v-flex v-if="hasPages()" xs1 align-self-center class="text-xs-center">
        <v-btn icon flat @click="prevPage()">
          <v-icon class="fa fa-angle-left fa-5x"/>
        </v-btn>
      </v-flex>
      <v-flex xs10>
        <v-layout wrap justify-center align-center>
          <v-flex xs12 class="text-xs-center">
            <span class="display-1">{{ $t('washer.step4.desc1') }}:&nbsp;</span>
            <span
              class="display-1 font-weight-bold wt-primary-font"
            >{{ $t('washer.step4.select', { number: controller_id }) }}</span>
          </v-flex>
          <v-flex xs12 class="text-xs-center" v-if="$i18n.locale === 'ko'">
            <span
              :class="$store.getters.isV2 ? 'display-1': 'display-2'"
            >{{ $t('washer.step4.desc2') }}&nbsp;</span>
            <span
              :class="$store.getters.isV2 ? 'display-1': 'display-2'"
              class="font-weight-bold wt-primary-font"
            >{{ $t('washer.step4.desc3') }}</span>
            <span
              :class="$store.getters.isV2 ? 'display-1': 'display-2'"
            >{{ $t('washer.step4.desc4') }}</span>
          </v-flex>
          <v-flex xs12 class="text-xs-center" v-else>
            <span
              :class="$store.getters.isV2 ? 'display-1': 'display-2'"
            >{{ $t('washer.step4.desc2') }}&nbsp;</span>
            <span
              :class="$store.getters.isV2 ? 'display-1': 'display-2'"
            >{{ $t('washer.step4.desc3') }}</span>
            <span
              :class="$store.getters.isV2 ? 'display-1': 'display-2'"
            >{{ $t('washer.step4.desc4') }}</span>
          </v-flex>
          <v-flex v-for="item in currentItems" :key="item.id" xs6 class="text-xs-center">
            <v-btn
              :class="item.id == course.id ? 'selected-course' : 'not-selected-course'"
              class="course ma-0 pa-0"
              flat
              top
              @click="selectCourse(item.id)"
            >
              <v-layout wrap ma-0 pa-0>
                <v-flex xs12 mt-4>
                  <span class="display-1" v-if="$i18n.locale === 'ko'">{{ item.title }}</span>
                  <span class="display-1" v-else-if="$i18n.locale === 'en'">{{ item.title_en }}</span>
                  <span class="display-1" v-else-if="$i18n.locale === 'vi'">{{ item.title_vn }}</span>
                </v-flex>
                <v-flex xs12 mt-3 mb-2>
                  <span class="display-2">{{ item.amount }}</span>
                </v-flex>
                <v-flex xs12 mt-5>
                  <span
                    class="headline black--text"
                    v-if="$i18n.locale === 'ko'"
                  >{{ item.description }}</span>
                  <span
                    class="headline black--text"
                    v-else-if="$i18n.locale === 'en'"
                  >{{ item.description_en }}</span>
                  <span
                    class="headline black--text"
                    v-else-if="$i18n.locale === 'vi'"
                  >{{ item.description_vn }}</span>
                </v-flex>
              </v-layout>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex v-if="hasPages()" xs1 align-self-center class="text-xs-center">
        <v-btn icon flat @click="nextPage()">
          <v-icon class="fa fa-angle-right fa-5x"/>
        </v-btn>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: 'WasherStep4',
  components: {
  },
  props: {
    selected: {
      type: Number,
      default: Number
    },
    course: {
      type: Object,
      default: Object
    },
    dialog: {
      type: Boolean
    }
  },
  data () {
    return {
      page: 0,
      items: [],
      controller_id: 0
    }
  },
  computed: {
    maxPage () {
      if (!this.items) {
        return 0
      }
      return parseInt(this.items.length % 4 === 0 ? this.items.length / 4 - 1 : this.items.length / 4)
    },
    currentItems () {
      if (!this.items) {
        return []
      }
      return this.items.slice(this.page * 4, (this.page + 1) * 4)
    }
  },
  watch: {
    selected (val) {
      if (val !== null) {
        this.controller_id = this.$store.state.devices.washer[val].controller_id
        this.items = this.$store.state.devices.washer[val].courses
      }
    }
  },
  methods: {
    selectCourse (id) {
      let item = this.items.find(item => item.id === id)
      if (item) {
        this.$emit('update:course', item)
        this.$emit('update:dialog', true)
      }
    },
    isChecked (id) {
      if (this.course && this.course.id === id) {
        return true
      }
      return false
    },
    nextPage () {
      if (this.page < this.maxPage) {
        this.page += 1
      }
    },
    prevPage () {
      if (this.page > 0) {
        this.page -= 1
      }
    },
    hasPages () {
      return (this.maxPage > 0)
    }
  }
}
</script>

<style scoped>
.selected-course {
  background-color: transparent !important;
  background: url("../../../assets/course_on_pink.png") no-repeat;
  background-position: center;
  background-size: contain;
  color: #fff !important;
}

.not-selected-course {
  background-color: transparent !important;
  background: url("../../../assets/course_off.png") no-repeat;
  background-position: center;
  background-size: contain;
  color: #000 !important;
}
.course {
  width: 350px;
  height: 270px;
}
</style>
