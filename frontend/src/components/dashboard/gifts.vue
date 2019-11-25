<template>
  <v-card class="fill-height">
    <v-card-title>
      {{ $tc('gifts.title', 2) }}
    </v-card-title>
    <v-card-text>
      <v-row no-gutters>
        <v-col v-html="$store.state.moduleApp.objectTexts.giftsDashboard" />
      </v-row>

      <v-row no-gutters>
        <v-col>
          <v-list dense>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>fas fa-university fa-fw</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                IBAN: DE64 1203 0000 1060 8481 14
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>fab fa-cc-paypal fa-fw</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <a href="paypal.me/krittendotorg">paypal.me/krittendotorg</a>
              </v-list-item-content>
            </v-list-item>
          </v-list>
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
