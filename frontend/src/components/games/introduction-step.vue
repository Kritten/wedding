<template>
  <v-stepper-content v-bind:step="step">
    <v-row no-gutters>
      <v-col cols="12">
        <v-card flat>
          {{ description }}
        </v-card>
      </v-col>
      <v-col cols="12">
        <v-card flat>
          <slot />
        </v-card>
      </v-col>
      <v-col cols="12">
        <v-btn
          v-if="stepCurrent > 1"
          class="mt-3 primary--text"
          text
          small
          v-on:click="$emit('update:step-current', stepCurrent - 1)"
        >
          {{ $t('games.introduction.common.back') }}
        </v-btn>
        <v-btn
          v-if="stepCurrent < 4"
          class="mt-3"
          color="secondary primary--text"
          small
          v-on:click="$emit('update:step-current', stepCurrent + 1)"
        >
          {{ $t('games.introduction.common.continue') }}
        </v-btn>
      </v-col>
    </v-row>
  </v-stepper-content>
</template>

<script>
export default {
  name: 'IntroductionStep',
  props: {
    step: {
      required: true,
      type: Number,
    },
    stepCurrent: {
      required: true,
      type: Number,
    },
    description: {
      required: true,
      type: String,
    },
  },
};
</script>

<style scoped>

</style>
