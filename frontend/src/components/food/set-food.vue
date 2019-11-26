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
        {{ $t('food.setFood') }}
      </v-btn>
    </template>

    <v-card>
      <form v-on:submit.prevent="submit">
        <v-card-title>{{ $t('food.setFood') }}</v-card-title>
        <v-card-text>
          <p>{{ $t('food.setFoodDescription') }}</p>
          <v-textarea
            v-model="food"
            v-bind:label="$tc('food.notes')"
            outlined
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
          <v-btn
            text
            v-on:click="cancel"
          >
            {{ $t('common.cancel') }}
          </v-btn>
        </v-card-actions>
      </form>
    </v-card>
  </v-dialog>
</template>

<script>
import { required } from 'vuelidate/lib/validators';
import { ServiceUser } from '../../service/user.service';

export default {
  name: 'SetFood',
  data() {
    return {
      open: false,
      food: this.$store.state.moduleApp.objectUser.food,
    };
  },
  methods: {
    submit() {
      ServiceUser.update({
        food: this.food,
      }).then(() => {
        this.cancel();

        this.$store.dispatch('moduleApp/openSnackbar', {
          text: this.$i18n.t('food.addedFood'),
          timeout: 6000,
        });
      });
    },
    cancel() {
      this.open = false;
      this.food = this.$store.state.moduleApp.objectUser.food;
    },
  },
  validations: {
  },
};
</script>

<style scoped>

</style>
