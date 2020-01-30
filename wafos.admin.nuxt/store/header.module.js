const state = {
  title: null
}

const getters = {
  currentTitle (state) {
    return state.title
  }
}

const mutations = {
  stateTitle (state, _title) {
    state.title = _title
  }
}

const actions = {
  updateTitle (context, title) {
    context.commit('stateTitle', title)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
