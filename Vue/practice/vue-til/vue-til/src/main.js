import Vue from 'vue';
import App from './App.vue';
import router from '@/routes/index';
import store from '@/store/index';

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app');
