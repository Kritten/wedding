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
      Spiele
    </v-col>
    <v-col
      cols="12"
      xl="6"
    >
      Geschenke
    </v-col>
  </v-row>
</template>

<script>
import Confirmation from '../../components/dashboard/confirmation';
import TheCountdown from '../../components/dashboard/the-countdown';

export default {
  name: 'DashboardView',
  components: {
    TheCountdown,
    Confirmation,
  },
};
</script>

<style scoped>

</style>
