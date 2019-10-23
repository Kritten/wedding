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

      <v-toolbar-title>Hochzeit</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-content>
  </div>
</template>

<script>
import { ServiceApp } from '../../service/app.service';

export default {
  name: 'AppView',
  data() {
    return {
      drawer: true,
      items: [
        {
          title: this.$i18n.t('dashboard.title'),
          icon: 'mdi-view-dashboard',
          to: { name: 'dashboard' },
        },
        {
          title: this.$i18n.t('events.title'),
          icon: 'mdi-image',
          to: { name: 'events' },
        },
        {
          title: this.$i18n.t('security.logout'),
          icon: 'mdi-logout-variant',
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
