import ApiService from '@/plugins/axios'

const API_PATH = {
  ADMIN_LIST: '/api/admin/',
  ADMIN_INIT_PWD: '/api/admin/pwd/',
  ADMIN_CHANGE_PWD: '/api/admin/pwd/change/',
  LOGIN: '/api/admin/login/',
  LOGOUT: '/api/admin/logout/',
  TRANSLATE: '/api/trans/'
}

const state = {
  acc: null
}

const getters = {
  AdminAccount (state) {
    return state.acc
  }
}

const mutations = {
  stateAccount (state, _data) {
    state.acc = _data
  }
}

const actions = {
  doLogin (context, credentials) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.LOGIN, {
        login_id: credentials.login_id,
        pwd: credentials.pwd
      })
        .then((result) => {
          ApiService.setAdminInfo(result.data)
          context.commit('stateAccount', result.data)
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  doLogout (context) {
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
  // ADMIN USER MGR
  adminUserList (context) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.ADMIN_LIST)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  adminUserDetail (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.ADMIN_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  adminUserDelete (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.ADMIN_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  adminUserRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.ADMIN_LIST, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  adminUserModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      console.log(dataInfo)
      ApiService.put(API_PATH.ADMIN_LIST + dataInfo.id, {
        login_id: dataInfo.login_id,
        name: dataInfo.name,
        enterMember: dataInfo.enterMember,
        enterAgency: dataInfo.enterAgency,
        enterDevice: dataInfo.enterDevice,
        enterPayment: dataInfo.enterPayment,
        enterHoliday: dataInfo.enterHoliday,
        enterAccount: dataInfo.enterAccount
      })
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  adminInitPWD (context, dataInfo) {
    return new Promise((resolve, reject) => {
      console.log(dataInfo)
      ApiService.post(API_PATH.ADMIN_INIT_PWD + dataInfo.id)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  adminChangePWD (context, dataInfo) {
    return new Promise((resolve, reject) => {
      console.log(dataInfo)
      ApiService.post(API_PATH.ADMIN_CHANGE_PWD, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  // ADMIN USER MGR
  transList (context, params) {
    return new Promise((resolve, reject) => {
      let uri = API_PATH.TRANSLATE
      if (params.category) {
        uri += '?category=' + params.category
      }
      ApiService.get(uri)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  transModify (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.TRANSLATE + params.id, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  transDelete (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.TRANSLATE + aId)
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
