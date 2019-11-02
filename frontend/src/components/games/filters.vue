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
        <v-col md="3">
          <v-slider
            v-bind:disabled="true"
            v-bind:value="filters.count_players_min"
            v-bind:min="1"
            v-bind:max="6"
            hide-details
            ticks="always"
            tick-size="4"
            label="test"
            v-bind:tick-labels="[1, 2, 3, 4, 5, 6]"
            v-on:change="filters.count_players_min = $event"
          />
        </v-col>
        <v-col md="3">
          <v-slider
            v-bind:value="filters.count_players_max"
            v-bind:min="2"
            v-bind:max="10"
            hide-details
            ticks="always"
            tick-size="4"
            label="test"
            v-bind:tick-labels="[2, 3, 4, 5, 6, 7, 8, 9, '10+']"
            v-on:change="filters.count_players_max = $event"
          />
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script>
export default {
  name: 'Filters',
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
