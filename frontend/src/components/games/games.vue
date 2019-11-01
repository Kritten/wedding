<template>
  <v-data-iterator
    v-bind:items="arrayGames"
  >
    <template v-slot:default="{ items }">
      <v-row>
        <game
          v-for="game in items"
          v-bind:key="game.id"
          v-bind:game="game"
        />
      </v-row>
    </template>
  </v-data-iterator>
</template>

<script>
import Game from './game';
import { ServiceGames } from '../../service/games.service';

export default {
  name: 'Games',
  components: { Game },
  data() {
    return {
    };
  },
  computed: {
    arrayGames() {
      return this.$store.state.moduleGames.arrayGames;
    },
  },
  async created() {
    await ServiceGames.loadGames();
  },
};
</script>

<style scoped>

</style>
