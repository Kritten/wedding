<template>
  <v-col
    cols="12"
    md="6"
    xl="4"
  >
    <v-card class="fill-height">
      <v-card-title>
        {{ game.title }}
      </v-card-title>
      <v-card-text>
        <v-row dense>
          <v-col>
            {{ $tc('games.infoCountPlayers', game.count_players_min === game.count_players_max ? 1 : 2, {
              countPlayersMin: game.count_players_min,
              countPlayersMax: game.count_players_max,
            }) }}
          </v-col>
        </v-row>
        <v-row dense>
          <v-col>
            {{ game.description }}
          </v-col>
        </v-row>
      </v-card-text>
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
};
</script>

<style scoped>

</style>
