<template>
  <v-content>
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
                        <v-select
                          :items="classifyTypes"
                          v-model="classifyTypesVal"
                          label="타입"
                        ></v-select>
                        <v-flex text-xs-right pt-1>
                          <v-btn color="primary" @click="addDevice()">장비 추가</v-btn>
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
            :items="items"
            :pagination.sync="pagination"
            :rows-per-page-items="[20,{'text':'All','value':-1}]"
            :total-items="totalitems"
            :loading="loading"
            no-data-text="등록된 데이터가 없습니다"
            no-results-text="검색 결과가 없습니다"
            light>

            <template slot="items" slot-scope="props">
              <tr style="cursor: pointer;" @click="onDetail(props.index, props.item)">
                <td >
                  <v-layout row pa-2>
                    <v-img
                      :src="props.item.photo"
                      :lazy-src="props.item.photo"
                      aspect-ratio="1"
                      class="grey lighten-2"
                    >
                      <v-layout
                        slot="placeholder"
                        fill-height
                        align-center
                        justify-center
                        ma-0
                      >
                        <!-- <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular> -->
                      </v-layout>
                    </v-img>
                  </v-layout>
                </td>
                <td class="text-xs-center">{{ props.item.brand.name }}</td>
                <td class="text-xs-center">{{ props.item.model.name }}</td>
                <td class="text-xs-center">{{ getTypeStr(props.item.type) }}</td>
                <td class="text-xs-center">{{ props.item.kg }}</td>
                <td class="text-xs-center">{{ props.item.reg_dttm }}</td>
                <td>
                  <v-menu open-on-hover top offset-y>
                    <!-- <v-icon
                      slot="activator"
                      color="primary"
                      dark
                    >
                      Dropdown
                    </v-btn> -->
                    <v-icon
                      color="primary"
                      slot="activator">settings_applications</v-icon>

                    <v-list>
                      <v-list-tile
                        v-for="(item, index) in actionItems"
                        :key="index"
                        @click="onOptionClick(index, props.item)"
                      >
                        <v-list-tile-title>{{ actionItems[index] }}</v-list-tile-title>
                      </v-list-tile>
                    </v-list>
                  </v-menu>
                </td>
              </tr>
            </template>
            <template slot="footer">
            </template>
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="model_delete_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <span class="subheading">삭제하시겠습니까?</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="deleteData(model_delete_dialog)">삭제하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_delete_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="model_register_dialog.show" max-width="50%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-subheader class="black--text">장비 추가</v-subheader>
          <v-layout row wrap>
              <v-flex xs3 mr-2 mt-3>
                <v-layout row>
                  <v-img
                    :src="imageSrc"
                    :lazy-src="imageSrc"
                    aspect-ratio="1"
                    class="grey lighten-2"
                  >
                    <v-layout
                      slot="placeholder"
                      fill-height
                      align-center
                      justify-center
                      ma-0
                    >
                      <!-- <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular> -->
                    </v-layout>
                  </v-img>
                </v-layout>
                <v-layout row>
                  <v-flex text-xs-center v-if="!model_register_dialog.read">
                    <v-btn color="primary" @click="pickFile()">장비 이미지 추가</v-btn>
                    <input
                      type="file"
                      style="display: none"
                      ref="image"
                      accept="image/*"
                      @change="onFilePicked"
                    >
                  </v-flex>
                </v-layout>
              </v-flex>
              <v-flex xs8>
                <v-layout wrap>
                  <v-flex xs12 ma-2>
                    <v-layout wrap >
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs4>
                            <v-select
                              :items="selBrand"
                              v-model="selectBrandName"
                              hint="제조사 선택 후 모델 선택"
                              persistent-hint
                              :disabled="model_register_dialog.read"
                              label="제조사"
                            ></v-select>
                            <!-- <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="제조사"
                              hint="제조사 선택 후 모델 선택"
                              persistent-hint></v-text-field> -->
                          </v-flex>
                          <v-flex xs4 pl-2>
                            <v-select
                              :items="selModel"
                              v-model="model_register_dialog.model_name"
                              :disabled="model_register_dialog.read"
                              label="모델"
                            ></v-select>
                            <!-- <v-text-field
                              color="primary lighten-2"
                              type="text"
                              label="모델"></v-text-field> -->
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs4>
                            <v-select
                              :items="selTypes"
                              v-model="selectTypeItem"
                              :disabled="model_register_dialog.read"
                              label="타입 선택"
                            ></v-select>
                            <!-- <v-text-field
                              color="primary lighten-2"
                              type="number"
                              label="기기종류"></v-text-field> -->
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs4>
                            <v-text-field
                              color="primary lighten-2"
                              type="number"
                              suffix="kg"
                              :disabled="model_register_dialog.read"
                              v-model="model_register_dialog.kg"
                              label="용량"></v-text-field>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                      <v-flex xs12>
                        <v-layout wrap>
                          <v-flex xs12>
                            <v-textarea
                              color="primary lighten-2"
                              type="text"
                              :disabled="model_register_dialog.read"
                              v-model="model_register_dialog.memo"
                              label="비고"></v-textarea>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <div v-if="!model_register_dialog.read">
            <v-btn color="primary darken-1" v-if="!model_register_dialog.mode" flat @click="registerData(model_register_dialog)">등록하기</v-btn>
            <v-btn color="primary darken-1" v-if="model_register_dialog.mode" flat @click="modifyData(model_register_dialog)">수정하기</v-btn>
          </div>
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
  name: 'DeviceMgr',
  methods: {
    // Brand, Model Load
    reloadBrandDatas () {
      this.$store.dispatch('BrandList')
        .then((result) => {
          for(let k in result.results) {
            this.selBrand.push(result.results[k].name)
          }
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    reloadModelDatas (brandName) {
      this.selModel = []
      this.$store.dispatch('ModelList', { brand: brandName })
        .then((result) => {
          for(let k in result.results) {
            this.selModel.push(result.results[k].name)
          }
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    // API
    reloadDatas () {
      console.log(this.selTypes)
      this.loading = true
      this.$store.dispatch('DeviceList',{
        page: this.pagination.page,
        sortby : this.pagination.sortBy,
        descending : this.pagination.descending,
        type : this.classifyTypesVal
      })
        .then((result) => {
          this.loading = false
          this.items = result.results
          this.totalitems = result.count//추가
          console.log(result)
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    onDetail (index, item) {
      console.log(item)
      this.selectBrandName = item.brand.name
      this.imageSrc = item.photo
      this.model_register_dialog = item
      this.selectTypeItem = this.selTypes[item.type]
      this.model_register_dialog.model_name = item.model.name
      this.model_register_dialog.read = true
      this.model_register_dialog.show = true
    },
    onOptionClick (index, item) {
      if (index === 0) {
        this.selectBrandName = item.brand.name
        this.imageSrc = item.photo
        this.model_register_dialog = item
        this.selectTypeItem = this.selTypes[item.type]
        this.model_register_dialog.model_name = item.model.name
        this.model_register_dialog.mode = true
        this.model_register_dialog.read = false
        console.log(this.model_register_dialog)
        this.model_register_dialog.show = true
      } else if (index === 1) {
        this.model_delete_dialog = item
        this.model_delete_dialog.show = true
      }
    },
    addDevice () {
      this.selectTypeItem = null
      this.imageSrc = ''
      this.selectBrandName = null
      this.model_register_dialog.show = true
    },
    registerData (item) {
      let param = item
      param.brand_name = this.selectBrandName
      param.photo = this.imageSrc
      param.type = this.selectTypeItem
      this.$store.dispatch('DeviceRegister', param)
        .then((result) => {
          this.model_register_dialog = { show: false, mode: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '등록되었습니다.'
          this.selectBrandName = null
          this.imageSrc = ''
          this.selectTypeItem = null
          this.reloadDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    modifyData (item) {
      let param = item
      param.brand_name = this.selectBrandName
      param.photo = this.imageSrc
      param.type = this.selectTypeItem
      this.$store.dispatch('DeviceModify', param)
        .then((result) => {
          console.log('#######')
          this.model_register_dialog = { show: false, mode: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '수정되었습니다.'
          this.selectBrandName = null
          this.imageSrc = ''
          this.selectTypeItem = null
          this.reloadDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    deleteData (item) {
      this.$store.dispatch('DeviceDelete', item.id)
        .then((result) => {
          this.model_delete_dialog = { show: false }
          this.snackbar = true
          this.snackbar_color = 'success'
          this.snackbar_msg = '삭제되었습니다.'
          this.reloadDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    getTypeStr (item) {
      return this.selTypes[item]
    },
    // 이미지 추가
    pickFile () {
      this.$refs.image.click()
    },
    onFilePicked (e) {
      const files = e.target.files
      if (files[0] !== undefined) {
        this.imageName = files[0].name
        if (this.imageName.lastIndexOf('.') <= 0) {
          return
        }
        const fr = new FileReader()
        fr.readAsDataURL(files[0])
        fr.addEventListener('load', () => {
          this.imageUrl = fr.result
          this.imageFile = files[0] // this is an image file that can be sent to server...
          // console.log(this.imageUrl, this.imageFile)
          let formData = new FormData()
          formData.append('file', this.imageFile)
          this.$store.dispatch('commonFileUpload', formData)
            .then((result) => {
              this.imageSrc = result.image_url
              console.log(this.model_register_dialog.photo)
            })
            .catch((result) => {
              this.userDialog = {}
              this.error = '실패했습니다'
            })
        })
      } else {
        this.imageName = ''
        this.imageFile = ''
        this.imageUrl = ''
      }
    }
  },
  created () {
    this.reloadBrandDatas()
    this.reloadDatas()
  },
  mounted () {
    this.$store.dispatch('updateTitle', '장비 관리')
    // this.reloadDatas()
  },
  watch: {
    pagination: {
      handler () {
        this.reloadDatas()
      },
      deep: true
    },
    search: {
      handler () {
        this.pagination.page = 1
        this.reloadDatas()
      }
    },
    selectBrandName: {
      handler () {
        this.reloadModelDatas(this.selectBrandName)
      }
    },
    classifyTypesVal: {
      handler () {
        this.pagination.page = 1
        this.reloadDatas()
      },
      deep: true
    },

  },
  data () {
    return {
      date: null,
      menu: null,
      imageName: '',
      imageUrl: '',
      imageFile: '',
      imageSrc: '',
      actionItems: ['수정', '삭제'],
      selBrand: [],
      selectBrandName: null,
      selModel: [],
      selTypes: [ '세탁기', '건조기'],
      selectTypeItem: null,
      model_register_dialog: { show: false, mode: false },
      model_delete_dialog: { show: false },
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      items: [],
      selected: [],
      classifyTypes:[ '전체', '세탁기', '건조기'],
      classifyTypesVal: '전체',
      headers: [
        {
          text: '제품이미지',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '제조사',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '모델',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '타입',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '용량(kg)',
          value: '',
          align: 'center',
          sortable: false
        },
        {
          text: '등록일',
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
