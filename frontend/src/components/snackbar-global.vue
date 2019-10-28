<template>
  <v-snackbar
    v-model="open"
    v-bind:timeout="timeout"
    v-bind:color="color"
  >
    {{ text }}
    <v-btn
      text
      icon
      v-on:click="open = false"
    >
      <v-icon>fas fa-times</v-icon>
    </v-btn>
  </v-snackbar>
</template>

<script>
export default {
  name: 'SnackbarGlobal',
  data() {
    return {
      open: false,
      text: null,
      timeout: null,
      color: null,
    };
  },
  watch: {
    '$store.state.moduleApp.objectSnackbar': function (objectSnackbar) {
      this.text = objectSnackbar.text;
      this.timeout = objectSnackbar.timeout === undefined ? 3000 : objectSnackbar.timeout;
      this.color = objectSnackbar.color === undefined ? 'primary' : objectSnackbar.color;
      this.open = true;
    },
  },
};
</script>

<style scoped>

</style>
