<template>
  <v-row no-gutters>
    <v-col class="shrink">
      <v-checkbox
        v-model="filter.active"
        class="mt-0"
        hide-details
      />
    </v-col>
    <slot
      v-bind:parts="filter.parts"
      v-bind:disabled="!filter.active"
    />
  </v-row>
</template>

<script>
export default {
  name: 'BaseFilter',
  props: {
    filter: {
      required: true,
      type: Object,
    },
  },
};
</script>

<style scoped>

</style>
