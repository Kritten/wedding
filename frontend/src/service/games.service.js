import cloneDeep from 'lodash-es/cloneDeep';
import { ServiceEndpoint } from './endpoint.service';
import { store } from '../store/vuex';

class ClassServiceGames {
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

    return result;
  }
}
export const ServiceGames = new ClassServiceGames();
