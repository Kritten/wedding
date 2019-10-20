<template>
  <v-content>
    <v-container class="fill-height">
      <v-row
        align="center"
        justify="center"
        class="fill-height"
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
                >
                  {{ $t('security.login') }}
                </v-btn>
              </form>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
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
    login() {
      ServiceApp.login({
        username: this.username,
        password: this.password,
      });
    },
  },
};
</script>

<style scoped>

</style>
