<template>
  <div>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app>
      <!-- <v-list>
        <v-list-tile
          :to="'/wadmin/'"
          :active-class="isDashActive"
        >
          <v-list-tile-action>
            <v-icon>dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-title :to="'/wadmin/'" @onclick="onDashboardClick()">Dashboard</v-list-tile-title>
        </v-list-tile>

      </v-list> -->
      <v-list>
        <v-list-group
          v-for="item in menuItems"
          v-model="item.active"
          :key="item.action"
          :prepend-icon="item.icon"
          no-action>
            <v-list-tile slot="activator">
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile>
            <div v-if="'items' in item">
              <v-list-tile
                  v-for="subItem in item.items"
                  :key="subItem.title"
                  @click="move(item, subItem)">
                <v-list-tile-content>
                  <v-list-tile-title>{{ subItem.title }}</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </div>
            <div v-else>
              <v-list-tile
                :key="item.title"
                @click="moveSingle(item)">
                <v-list-tile-content>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </div>
        </v-list-group>
        <!-- <v-list-tile
          to="/wadmin/logout"
          :active-class="false"
        >
          <v-list-tile-action>
            <v-icon>power_settings_new</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Logout</v-list-tile-title>
        </v-list-tile> -->
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="primary" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>WAFOS ADMIN - {{ title }}</v-toolbar-title>
    </v-toolbar>
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
      <v-btn
        dark
        flat
        @click="snackbar = false"
        >
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  beforeUpdate () {
    for (let item of this.menuItems) {
      if (item.title === this.title) {
        item.active = true
        break
      }
    }
  },
  mounted () {
  },
  methods: {
    onDashboardClick () {
      this.isDashActive = !this.isDashActive
    },
    move (item, subItem) {
      console.log(this.$store.state.admin)
      console.log('## ', JSON.parse(this.$cookie.get('admin-acc')))
      if (this.$store.state.admin.acc == null) {
        this.$store.state.admin.acc = JSON.parse(this.$cookie.get('admin-acc'))
      }
      console.log('1', this.$cookie.get('admin-id'), this.$cookie.get('admin-id') > 2)
      if (this.$cookie.get('admin-id') > 2 && subItem.action == 'admin') {
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '접근권한이 없습니다.'
        return
      }
      if (subItem.action == 'members' && !this.$store.state.admin.acc.enterMember
        || item.action == 'agency' && !this.$store.state.admin.acc.enterAgency
        || item.action == 'device' && !this.$store.state.admin.acc.enterDevice
        || item.action == 'payment' && !this.$store.state.admin.acc.enterPayment
        || subItem.action == 'rest' && !this.$store.state.admin.acc.enterHoliday
        || subItem.action == 'admin' && !this.$store.state.admin.acc.enterAccount) {
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '접근권한이 없습니다.'
        return
      }
      var path = '/wadmin/'+item.action+'/'+subItem.action
      this.$router.push(path)
    },
    moveSingle (item) {
      console.log('2', item.action)
      if (item.action == 'members' && !this.$store.state.admin.acc.enterMember
        || item.action == 'agency' && !this.$store.state.admin.acc.enterAgency
        || item.action == 'device' && !this.$store.state.admin.acc.enterDevice
        || item.action == 'payment' && !this.$store.state.admin.acc.enterPayment
        || item.action == 'rest' && !this.$store.state.admin.acc.enterHoliday
        || item.action == 'admin' && !this.$store.state.admin.acc.enterAccount) {
        this.snackbar = true
        this.snackbar_color = 'error'
        this.snackbar_msg = '접근권한이 없습니다.'
        return
      }
      var path = '/wadmin/'+item.action
      this.$router.push(path)
    }
  },
  props: [
    'title'
  ],
  data () {
    return {
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      isDashActive: true,
      admins: [
        ['Management', 'people_outline'],
        ['Settings', 'settings']
      ],
      drawer: null,
      menuItems: [
        {
          icon: 'person',
          action: 'members',
          title: '고객 관리',
          single: true
        },
        {
          icon: 'domain',
          action: 'agency',
          title: '가맹점 관리',
          single: false,
          items: [
            {
              action: '',
              title: '가맹점 조회'
            }
          ]
        },
        {
          icon: 'local_laundry_service',
          action: 'device',
          title: '장비 관리',
          single: false,
          items: [
            {
              action: 'list',
              title: '장비 조회'
            },
            {
              action: 'brand',
              title: '제조사,모델 관리'
            },
            // {
            //   action: 'model',
            //   title: '장비 - 모델 관리'
            // },
            {
              action: 'etc_list',
              title: '기타 장비 관리'
            },
            {
              action: 'course',
              title: '표준 코스 관리'
            }
          ]
        },
        {
          icon: 'attach_money',
          action: 'payment',
          title: '매출 관리',
          single: false,
          items: [
            {
              action: '',
              title: '가맹점 매출 조회'
            },
            {
              action: 'month',
              title: '월별 매출 조회'
            },
            {
              action: 'day',
              title: '일별 매출 조회'
            }
          ]
        },
        {
          icon: 'notifications_active',
          action: 'siren',
          title: '경고 알림 관리',
          single: false
        },
        {
          icon: 'slideshow',
          action: 'marketing',
          title: 'WAFOS 광고 관리',
          single: false
        },
        {
          icon: 'settings',
          action: 'settings',
          title: '설정',
          single: false,
          items: [
            {
              action: 'translation',
              title: '번역 관리'
            },
            {
              action: 'update',
              title: '업데이트 관리'
            },
            {
              action: 'rest',
              title: '휴일 관리'
            },
            {
              action: 'admin',
              title: '관리자 계정 관리'
            },
            {
              action: 'changepassword',
              title: '비밀번호 변경'
            },
            {
              action: 'logout',
              title: '로그아웃'
            }
          ]
        }
      ]
    }
  }
}
</script>
