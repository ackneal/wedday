<template>
  <div :class="classObject" @click="upload">
    <img v-if="source" :src="source">
    <label v-else>點擊上傳照片</label>
    <input type="file" accept="image/*" @change="preview" ref="input" style="display:none;"/>
  </div>
</template>

<script>
export default {
  name: 'ImageInput',
  props: {
    image: File,
    "isInvalid": Boolean
  },
  computed: {
    classObject: function () {
      return {
        "w-input-image": true,
        "no-image": !this.source,
        "is-invalid": this.isInvalid,
      }
    },
    source: function () {
      if (this.image) {
        return URL.createObjectURL(this.image)
      }
      return '';
    }
  },
  methods: {
    preview(e) {
      if (e.target.files && e.target.files[0]) {
        this.$emit('update:image', e.target.files[0])
      }
    },
    upload() {
      this.$refs.input.click()
    }
  }
}
</script>
