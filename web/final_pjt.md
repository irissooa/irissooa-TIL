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



### summernote

> [Summernote](https://summernote.org/getting-started/#requires-html5-doctype) 이거 구현...이따 시간나면 해보자...ㅠ 안된당....퓨

```css
<!-- include libraries(jQuery, bootstrap) -->
<link href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet">
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

<!-- include summernote css/js -->
<link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.js"></script>
```



## 20201120

### User오류 왜 자꾸 날까?

> 로그인도 되고, User db에도 데이터가 있는데 CreateReview를 하려고 하면 자꾸 User가 Anonymous라고 뜬다....ㅠ

![image-20201121000643977](final_pjt.assets/image-20201121000643977.png)

![image-20201121000654375](final_pjt.assets/image-20201121000654375.png)

![image-20201121000801548](final_pjt.assets/image-20201121000801548.png)



### package.json

> ![image-20201121000815294](final_pjt.assets/image-20201121000815294.png)

```json
{
  "name": "todo-vue-cli",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint"
  },
  "dependencies": {
    "core-js": "^3.3.2",
    "vue": "^2.6.10"
  },
  "devDependencies": {
    "@vue/cli-plugin-babel": "^4.0.0",
    "@vue/cli-plugin-eslint": "^4.0.0",
    "@vue/cli-service": "^4.0.0",
    "babel-eslint": "^10.0.3",
    "eslint": "^5.16.0",
    "eslint-plugin-vue": "^5.0.0",
    "vue-template-compiler": "^2.6.10"
  },
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "rules": {},
    "parserOptions": {
      "parser": "babel-eslint"
    }
  },
  "postcss": {
    "plugins": {
      "autoprefixer": {}
    }js
  },
  "browserslist": [
    "> 1%",
    "last 2 versions"
  ]
}
```

------

- `npm init`으로 설정을 모두 완료하면 `package.json`이 새로 생긴다.
- 또는 vue-cli 모듈 설치 후 vue 프로젝트를 생성(ex. `vue create todo-vue-cli`)하면 `package.json` 파일이 생긴다.

1. `name`

- 프로젝트의 이름을 적는 곳
- 만약 node package에 직접 만든 패키지를 등록하려고 한다면 version과 마찬가지로 필수 입력해줘야 한다.
- 다만 그렇지 않다면 해당 값은 선택값이다.
- `version` 과 `name`은 함께 해당 프로젝트의 `unique`한 값이다.
- `name`은 점(.)이나 언더스코어(_)로 시작될 수 없고 대문자를 포함하면 안 된다.

2. `version`

- 만약 해당 모듈을 npm에 올릴 계획이 있다면 `name`과 `version`은 필수인자이다.
- 다만 그렇지 않다면 해당 값은 선택값이다.

3. `private`

- 만약 해당 옵션을 `true`로 설정한다면, 해당 모듈을 npm에 올릴 수 없다.
- 개발자가 실수로 private한 모듈을 올리더라도 올린 모듈에 대해 배포를 막을 수 있는 방법 중 하나이다.

4. `scripts`

- 패키지의 다양한 생명주기 동안 실행되는 명령어를 포함하고 있다.
- key는 생명주기 이벤트를 나타내면, value는 해당 생명주기에 실행되는 명령어를 나타낸다.
- 개발자가 직접 정의한 script의 경우, run과 함께 사용하면 되고, 기본적으로 npm에서 제공되는 명령어는 그냥 해당 명령어만 실행시켜주면 된다.

5. `devDependencies`

- 이 안에 있는 모듈들은 프로젝트의 루트에서 `npm install` 이나 `npm link`를 실행하게 되면 설치 된다.

6. `description`

- 프로젝트에 대한 설명을 문자열로 입력
- `npm search` 명령어를 사용했을 때, 사람들로 하여금 해당 모듈을 찾을 수 있게 도와준다.

7. `Author`

```json
{
  "author": {
    "name" : "Martin",
    "email" : "martin@within.com",
    "url" : "http://blog.martinwork.co.kr/"
  }
}
```

- 해당 값은 한 명의 사람에 대해서 나타낸다.
- 대신 `contributors` 값은 array 형태로 여려 명을 기입할 수 있다.
- 그리고 그 하나의 Person에 대해서는 name을 입력할 수 있으며, 선택값으로 email과 url을 입력할 수 있다.

8. `license`

- 해당 모듈에 대한 라이센스에 대한 정보를 기술하는 영역
- 해당 모듈이 npm에 올라갔을 경우 해당 모듈을 사용할 수 있는 권한에 대한 내용을 기술하는 영역

9. `browserslist`

```json
{
"browserslist": [
    "> 1%",
    "last 2 versions",
    "not ie <= 8"
  ]
}
```

- `browserslist` 라이브러리에 대한 옵션으로서, 서로 다른 front-end 둘 간에 브라우저의 타겟을 공유하기 위해 사용한다.
- 위의 예시와 같은 경우 다음을 의미한다.
  - 전 세계 사용 통계 속에서 상위 1% 이상 선택(사용)된 브라우저
  - 각 브라우저의 최신 버전 2개
  - Internet Explorer 8 이하의 버전은 호환하지 않음



### Webpack

> [출처](https://github.com/wally-wally/TIL/blob/master/07_vue/%5BSSAFY%5DVue_%231.md)

> | 요소    | 내용                                                         |
> | ------- | ------------------------------------------------------------ |
> | entry   | 여러 js 파일들의 시작점 => 웹팩이 파일을 읽어 들이기 시작하는 부분전체 애플리케이션 설치, 필요 라이브러리를 로딩하는 로직을 포함웹팩으로 빌드(변환)할 대상 파일을 지정 |
> | module  | 웹팩은 JS 만 변환 가능하기 때문에 HTML, CSS 등은 모듈을 통해서 웹팩이 이해할 수 있도록 변환이 필요하다.변환 내용을 담는 곳 |
> | plugins | 웹팩을 통해 번들된 결과물을 추가로 처리하는 부분ex) 결과물의 사이즈를 줄이거나 결과물(기본적으로 JS)을 기타 CSS, HTML 파일로 분리하는 기능 등이 있음 |
> | output  | 여러 js 파일을 **하나로 만들어 낸 결과물**결과물의 위치, 파일명 등 세부 옵션을 설정 |

- `webpack.config.js`

  ```json
  // webpack 설정 파일
  const VueLoaderPlugin = require('vue-loader/lib/plugin')
  const path = require('path')
  
  module.exports = {
    entry: {
      // __dirname : 최상위 위치(entry point) - Django 에서 BASE_DIR 역할과 동일
      // 여기서 __dirname은 '02_vue_webpack'이다.
      app: path.join(__dirname, 'src', 'main.js')
      // 경로 설정 (src(entry의 시작 파일)는 vue-cli의 기본값임)
      // main.js가 entry 역할을 한다.
    },
    module: {
      rules: [ // rules는 배열로 선언
        {
          test: /\.vue$/, // 정규 표현식 : '.vue' 확장자를 가진 모든 파일을 test 한다는 의미
          use: 'vue-loader',
        }
      ]
    },
    plugins: [ // plugins는 배열로 선언
      new VueLoaderPlugin(),
    ],
    output: {
      filename: 'app.js',
      path: path.join(__dirname, 'dist'), // (dist는 vue-cli의 기본값임)
    },
  }
  ```

- `package.json`

  ```json
  {
    "name": "02_vue_webpack",
    "version": "1.0.0",
    "description": "",
    "main": "module.js",
    "scripts": {
      "build": "webpack" // 기존의 test 구문 삭제
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "vue": "^2.6.10"
    },
    "devDependencies": {
      "vue-loader": "^15.7.2",
      "vue-template-compiler": "^2.6.10",
      "webpack": "^4.41.2",
      "webpack-cli": "^3.3.10"
    }
  }
  ```

- `src` > `main.js`

  `main.js`가 entry 역할을 한다.

  ```js
  // Vue 인스턴스를 최종으로 만드는 파일
  
  // 1. 설치된 vue를 추가
  // (내가 만든 파일 아닌 경우) 현재 위치에서 vue 이름을 가진 폴더가 없음 => 자동으로 node_modules 에서 가져옴
  import Vue from 'vue'
  
  // 2. 최상위 컴포넌트 추가(App.vue)
  // (내가 만든 파일인 경우) 상대 경로 표시를 해야 함
  import App from './App.vue'
  
  new Vue({
    render: h => h(App)// 보통 createElement를 h로 줄인다.
  }).$mount('#app') // .$mount('#app')는 el: '#app'과 유사한 역할 수행
  ```

- `App.vue`

  ```vue
  <template>
    <h1>여기는 최상위 컴포넌트 입니다.</h1>
  </template>
  
  <script>
  
  </script>
  
  <style>
  
  </style>
  ```

- `npm install vue-loader vue-template-compiler -D`

  - 웹팩은 js 코드만 이해 가능하기 때문에 vue파일(`vue-loader`) 및 html, css 파일(`vue-template-compiler`) 등을 변환하기 위하여 모듈을 설치

- `npm run build` : webpack 만드는 구문

- `dist` 폴더가 새로 생기고 이 안에 `app.js` 파일이 생성됨을 볼 수 있다.

- `public` > `index.html`

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  </head>
  <body>
    <div id="app">
  
    </div>
    <script src="../dist/app.js">
  
    </script>
  </body>
  </html>
  ```

- 하지만 현재 상황에서 chrome 에서 vue 창을 열 수 없다. 그래서 `webpack.config.js`에 `mode: 'development',`를 추가하고 다시 `npm run build`를 수행하면 chorme 창에서 vue 창을 볼 수 있다.

  ```js
  // webpack.config.js
  
  module.exports = {
    mode: 'development',
    entry: {
      ...
    }
    ...
  }
  ```



### router 컴포넌트에 props전달

> [참고문헌](https://router.vuejs.org/kr/guide/essentials/passing-props.html)
>
> 컴포넌트에서 `$route`를 사용하면 특정 URL에서만 사용할 수 있는 컴포넌트의 유연성을 제한하는 라우트와 강한 결합을 만든다.
>
> 컴포넌트와 라우터 속성을 분리하려면 다음과 같이 하십시오.
>
> **$route에 의존성 추가**
>
> ```js
> const User = {
>   template: '<div>User {{ $route.params.id }}</div>'
> }
> const router = new VueRouter({
>   routes: [
>     { path: '/user/:id', component: User }
>   ]
> })
> ```
>
> **속성에 의존성 해제**
>
> ```js
> const User = {
>   props: ['id'],
>   template: '<div>User {{ id }}</div>'
> }
> const router = new VueRouter({
>   routes: [
>     { path: '/user/:id', component: User, props: true },
>   ]
> })
> ```
>
> 이를 통해 어디서나 컴포넌트를 사용할 수 있으므로 컴포넌트 재사용 및 테스트하기가 더 쉽습니다.
>
> ### Boolean 모드
>
> `props`를 `true`로 설정하면 `route.params`가 컴포넌트 `props`로 설정됩니다.
>
> ### 객체 모드
>
> `props`가 객체일때 컴포넌트 `props`가 있는 그대로 설정됩니다. `props`가 정적일 때 유용합니다.
>
> ```js
> const router = new VueRouter({
>   routes: [
>     { path: '/promotion/from-newsletter', component: Promotion, props: { newsletterPopup: false } }
>   ]
> })
> ```
>
> ### 함수 모드
>
> `props`를 반환하는 함수를 만들 수 있습니다. 이를 통해 전달인자를 다른 타입으로 캐스팅하고 적정인 값을 라우트 기반 값과 결합됩니다.
>
> ```js
> const router = new VueRouter({
>   routes: [
>     { path: '/search', component: SearchUser, props: (route) => ({ query: route.query.q }) }
>   ]
> })
> ```
>
> `/search?q=vue`는 `{query: "vue"}`를 `SearchUser` 컴포넌트에 전달합니다.
>
> 라우트 변경시에만 평가되므로 `props` 함수는 상태를 저장하지 않도록 합니다. `props`를 정의할 상태가 필요한 경우 래퍼 컴포넌트를 사용하면 상태가 변경될 때마다 응답할 수 있습니다.

공식문서를 참고해서 해봤다! 

reviewList에서 reviewItem으로 갈때 id값으로 router가 이동은 되지만 해당 reviewItem에서 data를 쓰려면 props로 넘겨줘야되는데 방법을 몰라서 구글링을 했더니, 위와 같은 여러 방법들이 있는데 나는 그중에 함수로 전달하는 것을 해봤다.

✔️ **props로 전달하지 않아도 id값을 받는 방법**

```vue
template>
  <div class="product">
    <h1>상품 정보</h1>
    <p>이 페이지는 ID.{{ $route.params.id }}의 상세를 출력합니다.</p>
  </div>
</template>
```

`{{ $route.params.id }}` 이거로 props로 전달하지 않아도 id값을 받을 수 있지만 type을 찍어봤더니 `String`값이 나왔다.

reviews를 get방식으로 서버에서 불러온다고 해도, review.id는 number라 `==`동등연산자로 계산하면 굳이 props로 전달하지 않고 아래와 같이 쓸수 있지만, 나는 `===`일치연산자를 쓰고 싶어서  props로 id값을 Number로 받아왔다.

✔️ **`{{ $route.params.id }}` 사용해서 review data가져오는 법 **

> id값을 이용해 reviews에서 id값이 동등(숫자와 문자이지만 숫자형 문자는 같다고 인식함)하는 것을 가져옴!

```vue
<script>
import axios from 'axios'
export default {
  data(){
    return {
      review:{}
    }
  },
  created(){
    const reviewId = this.$route.params.id
    axios.get('http://127.0.0.1:8000/reviews/')
      .then((res) => {
        res.data.forEach((review)=>{
          if (review.id == reviewId){
            this.review = review
          }
        })
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>
```



✔️ **매개 변수를 props로 컴포넌트에 전달하기 **

`router > index.js`

```js
...
const routes = [
 ...
  {
    path: '/reviews/:id',
    name: 'ReviewItem',
    component: ReviewItem,
    //아래 내용 추가, 해당 route에 props로 id값을 Number type으로 넘겨줌
    // 함수로 지정하면 첫 번째 매개변수로 현재 라우트 객체를 사용할 수 있음
    props: route => ({
      id: Number(route.params.id)
    })
...
```

- `views > ReviewItem.vue`

> id값을 이용해 reviews에서 id값이 일치하는 것을 가져옴!
>
> 동등연산자는 언제 오류가 날지 모르니 일치 연산자로 확실하게 하기위해 이렇게 했다!

```vue
<script>
import axios from 'axios'
export default {
  // id를 라우터로 보낸 props
  props:{
    id:Number,
  },
  data(){
    return {
      review:{}
    }
  },
  created(){
    const reviewId = this.$route.params.id
    console.log(reviewId)
    axios.get('http://127.0.0.1:8000/reviews/')
      .then((res) => {
        res.data.forEach((review)=>{
          if (review.id === this.id){
            this.review = review
          }
        })
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
```

