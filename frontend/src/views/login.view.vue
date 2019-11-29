<template>
  <v-content>
    <v-container class="fill-height">
      <v-row
        align="center"
        justify="center"
        class="fill-height"
      >
        <v-col>
          <v-row
            no-gutters
          >
            <v-col cols="12">
              <v-row
                no-gutters
                justify="center"
              >
                <v-col
                  cols="12"
                  lg="5"
                >
                  <v-alert
                    outlined
                    color="primary"
                    class="text-center"
                  >
                    <div>Die Zugangsdaten befinden sich auf der Rückseite der "Infos"-Karte der Einladung</div>
                  </v-alert>
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <v-row
            no-gutters
            justify="center"
          >
            <v-col
              xs="12"
              lg="4"
            >
              <v-row>
                <v-col class="text-center">
                  <form
                    v-on:submit.prevent="login"
                  >
                    <v-text-field
                      ref="username"
                      v-model="username"
                      v-bind:label="$t('security.username')"
                    />
                    <v-text-field
                      v-model="password"
                      type="password"
                      v-bind:label="$t('security.password')"
                    />
                    <v-btn
                      color="primary"
                      type="submit"
                      v-bind:disabled="$v.$invalid"
                    >
                      {{ $t('security.login') }}
                    </v-btn>
                  </form>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import { required } from 'vuelidate/lib/validators';
import { ServiceApp } from '../service/app.service';

export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    };
  },
  mounted() {
    this.$refs.username.focus();
  },
  methods: {
    async login() {
      const result = await ServiceApp.login({
        username: this.username,
        password: this.password,
      });

      if (result === false) {
        this.$store.dispatch('moduleApp/openSnackbar', {
          text: this.$i18n.t('security.wrongCredentials'),
          color: 'error',
        });
      }
    },
  },
  validations: {
    username: {
      required,
    },
    password: {
      required,
    },
  },
};
</script>

<style scoped>

</style>
