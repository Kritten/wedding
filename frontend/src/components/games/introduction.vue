<template>
  <v-row no-gutters>
    <v-col>
      {{ stepCurrent }}
      {{ filters }}
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
            <v-btn-toggle
              v-model="playtime"
              mandatory
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
                class="ml-5 text-none"
                x-large
              >
                {{ $t('games.introduction.playtime.none') }}
              </v-btn>
            </v-btn-toggle>
          </introduction-step>
          <introduction-step
            v-bind:step="2"
            v-bind:step-current.sync="stepCurrent"
            v-bind:description="$t('games.introduction.explanation.description')"
          >
            <v-btn-toggle
              v-model="explanation"
              mandatory
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
                class="ml-5 text-none"
                x-large
              >
                {{ $t('games.introduction.explanation.none') }}
              </v-btn>
            </v-btn-toggle>
          </introduction-step>
          <introduction-step
            v-bind:step="3"
            v-bind:step-current.sync="stepCurrent"
            v-bind:description="$t('games.introduction.coop.description')"
          >
            <v-btn-toggle
              v-model="isCoop"
              mandatory
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
          </introduction-step>
          <introduction-step
            v-bind:step="4"
            v-bind:step-current.sync="stepCurrent"
            v-bind:description="$t('games.introduction.properties.description')"
          >
            playtime
          </introduction-step>
        </v-stepper-items>
      </v-stepper>
    </v-col>
  </v-row>
</template>

<script>
import IntroductionStep from './introduction-step';

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
    };
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
  },
  methods: {
    // console.log(this.$store.state.moduleGames.hasSeenIntroduction);
    // this.$store.dispatch('moduleGames/setState', {
    //   objectState: true,
    //   nameState: 'hasSeenIntroduction',
    //   nameStorage: 'hasSeenIntroduction',
    // });
  },
};
</script>

<style scoped>

</style>
