<template>
  <v-content>
    <v-layout row wrap>
      <v-toolbar>
        <v-btn
         icon
         @click="onBack()">
          <v-icon>arrow_back</v-icon>
        </v-btn>

        <v-toolbar-title>점포정보관리</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>
    </v-layout>
    <div>
      <v-layout wrap>
        <v-flex xs12 ma-2>
          <v-card>
            <v-layout row wrap>
              <v-subheader class="black--text">가맹점 정보 입력</v-subheader>
              <v-icon
                color="primary"
                style="cursor: pointer;"
                @click="onModify()">settings_applications</v-icon>
                <v-layout row pt-1 ml-4 v-if="isModify">
                  <v-btn 
                    color="success"
                    @click="alertDialog.show = true" small >수정</v-btn>
                </v-layout>
            </v-layout>
            <v-layout wrap>
              <v-flex xs12>
                <v-layout wrap pa-4>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs6>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="가맹점 코드"
                          readonly
                          v-model="detailData.agency_code"
                          ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs6>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="가맹점 이름"
                          readonly
                          v-model="detailData.agency_name"
                          ></v-text-field>
                      </v-flex>
                      <v-flex xs6 pl-2>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="점주 이름"
                          :disabled="!isModify"
                          v-model="detailData.agency_owner"
                          ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs6>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="가맹점 전화번호"
                          :disabled="!isModify"
                          v-model="detailData.tel"
                          ></v-text-field>
                      </v-flex>
                      <v-flex xs6 pl-2>
                        <v-text-field
                          color="primary lighten-2"
                          type="number"
                          label="휴대폰번호"
                          :disabled="!isModify"
                          v-model="detailData.phone"
                          ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs6>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="사업자등록번호"
                          :disabled="!isModify"
                          v-model="detailData.cor_number"
                          ></v-text-field>
                      </v-flex>
                      <v-flex xs6 pl-2>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="IP 주소"
                          readonly
                          v-model="detailData.ip_addr"
                          ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs4>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="우편번호"
                          readonly
                          v-model="detailData.zipcode"
                          ></v-text-field>
                      </v-flex>
                      <v-flex xs2 pl-2 v-if="isModify">
                        <v-btn @click="onPostcode()">우편번호검색</v-btn>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="가맹점 주소"
                          readonly
                          v-model="detailData.addr1"
                          ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs12>
                        <v-text-field
                          color="primary lighten-2"
                          type="text"
                          label="상세주소"
                          :disabled="!isModify"
                          v-model="detailData.addr2"
                          ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs12>
                        <v-textarea
                          color="primary lighten-2"
                          type="text"
                          label="비고"
                          :disabled="!isModify"
                          v-model="detailData.memo"
                          ></v-textarea>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12>
                    <v-layout wrap>
                      <v-flex xs6>
                        <v-text-field
                          v-model="detailData.expire_date"
                          label="유효기간"
                          prepend-icon="event"
                          readonly
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
    <v-dialog v-model="alertDialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">변경된 데이터를 저장하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="modifyData(recipeDetailData)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="alertDialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="snackbar"
      :color="'error'"
      :multi-line="snackbar_mode === 'multi-line'"
      :timeout="2500"
      :vertical="snackbar_mode === 'vertical'"
      >
      {{ errMessage }}
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
  layout: 'nomenu',
  name: 'AgencyDetail',
  // props: [
  //   'rid', 'mode'
  // ],
  methods: {
    // API
    loadDetailData () {
      if (this.$store.state.adminAgency.wash == null) {
        this.$store.state.adminAgency.wash = this.$cookie.get('agency-info')
      }
      this.$store.dispatch('AgencyDetail', this.$store.state.adminAgency.wash)
        .then((result) => {
          this.detailData = result
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    modifyData (item) {
      console.log('#')
    },
    // COMPONENT FUNC
    onBack () {
      this.$router.go(-1)
    },
    onModify () {
      // if (this.isModify) {
      //   this.alertDialog.show = true
      // } else {
        // 상태 전환
        this.isModify = !this.isModify
      // }
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '가맹점 상세보기')
    this.loadDetailData()
  },
  data () {
    return {
      // [[ Select Device Dialog
      detailData: {},
      detailData: { show: false },
      select_device_dialog: { show: false },
      // Select Device Dialog ]]
      selUsed: ['사용', '사용안함'],
      selectUsedItem: '사용',
      snackbar: false,
      snackbar_mode: false,
      panel: false,
      active: null,
      date: null,
      menu: false,
      uiChange: 0,
      actionItems: ['수정', '삭제'],
      alertDialog: { show: false },
      isModify: false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .tile {
    margin: 5px;
    border-radius: 4px;
  }
  .tile:hover {
    background: green;
  }
  .tile:active {
    background: yellow;
  }
</style>
