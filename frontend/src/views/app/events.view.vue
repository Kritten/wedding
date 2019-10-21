<template>
  <v-timeline v-if="events.length > 0">
    <v-timeline-item
      v-for="(event, index) in events"
      v-bind:key="event.id"
      v-bind:opposite="index % 2 === 0"
    >
      <span slot="opposite">{{ datetimeFormatted(event.datetime) }}</span>

      <v-card>
        <v-card-title class="headline">
          {{ event.title }}
        </v-card-title>
        <v-card-text>{{ event.description }}</v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

<script>
import parseISO from 'date-fns/parseISO';
import lightFormat from 'date-fns/lightFormat';
import { ServiceEvents } from '../../service/events.service';

export default {
  name: 'EventsView',
  computed: {
    events() {
      return this.$store.state.moduleEvents.arrayEvents;
    },
  },
  created() {
    ServiceEvents.loadEvents();
  },
  methods: {
    datetimeFormatted(datetime) {
      const datetimeParsed = parseISO(datetime);
      return lightFormat(datetimeParsed, 'H:mm, dd.MM.yyyy');
    },
  },
};
</script>

<style scoped>

</style>
