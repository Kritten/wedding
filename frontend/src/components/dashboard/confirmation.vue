<template>
  <v-card>
    <v-card-title>
      {{ $t('confirmation.title') }}
    </v-card-title>
    <v-card-text>
      <v-container pa-0>
        <v-row
          v-if="hasDecided === false"
          no-gutters
        >
          <v-col>
            <v-alert
              dense
              type="warning"
              class="mb-0"
            >
              {{ $t('confirmation.noDecision') }}
            </v-alert>
          </v-col>
        </v-row>
        <v-row
          v-else
          no-gutters
        >
          <v-col>
            <v-alert
              dense
              type="success"
              class="mb-0"
            >
              {{ currentState }}
            </v-alert>
          </v-col>
          <v-col
            align-self="center"
            class="text-center"
            sm="2"
          >
            <v-btn
              text
              color="primary"
              v-on:click="modeEdit = !modeEdit"
            >
              <template v-if="modeEdit === true">
                {{ $t('confirmation.cancel') }}
              </template>
              <template v-else>
                {{ $t('confirmation.edit') }}
              </template>
            </v-btn>
          </v-col>
        </v-row>
        <v-row
          v-if="buttonsEnabled"
          no-gutters
          class="mt-3"
        >
          <v-col>
            <v-row
              v-if="countMax === 1"
              no-gutters
            >
              <v-col>
                <v-btn-toggle
                  v-model="confirmation"
                  style="width: 100%"
                >
                  <v-btn
                    style="width: 50%"
                    color="accent"
                    v-bind:value="1"
                  >
                    {{ $t('confirmation.accept') }}
                    <v-icon
                      right
                      style="color: inherit"
                    >
                      fas fa-check
                    </v-icon>
                  </v-btn>
                  <v-btn
                    style="width: 50%"
                    color="accent"
                    v-bind:value="0"
                  >
                    {{ $t('confirmation.reject') }}
                    <v-icon
                      right
                      style="color: inherit"
                    >
                      fas fa-times
                    </v-icon>
                  </v-btn>
                </v-btn-toggle>
              </v-col>
            </v-row>
            <template v-else />
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
import { ServiceUser } from '../../service/user.service';

export default {
  name: 'Confirmation',
  data() {
    return {
      confirmation: null,
      modeEdit: false,
    };
  },
  computed: {
    buttonsEnabled() {
      return this.countConfirmation === null || this.modeEdit === true;
    },
    hasDecided() {
      return this.$store.state.moduleApp.objectUser.count !== null;
    },
    countConfirmation() {
      return this.$store.state.moduleApp.objectUser.count;
    },
    countMax() {
      return this.$store.state.moduleApp.objectUser.count_max;
    },
    currentState() {
      let result = this.$t('confirmation.currentState');

      result += ': ';
      result += this.countConfirmation === 0 ? this.$t('confirmation.rejected') : this.$t('confirmation.accepted');

      return result;
    },
  },
  watch: {
    async confirmation() {
      await ServiceUser.update({
        count: this.confirmation,
      });

      this.modeEdit = false;
      console.warn('this.confirmation', this.confirmation);
    },
  },
};
</script>

<style scoped>

</style>
