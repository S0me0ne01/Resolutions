<template>
  <div class="q-pa-md">
    <q-card dark>
      <q-card-section>
        <q-table title="Resolutions" :rows="rows" :columns="columns" row-key="title" flat :sorting="true" dark
          class="minimalistic-q-table" :no-data="true" :no-results="true" :pagination="false">
          <template v-slot:body-cell-delete="props">
            <q-td :props="props">
              <q-btn flat round dense color="negative" icon="delete" aria-label="Delete"
                @click="deleteResolution(props.row.pk)" />
            </q-td>
          </template>
        </q-table>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { useTableStore } from 'src/stores/store-table.js'
const store = useTableStore()

const columns = [
  {
    name: "title",
    required: true,
    label: "Text",
    align: "left",
    field: "title",
    sortable: false
  },
  { name: "published", align: "center", label: "Published", field: "published", sortable: true },
  { name: "rating", label: "Rating", field: "rating", sortable: true },
  { name: "format", label: "Format", field: "format" },
  { name: "category", label: "Category", field: "category" },
  { name: 'delete', label: 'Delete', field: 'pk', align: 'center' }
];

export default defineComponent({
  // eslint-disable-next-line vue/no-reserved-component-names
  name: 'Table',

  computed: {
    rows() {
      if (typeof window !== 'undefined' && !this.loaded) {
        store.setTableLoaded();
        // eslint-disable-next-line vue/no-side-effects-in-computed-properties
        this.loaded = store.getTableLoaded
        store.fetchResolutions();
      }
      return store.getResolutions;
    }
  },

  data() {
    return {
      columns,
      loaded: false
    };
  },

  methods: {
    async deleteResolution(pk) {
      try {
        await this.$axios.delete(`http://localhost:8000/resolution/delete/${pk}/`);
        store.fetchResolutions();
      } catch (error) {
        console.error(error);
      }
    }
  }
});
</script>

<style scoped>
.minimalistic-q-table {
  border: none;
  box-shadow: none;
}
</style>
