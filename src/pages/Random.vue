<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md flex-center">
      <RandomResCard />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import RandomResCard from 'components/RandomResCard.vue'

export default defineComponent({
  name: 'Index',

  components: {
    RandomResCard
  }
})
</script>
