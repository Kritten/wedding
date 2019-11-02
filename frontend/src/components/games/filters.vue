<template>
  <v-card
    color="primary"
    dark
  >
    <v-card-title>
      Filter
      <v-spacer />
      <span class="body-2">
        {{ $t('games.countGamesFiltered', {
          countGames: $store.state.moduleGames.countGames,
          countGamesTotal: $store.state.moduleGames.countGamesTotal,
        }) }}</span>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col md="6">
          <!--
            count players
          -->
          <base-filter v-bind:filter="filters.countPlayers">
            <template v-slot:default="{ parts, disabled }">
              <v-col>
                <v-slider
                  v-model="parts.count_players_min"
                  v-bind:disabled="disabled"
                  v-bind:min="1"
                  v-bind:max="6"
                  hide-details
                  ticks="always"
                  tick-size="4"
                  v-bind:label="$t('games.filters.countPlayersMin')"
                  v-bind:tick-labels="[1, 2, 3, 4, 5, 6]"
                />
              </v-col>
              <v-col>
                <v-slider
                  v-model="parts.count_players_max"
                  v-bind:disabled="disabled"
                  v-bind:min="2"
                  v-bind:max="10"
                  hide-details
                  ticks="always"
                  tick-size="4"
                  v-bind:label="$t('games.filters.countPlayersMax')"
                  v-bind:tick-labels="[2, 3, 4, 5, 6, 7, 8, 9, '10+']"
                />
              </v-col>
            </template>
          </base-filter>
          <!--
            minutes playtime
          -->
          <base-filter v-bind:filter="filters.minutesPlaytime">
            <template v-slot:default="{ parts, disabled }">
              <v-col>
                <v-range-slider
                  v-bind:disabled="disabled"
                  v-bind:value="[parts.minutes_playtime_min, parts.minutes_playtime_max]"
                  v-bind:min="0"
                  v-bind:max="9"
                  hide-details
                  ticks="always"
                  tick-size="4"
                  v-bind:label="$t('games.filters.minutesPlaytime')"
                  v-bind:tick-labels="arrayLabelsPlaytimes"
                  v-on:change="parts.minutes_playtime_min = $event[0]; parts.minutes_playtime_max = $event[1]"
                />
              </v-col>
            </template>
          </base-filter>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script>
import BaseFilter from './base-filter';
import { ServiceGames } from '../../service/games.service';

export default {
  name: 'Filters',
  components: { BaseFilter },
  props: {
    filters: {
      required: true,
      type: Object,
    },
  },
  data() {
    return {
    };
  },
  computed: {
    arrayLabelsPlaytimes() {
      return this.arrayPlaytimes.map(entry => entry.label);
    },
    arrayPlaytimes() {
      return ServiceGames.arrayPlaytimes;
    },
  },
  watch: {
    objectFilters: {
      handler() {
        this.$emit('update:filters', this.filters);
      },
      deep: true,
    },
  },
};
</script>
