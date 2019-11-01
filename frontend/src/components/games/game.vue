<template>
  <span>{{game}}</span>
</template>

<script>
export default {
  name: 'Game',
  props: {
    game: {
      required: true,
      type: Object,
    },
  },
};
</script>

<style scoped>

</style>
