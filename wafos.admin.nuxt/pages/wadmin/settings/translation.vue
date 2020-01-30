<template>
  <v-content>
    <div>
      <v-tabs
        v-model="active"
        dark
        slider-color="blue"
      >
        <v-tab ripple>app</v-tab>
        <v-tab ripple>home</v-tab>
        <v-tab ripple>init</v-tab>
        <v-tab ripple>build</v-tab>
        <v-tab ripple>menu</v-tab>
        <v-tab ripple>payment</v-tab>
        <v-tab ripple>washer-step1</v-tab>
        <v-tab ripple>washer-step2</v-tab>
        <v-tab ripple>washer-step3</v-tab>
        <v-tab ripple>washer-step4</v-tab>
        <v-tab ripple>supplies-step1</v-tab>
        <v-tab ripple>airdresser-step1</v-tab>
        <v-tab ripple>shoes-washer-step1</v-tab>
        <v-tab ripple>shoes-washer-step2</v-tab>
        <v-tab ripple>shoes-washer-step3</v-tab>
        <v-tab ripple>shoes-dryer-step1</v-tab>
        <v-tab ripple>shoes-dryer-step2</v-tab>
        <v-tab ripple>shoes-dryer-step3</v-tab>
        <v-tab ripple>dryer-step1</v-tab>
        <v-tab ripple>dryer-step2</v-tab>
        <v-tab ripple>dryer-step3</v-tab>
        <v-tab ripple>dryer-step4</v-tab>
        <v-tab ripple>airconditioner-step1</v-tab>
        <v-tab ripple>register-phone</v-tab>
        <v-tab ripple>register-password</v-tab>
        <v-tab ripple>login-phone</v-tab>
        <v-tab ripple>login-password</v-tab>
      </v-tabs>
      <v-layout wrap>
        <v-flex xs12 ma-2>
          <v-card>
            <v-data-table
              :headers="headers"
              :items="transItems"
              no-data-text="등록된 데이터가 없습니다"
              hide-actions
              light>
              <template slot="items" slot-scope="props">
                <tr style="cursor: pointer;" @click="onModify(props.index, props.item)">
                  <td class="text-xs-left">{{ props.item.keyword }}</td>
                  <td class="text-xs-left">{{ props.item.kr }}</td>
                  <td class="text-xs-left">{{ props.item.en }}</td>
                  <td class="text-xs-left">{{ props.item.vn }}</td>
                </tr>
              </template>
              <template slot="footer">
              </template>
            </v-data-table>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
    <v-dialog v-model="modifyTextDialog.show" max-width="60%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row wrap>
            <v-flex xs4>
              <v-text-field
                color="primary lighten-2"
                v-model="modifyTextDialog.keyword"
                type="text"
                label="keyword"
                :disabled="true"
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex xs4>
              <v-text-field
                color="primary lighten-2"
                v-model="modifyTextDialog.kr"
                type="text"
                label="한국어"
                ></v-text-field>
            </v-flex>
            <v-flex xs4 pl-2>
              <v-text-field
                color="primary lighten-2"
                v-model="modifyTextDialog.en"
                type="text"
                label="영어"
                ></v-text-field>
            </v-flex>
            <v-flex xs4 pl-2>
              <v-text-field
                color="primary lighten-2"
                v-model="modifyTextDialog.vn"
                type="text"
                label="베트남어"
                ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="requestModifyData(modifyTextDialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="modifyTextDialog = { show: false }">닫기</v-btn>
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
  name: 'Translation',
  methods: {
    loadDatas (category) {
      if (category != null) {
        console.log(category)
        this.transItems = []
        this.$store.dispatch('transList', { category: category })
          .then((result) => {
            this.transItems = result
          })
          .catch((result) => {
            this.error = '실패했습니다'
          })
      }
    },
    onModify (index, item) {
      this.modifyTextDialog = item
      this.modifyTextDialog.show = true
    },
    requestModifyData (item) {
      this.$store.dispatch('transModify', item)
        .then((result) => {
          this.modifyTextDialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '수정되었습니다.'
        })
        .catch((result) => {
          this.error = '실패했습니다'
        })
    },
  },
  watch: {
    active: {
      handler () {
        let tabArrays = [
          'app',
          'home',
          'init',
          'build',
          'menu',
          'payment',
          'washer-step1',
          'washer-step2',
          'washer-step3',
          'washer-step4',
          'supplies-step1',
          'airdresser-step1',
          'shoes-washer-step1',
          'shoes-washer-step2',
          'shoes-washer-step3',
          'shoes-dryer-step1',
          'shoes-dryer-step2',
          'shoes-dryer-step3',
          'dryer-step1',
          'dryer-step2',
          'dryer-step3',
          'dryer-step4',
          'airconditioner-step1',
          'register-phone',
          'register-password',
          'login-phone',
          'login-password'
        ]
        this.loadDatas(tabArrays[this.active])
      }
    }
  },
  mounted () {
    this.$store
      .dispatch('updateTitle', '번역 설정')
  },
  data () {
    return {
      active: null,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      modifyTextDialog: { show: false },
      transItems: [
        {
          kr: '사과',
          en: 'apple',
          vn: 'táo'
        },
        {
          kr: '세탁기',
          en: 'washer',
          vn: 'Máy giặt'
        }
      ],
      headers: [
        {
          text: 'Keyword',
          value: 'keyword',
          align: 'left',
          sortable: false
        },
        {
          text: '한국어',
          value: 'kr',
          align: 'left',
          sortable: false
        },
        {
          text: '영어',
          value: 'en',
          align: 'left',
          sortable: false
        },
        {
          text: '베트남어',
          value: 'vn',
          align: 'left',
          sortable: false
        }
      ],
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.table-border {
  width: 100%;
  border: 1px solid #000;
}
</style>
