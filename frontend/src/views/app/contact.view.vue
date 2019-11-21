<template>
  <v-row>
    <v-col cols="12" xl="6">
      <v-card class="fill-height">
        <v-card-title>
          {{ $t('contact.title') }}
        </v-card-title>
        <v-card-text>
          <v-container fluid class="pa-0">
            <v-row no-gutters>
              <v-col cols="12" md="6" lg="5" xl="8">
                <v-row>
                  <v-col>Eileen Bartl</v-col>
                  <v-col class="text-right">
                    <v-icon class="pr-3" style="font-size:21px">
                      fas fa-phone
                    </v-icon>
                    <v-icon class="pr-3">
                      fab fa-telegram-plane
                    </v-icon>
                    <v-icon class="pr-3">
                      fab fa-whatsapp
                    </v-icon>
                  </v-col>
                  <v-col class="text-right shrink">
                    <a href="tel:0157/86256167">0157/86256167</a>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>Kristof Komlossy</v-col>
                  <v-col class="text-right">
                    <v-icon class="pr-3" style="font-size:21px">
                      fas fa-phone
                    </v-icon>
                    <v-icon class="pr-3">
                      fab fa-telegram-plane
                    </v-icon>
                    <v-icon class="pr-3">
                      fab fa-whatsapp
                    </v-icon>
                  </v-col>
                  <v-col class="text-right shrink">
                    <a href="tel:0176/20240334">0176/20240334</a>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>E-Mail</v-col>
                  <v-col class="text-right shrink">
                    <a href="mailto:hochzeit@kritten.org">hochzeit@kritten.org</a>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>Adresse</v-col>
                  <v-col class="text-right shrink text-no-wrap">
                    Maximilianstraße 15a, 48147 Münster
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-col>

    <v-col cols="12" xl="6">
      <v-card class="fill-height">
        <v-card-title>
          {{ $t('contact.lappen') }}
        </v-card-title>
        <v-card-text>
          <v-container fluid class="pa-0">
            <v-row no-gutters>
              <v-col cols="12" md="6" lg="5" xl="8">
                <v-row>
                  <v-col>Jo-Anne Bartl</v-col>
                  <v-col class="text-right">
                    <v-icon class="pr-3" style="font-size:21px">
                      fas fa-phone
                    </v-icon>
                    <v-icon class="pr-3">
                      fab fa-telegram-plane
                    </v-icon>
                    <v-icon class="pr-3">
                      fab fa-whatsapp
                    </v-icon>
                  </v-col>
                  <v-col class="text-right shrink">
                    <a href="tel:0152/29958008">0152/29958008</a>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>Johannes Schilling</v-col>
                  <v-col class="text-right">
                    <v-icon class="pr-3" style="font-size:21px">
                      fas fa-phone
                    </v-icon>
                    <v-icon class="pr-3">
                      fab fa-whatsapp
                    </v-icon>
                  </v-col>
                  <v-col class="text-right shrink">
                    <a href="tel:0176/84422642">0176/84422642</a>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Contact',
  methods: {
    foo() {
      console.warn('123', 123);
    }
  }
};
</script>

<style scoped>

</style>
