<template>
  <v-row no-gutters>
    <v-col>
      <v-stepper
        v-model="stepCurrent"
        non-linear
      >
        <v-stepper-header>
          <v-stepper-step
            v-bind:step="1"
            editable
          >
            {{ $t('games.introduction.playtime.header') }}
          </v-stepper-step>
          <v-divider />
          <v-stepper-step
            v-bind:step="2"
            editable
          >
            {{ $t('games.introduction.explanation.header') }}
          </v-stepper-step>
          <v-divider />
          <v-stepper-step
            v-bind:step="3"
            editable
          >
            {{ $t('games.introduction.coop.header') }}
          </v-stepper-step>
          <v-divider />
          <v-stepper-step
            v-bind:step="4"
            editable
          >
            {{ $t('games.introduction.properties.header') }}
          </v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <introduction-step
            v-bind:step="1"
            v-bind:step-current.sync="stepCurrent"
            v-bind:description="$t('games.introduction.playtime.description')"
          >
            <v-row
              no-gutters
              class="justify-center justify-md-start"
            >
              <v-col class="shrink">
                <v-btn-toggle
                  v-model="playtime"
                  mandatory
                  v-bind:style="objectStyles"
                >
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.playtime.0') }}
                  </v-btn>
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.playtime.1') }}
                  </v-btn>
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.playtime.2') }}
                  </v-btn>
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.playtime.3') }}
                  </v-btn>
                  <v-btn
                    class="ml-md-5 text-none"
                    x-large
                  >
                    {{ $t('games.introduction.playtime.none') }}
                  </v-btn>
                </v-btn-toggle>
              </v-col>
            </v-row>
          </introduction-step>
          <introduction-step
            v-bind:step="2"
            v-bind:step-current.sync="stepCurrent"
            v-bind:description="$t('games.introduction.explanation.description')"
          >
            <v-row
              no-gutters
              class="justify-center justify-md-start"
            >
              <v-col class="shrink">
                <v-btn-toggle
                  v-model="explanation"
                  mandatory
                  v-bind:style="objectStyles"
                >
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.explanation.0') }}
                  </v-btn>
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.explanation.1') }}
                  </v-btn>
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.explanation.2') }}
                  </v-btn>
                  <v-btn
                    class="ml-md-5 text-none"
                    x-large
                  >
                    {{ $t('games.introduction.explanation.none') }}
                  </v-btn>
                </v-btn-toggle>
              </v-col>
            </v-row>
          </introduction-step>
          <introduction-step
            v-bind:step="3"
            v-bind:step-current.sync="stepCurrent"
            v-bind:description="$t('games.introduction.coop.description')"
          >
            <v-row
              no-gutters
              class="justify-center justify-md-start"
            >
              <v-col class="shrink">
                <v-btn-toggle
                  v-model="isCoop"
                  mandatory
                  v-bind:style="objectStyles"
                >
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.coop.coop') }}
                  </v-btn>
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.coop.none') }}
                  </v-btn>
                  <v-btn
                    x-large
                    class="text-none"
                  >
                    {{ $t('games.introduction.coop.competitive') }}
                  </v-btn>
                </v-btn-toggle>
              </v-col>
            </v-row>
          </introduction-step>
          <introduction-step
            v-bind:step="4"
            v-bind:step-current.sync="stepCurrent"
            v-bind:description="$t('games.introduction.properties.description')"
          >
            <span class="title">{{ $t('games.filters.types') }}</span>
            <v-chip-group
              v-model="types"
              multiple
              column
              active-class="primary--text"
            >
              <v-chip
                v-for="genre in arrayTypes"
                v-bind:key="genre.id"
                filter
              >
                {{ genre.label }}
              </v-chip>
            </v-chip-group>

            <span class="title">{{ $t('games.filters.genres') }}</span>
            <v-chip-group
              v-model="genres"
              multiple
              column
              active-class="primary--text"
            >
              <v-chip
                v-for="genre in arrayGenres"
                v-bind:key="genre.id"
                filter
              >
                {{ genre.label }}
              </v-chip>
            </v-chip-group>

            <span class="title">{{ $t('games.filters.moods') }}</span>
            <v-chip-group
              v-model="moods"
              multiple
              column
              active-class="primary--text"
            >
              <v-chip
                v-for="genre in arrayMoods"
                v-bind:key="genre.id"
                filter
              >
                {{ genre.label }}
              </v-chip>
            </v-chip-group>
          </introduction-step>
        </v-stepper-items>
      </v-stepper>
    </v-col>
    <v-col
      cols="12"
      class="mt-3"
    >
      <v-btn
        color="primary"
        v-on:click="$emit('submit')"
      >
        {{ $t('games.introduction.common.submit') }}
      </v-btn>
      <v-btn
        text
        class="primary--text"
        v-on:click="$emit('skip')"
      >
        {{ $t('games.introduction.common.skip') }}
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
import IntroductionStep from './introduction-step';

const sortByLabel = (a, b) => {
  const labelA = a.label.toLowerCase();
  const labelB = b.label.toLowerCase();
  if (labelA < labelB) {
    return -1;
  }
  if (labelA > labelB) {
    return 1;
  }
  return 0;
};

export default {
  name: 'Introduction',
  components: { IntroductionStep },
  props: {
    filters: {
      required: true,
      type: Object,
    },
  },
  data() {
    return {
      stepCurrent: 1,
      isCoop: 1,
      playtime: 4,
      explanation: 3,
      types: [],
      genres: [],
      moods: [],
    };
  },
  computed: {
    objectStyles() {
      if (this.$vuetify.breakpoint.smAndDown === true) {
        return {
          'flex-direction': 'column',
        };
      }

      return {};
    },
    arrayGenres() {
      return this.$store.state.moduleGames.arrayGenres.map(genre => ({
        id: genre.id,
        label: this.$t(`games.genres.${genre.id}`),
      })).sort(sortByLabel);
    },
    arrayMoods() {
      return this.$store.state.moduleGames.arrayMoods.map(mood => ({
        id: mood.id,
        label: this.$t(`games.moods.${mood.id}`),
      })).sort(sortByLabel);
    },
    arrayTypes() {
      return this.$store.state.moduleGames.arrayTypes.map(type => ({
        id: type.id,
        label: this.$t(`games.types.${type.id}`),
      })).sort(sortByLabel);
    },
  },
  watch: {
    isCoop() {
      if (this.isCoop === 1) {
        this.filters.isCoop = {
          active: false,
          parts: {
            is_coop: false,
          },
        };
      } else {
        this.filters.isCoop = {
          active: true,
          parts: {
            is_coop: this.isCoop === 0,
          },
        };
      }
    },
    playtime() {
      if (this.playtime === 4) {
        this.filters.minutesPlaytime = {
          active: false,
          parts: {
            minutes_playtime_min: 0,
            minutes_playtime_max: 90,
          },
        };
      } else {
        let minutesPlaytimeMin = 0;
        let minutesPlaytimeMax = 20;

        switch (this.playtime) {
          case 1:
            minutesPlaytimeMin = 20;
            minutesPlaytimeMax = 33;
            break;
          case 2:
            minutesPlaytimeMin = 33;
            minutesPlaytimeMax = 60;
            break;
          case 3:
            minutesPlaytimeMin = 60;
            minutesPlaytimeMax = 90;
            break;
        }

        this.filters.minutesPlaytime = {
          active: true,
          parts: {
            minutes_playtime_min: minutesPlaytimeMin,
            minutes_playtime_max: minutesPlaytimeMax,
          },
        };
      }
    },
    explanation() {
      if (this.explanation === 3) {
        this.filters.minutesExplanation = {
          active: false,
          parts: {
            minutes_explanation_min: 1,
            minutes_explanation_max: 5,
          },
        };
      } else {
        let complexityMin = 1;
        let complexityMax = 2;

        switch (this.explanation) {
          case 1:
            complexityMin = 2;
            complexityMax = 3;
            break;
          case 2:
            complexityMin = 4;
            complexityMax = 5;
            break;
        }
        this.filters.minutesExplanation = {
          active: true,
          parts: {
            minutes_explanation_min: complexityMin,
            minutes_explanation_max: complexityMax,
          },
        };
      }
    },
    types() {
      const arrayIds = this.types.reduce((arrayIds, index) => {
        arrayIds.push(this.$store.state.moduleGames.arrayTypes[index].id);
        return arrayIds;
      }, []);

      if (arrayIds.length === 0) {
        this.filters.types = {
          active: false,
          parts: {
            types: [],
          },
        };
      } else {
        this.filters.types = {
          active: true,
          parts: {
            types: arrayIds,
          },
        };
      }
    },
    genres() {
      const arrayIds = this.genres.reduce((arrayIds, index) => {
        arrayIds.push(this.$store.state.moduleGames.arrayGenres[index].id);
        return arrayIds;
      }, []);

      if (arrayIds.length === 0) {
        this.filters.genres = {
          active: false,
          parts: {
            genres: [],
          },
        };
      } else {
        this.filters.genres = {
          active: true,
          parts: {
            genres: arrayIds,
          },
        };
      }
    },
    moods() {
      const arrayIds = this.moods.reduce((arrayIds, index) => {
        arrayIds.push(this.$store.state.moduleGames.arrayMoods[index].id);
        return arrayIds;
      }, []);

      if (arrayIds.length === 0) {
        this.filters.moods = {
          active: false,
          parts: {
            moods: [],
          },
        };
      } else {
        this.filters.moods = {
          active: true,
          parts: {
            moods: arrayIds,
          },
        };
      }
    },
  },
};
</script>

<style scoped>

</style>
