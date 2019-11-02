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
        <!--
            count players
          -->
        <v-col md="6">
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
        </v-col>
        <!--
            minutes playtime
          -->
        <v-col md="6">
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
        <!--
            minutes explanation
          -->
        <v-col md="6">
          <base-filter v-bind:filter="filters.minutesExplanation">
            <template v-slot:default="{ parts, disabled }">
              <v-col>
                <v-range-slider
                  v-bind:disabled="disabled"
                  v-bind:value="[parts.minutes_explanation_min, parts.minutes_explanation_max]"
                  v-bind:min="1"
                  v-bind:max="5"
                  hide-details
                  ticks="always"
                  tick-size="4"
                  v-bind:label="$t('games.filters.minutesExplanation')"
                  v-bind:tick-labels="['5m', '10m', '20m', '30m', '40m']"
                  v-on:change="parts.minutes_explanation_min = $event[0]; parts.minutes_explanation_max = $event[1]"
                />
              </v-col>
            </template>
          </base-filter>
        </v-col>
        <!--
            coop
          -->
        <v-col md="6">
          <base-filter v-bind:filter="filters.isCoop">
            <template v-slot:default="{ parts, disabled }">
              <v-col>
                <v-switch
                  v-model="parts.is_coop"
                  v-bind:disabled="disabled"
                  class="mt-0"
                  hide-details
                >
                  <template v-slot:prepend>
                    <div
                      class="mt-1"
                      style="cursor: pointer"
                      v-on:click="filters.isCoop.parts.is_coop = !filters.isCoop.parts.is_coop"
                    >
                      {{ $t('games.filters.isCoop') }}
                    </div>
                  </template>
                </v-switch>
              </v-col>
            </template>
          </base-filter>
        </v-col>
        <!--
            genres
          -->
        <v-col md="6">
          <base-filter v-bind:filter="filters.genres">
            <template v-slot:default="{ parts, disabled }">
              <v-col>
                <v-select
                  ref="filtersGenres"
                  v-model="parts.genres"
                  v-bind:disabled="disabled"
                  v-bind:items="arrayGenres"
                  chips
                  clearable
                  deletable-chips
                  small-chips
                  multiple
                  item-value="id"
                  item-text="label"
                  dense
                  hide-details
                  class="mt-0"
                >
                  <template v-slot:prepend>
                    <div
                      class="mt-1 text-no-wrap"
                      style="cursor: pointer"
                      v-on:click="$refs.filtersGenres.focus(); $refs.filtersGenres.isMenuActive = true"
                    >
                      {{ $t('games.filters.genres') }}
                    </div>
                  </template>
                </v-select>
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
    arrayGenres() {
      return this.$store.state.moduleGames.arrayGenres;
    },
    arrayMoods() {
      return this.$store.state.moduleGames.arrayMoods;
    },
    arrayTypes() {
      return this.$store.state.moduleGames.arrayTypes;
    },
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
