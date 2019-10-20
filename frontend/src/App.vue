<template>
  <v-app>
    <router-view v-if="$store.state.moduleApp.isInitialized === true" />
    <v-overlay v-else>
      <v-progress-circular
        indeterminate
        size="64"
      />
    </v-overlay>
  </v-app>
</template>

<script>

import { ServiceApp } from './service/app.service';

export default {
  name: 'App',
  created() {
    ServiceApp.init();
  },
};
</script>

<style lang="scss">
</style>
