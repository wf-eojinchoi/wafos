import ApiService from '@/plugins/axios'

const API_PATH = {
  LIST: '/api/agency/',
  LIST_ALL: '/api/agency/all/',
  DEVICE_LIST: '/api/agency/device/',
  DEVICE_DELETE: '/api/agency/device/delete/',
  POINT_INFO: '/api/agency/point/',
  ALERT_INFO: '/api/agency/alert/',
  UPDATE_KIOSK: '/api/agency/update/all/',
  COURSE_INFO: '/api/course_info/agency/',
  CONTROLLER_ID: '/api/agency/device/ctrl_id/',
  ALLOW_CONTROLLER_ID: '/api/agency/device/allow_ctrl_id/',
  ACCOUNT_INIT_PWD: '/api/account/agency/pwd/init/',
  ACCOUNT_CHANGE_PWD: '/api/account/agency/pwd/change/',
  LOGIN: '/api/account/agency/login/',
  LOOUT: '/api/account/agency/logout/'
}

const state = {
  me: null,
  wash: null
}

const getters = {
  Agency (state) {
    return state.me
  },
  WashAgencyId (state) {
    return state.wash
  }
}

const mutations = {
  stateUsers (state, _users) {
    state.me = _users
  },
  stateAgencyID (state, _agencyId) {
    state.wash = _agencyId
  }
}

const actions = {
  doWashLogin (context, credentials) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.LOGIN, {
        login_id: credentials.login_id,
        pwd: credentials.pwd
      })
        .then((result) => {
          ApiService.setAgencyInfo(result.data.id)
          context.commit('stateAgencyID', result.data.id)
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  doWashLogout (context) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.LOGOUT)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  // 가맹점 정보
  AgencyList (context, params) {
    let uri = API_PATH.LIST
    if (params.page) {
      uri += '?page=' + params.page
    } else {
      uri += '?page=1'
    }
    if (params.query) {
      uri += '&query=' + params.query
    }
    if (params.sortby) {
      uri += '&sortby=' + params.sortby
    } else {
      uri += '&sortby=agency_code'
    }

    if (params.descending) {
      uri += '&descending=' + params.descending
    }
    if (params.location) {
      uri += '&location=' + params.location
    }
    if (params.name) {
      uri += '&name=' + params.name
    }
    console.log('params:', params)
    console.log('params.page:', params.page)
    console.log('params.sortby:', params.sortby)
    console.log('params.location:', params.location)
    console.log('params.name:', params.name)
    console.log('uri:', uri)

    return new Promise((resolve, reject) => {
      ApiService.get(uri)
        .then((result) => {
          console.log('then result!!')
          console.log('result.data', result.data)
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyListAll (context, params) {
    let uri = API_PATH.LIST_ALL
    return new Promise((resolve, reject) => {
      ApiService.get(uri)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyDetail (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyDelete (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.LIST, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.LIST + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  // 가맹점 기기 정보
  AgencyDeviceControllerID (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.CONTROLLER_ID + dataInfo.agency_id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyAllowControllerID (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.ALLOW_CONTROLLER_ID + dataInfo.agency_id)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyDeviceList (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.DEVICE_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyDeviceDetail (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.DEVICE_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyDeviceDelete (context, id) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.DEVICE_DELETE + id)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyDeviceRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.DEVICE_LIST + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyDeviceModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.DEVICE_LIST + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          console.log(result)
          reject(result.response.data)
        })
    })
  },
  // 적립금 관리
  AgencyPointInfo (context, id) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.POINT_INFO + id)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyPointModify (context, dataInfo) {
    console.log('dataInfo.id = %s ', dataInfo.id)
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.POINT_INFO + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyCourseList (context, id) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.COURSE_INFO + id)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyCourseAdd (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.COURSE_INFO + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyCourseModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.COURSE_INFO + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyCourseDelete (context, id) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.COURSE_INFO + id)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyAccountPwdInit (context, id) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.ACCOUNT_INIT_PWD, { id: id })
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyAccountPwdChange (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.ACCOUNT_CHANGE_PWD, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyAlertReg (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.ALERT_INFO, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyUpdateAll (context) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.UPDATE_KIOSK)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
