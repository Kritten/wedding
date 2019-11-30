<template>
  <v-col
    cols="12"
    md="6"
    xl="4"
  >
    <v-card
      class="fill-height d-flex flex-column"
    >
      <v-row no-gutters class="flex-grow-0">
        <v-col>
          <v-card-title style="word-break: normal">
            {{ game.title }}
          </v-card-title>
        </v-col>
        <v-col class="shrink pa-3">
          <v-btn
            text
            icon
            v-bind:loading="loadingFavorite"
            color="primary"
            v-on:click="setFavorite"
          >
            <v-icon>{{ isFavorite ? 'mdi-star' : 'mdi-star-outline' }}</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <div v-show="showDetails === false">
        <v-carousel
          v-if="game.images.length > 0"
          height="200"
          v-bind:hide-delimiter-background="true"
          next-icon="mdi-chevron-right"
          prev-icon="mdi-chevron-left"
          v-bind:show-arrows="game.images.length > 1"
          v-bind:hide-delimiters="game.images.length === 1"
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
                    color="accent"
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
        <v-card-text><span style="white-space: pre; white-space: pre-wrap">{{ game.description }}</span></v-card-text>
      </div>
      <v-card-actions class="flex-grow-1 align-end">
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
    </v-card>
  </v-col>
</template>

<script>
import { ServiceGames } from '../../service/games.service';

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
      loadingFavorite: false,
    };
  },
  computed: {
    playtimeMinFormatted() {
      return this.formatPlaytime(this.game.minutes_playtime_min);
    },
    playtimeMaxFormatted() {
      return this.formatPlaytime(this.game.minutes_playtime_max);
    },
    isFavorite() {
      return this.$store.state.moduleApp.objectUser.games_favorite.some(idGame => idGame === this.game.id);
    },
  },
  methods: {
    formatPlaytime(playtime) {
      if (playtime >= 120) {
        return `${(playtime / 60).toFixed(1)}h`;
      }

      return `${playtime}m`;
    },
    async setFavorite() {
      this.loadingFavorite = true;

      const stateNew = !this.isFavorite;

      await ServiceGames.setFavorite({
        isFavorite: stateNew,
        idGame: this.game.id,
      });

      this.$store.dispatch('moduleApp/openSnackbar', {
        text: stateNew === true ? this.$i18n.t('games.addedFavorite') : this.$i18n.t('games.removedFavorite'),
      });

      this.loadingFavorite = false;
    },
  },
};
</script>

<style scoped>

</style>
