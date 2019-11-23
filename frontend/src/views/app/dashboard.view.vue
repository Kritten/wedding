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
      <the-food />
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
      <gifts />
    </v-col>
    <v-col
      cols="12"
      xl="6"
    >
      <hotels />
    </v-col>
  </v-row>
</template>

<script>
import Confirmation from '../../components/dashboard/confirmation';
import TheCountdown from '../../components/dashboard/the-countdown';
import TheGame from '../../components/dashboard/the-game';
import Gifts from '../../components/dashboard/gifts';
import TheFood from '../../components/dashboard/the-food';
import Hotels from '../../components/dashboard/hotels';

export default {
  name: 'DashboardView',
  components: {
    Hotels,
    TheFood,
    Gifts,
    TheGame,
    TheCountdown,
    Confirmation,
  },
};
</script>

<style scoped>

</style>
