<template>
  <v-card class="fill-height">
    <v-card-title>
      {{ $tc('games.title', 2) }}
    </v-card-title>
    <v-card-text>
      <v-row no-gutters>
        <v-col>
          {{ $t('games.description') }}
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <add-game />
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import AddGame from '../games/add-game';

export default {
  name: 'TheGame',
  components: { AddGame },
  data() {
    return {
    };
  },
  methods: {
  },
};
</script>

<style scoped>

</style>
