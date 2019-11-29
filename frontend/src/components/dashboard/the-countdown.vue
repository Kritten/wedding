<template>
  <countdown
    v-if="$vuetify.breakpoint.smAndUp"
    v-bind:end-time="endTime"
  >
    <template
      v-slot:process="{ timeObj }"
    >
      <span
        class="title"
      >noch {{ display(timeObj) }}</span>
    </template>
    <template
      v-slot:finish
    >
      <span>Done!</span>
    </template>
  </countdown>
</template>

<script>
import { parseISO } from 'date-fns';

export default {
  name: 'TheCountdown',
  data() {
    return {
      endTime: parseISO('2020-05-17T14:00:00').getTime(),
    };
  },
  methods: {
    display(timeObj) {
      let result = '';

      result += `${timeObj.d} ${this.$tc('countdown.days', timeObj.d)}`;

      if (this.$vuetify.breakpoint.mdAndUp === true) {
        result += `
        ${timeObj.h} ${this.$tc('countdown.hours', timeObj.h)}
        ${timeObj.m} ${this.$tc('countdown.minutes', timeObj.m)}
        ${timeObj.s} ${this.$tc('countdown.seconds', timeObj.s)}
      `;
      }
      return result;
    },
  },
};
</script>

<style scoped>

</style>
