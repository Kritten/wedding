<template>
  <v-card class="fill-height">
    <v-card-title>
      Countdown
    </v-card-title>
    <v-card-text>
      <countdown v-bind:end-time="endTime">
        <template
          v-slot:process="{ timeObj }"
        >
          <span
            v-bind:class="{
              'title': $vuetify.breakpoint.xsOnly,
              'headline': $vuetify.breakpoint.smOnly,
              'display-1': $vuetify.breakpoint.smAndUp,
            }"
          >{{ display(timeObj) }}</span>
        </template>
        <template
          v-slot:finish
        >
          <span>Done!</span>
        </template>
      </countdown>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'TheCountdown',
  data() {
    return {
      endTime: new Date(2020, 4, 17, 13).getTime(),
    };
  },
  methods: {
    display(timeObj) {
      let result = '';
      result += `
        ${timeObj.d} ${this.$tc('countdown.days', timeObj.d)}
        ${timeObj.h} ${this.$tc('countdown.hours', timeObj.h)}
        ${timeObj.m} ${this.$tc('countdown.minutes', timeObj.m)}
        ${timeObj.s} ${this.$tc('countdown.seconds', timeObj.s)}
      `;
      return result;
    },
  },
};
</script>

<style scoped>

</style>
