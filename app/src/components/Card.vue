<template>
  <div class="mdl-card mdl-cell mdl-cell--6-col">
    <div class="mdl-card__media mdl-color-text--grey-50">
      <img v-show="imageUrl" class="w-card-img" :src="imageUrl">
      <h4 v-if="imageUrl" class="w-card-msg">{{ message }}</h4>
      <h3 v-else class="w-card-msg__quote">{{ message }}</h3>
    </div>
    <div class="mdl-card__supporting-text meta mdl-color-text--grey-600">
      <div class="w-avatar"><span>{{ author.displayname.slice(0, 2).toUpperCase() }}</span></div>
      <div>
        <strong>{{ author.displayname }}</strong>
        <span>{{ publishedAt }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    author: Object,
    imageUrl: String,
    message: String,
    publishedAt: String
  },
}
</script>
