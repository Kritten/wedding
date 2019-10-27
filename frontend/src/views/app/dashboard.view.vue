<template>
  <v-row>
    <v-col
      sm="12"
      lg="6"
    >
      <confirmation />
    </v-col>
    <v-col
      sm="12"
      lg="6"
    >
      <v-card>
        <v-card-title />
        <v-card-text />
      </v-card>
    </v-col>
    <v-col
      sm="12"
      lg="6"
    >
      <v-card>
        <v-card-title />
        <v-card-text />
      </v-card>
    </v-col>
    <v-col
      sm="12"
      lg="6"
    >
      <v-card>
        <v-card-title />
        <v-card-text />
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import Confirmation from '../../components/dashboard/confirmation';

export default {
  name: 'DashboardView',
  components: { Confirmation },
};
</script>

<style scoped>

</style>
