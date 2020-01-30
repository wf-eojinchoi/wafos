import ApiService from '@/plugins/axios'

const API_PATH = {
  BRAND_LIST: '/api/device/brand/',
  MODEL_LIST: '/api/device/model/',
  DEVICE_LIST: '/api/device/info/'
}

const state = {
  me: null
}

const getters = {
  Device (state) {
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
  DeviceList (context, params) {
    let uri = API_PATH.DEVICE_LIST
    if (params.page) {
      uri += '?page=' + params.page
    } else {
      uri += '?page=1'
    }

    if (params.sortby) {
      uri += '?sortby=' + params.sortby
    }

    if (params.descending) {
      uri += '?descending=' + params.descending
    }

    return new Promise((resolve, reject) => {
      ApiService.get(uri)
        .then((result) => {
          console.log('result.data : ', result.data)
          resolve(result.data)
        })
        .catch((result) => {
          console.log('catch : ', result)
          reject(result.response.data)
        })
    })
  },
  DeviceDetail (context, aId) {
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
  DeviceDelete (context, aId) {
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
  DeviceRegister (context, dataInfo) {
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
  DeviceModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.DEVICE_LIST + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  // Brand
  BrandList (context) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.BRAND_LIST)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  BrandDetail (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.BRAND_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  BrandDelete (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.BRAND_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  BrandRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.BRAND_LIST, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  BrandModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      console.log(dataInfo)
      ApiService.put(API_PATH.BRAND_LIST + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  ModelList (context, param) {
    let uri = API_PATH.MODEL_LIST
    if (param.brand) {
      console.log('param.brand :', param.brand)
      uri += '?brand=' + param.brand
    } else {
      console.log('param.brand is null')
    }

    if (param.page) {
      console.log('page : ', param.page)
      uri += '&page=' + param.page
    } else {
      console.log('page :null')
      uri += '&page=1'
    }

    return new Promise((resolve, reject) => {
      ApiService.get(uri)
        .then((result) => {
          console.log('result.data : ', result.data)
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  ModelDetail (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.MODEL_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  ModelDelete (context, aId) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.MODEL_LIST + aId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  ModelRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.MODEL_LIST, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  ModelModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      console.log(dataInfo)
      ApiService.put(API_PATH.MODEL_LIST + dataInfo.id, dataInfo)
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
