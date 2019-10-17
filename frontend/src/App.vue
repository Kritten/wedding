<template>
  <span>test</span>
</template>

<script>

import {ServiceApp} from './service/app.service';

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
    };
  },
  created() {
    ServiceApp.init();
  },
};
</script>

<style lang="scss">
</style>
