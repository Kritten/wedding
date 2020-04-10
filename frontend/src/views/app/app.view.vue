<template>
  <div v-if="$store.state.moduleApp.isLoggedIn === true">
    <v-navigation-drawer
      v-model="drawer"
      clipped
      app
    >
      <v-list
        dense
        nav
      >
        <template
          v-for="item in items"
        >
          <v-divider
            v-if="item.separated === true"
            v-bind:key="`${item.title}-divider`"
          />
          <v-list-item
            v-bind:key="item.title"
            link
            v-bind="item.to !== undefined ? { to: item.to} : {}"
            exact
            v-on="item.click !== undefined ? { click: item.click } : {}"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      fixed
      clipped-left
      color="secondary"
    >
      <v-app-bar-nav-icon v-on:click.stop="drawer = !drawer" />

      <v-toolbar-title>Hochzeit von Eileen und Kristof</v-toolbar-title>
      <v-spacer />
      <the-countdown />
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <info-postponed />
        <router-view />
      </v-container>
    </v-content>
  </div>
</template>

<script>
import { ServiceApp } from '../../service/app.service';
import TheCountdown from '../../components/dashboard/the-countdown';
import InfoPostponed from '../../components/info-postponed';

export default {
  name: 'AppView',
  components: {
    InfoPostponed,
    TheCountdown,
  },
  data() {
    return {
      drawer: null,
      items: [
        {
          title: this.$i18n.t('dashboard.title'),
          icon: 'fas fa-fw fa-tachometer-alt',
          to: { name: 'dashboard' },
        },
        {
          title: this.$i18n.t('events.title'),
          icon: 'fas fa-fw fa-calendar',
          to: { name: 'events' },
        },
        {
          title: this.$i18n.tc('games.title', 2),
          icon: 'fas fa-fw fa-dice',
          to: { name: 'games' },
        },
        {
          title: this.$i18n.t('contact.title'),
          icon: 'fas fa-fw fa-address-card',
          to: { name: 'contact' },
        },
        {
          title: this.$i18n.t('security.logout'),
          icon: 'fas fa-fw fa-sign-out-alt',
          separated: true,
          click: () => {
            ServiceApp.logout();
          },
        },
      ],
    };
  },
};
</script>

<style scoped>

</style>
