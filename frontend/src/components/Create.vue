<template>
  <main class="w-new mdl-layout__content">
    <div class="mdl-card mdl-shadow--2dp mdl-cell mdl-cell--12-col">
      <div class="mdl-card__title">
        <h4>留言給新人祝福吧</h4>
      </div>
      <form>
        <image-input :image.sync="image" :is-invalid="invalidImage"/>
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" :class="{ 'is-invalid': name.invalid }">
          <input class="mdl-textfield__input" type="text" v-model="name.value">
          <label class="mdl-textfield__label">留下你的名字吧</label>
        </div>
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label" :class="{ 'is-invalid': message.invalid }">
          <textarea class="mdl-textfield__input" type="text" rows="3" v-model="message.value"></textarea>
          <label class="mdl-textfield__label">我想大聲說...</label>
        </div>
      </form>
       <div class="mdl-card__actions">
        <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent mdl-js-ripple-effect" @click="submit">
          送出
        </button>
        <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect" @click="backToIndex">
          等等再來
        </button>
      </div>
    </div>
  </main>
</template>

<script>

import { mapActions } from 'vuex'
import ImageInput from './Image-Input.vue'

export default {
  name: 'Create',
  components: {
    ImageInput
  },
  data: () => ({
    name: {
      value: '',
      invalid: false
    },
    message: {
      value: '',
      invalid: false
    },
    image: null,
    invalidImage: false,
  }),
  methods: {
    ...mapActions(['card/create']),
    submit() {
      this.name.invalid = !this.name.value
      this.message.invalid = !this.message.value
      this.invalidImage = !this.image

      if (this.name.invalid || this.message.invalid || this.invalidImage) {
        return
      }

      return this['card/create']({
        name: this.name.value,
        message: this.message.value,
        image: this.image
      }).then(res => {
        this.$socket.emit('new', JSON.stringify(res))
        this.backToIndex()
      })
    },
    backToIndex() {
      this.$router.replace('/')
    },
    initial() {
      this.name = {
        value: '',
        invalid: false,
      }
      this.message = {
        value: '',
        invalid: false,
      }
      this.image = null
      this.invalidImage = false
    },
  },
  mounted() {
    this.initial()
  }
}
</script>
