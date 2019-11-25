<template>
  <v-card class="fill-height d-flex flex-column">
    <v-card-title>
      {{ $tc('games.title', 2) }}
    </v-card-title>
    <v-card-text>
      <v-row no-gutters>
        <v-col v-html="$store.state.moduleApp.objectTexts.gamesDashboard" />
      </v-row>
    </v-card-text>
    <v-spacer />
    <v-card-actions>
      <add-game />
    </v-card-actions>
  </v-card>
</template>

<script>
import AddGame from '../games/add-game';

export default {
  name: 'TheGame',
  components: { AddGame },
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
