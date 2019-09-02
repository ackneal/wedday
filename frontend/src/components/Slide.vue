<template>
  <main class="slider_container">
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <template v-for="(card, index) in cards">
          <div class="swiper-slide" :id="index">
            <div class="swiper-message" style="max-width: 25%;">
              <h2 >{{ card.message }}</h2>
              <h3>From {{ card.name }}</h3>
            </div>
            <img class="swiper-img" :src="'https://storage.googleapis.com/cosmos-369.appspot.com/' + card.image">
          </div>
        </template>
      </div>
    </div>
  </main>
</template>

<script>

import { mapState, mapActions } from 'vuex'

export default {
  name: 'Slice',
  data: () => ({
    swiper: null,
  }),
  computed: {
    ...mapState({
      cards: state => state.card.list
    })
  },
  methods: {
    ...mapActions([
      'card/getMany',
      'card/splice',
    ]),
    initialSwiper: function () {
      this.swiper = new Swiper('.swiper-container', {
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: {
          delay: 5000,
          disableOnInteraction: true,
        }
      })
    },
    loadCards: function () {
      this['card/getMany'](100).then((ret) => {
        this.initialSwiper()
      })
    }
  },
  mounted() {
    this.loadCards()
    this.$socket.on('new', (msg) => {
      const card = JSON.parse(msg)
      this['card/splice']({ card }).then(() => {
        this.swiper.update()
      })
    });
  },
}
</script>
