<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 >
      </v-flex>
    </v-layout>
    <v-layout wrap>
      <v-flex xs4 ma-2>
        <v-flex xs12>
          <v-card>
            <v-card-title>
              <v-layout row>
                <v-flex xs12 >
                  <table width="100%">
                    <tbody>
                      <td >
                        <v-subheader class="black--text">제조사 목록</v-subheader>
                      </td>
                      <td >
                        <v-layout row>
                          <v-flex text-xs-right pt-1>
                            <v-btn color="primary" small @click="onBrandRegister()">제조사 추가</v-btn>
                          </v-flex>
                        </v-layout>
                      </td>
                    </tbody>
                  </table>
                </v-flex>
              </v-layout>
            </v-card-title>
            <v-data-table
              :search="search"
              :headers="headers"
              :items="brandItems"
              :loading="loading"
              no-data-text="등록된 데이터가 없습니다"
              no-results-text="검색 결과가 없습니다"
              light
              hide-actions>

              <template slot="items" slot-scope="props">
                <tr style="cursor: pointer;" @click="onBrandModify(props.index, props.item)">
                  <td class="text-xs-center">{{ props.item.name }}</td>
                  <td class="text-xs-center">
                    <v-icon class="red--text" @click.stop="onBranDeleteDialog(props.item)">delete_forever</v-icon>
                  </td>
                </tr>
              </template>
            </v-data-table>
          </v-card>
        </v-flex>
      </v-flex>
      <v-flex xs6>
        <v-flex xs12 ma-2>
          <v-card>
            <v-card-title>
              <v-layout row>
                <v-flex xs12 >
                  <table width="100%">
                    <tbody>
                      <td >
                        <v-subheader class="black--text">모델 목록</v-subheader>
                      </td>
                      <!-- <td class="text-xs-right">
                        <v-layout row >
                        </v-layout>
                      </td> -->
                      <td>
                        <v-layout row>
                          <v-spacer></v-spacer>
                          <v-flex xs4 text-xs-right>
                            <v-select
                              :items="selectBrand"
                              v-model="sort_by_brand"
                              label="제조사"
                            ></v-select>
                          </v-flex>
                        </v-layout>
                      </td>
                      <td >
                        <v-layout row>
                          <v-flex text-xs-right pt-1>
                            <v-btn color="primary" small @click="onModelRegister()">모델 추가</v-btn>
                          </v-flex>
                        </v-layout>
                      </td>
                    </tbody>
                  </table>
                </v-flex>
              </v-layout>
            </v-card-title>
            <v-data-table
              :search="search"
              :headers="modelHeaders"
              :items="modelItems"
              :pagination.sync="pagination"
              :rows-per-page-items="[20,{'text':'All','value':-1}]"
              :total-items="totalitems"
              :loading="loading"
              no-data-text="등록된 데이터가 없습니다"
              no-results-text="검색 결과가 없습니다"
              light>
              <template slot="items" slot-scope="props">
                <tr style="cursor: pointer;" @click="onModelModify(props.index, props.item)">
                  <td class="text-xs-center">{{ props.item.brand ? props.item.brand.name : '-' }}</td>
                  <td class="text-xs-center">{{ props.item.name }}</td>
                  <td class="text-xs-center">
                    <v-icon class="red--text" @click.stop="onModelDeleteDialog(props.item)">delete_forever</v-icon>
                  </td>
                </tr>
              </template>
              <template slot="footer">
              </template>
            </v-data-table>
          </v-card>
        </v-flex>
      </v-flex>
    </v-layout>
    <v-dialog v-model="brand_delete_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">'{{ brand_delete_dialog.name }}' 삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="deleteBrandData(brand_delete_dialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="brand_delete_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_delete_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">'{{ model_delete_dialog.name }}' 삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="deleteModelData(model_delete_dialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_delete_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="brand_register_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row>
            <v-flex xs12>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                v-model="brand_register_dialog.name"
                type="text"
                label="제조사명"
                :value="brand_register_dialog.name"
                ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" v-if="!brand_register_dialog.mode" flat @click="registerBrandData(brand_register_dialog)">등록하기</v-btn>
          <v-btn color="primary darken-1" v-if="brand_register_dialog.mode" flat @click="modifyBrandData(brand_register_dialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="brand_register_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_register_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row>
            <v-flex xs12>
            </v-flex>
          </v-layout>
          <v-layout row>
            <!-- <v-flex xs12 v-if="model_register_dialog.mode">
              <v-text-field
                color="primary lighten-2"
                v-model="model_register_dialog.brand.name"
                type="text"
                label="제조사명"
                :value="model_register_dialog.brand.name"
                ></v-text-field>
            </v-flex>
            <v-flex xs12 v-else> -->
            <v-flex xs12>
              <v-select
                :items="selBrand"
                v-model="model_register_dialog.brand_name"
                label="제조사 선택"
              ></v-select>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                v-model="model_register_dialog.name"
                type="text"
                label="모델명"
                ></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                v-model="model_register_dialog.serial"
                type="text"
                label="시리얼"
                ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" v-if="!model_register_dialog.mode" flat @click="registerModelData(model_register_dialog)">등록하기</v-btn>
          <v-btn color="primary darken-1" v-if="model_register_dialog.mode" flat @click="modifyModelData(model_register_dialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_register_dialog = { show: false }">닫기</v-btn>
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
  name: 'DeviceBrandMgr',
  methods: {
    // API
    reloadBrandDatas () {
      this.$store.dispatch('BrandList')
        .then((result) => {
          this.brandItems = result.results
          for(let k in result.results) {
            this.selBrand.push(result.results[k].name)
            this.selectBrand.push(result.results[k].name)
          }
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    reloadModelDatas () {
      this.$store.dispatch('ModelList', {
        brand: this.sort_by_brand,
        page : this.pagination.page//추가(2020.01.30)
      })
        .then((result) => {
          console.log('brand.vue result.results')
          this.modelItems = result.results
          this.totalitems = result.count//추가(2020.01.30)
          console.log('result :', result)
        })
        .catch((result) => {
          console.log('modellist catch : ', result)
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    // BRAND
    onBrandRegister () {
      this.brand_register_dialog.show = true
    },
    onBrandModify (index, item) {
      this.brand_register_dialog = item
      this.brand_register_dialog.mode = true
      this.brand_register_dialog.show = true
    },
    onBranDeleteDialog (item) {
      this.brand_delete_dialog = item
      this.brand_delete_dialog.show = true
    },
    registerBrandData (item) {
      this.$store.dispatch('BrandRegister', item)
        .then((result) => {
          this.brand_register_dialog = { show: false, mode: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '등록되었습니다.'
          this.reloadBrandDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    modifyBrandData (item) {
      this.$store.dispatch('BrandModify', item)
        .then((result) => {
          this.brand_register_dialog = { show: false, mode: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '수정하였습니다.'
          this.reloadBrandDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    deleteBrandData (item) {
      this.$store.dispatch('BrandDelete', item.id)
        .then((result) => {
          this.brand_delete_dialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '삭제되었습니다.'
          this.reloadBrandDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    // Model
    onModelRegister () {
      this.model_register_dialog.show = true
    },
    onModelModify (index, item) {
      this.model_register_dialog = item
      this.model_register_dialog.brand_name = item.brand.name
      this.model_register_dialog.mode = true
      this.model_register_dialog.show = true
    },
    onModelDeleteDialog (item) {
      this.model_delete_dialog = item
      this.model_delete_dialog.show = true
    },
    registerModelData (item) {
      this.$store.dispatch('ModelRegister', item)
        .then((result) => {
          this.model_register_dialog = { show: false, mode: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '등록되었습니다.'
          this.reloadModelDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    modifyModelData (item) {
      this.$store.dispatch('ModelModify', item)
        .then((result) => {
          this.model_register_dialog = { show: false, mode: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '수정하였습니다.'
          this.reloadModelDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    deleteModelData (item) {
      this.$store.dispatch('ModelDelete', item.id)
        .then((result) => {
          this.model_delete_dialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '삭제되었습니다.'
          this.reloadModelDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    }
  },
  created () {
    console.log('## brand.vue created ##')
    this.reloadBrandDatas()
  },
  mounted () {
    this.$store.dispatch('updateTitle', '장비 - 제조사 관리')
  },
  watch: {
    pagination: {
      handler () {
        console.log('watch pagination called')
        this.reloadModelDatas()
      },
    deep: true
    },
    search: {
      handler () {
        this.pagination.page = 1
        this.reloadDatas()
      }
    },
    sort_by_brand: {
      handler () {
        this.reloadModelDatas()
      }
    }
  },
  data () {
    return {
      sort_by_brand: '전체',
      selectBrand: ['전체'],
      selectBrandItem: null,
      table_selected: [],
      brand_register_dialog: { show: false, mode: false },
      model_register_dialog: { show: false, mode: false },
      brand_delete_dialog: { show: false },
      model_delete_dialog: { show: false },
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      brandItems: [],
      // Model
      selBrand: [],
      selectBrandItem: null,
      modelItems: [],
      selected: [],
      headers: [
        {
          text: '제조사명',
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
      ],
      modelHeaders: [
        {
          text: '제조사명',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '모델명',
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
