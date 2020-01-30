<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-card-text>
            <v-list dense>
              <v-list-tile>
                <v-list-tile-content>퇴출요청</v-list-tile-content>
                <v-list-tile-action>
                  <!-- <v-icon class="green--text" style="cursor: pointer;" @click.prevent="playSound('http://www.largesound.com/ashborytour/sound/brobob.mp3')">play_arrow</v-icon> -->
                </v-list-tile-action>
                <v-list-tile-action @click="pickFile0()">
                  <v-icon class="blue--text" style="cursor: pointer;">attach_file</v-icon>
                  <input
                    type="file"
                    style="display: none"
                    ref="audio0"
                    accept="audio/*"
                    @change="onFilePicked0"
                  >
                </v-list-tile-action>
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile>
                <v-list-tile-content>장난금지</v-list-tile-content>
                <v-list-tile-action>
                  <!-- <v-icon class="green--text" style="cursor: pointer;" @click.prevent="playSound('http://www.largesound.com/ashborytour/sound/brobob.mp3')">play_arrow</v-icon> -->
                </v-list-tile-action>
                <v-list-tile-action @click="pickFile1()">
                  <v-icon class="blue--text" style="cursor: pointer;">attach_file</v-icon>
                  <input
                    type="file"
                    style="display: none"
                    ref="audio1"
                    accept="audio/*"
                    @change="onFilePicked1"
                  >
                </v-list-tile-action>
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile>
                <v-list-tile-content>동물퇴출</v-list-tile-content>
                <v-list-tile-action>
                  <!-- <v-icon class="green--text" style="cursor: pointer;" @click.prevent="playSound('http://www.largesound.com/ashborytour/sound/brobob.mp3')">play_arrow</v-icon> -->
                </v-list-tile-action>
                <v-list-tile-action @click="pickFile2()">
                  <v-icon class="blue--text" style="cursor: pointer;">attach_file</v-icon>
                  <input
                    type="file"
                    style="display: none"
                    ref="audio2"
                    accept="audio/*"
                    @change="onFilePicked2"
                  >
                </v-list-tile-action>
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile>
                <v-list-tile-content>사이렌</v-list-tile-content>
                <v-list-tile-action>
                  <!-- <v-icon class="green--text" style="cursor: pointer;" @click.prevent="playSound('http://www.largesound.com/ashborytour/sound/brobob.mp3')">play_arrow</v-icon> -->
                </v-list-tile-action>
                <v-list-tile-action @click="pickFile3()">
                  <v-icon class="blue--text" style="cursor: pointer;">attach_file</v-icon>
                  <input
                    type="file"
                    style="display: none"
                    ref="audio3"
                    accept="audio/*"
                    @change="onFilePicked3"
                  >
                </v-list-tile-action>
              </v-list-tile>
              <!--새로운 알랏 -->
              <v-divider></v-divider>
              <v-list-tile>
                <v-list-tile-content>새 알람</v-list-tile-content>
                <v-list-tile-action>
                  <!-- <v-icon class="green--text" style="cursor: pointer;" @click.prevent="playSound('http://www.largesound.com/ashborytour/sound/brobob.mp3')">play_arrow</v-icon> -->
                </v-list-tile-action>
                <v-list-tile-action @click="pickFile4()">
                  <v-icon class="blue--text" style="cursor: pointer;">attach_file</v-icon>
                  <input
                    type="file"
                    style="display: none"
                    ref="audio4"
                    accept="audio/*"
                    @change="onFilePicked4"
                  >
                </v-list-tile-action>
              </v-list-tile>
            </v-list>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
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
          this.$store.dispatch('commonAudioFileUpload', formData)
            .then((result) => {
              this.atype = null
              // this.fileSrc = result.file_url
              this.fileName = ''
              this.fileFile = ''
              this.fileUrl = ''
            })
            .catch((result) => {
              this.userDialog = {}
              this.error = '실패했습니다'
            })
        })
      } else {
        this.fileName = ''
        this.fileFile = ''
        this.fileUrl = ''
      }
    },
    pickFile1 () {
      this.$refs.audio1.click()
    },
    onFilePicked1 (e) {
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
          formData.append('atype', 1)
          console.log(formData)
          this.$store.dispatch('commonAudioFileUpload', formData)
            .then((result) => {
              this.atype = null
              // this.fileSrc = result.file_url
              this.fileName = ''
              this.fileFile = ''
              this.fileUrl = ''
            })
            .catch((result) => {
              this.userDialog = {}
              this.error = '실패했습니다'
            })
        })
      } else {
        this.fileName = ''
        this.fileFile = ''
        this.fileUrl = ''
      }
    },
    pickFile2 () {
      this.$refs.audio2.click()
    },
    onFilePicked2 (e) {
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
          formData.append('atype', 2)
          console.log(formData)
          this.$store.dispatch('commonAudioFileUpload', formData)
            .then((result) => {
              this.atype = null
              // this.fileSrc = result.file_url
              this.fileName = ''
              this.fileFile = ''
              this.fileUrl = ''
            })
            .catch((result) => {
              this.userDialog = {}
              this.error = '실패했습니다'
            })
        })
      } else {
        this.fileName = ''
        this.fileFile = ''
        this.fileUrl = ''
      }
    },
    pickFile3 () {
      this.$refs.audio3.click()
    },
    onFilePicked3 (e) {
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
          formData.append('atype', 3)
          console.log(formData)
          this.$store.dispatch('commonAudioFileUpload', formData)
            .then((result) => {
              this.atype = null
              // this.fileSrc = result.file_url
              this.fileName = ''
              this.fileFile = ''
              this.fileUrl = ''
            })
            .catch((result) => {
              this.userDialog = {}
              this.error = '실패했습니다'
            })
        })
      } else {
        this.fileName = ''
        this.fileFile = ''
        this.fileUrl = ''
      }
    },
    pickFile4 () {
      this.$refs.audio4.click()
    },
    onFilePicked4 (e) {
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
          formData.append('atype', 3)
          console.log(formData)
          this.$store.dispatch('commonAudioFileUpload', formData)
            .then((result) => {
              this.atype = null
              // this.fileSrc = result.file_url
              this.fileName = ''
              this.fileFile = ''
              this.fileUrl = ''
            })
            .catch((result) => {
              this.userDialog = {}
              this.error = '실패했습니다'
            })
        })
      } else {
        this.fileName = ''
        this.fileFile = ''
        this.fileUrl = ''
      }
    },
  },
  mounted () {
    this.$store.dispatch('updateTitle', '기본 설정')
    this.reloadDatas()
  },
  data () {
    return {
      atype: null,
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
