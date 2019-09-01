const client = {
  index: function (query, callback, errCallback) {
    var qs = require('qs');
    return fetch('/api/cards?' + qs.stringify(query))
      .then(res => { return res.json() })
      .then(callback)
      .catch(errCallback)
  },
  store: function (data, callback, errCallback) {
    var formData = new FormData()
    formData.set('name', data.name)
    formData.set('message', data.message)
    formData.set('image', data.image)

    return fetch('/api/cards', {
      method: 'POST',
      body: formData
    }).then(res => { return res.json() })
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
  getMany({ commit, state }, limit) {
    var query = {
      offset: state.list.length,
      limit: limit
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
  create({ commit }, data) {
    return client.store(data, res => {
      commit('prepend', [ res.data ]);
      return res.data
    })
  },
  splice({ commit }, { card, index }) {
    if (! index) {
      index = state.list.length
    }

    commit('splice', { index, card })
  },
}

const mutations = {
  append(state, cards) {
    state.list.push(...cards);
  },
  prepend(state, cards) {
    state.list.unshift(...cards);
  },
  splice (state, { index, card }) {
    state.list.splice(index, 0, card)
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
