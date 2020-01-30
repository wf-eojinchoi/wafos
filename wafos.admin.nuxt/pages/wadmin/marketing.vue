<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 ma-2>
        <v-card>
          <v-card-text>
            <v-list dense>
              <v-list-tile>
                <v-list-tile-content>광고링크</v-list-tile-content>
                <v-list-tile-action @click="onModify(linkData)">
                  <span class="blue--text" style="cursor: pointer;">{{ linkData.link_path ? linkData.link_path : '광고 링크를 등록하세요.' }}</span>
                </v-list-tile-action>
                <v-list-tile-action @click="moveTube()">
                  <v-icon class="blue--text" style="cursor: pointer;">video_library</v-icon>
                </v-list-tile-action>
              </v-list-tile>
            </v-list>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="model_modi_dialog.show" max-width="60%" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row wrap>
            <v-flex xs12>
              <v-text-field
                label="유튜브 링크 입력"
                color="primary lighten-2"
                type="text"
                v-model="model_modi_dialog.link_path"
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="modify(model_modi_dialog)">변경하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_modi_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'Marketing',
  methods: {
    // API
    reloadDatas () {
      this.$store.dispatch('TubeLinkInfo')
        .then((result) => {
          this.linkData = result
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    },
    moveTube () {
      window.open(this.linkData.link_path)
    },
    onModify (item) {
      console.log(item)
      this.model_modi_dialog.link_path = item.link_path
      this.model_modi_dialog.show = true
    },
    modify (item) {
      this.$store.dispatch('TubeLinkModify', item)
        .then((result) => {
          this.model_modi_dialog = { show: false }
          this.reloadDatas()
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
          this.loading = false
        })
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '기본 설정')
    this.reloadDatas()
  },
  data () {
    return {
      model_modi_dialog: { show: false },
      isModify: false,
      linkData: {}
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
