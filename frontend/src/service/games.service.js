import cloneDeep from 'lodash-es/cloneDeep';
import { ServiceEndpoint } from './endpoint.service';
import { store } from '../store/vuex';

class ClassServiceGames {
  constructor() {
    this.arrayPlaytimes = [
      {
        minutes: 0,
        label: '0',
      },
      {
        minutes: 10,
        label: '10m',
      },
      {
        minutes: 20,
        label: '20m',
      },
      {
        minutes: 40,
        label: '40m',
      },
      {
        minutes: 60,
        label: '1h',
      },
      {
        minutes: 90,
        label: '1.5h',
      },
      {
        minutes: 120,
        label: '2h',
      },
      {
        minutes: 180,
        label: '3h',
      },
      {
        minutes: 240,
        label: '4h',
      },
      {
        minutes: 300,
        label: '5h',
      },
    ];
  }

  async loadGames({ page, initialize, filters }) {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: store.state.moduleApp.objectUrls.games,
      },
      method: 'get',
      params: {
        page,
        page_size: 20,
        sort_by: 'title',
        descending: false,
        ...this.generateFilters(filters),
      },
    });

    store.commit('moduleGames/setState', {
      nameState: 'countGames',
      objectState: response.data.items_total,
    });

    store.commit('moduleGames/setState', {
      nameState: 'arrayGames',
      objectState: initialize === true ? response.data.data : [...store.state.moduleGames.arrayGames, ...response.data.data],
    });
  }

  generateFilters(filters) {
    const result = {};
    for (const { active, parts } of Object.values(filters)) {
      if (active === true) {
        for (const [key, value] of Object.entries(parts)) {
          result[key] = value;
        }
      }
    }

    if (result.count_players_max !== undefined && result.count_players_max === 10) {
      result.count_players_max = 10000;
    }

    if (result.minutes_playtime_min !== undefined) {
      result.minutes_playtime_min = this.arrayPlaytimes[result.minutes_playtime_min].minutes;
    }
    if (result.minutes_playtime_max !== undefined) {
      result.minutes_playtime_max = this.arrayPlaytimes[result.minutes_playtime_max].minutes;
    }

    return result;
  }
}
export const ServiceGames = new ClassServiceGames();
