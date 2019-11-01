<template>
  <v-data-iterator
    v-bind:items="arrayGames"
  >
    <template v-slot:item="{ item }">
      <game
        v-bind:game="item"
      />
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
