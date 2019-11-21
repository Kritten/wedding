<template>
  <v-row>
    <v-col
      cols="12"
      xl="6"
    >
      <the-countdown />
    </v-col>
    <v-col
      cols="12"
      xl="6"
    >
      <confirmation />
    </v-col>
    <v-col
      cols="12"
      xl="6"
    >
      <the-game />
    </v-col>
    <v-col
      cols="12"
      xl="6"
    >
      Geschenke
    </v-col>
    <v-col
      cols="12"
      xl="6"
    >
      Essen
    </v-col>
  </v-row>
</template>

<script>
import Confirmation from '../../components/dashboard/confirmation';
import TheCountdown from '../../components/dashboard/the-countdown';
import TheGame from '../../components/dashboard/the-game';

export default {
  name: 'DashboardView',
  components: {
    TheGame,
    TheCountdown,
    Confirmation,
  },
};
</script>

<style scoped>

</style>
