<template>
  <v-content>
    <v-layout wrap>
      <v-flex xs12 >
        <v-card>
          <v-card-title>
            <v-flex xs6>
              <v-breadcrumbs flat>
                <v-icon slot="divider">chevron_right</v-icon>
                <v-breadcrumbs-item
                  v-for="item in bread_items"
                  :key="item.text"
                  :disabled="item.disabled"
                  @click.native="onBack(item.path)"
                  >
                    {{ item.text }}
                </v-breadcrumbs-item>
              </v-breadcrumbs>
            </v-flex>
            <v-flex xs6 text-xs-right>
              <v-btn color="primary" round @click="onRegisterDialog()">등록</v-btn>
            </v-flex>
          </v-card-title>
          <v-card-text>
            <v-layout row pl-3 pr-3>
              <v-flex xs12>
                <v-text-field
                color="primary lighten-2"
                type="text"
                label="이름"
                required
                ></v-text-field>
              </v-flex>
            </v-layout>
            <v-layout row pl-3 pr-3>
              <v-flex xs12>
                <v-text-field
                color="primary lighten-2"
                type="text"
                label="이메일"
                required
                ></v-text-field>
              </v-flex>
            </v-layout>
            <v-layout row>
                <v-subheader>권한 설정</v-subheader>
            </v-layout>
            <v-layout row>
                <v-flex xs6 ml-3>
                <v-data-table
                  :items="admin_prop"
                  hide-actions
                  hide-headers
                >
                  <template slot="items" slot-scope="props">
                    <td>{{ props.item.name }}</td>
                    <td class="text-xs-center"><v-switch v-model="props.item.swich"></v-switch></td>
                  </template>
                </v-data-table>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-content>
</template>

<script>
export default {
  layout: 'wadmin',
  name: 'SettingsAdminRegister',
  methods: {
    onBack (_path) {
      console.log(_path)
      if (_path) {
        this.$router.go(-1)
      }
    },
    toggleAll () {
      if (this.selected.length) this.selected = []
      else this.selected = this.data.slice()
    },
    changeSort (column) {
      if (this.pagination.sortBy === column) {
        this.pagination.descending = !this.pagination.descending
      } else {
        this.pagination.sortBy = column
        this.pagination.descending = false
      }
    },
    onDeleteDialog (user) {
      this.model_delete_dialog.show = true
    },
    onRegisterDialog (user) {
      this.model_register_dialog.show = true
    },
    onDetail (item) {
      this.model_register_dialog = item
      this.model_register_dialog.mode = true
      this.model_register_dialog.show = true
    }
  },
  mounted () {
    this.$store.dispatch('updateTitle', '관리자계정 등록')
  },
  data () {
    return {
      model_delete_dialog: { show: false },
      model_register_dialog: { show: false, mode: false },
      adminSwitch1: false,
      error: null,
      search: null,
      loading: false,
      pagination: {},
      totalitems: 0,
      items: [
      ],
      bread_items: [
        {
          text: '관리자계정 관리',
          path: true,
          disabled: false
        },
        {
          text: '관리자계정 상세보기',
          path: false,
          disabled: true
        }
      ],
      admin_prop: [
        {
          name: '조리관리',
          swich: false
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
