<template>
  <main class="w-lottery">
    <div class="mdl-grid">
      <div class="w-lottery-container swiper-container">
        <div class="swiper-wrapper">
          <template v-for="(card, index) in cards">
            <div class="swiper-slide" data-swiper-autoplay="10">
              <img :src="'//images.weserv.nl/?url=storage.googleapis.com/cosmos-369.appspot.com/' + card.image + '&w=1280&&maxage=31d'" height=400 width=400>
            </div>
          </template>
        </div>
      </div>
      <div class="w-lottery-block mdl-cell mdl-cell--2-col mdl-cell--5-offset">
        <form action="#">
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="w-lottery-input mdl-textfield__input" type="text" pattern="-?[1-5]?" id="number" v-model="number" :readonly="loading">
            <label class="mdl-textfield__label" for="number">抽出幾位幸運兒呢？</label>
            <span class="mdl-textfield__error">請輸入 1-5 數字!</span>
          </div>
          <button class="w-lottery-buttom mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" @click="lottery">
            <span v-if="loading">誰是命運兒呢...</span>
            <span v-else>抽獎</span>
          </button>
        </form>
      </div>
    </div>
    <dialog class="mdl-dialog" ref="dialog" style="width:80vw;">
      <h4 class="mdl-dialog__title">恭喜以下幸運兒</h4>
      <div class="mdl-dialog__content">
        <div class="w-main__posts mdl-grid" style="max-width:100%">
          <template v-for="card in random">
            <card v-bind="card" :col=2 />
          </template>
        </div>
      </div>
      <div class="mdl-dialog__actions">
        <button type="button" class="mdl-button" @click="dialog.close()">確認</button>
      </div>
    </dialog>
  </main>
</template>

<script>

import { mapGetters, mapActions } from 'vuex'
import Card from './Card.vue'

export default {
  name: 'Lottery',
  components: {
    Card,
  },
  data: () => ({
    dialog: null,
    swiper: null,
    loading: false,
    number: 5,
  }),
  computed: {
    ...mapGetters({
      cards: 'card/shuffle',
      random: 'card/lottery',
    }),
  },
  methods: {
    ...mapActions([
      'card/getMany',
      'card/getLottery',
    ]),
    initialSwiper: function () {
      this.swiper = new Swiper('.swiper-container', {
        spaceBetween: 30,
        centeredSlides: true,
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        loop: true,
        coverflowEffect: {
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows : true,
        },
      })
    },
    lottery: function () {
      this.swiper.autoplay.start()
      this.loading = true
      this['card/getLottery'](this.number)
      window.setTimeout(() => {
        window.dialogPolyfill.registerDialog(this.dialog);
        this.dialog.showModal()
        this.swiper.autoplay.stop()
        this.loading = false
      }, 5000)
    }
  },
  mounted() {
    this['card/getMany'](300).then(() => this.initialSwiper())
    this.dialog = this.$refs.dialog
    this.loading = false
  },
}
</script>
