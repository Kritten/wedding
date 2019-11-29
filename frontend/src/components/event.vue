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
      <v-card-text class="black--text">
        <v-container
          fluid
          class="pa-0"
        >
          <v-row>
            <v-col
              v-if="$vuetify.breakpoint.smAndDown"
              cols="12"
            >
              <p class="title mb-0">
                {{ $t('events.time') }}
              </p>
              {{ datetimeFormatted(event.datetime) }}
            </v-col>
            <v-col
              cols="12"
              md="6"
            >
              <v-row no-gutters>
                <v-col>
                  <span class="title">{{ $t('events.description') }}</span>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col>
                  <span style="white-space: pre; white-space: pre-wrap">{{ event.description }}</span>
                </v-col>
              </v-row>
            </v-col>
            <v-col
              cols="12"
              md="6"
            >
              <v-row
                no-gutters
                align="center"
              >
                <v-col class="title pr-3">
                  {{ $t('events.location') }}
                </v-col>
                <v-col class="shrink">
                  <v-dialog
                    v-model="dialogMap"
                    content-class="full-height"
                  >
                    <template v-slot:activator="{ on }">
                      <v-btn
                        v-if="event.latitude !== null && event.longitude !== null"
                        color="primary"
                        small
                        v-on="on"
                      >
                        {{ $t('events.map') }} <v-icon right>
                          fas fa-map-marker-alt
                        </v-icon>
                      </v-btn>
                    </template>

                    <v-card height="calc(100%)">
                      <l-map
                        v-bind:zoom="zoom"
                        v-bind:center="center"
                      >
                        <l-tile-layer v-bind:url="url" />
                        <l-marker v-bind:lat-lng="center" />
                      </l-map>
                      <v-btn
                        style="z-index: 500; top: 16px;"
                        color="primary"
                        rounded
                        right
                        top
                        fab
                        absolute
                        v-on:click="dialogMap = false"
                      >
                        <v-icon>fas fa-times</v-icon>
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
      center: [this.event.latitude, this.event.longitude],
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
