import { ServiceEndpoint } from './endpoint.service';
import { Queue } from '../queue';
import { store } from '../store/vuex';

class ClassServiceApp {
  async init() {
    ServiceEndpoint.init();

    this.loadConfig();
  }

  async login({ username, password }) {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: 'login',
      },
      method: 'post',
      data: {
        username,
        password,
      },
    });

    if (response.success === true) {
      const responseConfig = await this.loadConfig();
      if (responseConfig.success === true) {
        Queue.notify('router', { name: 'dashboard' });
      }
    } else if (response.exception.response.status === 400) {
      console.warn('wrong credentials');
      return false;
    }
  }

  async logout() {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: 'logout',
      },
      method: 'post',
    });

    if (response.success === true) {
      Queue.notify('router', { name: 'login' });
    }
  }

  async loadConfig() {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: 'config',
      },
      method: 'get',
    });

    if (response.success === true) {
      await store.dispatch('moduleApp/init', response.data);

      await this.loadUser();

      store.commit('moduleApp/setState', {
        nameState: 'isInitialized',
        objectState: true,
      });
      store.commit('moduleApp/setState', {
        nameState: 'isLoggedIn',
        objectState: true,
      });
    }

    return response;
  }

  async loadUser() {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: store.state.moduleApp.objectUrls.user,
      },
      method: 'get',
    });

    store.commit('moduleApp/setState', {
      nameState: 'objectUser',
      objectState: response.data,
    });
  }
}
export const ServiceApp = new ClassServiceApp();
