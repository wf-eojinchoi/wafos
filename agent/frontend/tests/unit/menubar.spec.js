import Vue from 'vue'
import { shallowMount } from '@vue/test-utils'
import Vuetify from 'vuetify'
import Menubar from '@/components/Menubar.vue'

describe('Menubar.vue', () => {
  let wrp
  beforeEach(() => {
    Vue.use(Vuetify)

    wrp = shallowMount(Menubar)
  })

  it('has data correctly', () => {
    expect(typeof Menubar.data).toBe('function')
    const defaultData = Menubar.data()
    expect(typeof defaultData.items).toBe('object')
  })

  it('has aside tag successfully', () => {
    expect(wrp.contains('v-navigation-drawer-stub')).toBe(true)
  })
})
