const client = {
  index: function (query, callback, errCallback) {
    var qs = require('qs');
    return fetch('http://localhost:8081/api/cards?' + qs.stringify(query))
      .then(res => { return res.json() })
      .then(callback)
      .catch(errCallback)
  },
  store: function (data, callback, errCallback) {
    var formData = new FormData()
    formData.set('name', data.name)
    formData.set('message', data.message)
    formData.set('image', data.image)

    return fetch('http://localhost:8081/api/cards', {
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
  getMany({ commit, state }) {
    var query = {
      offset: state.list.length,
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
  create({ commit }, data) {
    client.store(data, res => {
      commit('prepend', [ res.data ]);
    })
  },
}

const mutations = {
  append(state, cards) {
    state.list.push(...cards);
  },
  prepend(state, cards) {
    state.list.unshift(...cards);
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
