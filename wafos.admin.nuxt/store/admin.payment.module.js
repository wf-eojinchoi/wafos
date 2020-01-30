import ApiService from '@/plugins/axios'

const API_PATH = {
  LIST: '/api/payment/',
  MONTH_LIST: '/api/payment/month/',
  DAY_LIST: '/api/payment/day/',
  YEAR_LIST: '/api/payment/year/',
  PAY_MEMBER_LIST: '/api/payment/member/'
}

const state = {
  me: null
}

const getters = {
  Payment (state) {
    return state.me
  }
}

const mutations = {
  stateUsers (state, _users) {
    state.me = _users
  }
}

const actions = {
  PaymentList (context, params) {
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
    if (params.descending) {
      uri += '&descending=' + params.descending
    }
    if (params.agency_name) {
      uri += '&agency_name=' + params.agency_name
    }
    if (params.tel) {
      uri += '&tel=' + params.tel
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
  PaymentMonthList (context, params) {
    let uri = API_PATH.MONTH_LIST
    if (params.agency_name) {
      uri += '?agency_name=' + params.agency_name
    }
    return new Promise((resolve, reject) => {
      ApiService.post(uri, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  PaymentDayList (context, params) {
    let uri = API_PATH.DAY_LIST
    if (params.agency_name) {
      uri += '?agency_name=' + params.agency_name
    }
    return new Promise((resolve, reject) => {
      ApiService.post(uri, params)
        .then((result) => {
          resolve(result.data)
        })
        .catch((result) => {
          reject(result.response.data)
        })
    })
  },
  YearList (context) {
    let uri = API_PATH.YEAR_LIST
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
  MemberPaymentList (context, params) {
    let uri = API_PATH.PAY_MEMBER_LIST + params.agency_id + '/' + params.id
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
    return new Promise((resolve, reject) => {
      ApiService.get(uri)
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
