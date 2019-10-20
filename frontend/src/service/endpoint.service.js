import axios from 'axios';
import { Queue } from '../queue';
import { store } from '../store/vuex';

class ClassServiceEndpoint {
  constructor() {
    this.isInitialized = false;
    this.axios = null;
    this.urlBase = process.env.VUE_APP_URL_BASE;
  }

  init(force = false) {
    if (this.isInitialized === true && force === false) {
      console.error('Service Endpoint is already initialized!');
      return;
    }

    this.isInitialized = true;

    this.axios = axios.create({
      withCredentials: true,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  async makeRequest({
    url, method, data, params, options, withCredentials,
  }) {
    const config = {
      method,
      url: this.getUrlApi(url),
      data: JSON.stringify(data),
      params,
      ...options,
      withCredentials,
    };

    const objectResponse = {
      success: undefined,
      response: undefined,
      exception: undefined,
      data: undefined,
    };

    try {
      objectResponse.response = await this.axios.request(config);

      objectResponse.success = true;
      objectResponse.data = objectResponse.response.data;
    } catch (exception) {
      objectResponse.exception = exception;
      objectResponse.success = false;
    }

    if (objectResponse.success === false) {
      if (objectResponse.exception.response.status === 403) {
        store.commit('moduleApp/setState', {
          nameState: 'isInitialized',
          objectState: true,
        });
        Queue.notify('router', { name: 'login' });
      }
    }

    return objectResponse;
  }

  getUrlApi({
    host,
    path = '',
    value,
  }) {
    // TODO: Fix this approach
    // let url = new URL(path, store.state.module_app.url_api);

    let url;
    if (host !== undefined) {
      url = `${host}/${path}`;
    } else {
      url = `${this.urlBase}/${path}`;
    }

    if (value !== undefined) {
      url += `/${value}`;
    }

    return url;
  }
}

export const ServiceEndpoint = new ClassServiceEndpoint();
