import Vuex from 'vuex'

import header from './header.module'
import common from './common.module'
import admin from './admin.module'
import adminMember from './admin.member.module'
import adminAgency from './admin.agency.module'
import adminDevice from './admin.device.module'
import adminEtcDevice from './admin.etc.device.module'
import adminStandardCourse from './admin.standard.course'
import adminPayment from './admin.payment.module'

const store = () => new Vuex.Store({
  modules: {
    header,
    common,
    admin,
    // ADMIN UI
    adminMember,
    adminAgency,
    adminDevice,
    adminEtcDevice,
    adminStandardCourse,
    adminPayment
  }
})

export default store
