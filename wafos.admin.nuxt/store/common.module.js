import ApiService from '@/plugins/axios'

const API_PATH = {
  FILE_UPLOAD: '/api/common/file/',
  AUDIO_FILE_UPLOAD: '/api/common/file/audio/',
  UPDATE_FILE_UPLOAD: '/api/common/file/update/',
  TOKEN: '/api/token',
  DN_MEM: '/api/member/download/',
  DN_PAY: '/api/payment/download/',
  ALERT: '/api/alert_info/',
  MARKETING: '/api/tubelink/'
}

const state = {
  datas: null,
  holiday: null,
  me: null,
  token: null
}

const getters = {
  commData (state) {
    return state.datas
  }
}

const mutations = {
  stateList (state, _datas) {
    state.datas = _datas
  },
  stateData (state, _comm) {
    state.comm = _comm
  },
  stateToken (state, _token) {
    state.token = _token
  }
}

const actions = {
  commonFileDelete (context, userId) {
    return new Promise((resolve, reject) => {
      ApiService.delete(API_PATH.FILE_UPLOAD + userId)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  commonFileUpload (context, formData) {
    return new Promise((resolve, reject) => {
      ApiService.postFile(API_PATH.FILE_UPLOAD, formData)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  commonAudioFileUpload (context, formData) {
    return new Promise((resolve, reject) => {
      ApiService.postFile(API_PATH.AUDIO_FILE_UPLOAD, formData)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  commonBinFileUpload (context, formData) {
    return new Promise((resolve, reject) => {
      ApiService.postFile(API_PATH.UPDATE_FILE_UPLOAD, formData)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  TokenRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.TOKEN, dataInfo)
        .then((result) => {
          console.log(result)
          if (result.data.access) {
            ApiService.setToken(result.data.access)
            context.commit('stateToken', result.data.access)
          }
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  MemberDownload (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.DN_MEM, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  PayDownload (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.DN_PAY, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  TubeLinkInfo (context) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.MARKETING)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  TubeLinkModify (context, param) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.MARKETING, param)
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
