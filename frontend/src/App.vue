<template>
  <v-app>
    <router-view />
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
