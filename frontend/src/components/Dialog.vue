<template>
  <div class="w-dialog">
    <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-color--accent mdl-color-text--white w-open-button" @click="open">留言給新人祝福</button>
    <dialog class="mdl-dialog" ref="dialog">
      <div>
        <h4 class="mdl-dialog__title">留言給新人祝福</h4>
        <div class="mdl-dialog__content">
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
        </div>
        <div class="mdl-dialog__actions">
          <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent mdl-js-ripple-effect" @click="submit">
            送出
          </button>
          <button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect" @click="close">
            等等再來
          </button>
        </div>
      </div>
    </dialog>
  </div>
</template>

<script>

import { mapActions } from 'vuex'
import dialogPolyfill from 'dialog-polyfill'
import ImageInput from './Image-Input.vue'

export default {
  name: 'Dialog',
  components: {
    ImageInput
  },
  data: () => ({
    dialog: null,
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
    open() {
      dialogPolyfill.registerDialog(this.dialog);
      this.dialog.showModal();
    },
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
        this.close()
      })
    },
    close() {
      this.dialog.close()
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
    this.dialog = this.$refs.dialog;
  }
}
</script>
