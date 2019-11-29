<template>
  <v-card class="fill-height">
    <v-card-title>
      {{ $tc('hotels.title', 2) }}
    </v-card-title>
    <v-card-text class="black--text">
      <v-row no-gutters>
        <v-col v-html="$store.state.moduleApp.objectTexts.hotelsDashboard" />
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>

export default {
  name: 'Hotels',
  data() {
    return {
    };
  },
  methods: {
  },
};
</script>

<style scoped>

</style>
