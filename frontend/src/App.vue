<template>
  <v-app v-bind:style="{ background: $vuetify.theme.themes.light.background}">
    <router-view v-if="$store.state.moduleApp.isInitialized === true" />
    <v-overlay v-else>
      <v-progress-circular
        indeterminate
        size="64"
      />
    </v-overlay>
    <snackbar-global />
  </v-app>
</template>

<script>

import { ServiceApp } from './service/app.service';
import SnackbarGlobal from './components/snackbar-global';

export default {
  name: 'App',
  components: { SnackbarGlobal },
  created() {
    ServiceApp.init();
  },
};
</script>

<style lang="scss">
</style>
