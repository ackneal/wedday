<template>
  <main class="mdl-layout__content">
    <div class="w-main__posts mdl-grid">
      <div class="mdl-card mdl-cell mdl-cell--12-col">
        <div class="w-headline mdl-card__media mdl-color-text--grey-50"></div>
      </div>
      <template v-for="card in cards">
        <card v-bind="card" />
      </template>
      <div v-if="loading" class="w-loading mdl-cell mdl-cell--12-col">
        <div class="mdl-spinner mdl-js-spinner is-active"></div>
      </div>
    </div>
    <Dialog />
  </main>
</template>

<script>

import { mapState, mapActions } from 'vuex'
import Card from './Card.vue'
import Dialog from './Dialog.vue'

export default {
  name: 'Index',
  components: {
    Card,
    Dialog
  },
  data: () => ({
    has_more: true,
    loading: true
  }),
  computed: {
    ...mapState({
      cards: state => state.card.list
    })
  },
  methods: {
    ...mapActions(['card/getMany']),
    getCards: function () {
      this.loading = true
      this['card/getMany']().then(ret => {
        this.has_more = ret
        this.loading = false
      })
    },
    scroll: function (e) {
      var loading = ((e.target.scrollTop + e.target.clientHeight) >= e.target.scrollHeight);
      if (loading && this.has_more) {
        this.getCards()
      }
    }
  },
  created() {
    window.addEventListener('scroll', this.scroll, true)
  },
  destroyed() {
    window.removeEventListener('scroll', this.scroll)
  },
  mounted() {
    this.getCards()
  }
}
</script>
