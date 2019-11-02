import { ServiceEndpoint } from './endpoint.service';
import { store } from '../store/vuex';
import cloneDeep from 'lodash-es/cloneDeep';

class ClassServiceGames {
  async loadGames({ page, initialize, filters }) {
    const filtersCopy = cloneDeep(filters);
    if (filtersCopy.count_players_max !== undefined && filtersCopy.count_players_max === 10) {
      filtersCopy.count_players_max = 10000;
    }

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
        ...filtersCopy,
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
}
export const ServiceGames = new ClassServiceGames();
