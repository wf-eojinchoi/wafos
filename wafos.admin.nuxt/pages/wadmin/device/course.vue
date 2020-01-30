<template>
  <v-content>
    <div>
      <v-tabs
        v-model="active"
        dark
        slider-color="blue"
      >
        <v-tab
          ripple
        >
          세탁기
        </v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-card-title>
                  <v-layout row >
                    <v-flex xs12 >
                      <table width="100%">
                        <tbody>
                          <td >
                          </td>
                          <td >
                            <v-layout row>
                              <v-flex text-xs-right pt-1>
                                <v-btn color="primary" @click="onRegCourse()">코스 추가</v-btn>
                              </v-flex>
                            </v-layout>
                          </td>
                        </tbody>
                      </table>
                    </v-flex>
                  </v-layout>
                </v-card-title>
                <v-flex xs12>
                  <v-data-table
                    :items="courseItems"
                    :headers="headers"
                    hide-actions
                    no-data-text="등록된 코스가 없습니다"
                    light>
                    <!-- <template v-slot:items="props"> -->
                    <template slot="items" slot-scope="props">
                      <tr style="cursor: pointer;" @click="courseDetail(props.item)">
                        <!-- <td class="text-xs-center">{{ props.item.title }}</td> -->
                        <td class="text-xs-left">
                          [한글] {{ props.item.title }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.title_en ? props.item.title_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.title_vn ? props.item.title_vn : '등록안됨' }}</span>
                        </td>
                        <td class="text-xs-left">
                          [한글] {{ props.item.description }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.description_en ? props.item.description_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</span>
                        </td>
                        <!-- <td class="text-xs-center">{{ props.item.description_en ? props.item.description_en : '등록안됨' }}</td>
                        <td class="text-xs-center">{{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</td> -->
                        <td class="text-xs-center">{{ props.item.amount }}</td>
                        <td class="text-xs-center">
                          <v-icon class="red--text" @click.stop="onDelete(props.item)">delete_forever</v-icon>
                        </td>
                      </tr>
                    </template>
                  </v-data-table>
                </v-flex>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
        <v-tab
          ripple
        >
          트롬 스타일러
        </v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-card-title>
                  <v-layout row >
                    <v-flex xs12 >
                      <table width="100%">
                        <tbody>
                          <td >
                          </td>
                          <td >
                            <v-layout row>
                              <v-flex text-xs-right pt-1>
                                <v-btn color="primary" @click="onRegCourse()">코스 추가</v-btn>
                              </v-flex>
                            </v-layout>
                          </td>
                        </tbody>
                      </table>
                    </v-flex>
                  </v-layout>
                </v-card-title>
                <v-flex xs12>
                  <v-data-table                   
                    :headers="headers"
                    :items="courseItems"
                    :pagination.sync="pagination"
                    :rows-per-page-items="[10,{'text':'All','value':-1}]"
                    :total-items="totalitems"
                    :loading="loading"            
                    no-data-text="등록된 코스가 없습니다"
                    no-results-text="검색 결과가 없습니다"
                    light>
                    <!-- <template v-slot:items="props"> -->
                    <template slot="items" slot-scope="props">
                      <tr style="cursor: pointer;" @click="courseDetail(props.item)">
                        <!-- <td class="text-xs-center">{{ props.item.title }}</td> -->
                        <td class="text-xs-left">
                          [한글] {{ props.item.title }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.title_en ? props.item.title_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.title_vn ? props.item.title_vn : '등록안됨' }}</span>
                        </td>
                        <td class="text-xs-left">
                          [한글] {{ props.item.description }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.description_en ? props.item.description_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</span>
                        </td>
                        <!-- <td class="text-xs-center">{{ props.item.description_en ? props.item.description_en : '등록안됨' }}</td>
                        <td class="text-xs-center">{{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</td> -->
                        <td class="text-xs-center">{{ props.item.amount }}</td>
                        <td class="text-xs-center">
                          <v-icon class="red--text" @click.stop="onDelete(props.item)">delete_forever</v-icon>
                        </td>
                      </tr>
                    </template>
                    <template slot="footer">
                    </template> 
                  </v-data-table>
                </v-flex>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
        <v-tab
          ripple
        >
          운동화 세탁기
        </v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-card-title>
                  <v-layout row >
                    <v-flex xs12 >
                      <table width="100%">
                        <tbody>
                          <td >
                          </td>
                          <td >
                            <v-layout row>
                              <v-flex text-xs-right pt-1>
                                <v-btn color="primary" @click="onRegCourse()">코스 추가</v-btn>
                              </v-flex>
                            </v-layout>
                          </td>
                        </tbody>
                      </table>
                    </v-flex>
                  </v-layout>
                </v-card-title>
                <v-flex xs12>
                  <v-data-table
                    :items="courseItems"
                    :headers="headers"
                    hide-actions
                    no-data-text="등록된 코스가 없습니다"
                    light>
                    <!-- <template v-slot:items="props"> -->
                    <template slot="items" slot-scope="props">
                      <tr style="cursor: pointer;" @click="courseDetail(props.item)">
                        <!-- <td class="text-xs-center">{{ props.item.title }}</td> -->
                        <td class="text-xs-left">
                          [한글] {{ props.item.title }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.title_en ? props.item.title_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.title_vn ? props.item.title_vn : '등록안됨' }}</span>
                        </td>
                        <td class="text-xs-left">
                          [한글] {{ props.item.description }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.description_en ? props.item.description_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</span>
                        </td>
                        <!-- <td class="text-xs-center">{{ props.item.description_en ? props.item.description_en : '등록안됨' }}</td>
                        <td class="text-xs-center">{{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</td> -->
                        <td class="text-xs-center">{{ props.item.amount }}</td>
                        <td class="text-xs-center">
                          <v-icon class="red--text" @click.stop="onDelete(props.item)">delete_forever</v-icon>
                        </td>
                      </tr>
                    </template>
                  </v-data-table>
                </v-flex>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
        <v-tab
          ripple
        >
          멀티자판기
        </v-tab>
        <v-tab-item>
          <v-layout wrap>
            <v-flex xs12 ma-2>
              <v-card>
                <v-card-title>
                  <v-layout row >
                    <v-flex xs12 >
                      <table width="100%">
                        <tbody>
                          <td >
                          </td>
                          <td >
                            <v-layout row>
                              <v-flex text-xs-right pt-1>
                                <v-btn color="primary" @click="onRegCourse()">코스 추가</v-btn>
                              </v-flex>
                            </v-layout>
                          </td>
                        </tbody>
                      </table>
                    </v-flex>
                  </v-layout>
                </v-card-title>
                <v-flex xs12>
                  <v-data-table
                    :items="courseItems"
                    :headers="headers"
                    hide-actions
                    no-data-text="등록된 코스가 없습니다"
                    light>
                    <!-- <template v-slot:items="props"> -->
                    <template slot="items" slot-scope="props">
                      <tr style="cursor: pointer;" @click="courseDetail(props.item)">
                        <!-- <td class="text-xs-center">{{ props.item.title }}</td> -->
                        <td class="text-xs-left">
                          [한글] {{ props.item.title }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.title_en ? props.item.title_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.title_vn ? props.item.title_vn : '등록안됨' }}</span>
                        </td>
                        <td class="text-xs-left">
                          [한글] {{ props.item.description }}<br>
                          <span style="color: #10308F;">[영어] {{ props.item.description_en ? props.item.description_en : '등록안됨' }}</span><br>
                          <span style="color: #8F2510;">[베트남어] {{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</span>
                        </td>
                        <!-- <td class="text-xs-center">{{ props.item.description_en ? props.item.description_en : '등록안됨' }}</td>
                        <td class="text-xs-center">{{ props.item.description_vn ? props.item.description_vn : '등록안됨' }}</td> -->
                        <td class="text-xs-center">{{ props.item.amount }}</td>
                        <td class="text-xs-center">
                          <v-icon class="red--text" @click.stop="onDelete(props.item)">delete_forever</v-icon>
                        </td>
                      </tr>
                    </template>
                  </v-data-table>
                </v-flex>
              </v-card>
            </v-flex>
          </v-layout>
        </v-tab-item>
      </v-tabs>
    </div>
    <v-dialog v-model="courseRegDialog.show" max-width="70%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout wrap>
            <v-flex xs4>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.title"
                label="코스이름"></v-text-field>
            </v-flex>
            <v-flex xs4 pl-2>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.title_en"
                label="코스이름(영어)"></v-text-field>
            </v-flex>
            <v-flex xs4 pl-2>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.title_vn"
                label="코스이름(베트남어)"></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.description"
                label="코스설명-한국어"></v-text-field>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.description_en"
                label="코스설명-영어"></v-text-field>
              <v-text-field
                color="primary lighten-2"
                type="text"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.description_vn"
                label="코스설명-베트남어"></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="number"
                suffix="원"
                :disabled="courseRegDialog.read"
                v-model="courseRegDialog.amount"
                label="금액"></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="courseModify(courseRegDialog)" v-if="courseRegDialog.mode">코스수정</v-btn>
          <v-btn color="primary darken-1" flat @click="courseRegist(courseRegDialog)" v-else>코스추가</v-btn>
          <v-btn color="grey darken-1" flat @click.native="courseRegDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_delete_dialog.show" max-width="430" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="courseDelete(model_delete_dialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_delete_dialog = { show: false }">닫기</v-btn>
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
      <v-btn
        dark
        flat
        @click="snackbar = false"
        >
        Close
      </v-btn>
    </v-snackbar>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'DefaultCourseMgr',
  methods: {
    // API
    reloadDatas (active) {
      this.loading = true
      console.log('reloadDatas active:', active)
      console.log('reload->', active)
      if(active == null){
        console.log('active is null')
      }

      if (active != null) {
        this.courseItems = []
        if (active === 1){//active=1
          active = 2//트롬스타일러
        } else if (active === 2){//active=2
          active = 3//운동화세탁기
        } else if (active === 3){//active=3
          active = 6//멀티자판기
        }

        console.log('active :', this.active,', type :', active)

        this.$store.dispatch('StandardCourseList', {
          page: this.pagination.page,//undefined
          sortby: this.pagination.sortBy,
          descending: this.pagination.descending,
          type: active//
        })
          .then((result) => {
            this.loading = false
            this.courseItems = result.results
            console.log('courseItems :', courseItems)//추가
            this.totalitems = result.count//추가
            console.log('totalitems :', totalitems)//추가

            console.log(result)//추가
          })
          .catch((result) => {
            this.error = '실패했습니다'
            this.loading = false
          })
      }
    },
    // CRUD
    onRegCourse () {
      this.courseRegDialog.show = true
    },
    courseRegist (item) {
      var param = item
      param.type = this.active
      this.$store.dispatch('StandardCourseRegister', param)
        .then((result) => {
          if (result.success) {
            this.courseRegDialog = { show:false }
            this.reloadDatas(this.active)
          } else {
            this.courseRegDialog = null
            this.courseRegDialog = { show: false }
            this.snackbar = true
            this.snackbar_color = 'error'
            this.snackbar_msg = result.msg
          }
        })
        .catch((result) => {
          this.error = '실패했습니다'
          this.loading = false
          console.log(result)
        })
    },
    courseModify (item) {
      var param = item
      param.type = this.active
      this.$store.dispatch('StandardCourseModify', param)
        .then((result) => {
          this.courseRegDialog = { show:false }
          this.reloadDatas(this.active)
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
    courseDetail (item) {
      this.courseRegDialog = item
      this.courseRegDialog.mode = true
      this.courseRegDialog.show = true
    },
    onDelete (item) {
      this.model_delete_dialog = item
      this.model_delete_dialog.show = true
    },
    courseDelete (item) {
      this.$store.dispatch('StandardCourseDelete', item.id)
        .then((result) => {
          if (result) {
            this.model_delete_dialog = { show:false }
            this.reloadDatas(this.active)
          }
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    }
  },
  created () {
    console.log('## created ##')
    this.active = 0
  },
  mounted () {
    this.$store.dispatch('updateTitle', '표준 코스 관리')
    // this.reloadDatas()
  },
  watch: {
    //tab바뀔때는 페이지번호1번
    active: {
      handler () {
        console.log('watch active called')
        console.log('watch active this.active :', this.active)
        this.pagination.page = 1
        this.reloadDatas(this.active)
      },
    deep:true
    },
    pagination: {
      handler () {
        console.log('watch pagination called')
        console.log('watch pagination this.active :', this.active)
        console.log('watch pagination.page :', this.pagination.page)
        this.reloadDatas(this.active)
      }
    }
  },
  data () {
    return {
      // wash
      totalitems: 0,
      pagination: {},
      loading: false,
      model_delete_dialog: { show:false },
      courseRegDialog: { show:false },
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      active: null,
      courseItems: [],
      headers: [
        {
          text: '코스 이름',
          value: '',
          align: 'left',
          sortable: false
        },
        {
          text: '코스 설명',
          value: '',
          align: 'left',
          sortable: false
        },
        // {
        //   text: '코스 설명(영어)',
        //   value: '',
        //   align: 'center',
        //   sortable: false
        // },
        // {
        //   text: '코스 설명(베트남)',
        //   value: '',
        //   align: 'center',
        //   sortable: false
        // },
        {
          text: '금액',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '',
          value: '',
          align: 'center',
          sortable: false
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.font_color {
  color: darkblue;
}
</style>
