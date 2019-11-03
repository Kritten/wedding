<template>
  <v-row no-gutters>
    <v-col class="shrink">
      <v-checkbox
        v-bind:value="filter.active"
        class="mt-0"
        hide-details
        v-on:change="applyCallbacks"
      />
    </v-col>
    <slot
      v-bind:parts="filter.parts"
      v-bind:disabled="!filter.active"
      v-bind:activate="activate"
      v-bind:focus="focus"
      v-bind:apply-callbacks="applyCallbacks"
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
    callbacks: {
      required: false,
      type: Object,
      default() {
        return {};
      },
    },
  },
  methods: {
    applyCallbacks(force = false) {
      if (force === true || this.filter.active === false) {
        this.filter.active = true;

        for (const [key, value] of Object.entries(this.callbacks)) {
          if (key === 'focus') {
            this.focus(...value);
          }
        }
      } else {
        this.filter.active = false;
      }
    },
    activate() {
      if (this.filter.active === false) this.filter.active = true;
    },
    focus(ref, isList = false) {
      // this.activate();

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
