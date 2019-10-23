<template>
  <v-timeline v-if="events.length > 0">
    <v-timeline-item
      v-for="(event, index) in events"
      v-bind:key="event.id"
      v-bind:opposite="index % 2 === 0"
      color="white"
      fill-dot
    >
      <span slot="opposite">{{ datetimeFormatted(event.datetime) }}</span>
      <v-icon
        v-if="event.icon !== null"
        slot="icon"
        v-bind:color="event.color_icon"
      >
        {{ event.icon }}
      </v-icon>
      <v-card v-bind:color="event.color_background">
        <v-card-title class="headline pb-0">
          {{ event.title }}
        </v-card-title>
        <v-card-text>
          <v-container
            fluid
            class="pa-0"
          >
            <v-row dense>
              <v-col>
                <pre>{{ event.description }}</pre>
              </v-col>
            </v-row>
            <v-row dense>
              <v-col>
                <span class="title">{{ $t('events.location') }}</span>
                <pre>{{ event.address }}</pre>
                <v-btn
                  v-if="event.location !== null"
                  color="primary"
                  small
                >
                  {{ $t('events.map') }} <v-icon right>
                    mdi-map-search
                  </v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
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
