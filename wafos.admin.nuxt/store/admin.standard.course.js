import ApiService from '@/plugins/axios'

const API_PATH = {
  LIST: '/api/course_info/standard/',
  COPY: '/api/course_info/standard/copy/'
}

const state = {
  me: null
}

const getters = {
  StandardCourse (state) {
    return state.me
  }
}

const mutations = {
  stateUsers (state, _users) {
    state.me = _users
  }
}

const actions = {
  StandardCourseList (context, params) {
    let uri = API_PATH.LIST

    if (params.page) {
      uri += '?page=' + params.page
    } else {
      uri += '?page=1'
    }

    if (params.sortby) {
      uri += '&sortby=' + params.sortby
    }

    if (params.descending) {
      uri += '&descending=' + params.descending
    }

    if (params.type === 0) {
      uri += '&type=' + params.type
    } else {
      uri += '&type=' + params.type
    }

    console.log('params:', params)
    console.log('params.page:', params.page)
    console.log('params.type:', params.type)
    console.log('admin.standard uri: ', uri)

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
  StandardCourseDelete (context, aId) {
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
  StandardCourseRegister (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.LIST + dataInfo.type, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  StandardCourseModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.put(API_PATH.LIST + dataInfo.type, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  CopyStandardCourse (context, dataInfo) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.COPY, dataInfo)
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
