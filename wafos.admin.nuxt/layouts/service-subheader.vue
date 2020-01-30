<template>
  <v-app>
    <v-container text-xs-center fluid mx-0 px-0 pt-0>
      <wise-top-menu />
      <v-fab-transition>
        <v-btn
          color="#e8783c"
          class="elevation-0 hidden-sm-and-down float-menu"
          fab
          fixed
          bottom
          right>
          <img src="/chat_btn.png" width="25">
        </v-btn>
      </v-fab-transition>
      <!-- drawer button -->
      <v-btn
        :class="rightSideToggleClasses"
        color="#254D70"
        @click.stop="rightSide= !rightSide">
        <v-icon v-if="rightSide">
          chevron_right
        </v-icon>
        <v-icon v-else>
          chevron_left
        </v-icon>
      </v-btn>
      <v-navigation-drawer
        stateless
        fixed
        height="340"
        width="100"
        touchless
        dark
        floating
        class="rightside hidden-sm-and-down"
        v-model="rightSide"
        right>
        <div>
          <div class="mt-4">
            <v-layout wrap justify-center
              v-for="item in rightSideItems"
              :key="item.desc"
              class="white--text my-4"
              >
              <v-flex xs12 class="title">
                <animate-number
                  from="1" 
                  :to="item.value" 
                  duration="1000" 
                  easing="easeOutQuad"
                  :formatter="formatter"
                  >
                </animate-number>
              </v-flex>
              <v-flex xs12
                class="caption mt-1"
                max-width="40"
                v-html="item.desc">
              </v-flex>
            </v-layout>
          </div> <!-- mt-4 -->
        </div>
      </v-navigation-drawer>
    </v-container>
    <nuxt />
    <div class="footer">
      <v-container text-xs-center>
        <v-layout row wrap>
          <v-flex xs3>
            <div class="footer_logo">
              <router-link to="/">
                <img src="/footer_logo.png" alt="푸터로고">
              </router-link>
            </div>
          </v-flex>
          <v-flex xs3>
            <div class="footer_part1">
              경기도 남양주시 화도읍 폭포로242번길 35<br>
              <br>
              사업자번호 : 760-55-00228<br>
              통신판매업 : 제 2018-화도수동-0043호<br>
              대표자 : 박타미
            </div>
          </v-flex>
          <v-flex xs4>
            <div class="footer_part2">CALL CENTER<br>
              <div class="part2_text">
                  평일 10:00-18:00 (토,일,공휴일은 휴무입니다)<br>
                  <i class="material-icons">email</i><span class="email">care@yespicnic.com</span><br>
                  <i class="material-icons clear">call</i><span class="call">070-8823-1810</span>
              </div>
            </div>
          </v-flex>
          <v-flex xs2>
            <div class="sns">
                <a href="/"><img src="/fb.png"></a>
                <a href="/"><img src="/instargram.png"></a>
                <a href="/"><img src="/twitter.png"></a>
              </div>
          </v-flex>
        </v-layout>
      </v-container>
    </div>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'
import AnimateNumber from '@/components/AnimateNumber'
import WiseTopMenu from '@/components/WiseTopMenu'

export default {
  name: 'App',
  components: {
    AnimateNumber,
    WiseTopMenu
  },
  computed: {
    ...mapGetters([
      'currentTitle'
    ])
  },
  methods: {
    formatter (num) {
      if (num === 0) {
        return 0
      }

      num = num.toFixed(0)

      let reg = /(^[+-]?\d+)(\d{3})/
      let n = (num + '')
      while (reg.test(n)) {
        n = n.replace(reg, '$1' + ',' + '$2')
      }
      return n
    },
    getGlobalInfo () {
      this.$store.dispatch('GlobalInfo')
        .then((result) => {
          this.rightSideItems = [
            { 'desc': '총 방문자', 'value': result.hit },
            { 'desc': '함께한 반려견', 'value': result.pet },
            { 'desc': '총 끼니', 'value': result.recipe },
            { 'desc': '현재 함께<br/> 보고 있어요', 'value': result.view }
          ]
        })
        .catch((result) => {
          this.error = '사용자 정보를 가져오는데 실패했습니다'
        })
    }
  },
  watch: {
    rightSide (val) {
      if (val) {
        this.rightSideToggleClasses['rightside--toggle'] = true
        this.rightSideToggleClasses['rightside--toggle--hided'] = false
      } else {
        this.rightSideToggleClasses['rightside--toggle'] = false
        this.rightSideToggleClasses['rightside--toggle--hided'] = true
      }
    }
  },
  mounted () {
    this.getGlobalInfo()
  },
  data () {
    return {
      rightSideItems: [],
      rightSide: true,
      rightSideToggleClasses: {
        'rightside--toggle': true,
        'rightside--toggle--hided': false,
        'white--text': true,
        'text-xs-center': true,
        'elevation-0': true,
        'hidden-sm-and-down': true
      }
    }
  }
}
</script>

<style scoped>
#app {
  background:#fede57;
  width:100%;
}

.container{
  padding-bottom:0;
}

.primary_text {
  color: #e5873c;
}

.rightside {
  margin-top: 150px !important;
  background-color: #182534 !important;
  border-bottom-left-radius: 35px;
}

.rightside--toggle {
  position: fixed !important;
  left: calc(100% - 100px - 36px);
  top: 150px;
  margin: 0;
  padding: 0;
  width: 36px;
  min-width: 36px;
  border-bottom-left-radius: 10px;
  z-index: 1000;
}

.rightside--toggle--hided {
  position: fixed !important;
  left: calc(100% - 36px);
  top: 150px;
  margin: 0;
  padding: 0;
  width: 36px;
  min-width: 36px;
  border-bottom-left-radius: 10px;
  z-index: 1000;
}

.rightside--toggle:hover {
  position: fixed;
}

.rightside--toggle * {
  padding: 0 !important;
  margin: 0 !important;
  font-size: 30px !important;
}

.rightside--toggle--hided * {
  padding: 0 !important;
  margin: 0 !important;
  font-size: 30px !important;
}

/* footer */

.footer {
  background:#182534;
  padding-top:15px;
  color:#cdcecd;
}

.footer_logo img {
  width:150px;
  margin-left:-80px;
}

.footer_part1 {
  width:300px;
  float:left;
  text-align:left;
  margin-left:20px;
  font-size:13px;
}

.footer_part2 {
  width:300px;
  float:left;
  text-align:left;
  font-weight:bold;
  font-size:14px;
}

.part2_text {
  font-weight:normal;
  padding-top:10px;
  font-size:13px;
}

.material-icons {
  font-size:18px;
  margin-top:5px;
  float:left;
}

.email, .call {
  float:left;
  margin:4px 0 0 8px;
}

.clear {
  clear:both;
}

.sns {
  margin-top:25px;
}

.sns img {
  width:40px;
}

.float-menu {
  margin-bottom: 140px;
}
</style>
