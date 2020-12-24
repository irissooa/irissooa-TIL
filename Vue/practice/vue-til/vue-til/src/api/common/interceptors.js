import store from '@/store/index';

export function setInterceptors(instance) {
  instance.interceptors.request.use(
    function(config) {
      // Do something before request is sent
      //요청을 보내기전에 특정 코드를 넣을 수 있음
      config.headers.Authorization = store.state.token;
      return config;
    },
    function(error) {
      // Do something with request error
      //그 요청이 실패했을 때 error를 화면에 보이기 전에 처리할 수 있음
      return Promise.reject(error);
    },
  );

  // Add a response interceptor
  instance.interceptors.response.use(
    function(response) {
      // Any status code that lie within the range of 2xx cause this function to trigger
      //응답을 받기전에 처리를 할 수 있고
      // Do something with response data
      return response;
    },
    function(error) {
      // Any status codes that falls outside the range of 2xx cause this function to trigger
      //에러가 났을 경우 전처리를 할 수 있다
      // Do something with response error
      return Promise.reject(error);
    },
  );
  return instance;
}
