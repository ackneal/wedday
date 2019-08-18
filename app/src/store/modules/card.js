const client = {
  index: function (query, callback, errCallback) {
    var qs = require('qs');
    return fetch('http://localhost:8081/api/cards?' + qs.stringify(query))
      .then(res => { return res.json() })
      .then(callback)
      .catch(errCallback)
  },
}

const state = {
  list: [],
}

const getters = {
  //
}

const actions = {
  getMany({ commit, state }) {
    var query = {
      start: state.list.length,
      limit: 8
    }
    return client.index(query,
      (res) => {
        commit('append', res.data)
        return res.has_more
      },
      (err) => {
        return false
      })
  },
}

const mutations = {
  append(state, cards) {
    state.list.push(...cards);
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
