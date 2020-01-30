<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn icon @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>
        <v-toolbar-title>매출현황조회</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="success" flat @click="dnDialog.show = true">엑셀다운받기</v-btn>
      </v-toolbar>
    </v-layout>
    <v-layout row>
      <v-flex xs12>
        <v-list>
          <template v-for="(item, index) in items">
            <v-list-tile :key="item.title" avatar ripple @click="move(item.path)">
              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile-content>

              <v-list-tile-action>
                <!-- <v-list-tile-action-text>{{ item.action }}</v-list-tile-action-text> -->
                <v-icon>{{ item.action }}</v-icon>
              </v-list-tile-action>
            </v-list-tile>
            <v-divider v-if="index + 1 < items.length" :key="index"></v-divider>
          </template>
        </v-list>
      </v-flex>
    </v-layout>
    <v-dialog v-model="dnDialog.show" max-width="80%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-select :items="selData" v-model="selDataItem" label="기간선택"></v-select>
          <v-layout row v-if="selDataItem === '기간선택'">
            <v-flex xs6>
              <v-menu
                :close-on-content-click="false"
                v-model="dnDialog.menu1"
                :nudge-right="40"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="dnDialog.date1"
                  label="시작날짜"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="dnDialog.date1" @input="dnDialog.menu1 = false"></v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs6>
              <v-menu
                :close-on-content-click="false"
                v-model="dnDialog.menu2"
                :nudge-right="40"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="dnDialog.date2"
                  label="종료날짜"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker v-model="dnDialog.date2" @input="dnDialog.menu2 = false"></v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="requestExcel(dnDialog)">다운받기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="dnDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="snackbar"
      :color="snackbar_color"
      :left="true"
      :top="true"
      :multi-line="true"
      :timeout="3000"
      :vertical="true"
    >
      {{ snackbar_msg }}
      <v-btn dark flat @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </v-content>
</template>

<script>
export default {
  layout: 'nomenu',
  name: 'Main',
  methods: {
    reloadDatas () {
      // this.loading = true
      // this.$store.dispatch('dashboardInfo')
      //   .then((result) => {
      //     this.loading = false
      //     this.weeklyData = result.results
      //     this.todayData = result.today
      //     this.dayEtcData = result.day_etc
      //     this.smsData = result.sms_info
      //   })
      //   .catch((result) => {
      //     this.error = '사용자 리스트를 가져오는데 실패했습니다'
      //     this.loading = false
      //   })
    },
    move (path) {
      var id = 1
      var uri = '/wash/payment/' + path
      this.$router.push(uri)
    },
    onBack () {
      this.$router.go(-1)
    },
    requestExcel (item) {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      var params = {
        agency_id: this.$store.state.adminAgency.wash,
        st_date: item.date1,
        et_date: item.date2,
        type: this.selDataItem === '전체' ? 0 : 1
      }
      console.log(params)
      this.$store.dispatch('PayDownload', params)
        .then((result) => {
          console.log(result)
          if (result.success) {
            this.dnDialog = { show: false }
            // console.log(result.path)
            window.location.href = result.path
          } else {
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.error = result.msg
        })
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '매출현황관리')
    // this.reloadDatas()
  },
  data () {
    return {
      selData: ['전체', '기간선택'],
      selDataItem: '전체',
      dnDialog: { show: false },
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      items: [
        // {
        //   title: '전체보기',
        //   action: 'navigate_next',
        //   path: 'members'
        // },
        {
          title: '월별 보기',
          action: 'navigate_next',
          path: 'month'
        },
        {
          title: '일별 보기',
          action: 'navigate_next',
          path: 'day'
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
