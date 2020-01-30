import Vue from 'vue'
import axios from 'axios'
import VueCookie from 'vue-cookie'
import VueAxios from 'vue-axios'

const ApiService = {
  init () {
    Vue.use(VueCookie)
    Vue.use(VueAxios, axios)
    Vue.axios.defaults.baseURL = 'http://127.0.0.1:8000'
    // Vue.axios.defaults.baseURL = 'https://v2.washwapos.com'
  },

  query (resource, params) {
    return Vue.axios.get(resource, params)
  },

  setAdminInfo (acc) {
    Vue.cookie.set('admin-acc', JSON.stringify(acc))
  },
  setAgencyInfo (acc) {
    Vue.cookie.set('agency-info', acc)
  },
  setToken (token) {
    Vue.cookie.set('auth-token', token)
  },

  get (resource, slug = '') {
    let authToken = Vue.cookie.get('auth-token')
    if (authToken) {
      Vue.axios.defaults.headers.common['Authorization'] = 'JWT ' + authToken
    }
    return Vue.axios.get(`${resource}${slug}`)
  },

  post (resource, params) {
    let token = Vue.cookie.get('csrftoken')
    if (token) {
      axios.defaults.headers.common['X-CSRFToken'] = token
    }
    let authToken = Vue.cookie.get('auth-token')
    console.log(authToken)
    if (authToken) {
      Vue.axios.defaults.headers.common['Authorization'] = 'JWT ' + authToken
    }
    return Vue.axios.post(`${resource}`, params)
  },

  update (resource, slug, params) {
    return Vue.axios.put(`${resource}${slug}`, params)
  },

  put (resource, params) {
    let token = Vue.cookie.get('csrftoken')
    if (token) {
      Vue.axios.defaults.headers.common['X-CSRFToken'] = token
    }
    let authToken = Vue.cookie.get('auth-token')
    if (authToken) {
      Vue.axios.defaults.headers.common['Authorization'] = authToken
    }
    return Vue.axios.put(`${resource}`, params)
  },

  delete (resource) {
    let token = Vue.cookie.get('csrftoken')
    if (token) {
      Vue.axios.defaults.headers.common['X-CSRFToken'] = token
    }
    return Vue.axios.delete(resource)
  },

  postFile (resource, formData) {
    let token = Vue.cookie.get('csrftoken')
    if (token) {
      axios.defaults.headers.common['X-CSRFToken'] = token
    }
    return Vue.axios.post(
      `${resource}`,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
    )
  }
}
ApiService.init()
export default ApiService
