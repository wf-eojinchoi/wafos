<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12>
        <v-card>
          <v-card-text>
            <v-list dense>
              <v-list-tile>
              <v-list-tile-content>요리사 이름</v-list-tile-content>
              <v-list-tile-action class="align-start teal--text" @click="modifyChefDialog(globalSet)">
                {{ globalSet.chef_name }}
              </v-list-tile-action>
              </v-list-tile>
            </v-list>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog v-model="model_modi_dialog.show" max-width="300" lazy persistent>
      <v-card>
        <v-card-text>
          <v-layout row>
            <v-flex xs12>
              <v-text-field
                color="primary lighten-2"
                type="text"
                label="피크닉 요리사명"
                v-model="model_modi_dialog.chef_name"
                ></v-text-field>
            </v-flex>
          </v-layout>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary darken-1" flat @click="modifyChef(model_modi_dialog)">수정하기</v-btn>
          <v-btn color="grey darken-1" flat @click.native="model_modi_dialog = { show: false }">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'SettingsGlobalSet',
  methods: {
    // API
    reloadDatas () {
      this.$store.dispatch('globalsetInfo')
        .then((result) => {
          console.log('GlobalSet:%o', result)
          this.globalSet = result
        })
        .catch((result) => {
          this.error = '데이터를 가져오는데 실패했습니다'
        })
    },
    modifyChefDialog (item) {
      this.model_modi_dialog = item
      this.model_modi_dialog.show = true
    },
    modifyChef (item) {
      console.log(item)
      this.$store.dispatch('changeChefName', item)
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
      recipeDetailData: {},
      ori_capacities: [],
      globalSet: {}
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
