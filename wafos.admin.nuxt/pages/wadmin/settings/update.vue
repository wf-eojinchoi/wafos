<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-card-title>
            업데이트 할 바이너리(압축파일)를 등록해주세요.<br>
            등록된 바이너리는 가맹점별로 업데이트 신호를 전달하여 키오스크에서 자동으로 다운받아 업데이트를 진행합니다.<br>
            업데이트는 PC 재부팅과 함께 약 5~15분정도 걸립니다.
          </v-card-title>
          <v-card-text>
            <v-list dense>
              <v-list-tile>
                <v-list-tile-content>
                  <v-btn class="primary" style="cursor: pointer;" @click="pickFile0()">업데이트 파일 업로드</v-btn>
                  <input
                    type="file"
                    style="display: none"
                    ref="audio0"
                    accept="*/*"
                    @change="onFilePicked0"
                  >
                </v-list-tile-content>
              </v-list-tile>
            </v-list>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
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
  layout: 'wadmin',
  name: 'Siren',
  methods: {
    // API
    reloadDatas () {
      console.log('#')
    },
    playSound (sound) {
      if (sound) {
        var audio = new Audio(sound)
        audio.play()
      }
    },
    pickFile0 () {
      this.$refs.audio0.click()
    },
    onFilePicked0 (e) {
      const files = e.target.files
      if (files[0] !== undefined) {
        this.fileName = files[0].name
        if (this.fileName.lastIndexOf('.') <= 0) {
          return
        }
        const fr = new FileReader()
        fr.readAsDataURL(files[0])
        fr.addEventListener('load', () => {
          this.fileUrl = fr.result
          this.fileFile = files[0] // this is an image file that can be sent to server...
          console.log(this.fileUrl, this.fileFile)
          let formData = new FormData()
          console.log(this.atype)
          formData.append('file', files[0])
          formData.append('atype', 0)
          console.log(formData)
          this.$store.dispatch('commonBinFileUpload', formData)
            .then((result) => {
              this.atype = null
              // this.fileSrc = result.file_url
              this.fileName = ''
              this.fileFile = ''
              this.fileUrl = ''
              this.snackbar = true
              this.snackbar_color = 'success'
              this.snackbar_msg = '업데이트 파일이 등록되었습니다.'
              setTimeout(function(){
                window.location.reload()
              }, 1500)
            })
            .catch((result) => {
              this.userDialog = {}
              this.error = '실패했습니다'
              this.snackbar = true
              this.snackbar_color = 'error'
              this.snackbar_msg = '업데이트에 실패했습니다'
            })
        })
      } else {
        this.fileName = ''
        this.fileFile = ''
        this.fileUrl = ''
      }
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '기본 설정')
    this.reloadDatas()
  },
  data () {
    return {
      atype: null,
      snackbar: false,
      snackbar_color: 'info',
      snackbar_msg: null,
      fileName: '',
      fileUrl: '',
      fileFile: '',
      fileSrc: '',
      isModify: false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
