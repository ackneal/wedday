<template>
  <main class="slider_container">
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <template v-for="(card, index) in cards">
          <div class="swiper-slide" :id="index">
            <div class="swiper-message">
              <h3 >{{ card.message }}</h3>
              <h4>From {{ card.name }}</h4>
            </div>
            <img class="swiper-img" :src="'https://storage.googleapis.com/cosmos-369.appspot.com/' + card.image">
          </div>
        </template>
      </div>
    </div>
  </main>
</template>

<script>

import Swiper from 'swiper';
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Slice',
  data: () => ({
    //
  }),
  computed: {
    ...mapState({
      cards: state => state.card.list
    })
  },
  methods: {
    ...mapActions(['card/getMany']),
    initialSwiper: function () {
      new Swiper('.swiper-container', {
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: {
          delay: 5000,
          disableOnInteraction: true,
        }
      })
    },
    loadCards: function () {
      this['card/getMany']().then((ret) => {
        this.initialSwiper()
      })
    }
  },
  mounted() {
    this.loadCards()
  },
}
</script>
