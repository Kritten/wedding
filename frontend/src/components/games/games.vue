<template>
  <v-col>
    <v-row class="mt-n3">
      <v-col>
        <filters v-bind:filters.sync="filters" />
      </v-col>
    </v-row>

    <v-data-iterator
      v-bind:items="arrayGames"
      v-bind:disable-pagination="true"
      v-bind:hide-default-footer="true"
      v-bind:loading="isLoading"
      loading-text=""
    >
      <template v-slot:default="{ items }">
        <v-row class="mt-n3">
          <template
            v-for="(game, index) in items"
          >
            <game
              v-bind:key="game.id"
              v-intersect="arrayGames.length - index === 2 && intersected"
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
  </v-col>
</template>

<script>
import Game from './game';
import { ServiceGames } from '../../service/games.service';
import Filters from './filters';

export default {
  name: 'Games',
  components: {
    Filters,
    Game,
  },
  data() {
    return {
      page: 1,
      isLoading: false,
      showFilters: true,
      filters: {
        count_players_min: 3,
        count_players_max: 10,
      },
    };
  },
  computed: {
    arrayGames() {
      return this.$store.state.moduleGames.arrayGames;
    },
  },
  watch: {
    filters: {
      handler() {
        console.warn('this.filters', this.filters);
        this.page = 1;
        this.loadPage({ initialize: true });
      },
      deep: true,
    },
  },
  async created() {
    this.loadPage({
      initialize: true,
    });
  },
  methods: {
    intersected(entries, observer, isIntersecting) {
      if (
        isIntersecting
        && this.isLoading === false
        && this.arrayGames.length < this.$store.state.moduleGames.countGames
      ) {
        console.warn('123', 123);
        this.page += 1;
        this.loadPage({
          initialize: false,
        });
      }
    },
    async loadPage({ initialize = false }) {
      this.isLoading = true;

      await ServiceGames.loadGames({
        page: this.page,
        initialize,
        filters: this.filters,
      });

      this.isLoading = false;
    },
  },
};
</script>
