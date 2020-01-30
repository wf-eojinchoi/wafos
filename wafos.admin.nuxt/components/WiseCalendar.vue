<template>
  <div>
    <v-layout wrap justify-center>
      <!-- 캘린더 월 표기부분 -->
      <v-flex xs10 sm6>
        <v-layout wrap justify-space-around>
          <v-flex xs3>
            <v-btn fab icon color="black" dark small>
              <v-icon dark large>chevron_left</v-icon>
            </v-btn>
          </v-flex>
          <v-flex xs4 sm6 class="align-self-center text-xs-center">
            <span class="headline font-weight-bold">{{ headerDate }}</span>
          </v-flex>
          <v-flex xs3>
            <v-btn fab icon color="black" dark small>
              <v-icon dark large>chevron_right</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex> 
      <!-- 캘린더 표기부분 -->
      <v-flex xs12>
        <!-- 요일 -->
        <v-layout wrap justify-space-around my-5>
          <v-flex xs1 class="grey--text">일</v-flex>
          <v-flex xs1>월</v-flex>
          <v-flex xs1>화</v-flex>
          <v-flex xs1>수</v-flex>
          <v-flex xs1>목</v-flex>
          <v-flex xs1>금</v-flex>
          <v-flex xs1 class="grey--text">토</v-flex>
        </v-layout>
        <v-layout
          class="text-xs-center"
          v-for="(row, ridx) in calValues"
          :key="`row-${ridx}`"
          wrap justify-space-around my-5>
            <template
              v-for="(cell, cidx) in row">
              <v-flex xs1 :class="`cell`" :key="`col-${cidx}`">
                <v-layout wrap justify-center>
                  <v-flex xs12 sm8 md6 lg4 xl2
                    :class="`cell__number cell__number--${cell.type}`">
                    <v-img class="caption cell__numberbg" :src="`/calendar/${cell.type}-bg.png`">
                      {{ cell.value }}
                    </v-img>
                  </v-flex>
                  <v-flex xs12 :class="`cell__caption--${cell.type}`">
                    <span class="caption font-weight-bold">{{ cell.caption }}</span>
                  </v-flex>
                </v-layout>
              </v-flex>
            </template>
        </v-layout>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
export default {
  name: 'WiseCalendar',
  components: {
  },
  props: {
  },
  mounted () {

  },
  computed: {
    headerDate () {
      return this.today.getFullYear() + '. ' + ('0' + this.today.getMonth() + 1).slice(-2)
    },
    calValues () {
      let currentYear = this.today.getFullYear()
      let currentMonth = this.today.getMonth()
      let currentDate = this.today.getDate()
      let firstDay = new Date(currentYear, currentMonth, 1)
      let lastDay = null
      if (currentMonth === 12) lastDay = new Date(currentYear + 1, 1, 0)
      else lastDay = new Date(currentYear, currentMonth + 1, 0)

      let padded = firstDay.getDay()
      let paddedDate = new Date(firstDay - (1000 * 3600 * 24) * padded)
      let results = []
      let values = []

      /* 이전달 날짜를 채워 넣음 */
      for (let i = 0; i < padded; i++) {
        values.push(
          { disable: true, value: i + paddedDate.getDate() }
        )
      }
      /* 이달 날짜를 채워 넣음 */
      for (let i = 1; i <= lastDay.getDate(); i++) {
        if (i === currentDate) {
          values.push(
            { value: i, type: 'today', caption: '오늘' }
          )
        } else if (i === 15) {
          values.push(
            { value: i, type: 'payment', caption: '결제 예정일' }
          )
        } else if (i === 18) {
          values.push(
            { value: i, type: 'receive', caption: '배송 예정일' }
          )
        } else {
          values.push(
            { value: i, type: 'normal' }
          )
        }
        if (values.length === 7) {
          results.push(values)
          values = []
        }
      }
      /* 마지막 행이 모자라는 경우 채워서 추가 */
      if (values.length !== 0) {
        for (let i = values.length; i < 7; i++) {
          values.push({ value: '', type: 'disable' })
        }
        results.push(values)
      }
      console.log(results)
      return results
    }
  },
  data () {
    return {
      today: new Date()
    }
  }
}
</script>

<style scoped>
.cell {
  height: 50px;
}

.cell__number {
  width: 100%;
}

.cell__numberbg {
  align-items: center
}

.cell__number--normal {
  color: #000;
}

.cell__number--today {
  color: #dc6f30;
}

.cell__caption--today {
  color: #dc6f30;
}

.cell__number--payment {
  position: relative;
  color: #fff;
}

.cell__caption--payment {
  color: #37518c;
}

.cell__number--receive {
  position: relative;
  color: #fff;
}

.cell__caption--receive {
  color: #dc6f30;
}
.cell__number--disable {
  color: 'grey';
}

</style>
