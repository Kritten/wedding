import axios from 'axios';

class ClassServiceEndpoint {
  constructor() {
    this.is_initialized = false;
    this.axios = undefined;
    this.urlBase = 'http://localhost:8000';
  }

  init(force = false) {
    if (this.is_initialized === true && force === false) {
      console.error('Service Endpoint is already initialized!');
      return;
    }

    this.is_initialized = true;

    this.axios = axios.create({
      headers: {
        // Authorization: `Token ${store.state.module_app.token_instance}`,
        'Content-Type': 'application/json',
      },
    });
  }

  async makeRequest({
    url, method, data, params, options,
  }) {
    const config = {
      method,
      url: this.getUrlApi(url),
      data: JSON.stringify(data),
      params,
      ...options,
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

    // if (objectResponse.success === false) {
    //   // only send to connection_error if its an request to the api
    //   if (objectResponse.exception.message === 'Network Error' && url.host === undefined) {
    //     queue.notify('router', { name: 'connection_error' });
    //   } else {
    //     console.warn('Error', objectResponse.exception);
    //     // queue.notify('router', { name: 'connection_error' });
    //   }
    // }

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
