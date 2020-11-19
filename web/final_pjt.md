# final_pjt

[toc]

## 20201119

> 온갖 에러를 다 본 날......ㅎ

### 문제1. router 

- router를 깔았는데 `main.js`에 router가 import 되어있지 않아서 오류가 났다
- `npm install router` -> `vue add router`도 했는데 왜 안적혀있을깡....

```js
import Vue from 'vue'
import App from './App.vue'
// router등록하려면 적혀있어야됨
import router from './router'

Vue.config.productionTip = false

new Vue({
  // router등록하려면 적혀있어야됨
  router,
  render: h => h(App),
}).$mount('#app')
```

- 

