<template>
  <v-card class="fill-height">
    <v-card-title>
      {{ $tc('gifts.title', 2) }}
    </v-card-title>
    <v-card-text class="black--text">
      <v-row no-gutters>
        <v-col v-html="$store.state.moduleApp.objectTexts.giftsDashboard" />
      </v-row>

      <v-row no-gutters>
        <v-col>
          <v-row>
            <v-col class="shrink">
              <v-icon>fas fa-university fa-fw</v-icon>
            </v-col>
            <v-col>Inhaber: Kristof Komlossy und Eileen Bartl</v-col>
            <v-col>IBAN: DE64 1203 0000 1060 8481 14</v-col>
          </v-row>
          <v-row>
            <v-col class="shrink">
              <v-icon>fab fa-cc-paypal fa-fw</v-icon>
            </v-col>
            <v-col>
              <a
                href="https://paypal.me/krittendotorg"
                target="_blank"
              >paypal.me/krittendotorg</a>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>

export default {
  name: 'Gifts',
  data() {
    return {
    };
  },
  methods: {
  },
};
</script>

<style scoped>

</style>
