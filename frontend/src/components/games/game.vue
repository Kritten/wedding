<template>
  <v-col
    cols="12"
    md="6"
    xl="4"
  >
    <v-card class="fill-height">
      <v-card-title>
        {{ game.title }}
      </v-card-title>
      <v-card-text>
        {{ game.description }}
      </v-card-text>
    </v-card>
  </v-col>
</template>

<script>
export default {
  name: 'Game',
  props: {
    game: {
      required: true,
      type: Object,
    },
  },
};
</script>

<style scoped>

</style>
