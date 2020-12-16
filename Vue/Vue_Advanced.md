# Vue-Advanced

[toc]

## Vue_CLI

### Vue_CLI 2.x Vs CLI 3.x

> https://cli.vuejs.org/config/#lintonsave
>
> webpack 2점대에서는 있지만 3점대에 없는 이유는 너무 복잡해서 사용자가 안보이게 내부에서 해결하려고! 그래서 따로 설정을 추가하려면 홈페이지에 들어가서 다른 웹팩 설정방법을 알아야된다
>
> 3버전은 플러그인 기반으로 원하는 기능들을 추가하며 사용할 수 있다(더 유연해짐)
>
> (참고) 뒤에 `;`과 `trailing comma(,)`를 습관처럼 적기! 오류를 최소화!
>
> 3버전에서 ESLint설정 끄는 법 -> `vue.config.js`를 만들어서![image-20201216223343134](Vue_Advanced.assets/image-20201216223343134.png) 이렇게 꺼줌

![image-20201216221741251](Vue_Advanced.assets/image-20201216221741251.png)

## Vue_router

> [Vue.js 중급 ES6 Modules 강좌 링크](https://www.inflearn.com/course/vue-pwa-vue-js-중급/lecture/11542)
>
> [Vue.js 중급 ES6 Enhanced Object Literal 강좌 링크](https://www.inflearn.com/course/vue-pwa-vue-js-중급/lecture/11537)
>
> `views`폴더는 라우터 링크 관련된 컴포넌트만 넣는게 좋다!

```sh
$ npm i vue-router --save
```

- `src` > `routes` > `index.js`

```js
import Vue from 'vue';
import VueRouter from 'vue-router';
import NewsView from '../views/NewsView.vue';
import AskView from '../views/AskView.vue';
import JobsView from '../views/JobsView.vue';
import ItemView from '../views/ItemView.vue';
import UserView from '../views/UserView.vue';

// Vue를 인식하기위해선 import해와야됨
Vue.use(VueRouter);
// vue 라우터 객체
export default new VueRouter({
   // hash값을 제거해줌
  mode: 'history',
  routes: [
    {
      // path는 url에 대한 정보(주소)
      // 기본url!
      path: '/',
      // news로 바로가게함
      // redirect : router기본속성, path가 들어가자마자 redirect(news)로 바로감
      redirect: '/news' 
    },
    {
      path: '/news',
      // url주소로갔을때 표시될 컴포넌트(페이지)
      component: NewsView,
    },
    {
      path: '/ask',
      component: AskView,
    },
    {
      path: '/jobs',
      component: JobsView,
    },
    {
      path: '/item',
      component: ItemView,
    },
    {
      path: '/user',
      component: UserView,
    }
  ]
})
```

- `main.js`

```js
import Vue from 'vue'
import App from './App.vue'
import router from './routes/index.js';

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
// .$mount는 vue인스턴스가 생기고 나서 #app에 마운트 해준다는 뜻!
```

- `App.vue`

```vue
<template>
  <div id="app">
    <!-- router목록을 toobar컴포넌트에 넣음 -->
    <tool-bar></tool-bar>
      <!-- url이 만약 news면 router-view에 news컴포넌트가 들어감! -->
      <!-- url 주소에 따라 해당 컴포넌트가 들어감! -->
    <router-view></router-view>
  </div>
</template>

<script>
import ToolBar from './components/ToolBar.vue';

export default {
  components: {
    ToolBar
  }
}
</script>

<style>
body {
  margin: 0;
}

a {
  color: #34495e;
  text-decoration: none;
}
a:hover {
  color: #42b883;
  text-decoration: underline;
}
/* a router-link-active class */
a.router-link-active {
  text-decoration: underline;
}
</style>

```

- `ToolBar.vue`

```vue
<template>
  <div class="header">
    <img src="../assets/logo.svg" alt="logo" class="logo">
    <router-link to="/news">News</router-link> |
    <router-link to="/ask">Ask</router-link> |
    <router-link to="/jobs">Jobs</router-link>
  </div>
</template>

<style scoped>
.header {
  background-color: #42b883;
  color: white;
  padding: 8px 8px 8px 25px;
  display: flex;
  align-items: center;
}
/* a태그 방문됐을때 */
.header a:visited {
  color: white;
}
/* 헤더 a태그가 active돼있을때 */
.header a:active {
  color: #35495e;
}
.fixed {
  position: fixed;
  width: 100%;
  z-index: 999;
}
.logo {
  width: 30px;
  margin-right: 18px;
}
a {
  margin: 0 5px;
}

</style>
```



## API구현

> [해커 뉴스 API 문서 주소](https://github.com/tastejs/hacker-news-pwas/blob/master/docs/api.md)
>
> [Vue.js 중급 강좌 화살표 함수 강의 링크](https://www.inflearn.com/course/vue-pwa-vue-js-중급/lecture/11534)
>
> [Reactivity in Depth](https://vuejs.org/v2/guide/reactivity.html#ad)Q
>
> axios를 쓸 때 화살표함수를 안쓰면 아래와 같이 this를 따로 변수에 정의해줘야됨
>
> ![image-20201216230621240](Vue_Advanced.assets/image-20201216230621240.png)

```sh
$ npm i axios --save
```

- `src` > `api` > `index.js`

```js
import axios from 'axios';

// const config = {
//   baseURL = 'https://api.hnpwa.com/v0/',
// };
//1. HTTP Request& Response와 관련된 기본 설정
const api = {
  news: 'https://api.hnpwa.com/v0/news/1.json',
  ask: 'https://api.hnpwa.com/v0/ask/1.json',
  jobs: 'https://api.hnpwa.com/v0/jobs/1.json',
  user: 'https://api.hnpwa.com/v0/user/',
  item: 'https://api.hnpwa.com/v0/item/'
};

// 2. API함수들을 정리
function fetchNews() {
  // api의 news url을 가져와서 axios get요청 보냄
  return axios.get(api.news);
  // return axios.get(`${config.baseURL}news.1.json`);
}

function fetchAsk() {
  return axios.get(api.ask);
}

function fetchJobs() {
  return axios.get(api.jobs);
}

function fetchUser(id) {
  const url = `${api.user}${id}.json`;
  return axios.get(url);
}

function fetchItem(id) {
  const url = `${api.item}${id}.json`;
  return axios.get(url);
}

export {
  fetchNews,
  fetchAsk,
  fetchJobs,
  fetchUser,
  fetchItem
}
```

- `NewsView.vue`

```vue
<template>
  <div>
    news
  </div>
</template>

<script>
import { fetchNews } from '../api/index.js';

export default {
  created() {
    fetchNews()
      .then(response => console.log(response))
      .catch(error => console.log(error));
  }
}
</script>

<style>

</style>

```

- `AskView.vue`

```vue
<template>
  <div>
    ask
  </div>
</template>

<script>
import { fetchAsk } from '../api/index.js';

export default {
  // 컴포넌트 생성되자마자 실행 (라이프사이클 훅)
  created() {
    // axios의 결과로 promise가 return됨, 그래서 .then,.catch사용가능
    fetchAsk()
      .then(response => console.log(response))
      .catch(error => console.log(error));
  }
}
</script>

<style>

</style>
```



### (참고) this

> JS는 기본적으로 전역(`window`)으로 변수가 시작함
>
> 예시) this
>
> 1. ![image-20201216232540109](Vue_Advanced.assets/image-20201216232540109.png)
> 2. ![image-20201216232612516](Vue_Advanced.assets/image-20201216232612516.png)
>
> 이렇게 this는 함수에서도 전역에서도 window를 가리킴
>
> 하지만 여기 `Vue`라는 함수의 this는 함수자체를 가리킴
>
> 3. ![image-20201216232713050](Vue_Advanced.assets/image-20201216232713050.png)
> 4. ![image-20201216232854359](Vue_Advanced.assets/image-20201216232854359.png)![image-20201216232910888](Vue_Advanced.assets/image-20201216232910888.png)
>
> 4번의 this는 호출전에는 Vue를 가리키지만, 호출 후에는 undefined! why??
>
> 비동기호출을 할때는 현재 위치에서 벗어난 this가 생김! 그래서 특히 callback함수에서! 그래서 this가 처리 후에는 undefined가 되는것, 그래서 이럴때 this를 변수에 담아줘서 쓰던가, 화살표함수로 사용한다! 그러면 뷰의 this가 됨!



### Callback

> 인자로 전달되는 함수
>
>  [비동기 처리와 콜백 함수](https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/)

![image-20201216233515948](Vue_Advanced.assets/image-20201216233515948.png)

이렇게 callback함수를 ajax로 데이터 요청하고나서 요청한동안 3번이 먼저 찍히고, 성공한 2번이 찍히게됨 

![image-20201216233505495](Vue_Advanced.assets/image-20201216233505495.png)

이럴때 비동기처리가 필요하다!, 그렇기때문에 Promise가 등장함

### Promise

>  [프로미스 쉽게 이해하기 글 주소](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)
>
> [Promise MDN 주소](https://developer.mozilla.org/ko-KR/docs/Web/JavaScript/Reference/Global_Objects/Promise)
>
> Promise객체가 .then, .catch를 쓸 수 있음

![image-20201216234121543](Vue_Advanced.assets/image-20201216234121543.png)

callAjax는 Promise객체를 반환해서 ajax가 성공한 결과가 resolve(data)에 담기게 되고 그게 .then의 data로 들어가게됨!



## Vuex

> Vuex를 거쳐서 newView로 data를 보냄
>
> 여러컴포넌트간 data를 조작하기 위해 store에 data를 관리하고 그것을 가져와 쓸 수 있게 한다. 
>
> \- [Vue.js 중급 강좌 Vuex 강의 링크](https://www.inflearn.com/course/vue-pwa-vue-js-중급/lecture/11544)
>
> \- [Vuex Data Flow](https://vuex.vuejs.org/)
>
> \- [ES6 Destructuring 설명 글(e북)](https://joshua1988.github.io/es6-online-book/destructuring.html)
>
> ![image-20201216235116663](Vue_Advanced.assets/image-20201216235116663.png)

![image-20201216234338174](Vue_Advanced.assets/image-20201216234338174.png)

```sh
//dependencies에 vuex가 들어감
$ npm i vuex
```

- main.js에 store를 만들어도되지만 그러면 너무 복잡해지고 main.js는 전체를 그려주는데 본질을 흐리게됨, 관리하기 편하게 하기위해 `store` >`index.js`파일을 만들어 넣어줌

```js
//main.js
import Vue from 'vue'
import App from './App.vue'
import router from './routes/index.js';
import store from './store/index.js';

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

```

### Vuex 분리

- `store` > `index.js`

```js
import Vue from 'vue';
import Vuex from 'vuex';
import getters from './getters.js';
import mutations from './mutations.js';
import actions from './actions.js';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state: {
    news: [],
    ask: [],
    jobs: [],
    user: {},
    item: {}
  },
  getters,
  mutations,
  actions,
})
```

- `store` > `actions.js`

```js
import {
  fetchNews,
  fetchAsk,
  fetchJobs,
} from '../api/index.js';

 
export default {
  // 이렇게 {commit}을 인자로 하면 context.commit이라고 안적어도됨
  // {data} === response.data와 같은원리
  FETCH_NEWS({ commit }) {
    // respnse.data를 state에 담고싶다. 하지만 vuex구조상, api에서 불러온 데이터를 actions에서(비동기호출) 호출하고 -> 그 data를 꺼내서 바로 state에 넣고싶지만, mutation을 지나서 state에 넣어주게끔 되어있다
    // 그래서 commit으로 SET_NEWS라는 mutations을 호출하고, response.data를 인자로 보냄
    return fetchNews().then(response => commit('SET_NEWS', response.data));
    // return fetchNews().then({data} => commit('SET_NEWS', data));
  },
  FETCH_ASK({ commit }) {
    return fetchAsk().then(response => commit('SET_ASK', response.data));
  },
  FETCH_JOBS({ commit }) {
    return fetchJobs().then(response => commit('SET_JOBS', response.data));
  },
}
```

- `store` > `mutations.js`

```js
export default {
  // 첫번째인자는 state
  SET_NEWS(state, news) {
    // data로 넘어온것을 state에 저장해줌
    state.news = news;
  },
  SET_ASK(state, ask) {
    state.ask = ask;
  },
  SET_JOBS(state, jobs) {
    state.jobs = jobs;
  }
}
```

- `NewsView.vue`

```vue
<template>
  <div>
    <!-- store에서 state에저장된 news를 가져옴 -->
    <p v-for="news in this.$store.state.news" :key="news.id">
      <a :href="news.url">{{ news.title }}</a><br>
      <small>{{ news.time_ago }} by {{ news.domain }}</small>
    </p>
  </div>
</template>

<script>
export default {
  created() {
    // FETCH_NEWS라는 actions호출
    this.$store.dispatch('FETCH_NEWS')
    // axios결과 promise가반환되고 성공하면.then으로, 실패헤면 error를 .catch로 가져감
      .then(() => console.log('success'))
      .catch(() => console.log('fail'));
  }
}
</script>

<style>

</style>

```

