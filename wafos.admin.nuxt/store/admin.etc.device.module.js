import ApiService from '@/plugins/axios'

const API_PATH = {
  DEVICE_LIST: '/api/device/etc/'
}

const state = {
  me: null
}

const getters = {
  EtcDevice (state) {
    return state.me
  }
}

const mutations = {
  stateUsers (state, _users) {
    state.me = _users
  }
}

const actions = {
  // Device Info
  EtcDeviceList (context) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.DEVICE_LIST)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  EtcDeviceDetail (context, aId) {
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
  EtcDeviceDelete (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.DEVICE_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  EtcDeviceRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.DEVICE_LIST, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  EtcDeviceModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.DEVICE_LIST + dataInfo.id, dataInfo)
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
