<template>
  <v-timeline
    v-if="events.length > 0"
    v-bind:reverse="$vuetify.breakpoint.mdAndUp"
    v-bind:dense="$vuetify.breakpoint.smAndDown"
  >
    <event
      v-for="event in events"
      v-bind:key="event.id"
      v-bind:event="event"
    />
  </v-timeline>
</template>

<script>
import { ServiceEvents } from '../../service/events.service';
import Event from '../../components/event';


export default {
  name: 'EventsView',
  components: {
    Event,
  },
  computed: {
    events() {
      return this.$store.state.moduleEvents.arrayEvents;
    },
  },
  created() {
    ServiceEvents.loadEvents();
  },
};
</script>

<style>
</style>
