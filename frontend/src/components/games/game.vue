<template>
  <v-col
    cols="12"
    md="6"
    xl="4"
  >
    <v-card
      class="fill-height"
    >
      <v-card-title>
        {{ game.title }}
      </v-card-title>
      <div v-show="showDetails === false">
        <v-carousel
          v-if="game.images.length > 0"
          height="200"
          v-bind:hide-delimiter-background="true"
          next-icon="mdi-chevron-right"
          prev-icon="mdi-chevron-left"
          v-bind:show-arrows="game.images.length > 1"
        >
          <v-carousel-item
            v-for="image in game.images"
            v-bind:key="image.id"
          >
            <v-img
              v-bind:src="image.link"
              height="200px"
              contain
            />
          </v-carousel-item>
        </v-carousel>
        <v-card-text>
          <v-row dense>
            <v-col cols="5">
              <v-row no-gutters>
                <v-col
                  cols="12"
                  sm="6"
                  md="12"
                  xl="6"
                  class="font-weight-bold"
                >
                  {{ $t('games.countPlayers') }}
                </v-col>
                <v-col>
                  {{ $tc('games.infoCountPlayers', game.count_players_min === game.count_players_max ? 1 : 2, {
                    countPlayersMin: game.count_players_min,
                    countPlayersMax: game.count_players_max,
                  }) }}
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="2" />
            <v-col cols="5">
              <v-row no-gutters>
                <v-col
                  cols="12"
                  sm="6"
                  md="12"
                  xl="6"
                  class="font-weight-bold"
                >
                  {{ $t('games.complexity') }}
                </v-col>
                <v-col>
                  <v-rating
                    dense
                    x-small
                    readonly
                    v-bind:value="game.minutes_explanation"
                  />
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-row dense>
            <v-col cols="5">
              <v-row no-gutters>
                <v-col
                  cols="12"
                  sm="6"
                  md="12"
                  xl="6"
                  class="font-weight-bold"
                >
                  {{ $t('games.playtime') }}
                </v-col>
                <v-col>
                  {{ $tc('games.infoPlaytime', game.minutes_playtime_min === game.minutes_playtime_max ? 1 : 2, {
                    playtimeMin: playtimeMinFormatted,
                    playtimeMax: playtimeMaxFormatted,
                  }) }}
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="2" />
          </v-row>
        </v-card-text>
      </div>
      <div v-show="showDetails === true">
        <v-card-text>
          {{ game.description }}
        </v-card-text>
      </div>
      <v-card-actions>
        <v-btn
          text
          color="primary"
          v-on:click="showDetails = !showDetails"
        >
          <span v-if="showDetails === true">
            {{ $t('common.back') }}</span>
          <span v-else>
            {{ $t('games.details') }}</span>
        </v-btn>
      </v-card-actions>

      <!--      <v-expand-transition>-->
      <!--        <div v-show="showDetails">-->
      <!--          <v-divider />-->

      <!--          <v-card-text>-->
      <!--            {{ game.description }}-->
      <!--          </v-card-text>-->
      <!--        </div>-->
      <!--      </v-expand-transition>-->
    </v-card>
  </v-col>
</template>

<script>
export default {
  name: 'Game',
  props: {
    game: {
      required: true,
      type: Object,
    },
  },
  data() {
    return {
      showDetails: false,
    };
  },
  computed: {
    playtimeMinFormatted() {
      return this.formatPlaytime(this.game.minutes_playtime_min);
    },
    playtimeMaxFormatted() {
      return this.formatPlaytime(this.game.minutes_playtime_max);
    },
  },
  methods: {
    formatPlaytime(playtime) {
      if (playtime >= 120) {
        return `${(playtime / 60).toFixed(1)}h`;
      }

      return `${playtime}m`;
    },
  },
};
</script>

<style scoped>

</style>
