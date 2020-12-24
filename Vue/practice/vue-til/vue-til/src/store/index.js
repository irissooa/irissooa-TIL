import Vue from 'vue';
import Vuex from 'vuex';
// cookie.js의 함수들을 모두 가져와 store에 저장함
import {
  getAuthFromCookie,
  getUserFromCookie,
  saveAuthToCookie,
  saveUserToCookie,
} from '@/utils/cookies';
import { loginUser } from '@/api/index';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: getUserFromCookie() || '',
    token: getAuthFromCookie() || '',
  },
  getters: {
    isLogin(state) {
      return state.username !== '';
    },
  },
  mutations: {
    setUsername(state, username) {
      state.username = username;
    },
    clearUsername(state) {
      state.username = '';
    },
    setToken(state, token) {
      state.token = token;
    },
  },
  actions: {
    // loginForm에서 컴포넌트단에 너무 코드가 복잡해지는 것을 막기위해 actions활용(해도되고 loginform에 그냥 적어도됨)
    // 비동기처리 async await
    // LOGIN을 dispatch로 호출할때 userData를 받아옴,
    async LOGIN({ commit }, userData) {
      const { data } = await loginUser(userData);
      console.log(data.token);
      // this.$store은 안적어도됨! store안이니까 commit만 적으면됨!
      commit('setToken', data.token);
      commit('setUsername', data.user.username);
      saveAuthToCookie(data.token);
      saveUserToCookie(data.user.username);
      //  async는 무조건 Promise를 return, 하지만 나중에 활용될수 있는 data를 위해 data를 return!안넣어도 promise가 return돼서 안적어줘도됨!
      return data;
    },
  },
});
