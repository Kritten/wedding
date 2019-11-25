<template>
  <v-dialog
    v-model="open"
    max-width="600"
  >
    <template v-slot:activator="{ on }">
      <v-btn
        color="primary"
        text
        v-on="on"
      >
        {{ $t('games.addGame') }}
      </v-btn>
    </template>

    <v-card>
      <form v-on:submit.prevent="submit">
        <v-card-title>{{ $t('games.addGame') }}</v-card-title>
        <v-card-text>
          <p>{{ $t('games.addGameDescription') }}</p>
          <v-text-field
            v-model="game"
            v-bind:label="$tc('games.title')"
          />
        </v-card-text>
        <v-card-actions>
          <v-btn
            v-bind:disabled="$v.$invalid"
            color="primary"
            type="submit"
          >
            {{ $t('common.save') }}
          </v-btn>
          <v-btn text v-on:click="cancel">
            {{ $t('common.cancel') }}
          </v-btn>
        </v-card-actions>
      </form>
    </v-card>
  </v-dialog>
</template>

<script>
import { required } from 'vuelidate/lib/validators';
import { ServiceGames } from '../../service/games.service';

export default {
  name: 'AddGame',
  data() {
    return {
      open: false,
      game: null,
    };
  },
  methods: {
    submit() {
      ServiceGames.addSuggestion({
        title: this.game,
      }).then(() => {
        this.cancel();

        this.$store.dispatch('moduleApp/openSnackbar', {
          text: this.$i18n.t('games.addedGame'),
          timeout: 6000,
        });
      });
    },
    cancel() {
      this.open = false;
      this.game = null;
    },
  },
  validations: {
    game: {
      required,
    },
  },
};
</script>

<style scoped>

</style>
