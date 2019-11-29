<template>
  <v-card class="fill-height d-flex flex-column">
    <v-card-title>
      {{ $t('food.title') }}
    </v-card-title>
    <v-card-text class="black--text">
      <v-row no-gutters>
        <v-col v-html="$store.state.moduleApp.objectTexts.foodDashboard" />
      </v-row>
    </v-card-text>
    <v-spacer />
    <v-card-actions>
      <set-food />
    </v-card-actions>
  </v-card>
</template>

<script>

import SetFood from '../food/set-food';

export default {
  name: 'TheFood',
  components: { SetFood },
};
</script>

<style scoped>

</style>
