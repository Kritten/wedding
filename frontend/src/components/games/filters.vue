<template>
  <v-card
    color="primary"
    dark
  >
    <v-card-title v-on:click="showFilters = !showFilters">
      Filter
      <v-spacer />
      <v-btn
        v-if="hasActiveFilters"
        small
        color="accent"
        v-bind:icon="$vuetify.breakpoint.xs === true"
        class="mr-3"
        v-on:click.stop="$emit('reset-filters')"
      >
        <v-icon v-if="$vuetify.breakpoint.xs === true">
          fas fa-undo
        </v-icon>
        <span v-else>{{ $t('games.resetFilters') }}</span>
      </v-btn>

      <v-btn
        color="accent"
        small
        class="mr-3"
        v-bind:icon="$vuetify.breakpoint.xs === true"
        v-on:click="$emit('start-introduction')"
      >
        <v-icon v-if="$vuetify.breakpoint.xs === true">
          fas fa-question
        </v-icon>
        <span v-else>
          {{ $t('games.introduction.common.title') }}
        </span>
      </v-btn>

      <span class="body-2">
        {{ $t('games.countGamesFiltered', {
          countGames: $store.state.moduleGames.countGames,
          countGamesTotal: $store.state.moduleGames.countGamesTotal,
        }) }}
      </span>

      <v-btn
        icon
      >
        <v-icon>{{ showFilters ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-title>

    <v-expand-transition>
      <v-card-text v-if="showFilters">
        <v-row>
          <!--
            title
          -->
          <v-col
            cols="12"
            md="6"
          >
            <base-filter
              v-bind:filter="filters.title"
              v-bind:callbacks="{
                focus: [$refs.filtersTitle],
              }"
            >
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks} : {}"
                >
                  <v-text-field
                    ref="filtersTitle"
                    v-bind:value="parts.title"
                    v-bind:disabled="disabled"
                    hide-details
                    dense
                    class="mt-0"
                    v-on:change="parts.title = $event"
                  >
                    <template v-slot:prepend>
                      <div
                        class="mt-1 text-no-wrap"
                        style="cursor: pointer"
                        v-on:click="applyCallbacks(true)"
                      >
                        {{ $t('games.filters.title') }}
                      </div>
                    </template>
                  </v-text-field>
                </v-col>
              </template>
            </base-filter>
          </v-col>
          <!--
            description
          -->
          <v-col
            cols="12"
            md="6"
          >
            <base-filter
              v-bind:filter="filters.description"
              v-bind:callbacks="{
                focus: [$refs.filtersDescription],
              }"
            >
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks} : {}"
                >
                  <v-text-field
                    ref="filtersDescription"
                    v-bind:value="parts.description"
                    v-bind:disabled="disabled"
                    hide-details
                    dense
                    class="mt-0"
                    v-on:change="parts.description = $event"
                  >
                    <template v-slot:prepend>
                      <div
                        class="mt-1 text-no-wrap"
                        style="cursor: pointer"
                        v-on:click="applyCallbacks(true)"
                      >
                        {{ $t('games.filters.description') }}
                      </div>
                    </template>
                  </v-text-field>
                </v-col>
              </template>
            </base-filter>
          </v-col>
          <!--
            count players
          -->
          <v-col
            cols="12"
            md="6"
          >
            <base-filter v-bind:filter="filters.countPlayers">
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks} : {}"
                >
                  <v-row no-gutters>
                    <v-col
                      cols="12"
                      sm="6"
                    >
                      <v-slider
                        ref="filtersCountPlayerMin"
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
                    <v-col
                      cols="12"
                      sm="6"
                      class="pl-3"
                    >
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
                  </v-row>
                </v-col>
              </template>
            </base-filter>
          </v-col>
          <!--
            minutes playtime
          -->
          <v-col
            cols="12"
            md="6"
          >
            <base-filter v-bind:filter="filters.minutesPlaytime">
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks} : {}"
                >
                  <v-range-slider
                    v-bind:disabled="disabled"
                    v-bind:value="[parts.minutes_playtime_min, parts.minutes_playtime_max]"
                    v-bind:min="0"
                    v-bind:max="90"
                    hide-details
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
          <v-col
            cols="12"
            md="6"
          >
            <base-filter v-bind:filter="filters.minutesExplanation">
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks} : {}"
                >
                  <v-row no-gutters>
                    <v-col
                      cols="12"
                      sm="6"
                    >
                      <v-slider
                        ref="filtersCountPlayerMin"
                        v-model="parts.minutes_explanation_min"
                        v-bind:disabled="disabled"
                        v-bind:min="1"
                        v-bind:max="5"
                        hide-details
                        ticks="always"
                        tick-size="4"
                        v-bind:label="$t('games.filters.complexityMin')"
                        v-bind:tick-labels="[1, 2, 3, 4, 5]"
                      />
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      class="pl-3"
                    >
                      <v-slider
                        v-model="parts.minutes_explanation_max"
                        v-bind:disabled="disabled"
                        v-bind:min="1"
                        v-bind:max="5"
                        hide-details
                        ticks="always"
                        tick-size="4"
                        v-bind:label="$t('games.filters.complexityMax')"
                        v-bind:tick-labels="[1, 2, 3, 4, 5]"
                      />
                    </v-col>
                  </v-row>
                  <!--                  <v-range-slider-->
                  <!--                    v-bind:disabled="disabled"-->
                  <!--                    v-bind:value="[parts.minutes_explanation_min, parts.minutes_explanation_max]"-->
                  <!--                    v-bind:min="5"-->
                  <!--                    v-bind:max="40"-->
                  <!--                    hide-details-->
                  <!--                    ticks="always"-->
                  <!--                    tick-size="4"-->
                  <!--                    v-bind:tick-labels="arrayLabelsExplanation"-->
                  <!--                    v-on:change="parts.minutes_explanation_min = $event[0]; parts.minutes_explanation_max = $event[1]"-->
                  <!--                  />-->
                </v-col>
              </template>
            </base-filter>
          </v-col>
          <!--
            coop
          -->
          <v-col
            cols="12"
            md="6"
          >
            <base-filter v-bind:filter="filters.isCoop">
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks} : {}"
                >
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
          <v-col
            cols="12"
            md="6"
          >
            <base-filter
              v-bind:filter="filters.genres"
              v-bind:callbacks="{
                focus: [$refs.filtersGenres, true],
              }"
            >
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks } : {}"
                >
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
                        v-on:click="applyCallbacks(true)"
                      >
                        {{ $t('games.filters.genres') }}
                      </div>
                    </template>
                  </v-select>
                </v-col>
              </template>
            </base-filter>
          </v-col>
          <!--
            moods
          -->
          <v-col
            cols="12"
            md="6"
          >
            <base-filter
              v-bind:filter="filters.moods"
              v-bind:callbacks="{
                focus: [$refs.filtersMoods, true],
              }"
            >
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks } : {}"
                >
                  <v-select
                    ref="filtersMoods"
                    v-model="parts.moods"
                    v-bind:disabled="disabled"
                    v-bind:items="arrayMoods"
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
                        v-on:click="applyCallbacks(true)"
                      >
                        {{ $t('games.filters.moods') }}
                      </div>
                    </template>
                  </v-select>
                </v-col>
              </template>
            </base-filter>
          </v-col>
          <!--
            types
          -->
          <v-col
            cols="12"
            md="6"
          >
            <base-filter
              v-bind:filter="filters.types"
              v-bind:callbacks="{
                focus: [$refs.filtersTypes, true],
              }"
            >
              <template v-slot:default="{ parts, disabled, applyCallbacks }">
                <v-col
                  v-on="disabled === true ? { click: applyCallbacks } : {}"
                >
                  <v-select
                    ref="filtersTypes"
                    v-model="parts.types"
                    v-bind:disabled="disabled"
                    v-bind:items="arrayTypes"
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
                        v-on:click="applyCallbacks(true)"
                      >
                        {{ $t('games.filters.types') }}
                      </div>
                    </template>
                  </v-select>
                </v-col>
              </template>
            </base-filter>
          </v-col>
        </v-row>
      </v-card-text>
    </v-expand-transition>
  </v-card>
</template>
<script>
import BaseFilter from './base-filter';
import { ServiceGames } from '../../service/games.service';

const sortByLabel = (a, b) => {
  const labelA = a.label.toLowerCase();
  const labelB = b.label.toLowerCase();
  if (labelA < labelB) {
    return -1;
  }
  if (labelA > labelB) {
    return 1;
  }
  return 0;
};

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
      arrayLabelExplanationInitial: ['20m', '30m', '40m'],
      showFilters: true,
    };
  },
  computed: {
    hasActiveFilters() {
      return Object.values(this.filters).map(filter => filter.active).some(value => value === true);
    },
    arrayGenres() {
      return this.$store.state.moduleGames.arrayGenres.map(genre => ({
        id: genre.id,
        label: this.$t(`games.genres.${genre.id}`),
      })).sort(sortByLabel);
    },
    arrayMoods() {
      return this.$store.state.moduleGames.arrayMoods.map(mood => ({
        id: mood.id,
        label: this.$t(`games.moods.${mood.id}`),
      })).sort(sortByLabel);
    },
    arrayTypes() {
      return this.$store.state.moduleGames.arrayTypes.map(type => ({
        id: type.id,
        label: this.$t(`games.types.${type.id}`),
      })).sort(sortByLabel);
    },
    arrayLabelsExplanation() {
      const result = ['5m', null, null, null, null, '10m'];

      for (let i = 0; i < 3; i += 1) {
        for (let j = 0; j < 9; j += 1) {
          result.push(null);
        }

        result.push(this.arrayLabelExplanationInitial[i]);
      }

      return result;
    },
    arrayLabelsPlaytimes() {
      const result = [];

      for (let i = 0; i < this.arrayPlaytimes.length - 1; i += 1) {
        result.push(this.arrayPlaytimes[i].label);

        for (let j = 0; j < 9; j += 1) {
          result.push(null);
        }
      }

      result.push(this.arrayPlaytimes[this.arrayPlaytimes.length - 1].label);

      return result;
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
