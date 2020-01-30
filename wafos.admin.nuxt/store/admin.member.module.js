import ApiService from '@/plugins/axios'

const API_PATH = {
  LIST: '/api/member/',
  CHANGE_POINT: '/api/member/change/point/',
  CHANGE_MONEY: '/api/member/change/money/',
  INIT_PWD: '/api/member/change/pwd/',
  CHANGE_MEMO: '/api/member/change/memo/',
  AGENCY_LIST: '/api/member/agency/'
}

const state = {
  me: null
}

const getters = {
  Member (state) {
    return state.me
  }
}

const mutations = {
  stateUsers (state, _users) {
    state.me = _users
  }
}

const actions = {
  MemberList (context, params) {
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
    }
    if (params.tel) {
      uri += '&tel=' + params.tel
    }
    if (params.descending) {
      uri += '&descending=' + params.descending
    }
    if (params.agency_name) {
      uri += '&agency_name=' + params.agency_name
    }
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
  MemberDetail (context, aId) {
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
  MemberDelete (context, aId) {
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
  MemberRegister (context, dataInfo) {
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
  MemberModify (context, dataInfo) {
    return new Promise((resolve, reject) => {
      console.log(dataInfo)
      ApiService.put(API_PATH.LIST + dataInfo.id, dataInfo)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  AgencyMemberList (context, params) {
    let uri = API_PATH.AGENCY_LIST + params.id
    if (params.page) {
      uri += '?page=' + params.page
    } else {
      uri += '?page=1'
    }
    if (params.tel) {
      uri += '&tel=' + params.tel
    }
    if (params.sortby) {
      uri += '&sortby=' + params.sortby
    }
    if (params.descending) {
      uri += '&descending=' + params.descending
    }
    // if (params.agency_name) {
    //   uri += '&agency_name=' + params.agency_name
    // }
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
  AgencyMemberDetail (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.get(API_PATH.AGENCY_LIST + params.agency_id + '/' + params.id)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  MemberChangePoint (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.CHANGE_POINT, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  MemberChangeMoney (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.CHANGE_MONEY, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  MemberInitPassword (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.INIT_PWD, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  MemberChangeMemo (context, params) {
    return new Promise((resolve, reject) => {
      ApiService.post(API_PATH.CHANGE_MEMO, params)
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
