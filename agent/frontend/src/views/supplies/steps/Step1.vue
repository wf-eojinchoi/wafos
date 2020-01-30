<template>
  <v-card class="mb-5 elevation-0" height="640px">
    <v-layout wrap justify-center fill-height>
      <v-flex xs10>
        <v-layout wrap justify-center align-center>
          <v-flex xs12 class="text-xs-center" v-if="$i18n.locale === 'ko'">
            <span class="display-2">{{ $t('supplies.step1.desc1') }}&nbsp;</span>
            <span
              class="display-2 font-weight-bold wt-primary-font"
            >{{ $t('supplies.step1.desc2') }}</span>
            <span class="display-2">{{ $t('supplies.step1.desc3') }}</span>
          </v-flex>
          <v-flex xs12 class="text-xs-center" v-else>
            <span class="display-1">{{ $t('supplies.step1.desc1') }}&nbsp;</span>
            <span class="display-1">{{ $t('supplies.step1.desc2') }}&nbsp;</span>
            <span class="display-1">{{ $t('supplies.step1.desc3') }}</span>
          </v-flex>
          <v-flex v-for="item in currentItems " :key="item.id" xs6 class="text-xs-center">
            <v-btn
              :class="item.id === supply.id? 'selected-supply' : 'not-selected-supply'"
              class="supply ma-0 pa-0"
              flat
              top
              @click="selectSupply(item.id)"
            >
              <v-layout wrap ma-0 pa-0>
                <v-flex xs12 mt-5>
                  <span class="display-1" v-if="$i18n.locale === 'ko'">{{ item.title }}</span>
                  <span class="title" v-else-if="$i18n.locale === 'en'">{{ item.title_en }}</span>
                  <span class="title" v-else-if="$i18n.locale === 'vi'">{{ item.title_vn }}</span>
                </v-flex>
                <v-flex xs12 mt-3 mb-2>
                  <span class="display-2">{{ item.amount }}</span>
                </v-flex>
                <v-flex xs12 mt-4>
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
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: 'SuppliesStep1',
  components: {
  },
  props: {
    supply: {
      type: Object,
      default: Object
    },
    dialog: {
      type: Boolean,
      default: false
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
  data () {
    return {
      page: 0,
      items: []
    }
  },
  mounted () {
    if (this.$store.state.devices.supplies[0]) {
      this.items = this.$store.state.devices.supplies[0].courses
    }
  },
  methods: {
    selectSupply (id) {
      let item = this.items.find(item => item.id === id)
      if (item) {
        this.$emit('update:supply', item)
        this.$emit('update:dialog', true)
      }
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
.selected-supply {
  background-color: transparent !important;
  background: url("../../../assets/course_on_pink.png") no-repeat;
  background-position: center;
  background-size: contain;
  color: #fff !important;
}

.not-selected-supply {
  background-color: transparent !important;
  background: url("../../../assets/course_off.png") no-repeat;
  background-position: center;
  background-size: contain;
  color: #000 !important;
}
.supply {
  width: 350px;
  height: 270px;
}
</style>
