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
      v-bind:activate="activate"
      v-bind:focus="focus"
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
  methods: {
    activate() {
      if (this.filter.active === false) this.filter.active = true;
    },
    focus(ref, isList = false) {
      this.activate();

      this.$nextTick(() => {
        ref.focus();
      });

      if (isList === true) {
        ref.isMenuActive = true;
      }
    },
  },
};
</script>

<style scoped>

</style>
