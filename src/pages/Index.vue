<template>
  <q-page class="align-center">
    <div class="flex flex-center">
      <Table />
    </div>
    <div class="text-center">
      <Input />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import Table from 'components/Table.vue'
import Input from 'components/Input.vue'

export default defineComponent({
  name: 'Index',

  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Table,
    // eslint-disable-next-line vue/no-reserved-component-names
    Input
  }
})
</script>
