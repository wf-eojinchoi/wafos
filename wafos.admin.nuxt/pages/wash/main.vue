<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card
        elevation="0">
        <v-card-title>
          <v-flex xs12 text-xs-center>
            <img src="/logo.png" alt="(주)워시홀딩스 셀프빨래방" style="width: 80%;">
          </v-flex>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-flex xs12 text-xs-center>
            <v-subheader class="teal--text">
              유지보수 만기일 : {{ expireDate }}까지
            </v-subheader>
          </v-flex>
        </v-card-text>
        <v-divider></v-divider>
        <v-list >
          <template v-for="(item, index) in items">
            <v-list-tile
              :key="item.title"
              avatar
              ripple
              @click="move(item.path)"
            >
              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile-content>

              <v-list-tile-action>
                <!-- <v-list-tile-action-text>{{ item.action }}</v-list-tile-action-text> -->
                <v-icon>{{ item.action }}</v-icon>
              </v-list-tile-action>
            </v-list-tile>
            <v-divider
              v-if="index + 1 < items.length"
              :key="index"
            ></v-divider>
          </template>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
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
      var uri = '/wash/' + path
      this.$router.push(uri)
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', 'Main')
    this.expireDate = this.$cookie.get('expire-date')
    // this.reloadDatas()
  },
  data () {
    return {
      expireDate: null,
      items: [
        {
          title: '고객정보관리',
          action: 'navigate_next',
          path: 'members'
        },
        {
          title: '매출현황조회',
          action: 'navigate_next',
          path: 'payment'
        },
        {
          title: '장비관리',
          subtitle: '(세탁기,건조기)',
          action: 'navigate_next',
          path: 'device'
        },
        {
          title: '경고 방송 및 기기 제어 관리',
          subtitle: '',
          action: 'navigate_next',
          path: 'alert'
        },
        {
          title: '적립금 설정',
          action: 'navigate_next',
          path: 'info/point'
        },
        {
          title: '점포정보관리',
          action: 'navigate_next',
          path: 'info'
        },
        {
          title: '비밀번호관리',
          action: 'navigate_next',
          path: 'changepwd'
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
