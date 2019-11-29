<template>
  <v-card class="fill-height">
    <v-card-title>
      {{ $t('confirmation.title') }}
    </v-card-title>
    <v-card-text>
      <v-container
        fluid
        pa-0
      >
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
            class="text-md-center"
            cols="12"
            md="2"
          >
            <v-btn
              text
              color="primary"
              class="pl-0 pl-md-4"
              v-on:click="modeEdit = !modeEdit"
            >
              <template v-if="modeEdit === true">
                {{ $t('common.cancel') }}
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
            >
              <v-col
                class="py-0"
              >
                <v-btn
                  color="primary"
                  v-bind:value="1"
                  block
                  v-on:click="updateConfirmation(1)"
                >
                  {{ $t('confirmation.accept') }}
                  <v-icon
                    right
                    style="color: inherit"
                  >
                    fas fa-check
                  </v-icon>
                </v-btn>
              </v-col>
              <v-col
                class="py-0"
              >
                <v-btn
                  color="primary"
                  v-bind:value="0"
                  block
                  v-on:click="updateConfirmation(0)"
                >
                  {{ $t('confirmation.reject') }}
                  <v-icon
                    right
                    style="color: inherit"
                  >
                    fas fa-times
                  </v-icon>
                </v-btn>
              </v-col>
            </v-row>
            <v-row
              v-else
              dense
            >
              <v-col
                cols="12"
                md="6"
                class="py-0"
              >
                <v-row
                  dense
                >
                  <v-col
                    cols="12"
                    md="2"
                    class="py-md-0"
                  >
                    <v-select
                      v-model="count"
                      v-bind:items="arrayItems"
                      hide-details
                      dense
                    />
                  </v-col>
                  <v-col
                    class="py-md-0"
                  >
                    <v-btn
                      color="primary"
                      v-bind:value="1"
                      block
                      v-bind:disabled="count === 0"
                      v-on:click="updateConfirmation(count)"
                    >
                      {{ $tc('confirmation.acceptWith', count) }}
                      <v-icon
                        right
                        style="color: inherit"
                      >
                        fas fa-check
                      </v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
              </v-col>

              <v-col
                cols="12"
                md="4"
                class="py-0"
              >
                <v-btn
                  color="primary"
                  v-bind:value="0"
                  block
                  v-on:click="updateConfirmation(0)"
                >
                  {{ $t('confirmation.reject') }}
                  <v-icon
                    right
                    style="color: inherit"
                  >
                    fas fa-times
                  </v-icon>
                </v-btn>
              </v-col>
            </v-row>
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
      modeEdit: false,
      count: 1,
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
    arrayItems() {
      return [...Array(this.countMax)].map((value, index) => index + 1);
    },
    countMax() {
      return this.$store.state.moduleApp.objectUser.count_max;
    },
    currentState() {
      let result = this.$t('confirmation.currentState');

      result += ': ';

      switch (this.countConfirmation) {
        case 0:
          result += this.$t('confirmation.rejected');
          break;
        case 1:
          result += this.countMax === 1 ? this.$t('confirmation.accepted') : this.$tc('confirmation.acceptedWith', 1);
          break;
        default:
          result += this.$tc('confirmation.acceptedWith', this.countConfirmation);
          break;
      }

      return result;
    },
  },
  created() {
    const { count } = this.$store.state.moduleApp.objectUser;
    this.count = count !== null && count > 1 ? count : 1;
  },
  methods: {
    async updateConfirmation(count) {
      await ServiceUser.update({
        count,
      });

      this.modeEdit = false;

      this.$store.dispatch('moduleApp/openSnackbar', {
        text: this.$i18n.t('confirmation.message.changed'),
      });
    },
  },
};
</script>

<style scoped>

</style>
