<template>
  <main class="mdl-layout__content">
    <div class="w-main__posts mdl-grid">
      <div class="mdl-card mdl-cell mdl-cell--12-col">
        <div class="w-headline mdl-card__media mdl-color-text--grey-50">
        </div>
      </div>
    </div>
    <Dialog />
  </main>
</template>

<script>

import Card from './Card.vue'
import Dialog from './Dialog.vue'

export default {
  name: 'Index',
  components: {
    Card,
    Dialog
  },
  data: () => ({
    //
  })
}
</script>
