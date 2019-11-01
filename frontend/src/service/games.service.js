import { ServiceEndpoint } from './endpoint.service';
import { store } from '../store/vuex';

class ClassServiceGames {
  async loadGames({ page }) {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: store.state.moduleApp.objectUrls.games,
      },
      method: 'get',
      params: {
        page: page,
        page_size: 20,
        sort_by: 'title',
        descending: false,
      },
    });

    store.commit('moduleGames/setState', {
      nameState: 'countGames',
      objectState: response.data.items_total,
    });

    console.warn('[...store.state.moduleGames.arrayGames, ...response.data.data]', [...store.state.moduleGames.arrayGames, ...response.data.data]);
    store.commit('moduleGames/setState', {
      nameState: 'arrayGames',
      objectState: [...store.state.moduleGames.arrayGames, ...response.data.data],
    });
  }
}
export const ServiceGames = new ClassServiceGames();
