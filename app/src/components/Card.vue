<template>
  <div class="mdl-card mdl-cell mdl-cell--6-col">
    <div class="mdl-card__media mdl-color-text--grey-50">
      <img v-show="image" class="w-card-img" :src="image">
      <h4 v-if="image" class="w-card-msg">{{ message }}</h4>
      <h3 v-else class="w-card-msg__quote">{{ message }}</h3>
    </div>
    <div class="mdl-card__supporting-text meta mdl-color-text--grey-600">
      <div class="w-avatar"><span>{{ name.slice(0, 2).toUpperCase() }}</span></div>
      <div>
        <strong>
          {{ name }} 在 <span>{{ publishAt }}</span>寫下了祝福...
        </strong>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    name: String,
    message: String,
    image: String,
    created_at: Number,
  },
  computed: {
    publishAt: function () {
      const current = parseInt(new Date().getTime() / 1000)
      const diff = current - this.created_at

      if (diff < 60) {
        return '剛剛'
      }

      if (diff < 3600) {
          return Math.floor(diff/60) + " 分鐘前";
      }

      return new Date(this.created_at * 1000).toTimeString().slice(0, 5) + ' '
    },
  },
}
</script>
