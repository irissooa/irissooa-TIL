import Vue from 'vue';
import VueRouter from 'vue-router';
// import NewsView from '../views/NewsView.vue'
// import AskView from '../views/AskView.vue'
// import JobsView from '../views/JobsView.vue'
import ItemView from '../views/ItemView.vue'
import UserView from '../views/UserView.vue'
// hoc
import createListView from '../views/CreateListView';
import store from '../store/index.js';
import bus from '../utils/bus.js';

Vue.use(VueRouter);
export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/news'
    },
    {
      path: '/news',
      name: 'news',
      component: createListView('NewsView'),
      beforeEnter(routeTo, routeFrom, next) {
        bus.$emit('on:progress');
        bus.$emit('start:spinner');
        store.dispatch('FETCH_LIST', routeTo.name)
          .then(next())
          .catch((() => new Error('failed to fetch news items')));
      },
    },
    {
      path: '/ask',
      name: 'ask',
      component: createListView('AskView'),
      beforeEnter(routeTo, routeFrom, next) {
        bus.$emit('on:progress');
        bus.$emit('start:spinner');
        store.dispatch('FETCH_LIST', routeTo.name)
          .then(next())
          .catch((() => new Error('failed to fetch news items')));
      },
    },
    {
      path: '/jobs',
      name: 'jobs',
      component: createListView('JobsView'),
      beforeEnter(routeTo, routeFrom, next) {
        bus.$emit('on:progress');
        bus.$emit('start:spinner');
        store.dispatch('FETCH_LIST', routeTo.name)
          .then(next())
          .catch((() => new Error('failed to fetch news items')));
      },
    },
    {
      path: '/item/:id',
      component: ItemView,
      beforeEnter(routeTo, routeFrom, next) {
        bus.$emit('on:progress');
        bus.$emit('start:spinner');
        const itemId = routeTo.params.id;
        store.dispatch('FETCH_ITEM', itemId)
          .then(() => next())
          .catch(err => new Error('failed to fetch item details', err));
      },
    },
    {
      path: '/user/:id',
      component: UserView,
      beforeEnter(routeTo, routeFrom, next) {
        bus.$emit('on:progress');
        bus.$emit('start:spinner');
        const itemId = routeTo.params.id;
        store.dispatch('FETCH_USER', itemId)
          .then(() => next())
          .catch(err => new Error('failed to fetch user profile', err));
      },
    }
  ]
})