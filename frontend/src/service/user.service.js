import { ServiceEndpoint } from './endpoint.service';
import { store } from '../store/vuex';

class ClassServiceUser {
  async update(user) {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: store.state.moduleApp.objectUrls.user,
      },
      method: 'put',
      data: user,
    });

    if (response.success === true) {
      store.commit('moduleApp/setState', {
        nameState: 'objectUser',
        objectState: response.data,
      });
    }
  }
}
export const ServiceUser = new ClassServiceUser();
