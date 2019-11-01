<template>
  <v-data-iterator
    v-bind:items="arrayGames"
    v-bind:disable-pagination="true"
    v-bind:hide-default-footer="true"
    v-bind:loading="isLoading"
    loading-text=""
  >
    <template v-slot:default="{ items }">
      <v-row>
        <template
          v-for="(game, index) in items"
        >
          <game
            v-bind:key="game.id"
            v-intersect="arrayGames.length - index === 2 && intersected"
            style="height: 200px"
            v-bind:game="game"
          />
        </template>
      </v-row>
    </template>

    <template v-slot:footer>
      <v-row v-if="isLoading === true">
        <v-col class="text-center">
          <v-progress-circular indeterminate />
        </v-col>
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
      page: 1,
      isLoading: false,
    };
  },
  computed: {
    arrayGames() {
      return this.$store.state.moduleGames.arrayGames;
    },
  },
  async created() {
    this.loadPage();
  },
  methods: {
    intersected(entries, observer, isIntersecting) {
      // console.warn('entries', entries);
      // console.log('observer', observer);
      // console.log('isIntersecting', isIntersecting);
      if (
        isIntersecting
        && this.isLoading === false
        && this.arrayGames.length < this.$store.state.moduleGames.countGames
      ) {
        console.warn('123', 123);
        this.page += 1;
        this.loadPage();
      }
    },
    async loadPage() {
      this.isLoading = true;

      await ServiceGames.loadGames({
        page: this.page,
      });

      this.isLoading = false;
    },
  },
};
</script>

<style scoped>

</style>
