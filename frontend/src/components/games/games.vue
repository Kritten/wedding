<template>
  <v-col>
    <v-row no-gutters>
      <v-col
        v-if="isActiveIntroduction === true"
        cols="12"
      >
        <introduction
          v-bind:filters.sync="filtersIntroduction"
          v-on:skip="skip"
          v-on:submit="submit"
        />
      </v-col>
      <v-col
        v-else
        cols="12"
      >
        <v-row class="mt-n3">
          <v-col>
            <filters
              v-bind:filters.sync="filters"
              v-on:reset-filters="resetFilters"
              v-on:start-introduction="isActiveIntroduction = true"
            />
          </v-col>
        </v-row>

        <v-data-iterator
          v-bind:items="arrayGames"
          v-bind:disable-pagination="true"
          v-bind:hide-default-footer="true"
          v-bind:loading="isLoading"
          loading-text=""
        >
          <template v-slot:no-data>
            <v-alert type="info">
              {{ $t('games.noGamesFound') }}
            </v-alert>
          </template>
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
    </v-row>
  </v-col>
</template>

<script>
import cloneDeep from 'lodash-es/cloneDeep';
import Game from './game';
import { ServiceGames } from '../../service/games.service';
import Filters from './filters';
import Introduction from './introduction';

const filtersInitial = {
  title: {
    active: false,
    parts: {
      title: '',
    },
  },
  description: {
    active: false,
    parts: {
      description: '',
    },
  },
  countPlayers: {
    active: false,
    parts: {
      count_players_min: 1,
      count_players_max: 10,
    },
  },
  minutesPlaytime: {
    active: false,
    parts: {
      minutes_playtime_min: 0,
      minutes_playtime_max: 90,
    },
  },
  minutesExplanation: {
    active: false,
    parts: {
      minutes_explanation_min: 1,
      minutes_explanation_max: 5,
    },
  },
  isCoop: {
    active: false,
    parts: {
      is_coop: false,
    },
  },
  genres: {
    active: false,
    parts: {
      genres: [],
    },
  },
  moods: {
    active: false,
    parts: {
      moods: [],
    },
  },
  types: {
    active: false,
    parts: {
      types: [],
    },
  },
};

export default {
  name: 'Games',
  components: {
    Introduction,
    Filters,
    Game,
  },
  data() {
    return {
      page: 1,
      isLoading: false,
      showFilters: true,
      filters: cloneDeep(filtersInitial),
      filtersIntroduction: cloneDeep(filtersInitial),
      isActiveIntroduction: false,
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
    if (this.$store.state.moduleGames.hasSeenIntroduction === false) {
      this.isActiveIntroduction = true;
    } else {
      this.loadPage({
        initialize: true,
      });
    }
  },
  methods: {
    skip() {
      this.$store.dispatch('moduleGames/setState', {
        objectState: true,
        nameState: 'hasSeenIntroduction',
        nameStorage: 'hasSeenIntroduction',
      });

      this.isActiveIntroduction = false;

      this.filtersIntroduction = cloneDeep(filtersInitial);

      this.loadPage({
        initialize: true,
      });
    },
    submit() {
      this.$store.dispatch('moduleGames/setState', {
        objectState: true,
        nameState: 'hasSeenIntroduction',
        nameStorage: 'hasSeenIntroduction',
      });

      this.isActiveIntroduction = false;

      this.filters = this.filtersIntroduction;

      this.loadPage({
        initialize: true,
      });

      this.filtersIntroduction = cloneDeep(filtersInitial);
    },
    resetFilters() {
      this.filters = cloneDeep(filtersInitial);
    },
    intersected(entries, observer, isIntersecting) {
      if (
        isIntersecting
        && this.isLoading === false
        && this.arrayGames.length < this.$store.state.moduleGames.countGames
      ) {
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
