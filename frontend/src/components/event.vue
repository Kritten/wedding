<template>
  <v-timeline-item
    color="white"
    fill-dot
  >
    <span slot="opposite">{{ datetimeFormatted(event.datetime) }}</span>
    <v-icon
      v-if="event.icon !== null"
      slot="icon"
      color="primary"
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
              <span class="title">{{ $t('events.description') }}</span>
              <pre>{{ event.description }}</pre>
            </v-col>
            <v-col>
              <v-row
                no-gutters
                align="center"
              >
                <v-col class="title shrink pr-3">
                  {{ $t('events.location') }}
                </v-col>
                <v-col>
                  <v-dialog
                    v-model="dialogMap"
                    content-class="full-height"
                  >
                    <template v-slot:activator="{ on }">
                      <v-btn
                        v-if="event.location !== null"
                        color="primary"
                        x-small
                        v-on="on"
                      >
                        {{ $t('events.map') }} <v-icon right>
                          mdi-map-search
                        </v-icon>
                      </v-btn>
                    </template>

                    <v-card height="100%">
                      <l-map
                        v-bind:zoom="zoom"
                        v-bind:center="center"
                      >
                        <l-tile-layer v-bind:url="url" />
                        <l-marker v-bind:lat-lng="center" />
                      </l-map>
                      <v-btn
                        style="z-index: 500; top: 16px;"
                        rounded
                        right
                        top
                        fab
                        absolute
                        v-on:click="dialogMap = false"
                      >
                        <v-icon>mdi-close</v-icon>
                      </v-btn>
                    </v-card>
                  </v-dialog>
                </v-col>
              </v-row>
              <pre>{{ event.address }}</pre>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </v-timeline-item>
</template>

<script>
import parseISO from 'date-fns/parseISO';
import lightFormat from 'date-fns/lightFormat';
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';

export default {
  name: 'Event',
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  props: {
    event: {
      required: true,
      type: Object,
    },
  },
  data() {
    return {
      dialogMap: false,
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      zoom: 20,
      center: [51.96329, 7.62171],
    };
  },
  methods: {
    datetimeFormatted(datetime) {
      const datetimeParsed = parseISO(datetime);
      return lightFormat(datetimeParsed, 'H:mm, dd.MM.yyyy');
    },
  },
};
</script>

<style>
  .full-height {
    height: 100%;
  }

</style>
