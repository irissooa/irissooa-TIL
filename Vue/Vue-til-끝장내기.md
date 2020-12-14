# Vue-til-끝장내기

[toc]

## NVM 설치 및 버전 변경 방법

> [NVM 깃헙 설치 링크](https://github.com/nvm-sh/nvm#installing-and-updating)
> 노드 버전을 그냥 전환하고 싶으면 `npm use 버전`을 쓰면됨

### 설치 절차

1. VSCode의 내장 터미널을 `bash`로 실행하고 아래 명령어를 입력한다.

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash
```

2. 설치가 완료되면 터미널에서 아래 명령어로 `nvm` 명령어를 시스템 레벨에 추가한다.

> - vi라는 편집기를 이용해 `~/.bashrc`라는 폴더를 편집하겠다고 bash에 적음
>
> ```sh
> $ vi ~/.bashrc
> ```
>
> - 그런뒤에 export를 붙여넣는다.
>
> ```sh
> export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
> [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
> ```
>
> - `i`를 쓰면 쓰기모드!
> - 붙여넣은 상태에서 `esc`누르면 쓰기모드 해제!  그런뒤에 `:wq`를 적으면 저장됨!
> - 다시 `$ vi ~/.bashrc`를 적어 저장됐는지 확인
> - 그냥 아무것도 안하고 나오고 싶을 땐 `:q` :종료, 
> - 만약 뭔가를 잘못해서 강제로 종료하고 싶을 땐 `:q!` : 강제종료

```sh
vi ~/.bashrc
# vi로 연 .bashrc 파일에 "i" 키를 입력하여 쓰기 모드로 진입합니다.
# 그리고 나서 아래 내용을 추가하고 ":"를 입력한 다음 "wq"를 입력하여 저장 후 종료합니다.
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

3. 이제 터미널에 `nvm` 명령어를 입력하면 인식이 되는지 확인한다.

4. 인식되면 아래의 명령어로 Node.js를 설치한다.

```sh
nvm install 10.16
```

5. 설치가 끝나면 아래의 명령어로 Node.js 버전을 변경한다.

```sh
nvm use 10.16
```

6. 설치한 이후 아래 명령어로 Node.js 버전이 잘 설정되었는지 확인한다.

```shell
node -v
```



### 서버 실행 절차

> 서버 실행 명령어 `npm run dev`
>
> `vue-til-server-master`폴더가 서버다! 프론트할때 같이 켜줘야 함

1. 로컬에 Node.js를 설치합니다.
2. 리포지토리를 클론한 다음 아래 명령어를 실행합니다.

```shell
# Node.js를 실행하기 위해 필요한 라이브러리를 설치하는 명령어
npm i
```

3. `package.json`에 정의되어 있는 실행 명령어를 입력합니다.

```shell
npm run dev
```

4. 명령어 실행 창에서 아래와 같은 메시지가 떴는지 확인합니다.

![image-20201214100443218](Vue-til-끝장내기.assets/image-20201214100443218.png)



### API 문서 확인 절차

TIL 애플리케이션의 백엔드 API는 아래 주소에서 확인할 수 있다.

http://localhost:3000/api/docs

### Mongo Cloud 가입 절차

애플리케이션의 데이터는 몽고 DB에 저장한다. 실습 환경을 빠르게 구성하기 위해서 로컬에 몽고 DB를 설치하지 않고 몽고 DB 클라우드 서비스를 사용!

[몽고 DB 클라우드 서비스 사이트](https://cloud.mongodb.com/)

1. 다음 링크로 몽고 DB 클라우드 서비스에 가입한다. [가입 페이지](https://cloud.mongodb.com/user#/atlas/register/accountProfile)

2. 가입한 계정으로 로그인

3. 무료 인스턴스 생성. **꼭 Free Tier**를 선택!

4. Database Access - 데이터베이스 접속을 위한 계정 생성. 예시) test/1234

5. Network Access - `ADD IP ADDRESS` 버튼 클릭 후 `ALLOW ACCESS FROM ANYWHERE` 버튼 클릭 또는 현재 IP만 화이트리스트로 등록

6. Clusters

   1. 메인 페이지의 `CONNECT` 버튼 클릭
   2. Connect Your Application 클릭
   3. `DRIVER`에 `Node.js` 선택
   4. `VERSION`에 `3.0 or later` 선택
   5. Connection String 복사 후 `app.js` 파일의 아래 부분에 붙여넣기

   ![image-20201214103742294](Vue-til-끝장내기.assets/image-20201214103742294.png)

```sh
mongoose.connect('여기다가 붙여넣으세요.', {
  useNewUrlParser: true,
});
```

7. Node.js 서버 재 실행 후 API 동작 여부 확인

### API 문서 보는법 

> Swagger : 프론트앤드 개발자가 api node.js로직을 이해할 수 있게 명시해둠

![image-20201214104214439](Vue-til-끝장내기.assets/image-20201214104214439.png)

![image-20201214104232835](Vue-til-끝장내기.assets/image-20201214104232835.png)

![image-20201214104346829](Vue-til-끝장내기.assets/image-20201214104346829.png)



## Vue Cli project

> [Vue CLI 설치 안내 페이지](https://cli.vuejs.org/guide/installation.html)

```sh
//vue 최신버전 설치
npm install -g @vue/cli
vue create vue-til
```

- `Babel, Linter, Unit Testing`선택 -> `ESLint + Prettier`선택 -> `Lint on save`선택 -> `Jest`선택 -> `In dedicated config files`선택 -> `N`

![image-20201214104919839](Vue-til-끝장내기.assets/image-20201214104919839.png)

![image-20201214105300869](Vue-til-끝장내기.assets/image-20201214105300869.png)

### ESLint

> [Vue.js 개발 생산성을 높여주는 도구 3가지](https://joshua1988.github.io/web-development/vuejs/boost-productivity/)
>
> [ESLint](https://eslint.org/) JavaScript 코드에서 발견 된 문제 패턴을 식별하기위한 정적 코드 분석 도구
>
> 린트(ESLint)는 잘못된 코드 스타일로 인해 에러가 나지 않게 코드 문법을 잡아주는 문법 검사기이다. 문장 뒤에 자동으로 세미콜론, 콤마를 붙여주기도 하고 의미 없는 변수, API 사용에 대해 경고해주는 등 여러 문법 오류에 대해서 미리 알려준다. 가급적 덜 에러가 나는 코드를 작성하면 자연스럽게 버그도 줄어들기 때문에 서비스 품질을 높이는데도 도움이 됨!ㄴ

#### (참고) ESLint 에러 화면 표시안되게 하는 법

- 프로젝트 폴더 위치에 `vue.config.js`파일을 만든 뒤 아래의 코드를 적는다.

```js
// vue 설정파일을 추가로 만듦 돌아갔을때 화면에서 덮어쓰는 기능을 해지한다는 뜻
module.exports = {
	devServer: {
		overlay: false,
	},
};
```

이렇게 하면 에러는 콘솔에만 찍히고 화면에는 표현되지 않는다!

![image-20201214112742847](Vue-til-끝장내기.assets/image-20201214112742847.png)

- `.eslintrc.js`

> 관리도구, 설정파일의 내용을 바꿨을 때는 서버를 껐다가 재실행 해야된다!

```js
module.exports = {
  root: true,
  env: {
    node: true
  },
   // node modules에 깔려있는 prettier 모듈을 가져와서 이부분에 들어와있다고 생각하면된다
  extends: ["plugin:vue/essential", "@vue/prettier"],
  rules: {
      //error라고 하면 무조건 콘솔있으면 에러가 남
      //off는 콘솔이 있더라도 에러가 나지 않는다.
    "no-console": "off",
      //개발모드일때 콘솔이 있으면 error를 내보내고, 일반 prototype 모드면 off란 뜻!
    // "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    // "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off"
  
      //prettier설정에 대한 객체 [eslint의 log level,프리티어의 속성]
  "prettier/prettier": ['error', {
      singleQuote: true,
      semi: true,
      useTabs: false,
      tabWidth: 2,
      trailingComma: 'all',
      printWidth: 80,
      bracketSpacing: true,
      arrowParens: 'avoid',
    }]
  },
  parserOptions: {
    parser: "babel-eslint"
  },
  overrides: [
    {
      files: [
        "**/__tests__/*.{j,t}s?(x)",
        "**/tests/unit/**/*.spec.{j,t}s?(x)"
      ],
      env: {
        jest: true
      }
    }
  ]
};

```

#### Prettier

> https://prettier.io/
>
> 프리티어(Prettier)는 코드 스타일을 정리해주는 도구이다. ESLint와 함께 사용하면 좀 더 개인 취향에 맞는 코드 스타일로 전체 코드를 정리할 수 있다. VSCode(Visual Studio Code), Atom, Sublime 등 대중적인 텍스트 편집기에서 이미 플러그인 형태로 지원하고 있으며 VSCode에서는 아래와 같이 확장 플러그인으로 설치할 수 있다.
>
> `.prettierrc`라는 파일을 만들면, 프리티어에서 정의한 규칙대로 코드가 만들어짐! 처음 vue cli설치를 할 때 prettier를 설정했기 때문
>
> 하지만 이거를 `.eslintrc.js`에 프리티어를 포함시켜야된다!
>
> 왜냐하면 두개가 충돌이 일어날 수 있기 때문!
>
> 프리티어는 코드 작성 뒤 저장을 하면 알아서 문법적으로 자동으로 변환해줌

- VScode에서 `ctrl`+`,` 눌러서 설정으로 들어가 `settings.json`으로 들어가서 아래의 코드 추가함!

![image-20201214120536919](Vue-til-끝장내기.assets/image-20201214120536919.png)

```json
{
    "editor.tabSize": 2,
    "[python]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 4

    },

    "files.associations": {
        "**/*.html": "html",
        "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "atomKeymap.promptV3Features": true,
    "editor.multiCursorModifier": "ctrlCmd",
    "editor.formatOnPaste": true,
    "workbench.iconTheme": "material-icon-theme",
    "workbench.colorTheme": "Night Owl",
    "editor.fontSize": 20,
        
        //아래의 내용 추가
    "eslint.validate": [
        
        {
            "language": "vue",
            "autoFix": true
        },
        {
            "language": "javascript",
            "autoFix": true
        },
    ],

    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
    },
    "eslint.workingDirectories": [
        {
            "mode": "auto"
        }
    ],

}
```

- Vs코드 prettier플러그인 설치돼있으면 오른쪽마우스키 눌러서 `작업영역에서 사용안함 클릭`
- `format on save`도 꺼줘야 됨!! 그래야 충돌안나게 `ESLint`사용 할 수 있음

> 위 속성은 코드를 작성하고 저장 버튼을 눌렀을 때 자동으로 코드를 정리해줌
>
> BUT!! 이렇게 플러그인으로 간단하게 코드를 정리할 수도 있지만 개인적으로는 ESLint와 결합하여 프로젝트 설정 파일로 관리하는 것을 추천
>
> ```json
> //settings.json파일에 추가하면 코드 작성시 자동 코드 정리
> {
>   "editor.formatOnSave": true,
>   "editor.formatOnType": true
> }
> ```
>
> 

![image-20201214120716383](Vue-til-끝장내기.assets/image-20201214120716383.png)



#### ESLint와 Prettier를 뷰 프로젝트에 적용하기

> 위에 프로젝트를 생성할 때 추가할 수 있지만 만약 프로젝트를 이미 생성했다면!! 아래와 같이 구성하면 됨

**1.**노드 패키지 매니저(NPM)로 린트 및 프리티어 라이브러리를 설치.

```bash
npm i eslint eslint-config-prettier eslint-plugin-prettier eslint-plugin-vue --save-dev
BashCopy
```

**2.**프로젝트 루트 레벨에 린트 설정 파일인 `.eslintrc.js`를 추가.

```js
// .eslintrc.js
module.exports = {
  // 현재 eslintrc 파일을 기준으로 ESLint 규칙을 적용
  root: true,
  // 추가적인 규칙들을 적용
  extends: [
    'eslint:recommended',
    'plugin:vue/essential',
    'prettier',
    'plugin:prettier/recommended',
  ],
  // 코드 정리 플러그인 추가
  plugins: ['prettier'],
  // 사용자 편의 규칙 추가
  rules: {
    'prettier/prettier': [
      'error',
      // 아래 규칙들은 개인 선호에 따라 prettier 문법 적용
      // https://prettier.io/docs/en/options.html
      {
        singleQuote: true,
        semi: true,
        useTabs: true,
        tabWidth: 2,
        trailingComma: 'all',
        printWidth: 80,
        bracketSpacing: true,
        arrowParens: 'avoid',
      },
    ],
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
  },
};
JsCopy
```

각 주요 속성 특징

- `root`: 현재 폴더 위치를 기준으로 하위의 파일에 린트를 적용한다. 상위 폴더에 린트를 적용하지 않는다.
- `extends`: 린트의 기본적인 문법 검사 규칙 이외에 추가적인 규칙들을 적용한다. 이미 누군가에 의해 정해진 몇 개의 규칙을 추가한다고 보면 된다.
- `plugins`: NPM으로 설치하여 사용할 수 있는 확장 규칙이다. 대중적인 라이브러리와 결합하여 린트를 사용할 수 있다.
- `rules`: 린트를 실행할 때 사용자가 임의로 규칙을 추가하여 검사에서 제외 또는 추가하는 속성이다.

참고로 린트 설정 파일 대신에 `package.json` 파일에 `eslintConfig` 속성을 사용해도 되지만 규칙 적용에 대한 우선순위는 린트 설정 파일이 더 높기 때문에 설정 파일을 따로 만들어서 사용하는 것 추천!

**3.** NPM 설정 파일인 `package.json` 파일에 아래의 NPM 커스텀 명령어를 추가한다.

```json
{
  "lint": "eslint --ext .js,.vue src"
}
JSONCopy
```

콘솔 창에서 위 명령어를 수행하면 src 폴더 밑의 js, vue 파일에 대해서 린트 검사를 수행한다. 앞에서 린트 설정에 프리티어 내용을 추가했기 때문에 린트의 기본 규칙과 함께 `rules`에 설정한 프리티어 규칙도 함께 적용되어 검사된다.

**4.**마지막으로 비주얼 스튜디오 코드의 프리티어 플러그인을 비활성화하고 `settings.json` 파일에 아래의 내용을 추가한다.

```json
{
  ...
  "editor.formatOnSave": false,
  "editor.codeActionsOnSave": {
      "source.fixAll.eslint": true
  },
  "eslint.alwaysShowStatus": true,
  "eslint.workingDirectories": [
      {"mode": "auto"}
  ],
  "eslint.validate": [
      "javascript",
      "typescript"
  ],
}
JSONCopy
```

프리티어 플러그인을 비활성화하지 않으면 VSCode의 Formatter 기능과 린트 검사 기능이 겹치게 되어 코드가 일관되게 정리되지 않는다. 꼭 프리티어 플러그인을 사용하지 않음으로 설정하고 VSCode의 오른쪽 아래에 있는 Formatting을 X로 전환한다.



### VScode에서 제공하는 절대경로 찾기 설정

> [VSCode의 jsconfig.json 파일 설명 글](https://code.visualstudio.com/docs/languages/jsconfig)

- 프로젝트 폴더 위치에 `jsonconfig.json` 파일을 생성

```json
{
  "compilerOptions": {
    // 현재 위치 기준으로 하려고 프로젝트 폴더에 이 파일을 만듦
    "baseUrl": ".",
    // 별칭이 들어감, 
    "paths": {
      "~/*": [
        "./*"
      ],
      // 이 프로젝트를 기준으로 @를 쓰면 src밑에 파일을 바로 확인할 수 있단 말
      "@/*": [
        "./src/*"
      ],
    }
  },
  // conpilerOptions에 해당하지 않을 폴더, 라이브러리폴더 등
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```

- 아래와 같이 절대경로를 표시할 수 있음

```vue
<template>
	<div>header</div>
</template>

<script>
// 상대경로 ..는 한단계 올라간단말, 파일의 레벨이 깊어질수록 거슬러올라가는 것이 많이 붙게되는데 번거로워짐
import Demo from '../../demo/basic/Demo'
// 절대경로로 설정을 해서 찾아가는것이 더 좋다
import Demo from '@/demo/basic/Demo'
// import Demo from '@/demo/basic/Demo'

export default {};
</script>

<style></style>
```



### (참고)Vue.js 스타일 가이드

> [Vue.js 스타일 가이드 문서](https://kr.vuejs.org/v2/style-guide/index.html)



## Vue router

> [뷰 라우터 오픈 소스](https://github.com/vuejs/vue-router)
>
> [뷰 라우터 History Mode 주의 사항 문서](https://router.vuejs.org/guide/essentials/history-mode.html)
>
> [Window History API](https://developer.mozilla.org/en-US/docs/Web/API/Window/history)
>
> [웹팩 코드 스플리팅 문서](https://webpack.js.org/guides/code-splitting/)
>
> [Vue.js 다이나믹 임포트 문서](https://vuejs.org/v2/guide/components-dynamic-async.html#ad)

- `src`폴더 아래에 `routes`폴더를 만들고, 그 아래에 `index.js`파일을 만든다.

> ### Code Spliting
>
> 화면의 개수가 많아졌을 때, 처음에는 지정한 페이지만 가져오고, 나머지 페이지도 해당 페이지로 이동했을 때만 불러오게 하는 것!
>
> `component: () => import('@/views/LoginPage.vue')`

```js
//index.js
import Vue from 'vue';
import VueRouter from 'vue-router';
// import LoginPage from '@/views/LoginPage.vue';
// import SignupPage from '@/views/SignupPage.vue';

// 플러그인을 초기화하기위한 코드라고 생각하면됨
Vue.use(VueRouter);

// 뷰 라우터 인스턴스를 만드는데, 그걸 export default로 꺼내게 되면 라우터 인스턴스가 현재 파일에서 나가게됨
export default new VueRouter({
	// url에 #이 제거됨,저 #을 떼면 서버입장에서 새로운 서버라고 생각을 함, 
	// 서버의 유형에따라 서버가 #이 없어도 놀라지 않게(?) 뷰 라우터 히스토리모드 주의사항 문서를 보고 적용을 해줘야됨
	mode: 'history',
	//라우트의 페이지 정보들을 적음!
	routes: [
		{
			// 뷰 라우터 오픈소스, 로컬host에 진입할때마다 바로 login페이지로감
			path: '/',
			redirect: '/login',
		},
		{
			path: '/login',
			//views 폴더를 새로 만들어서 그아래에 라우터 페이지 컴포넌트들을 생성
			// 이렇게 화살표함수를 써서 import를 하면 이게 code spliting이 된다, 그 곳으로 이동할때만 import를 해옴!
			component: () => import('@/views/LoginPage.vue'),
		},
		{
			path: '/signup',
			component: () => import('@/views/SignupPage.vue'),
		},
		// 라우터 콜백기능, 없는페이지를 접근할때의 라우터 처리
		{
			path: '*',
			// views폴더밑에 없는페이지로 가면 해당 페이지로 감!!
			component: () => import('@/views/NotFoundPage.vue'),
		},
	],
});




//main.js
import Vue from 'vue';
import App from './App.vue';
// export한 라우터를 가져와서 웹팩의 별칭옵션으로 절대경로 표시 .js붙이지 않더라도 자동으로 인식함
import router from '@/routes/index';

Vue.config.productionTip = false;

new Vue({
	render: h => h(App),
	//router등록(연결)
	router,
}).$mount('#app');
```

- App.vue

```vue
<template>
  <div>
    <header>
      <!-- to에 지정된 문자열로  url을 이동시켜줌 -->
      <router-link to="/login">로그인</router-link> |
      <router-link to="/signup">회원가입</router-link>
    </header>
    <!-- url이 변경됐을 때 해당 라우터 컴포넌트가 여기에 표시됨 -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style></style>

```



## Signup

- App.vue의 header ->`components` > `common` > `AppHeader.vue`

```vue
<template>
  <header>
    <router-link to="/login">로그인</router-link> |
    <router-link to="/signup">회원가입</router-link>
  </header>
</template>

<script>
export default {};
</script>

<style></style>
```

- `SignupPage.vue`

```vue
<template>
  <div>
    <h1>회원 가입 페이지</h1>
    <!-- 페이지는 가급적 각 기능별로 컴포넌트를 나눠 그 컴포넌트를 등록하는게 좋다 -->
    <SignupForm></SignupForm>
  </div>
</template>

<script>
import SignupForm from '@/components/SignupForm.vue';

export default {
  components: {
    SignupForm,
  },
};
</script>

<style></style>
```



### Signup API

- signup api문서를 통해 어떤 정보를 보내야되는지 알 수 있다

![image-20201214133220521](Vue-til-끝장내기.assets/image-20201214133220521.png)

![image-20201214133322043](Vue-til-끝장내기.assets/image-20201214133322043.png)

- axios설치

```sh
$ npm i axios
```

#### API 구조화

> [axios create() 문서](https://github.com/axios/axios#axioscreateconfig)
>
> 한 컴포넌트에 계속 `import axios from 'axios'`를 쓰는 것이 아니라, src폴더 아래에 api폴더를 만들고, axios에 대한 공통부분을 구조화하고, 가져와 편하게 쓸 수 있다.

- `src` > `api` > `index.js`

> [타입스크립트 핸드북](https://joshua1988.github.io/ts/)
>
> 타입스크립트는 자바스크립트에 타입을 부여한 언어다. 자바스크립트의 확장된 언어라고 볼 수 있다. 타입스크립트는 자바스크립트와 달리 브라우저에서 실행하려면 파일을 한번 변환해주어야 한다. 이 변환 과정을 우리는 **컴파일(complile)** 이라고 부른다
>
> 왜 써야되는가??
>
> - [에러의 사전 방지](https://joshua1988.github.io/ts/why-ts.html#에러의-사전-방지)
> - [코드 가이드 및 자동 완성(개발 생산성 향상)](https://joshua1988.github.io/ts/why-ts.html#코드-자동-완성과-가이드)
>
> - 예) 인자로 뭐가 들어가야되는지 알려줌
>
> ![image-20201214134239588](Vue-til-끝장내기.assets/image-20201214134239588.png)

```js
import axios from 'axios';

// axios create api이용 공통설정을 여기에 넣음, instance에 넣어서 라이브러리 재사용가능 
const instance = axios.create({
  // url을 공통화, 환경변수에 저장 `VUE_APP`을 쓰면 자동으로 로드돼서 쓸 수 있음!
  baseURL: process.env.VUE_APP_API_URL,
});

// post로 회원가입을 요청을 날릴 수 있는 함수를 만듦
function registerUser(userData) {
  // signupform에서 export된 이 함수를 호출, 함수 결과가 promise이기 떄문에 return으로 해줘야 이후에 비동기동작을 수행할 수 있다
  // instance.post는 axios.post(url,data)를 다 적지않고 코드를 줄일 수 있음
  return instance.post('signup', userData);
}

export { registerUser };
```

##### 환경변수 만들기 프로젝트 폴더 위에 `.env`파일을 만듦

> `VUE_APP`접두사가 붙은 변수는 자동로드!
>
> [웹팩 DefinePlugin 문서](https://webpack.js.org/plugins/define-plugin/)
>
> - env파일 규칙
>
> [Vue CLI env 파일 규칙 문서](https://cli.vuejs.org/guide/mode-and-env.html#modes-and-environment-variables)

- `.env`

> 혹시나 development, production이 없을 때 공통으로 들어가는 url, develope나 production이 없을 때 우선순위를 가짐

```sh
VUE_APP_API_URL=https://vue-til.com/
```

- `.env.development`

> 개발용 환경변수, prototype때는 이 url씀
>
> 가장 높은 우선순위를 가짐

```sh
VUE_APP_API_URL=http://localhost:3000/
```

- `.env.production`

> 좀더 정확하게하려면 `npm run build`를 했을 때 porduction으로 들어감
>
> 배포에 해당하는 도메인 주소

```sh
VUE_APP_API_URL=https://vue-til.com/
```

#### 비동기처리

> - [async await 정리글](https://joshua1988.github.io/web-development/javascript/js-async-await/)
> - [ES6 템플릿 리터럴(백틱) 정리글](https://joshua1988.github.io/es6-online-book/template-literal.html)
> - [ES6 Destructuring 정리글](https://joshua1988.github.io/es6-online-book/destructuring.html)

- `components` > `SignupForm.vue`

```vue
<template>
<!--.prevent를 하면 form의 기본 동작인 새로고침을 막을 수 있음 -->
  <form @submit.prevent="submitForm">
    <div>
      <label for="username">id: </label>
      <input id="username" type="text" v-model="username" />
    </div>
    <div>
      <label for="password">pw: </label>
      <input id="password" type="text" v-model="password" />
    </div>
    <div>
      <label for="nickname">nickname: </label>
      <input id="nickname" type="text" v-model="nickname" />
    </div>
    <button type="submit">회원 가입</button>
    <p>{{ logMessage }}</p>
  </form>
</template>

<script>
// 회원가입 api함수를 가져옴
import { registerUser } from '@/api/index';

export default {
  // vda입력후 tab하면 data속성 만들어짐
  data() {
    return {
      // form values
      // 이 data를 서버로 보내야됨, api문서의 parameter이름과 같게 적용해줘야된다!!
      username: '',
      password: '',
      nickname: '',
      // log
      logMessage: '',
    };
  },
  methods: {
    // form태그에 연결이되는 이벤트-> 폼태그에 버튼의 submit이벤트가 버블링에 의해 form태그로 올라옴 그래서 @submit으로 이벤트 인지할 수 있음!
    async submitForm() {
      const userData = {
        username: this.username,
        password: this.password,
        nickname: this.nickname,
      };
      // url은 이미 index.js에 적혀있으니 userData만 보내주면됨!
      // promise의 결과를 {data}로 받을 수 있게 await로 받음 
      // response.data = {data}
      const { data } = await registerUser(userData);
      // inpuutdata가 잘넘어갔는지 확인을 해야됨 -> api가 예상대로 동작을 안했을 때 -> network패널을보고 파라미터가 잘넘어갔는지 확인하고, response에 어떻게 떴는지까지 다 확인해봐라!!
      console.log(data.username);
      this.logMessage = `${data.username} 님이 가입되었습니다`;
      this.initForm();
    },
    // form데이터를 비우는 함수
    initForm() {
      // ''이게아니라 null로 작성해도됨, type이 정해져있기 때문! 그래도 bug를 줄이기 위해선 각 type을 지정해주는게 좋음
      this.username = '';
      this.password = '';
      this.nickname = '';
    },
  },
};
</script>

<style></style>
```



## Login

![image-20201214165233151](Vue-til-끝장내기.assets/image-20201214165233151.png)

![image-20201214165345363](Vue-til-끝장내기.assets/image-20201214165345363.png)

![image-20201214165359636](Vue-til-끝장내기.assets/image-20201214165359636.png)

- index.js

```js
import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
});

function registerUser(userData) {
  return instance.post('signup', userData);
}

function loginUser(userData) {
  return instance.post('login', userData);
}

// 다른 컴포넌트에서 사용할 수 있게 내보냄
export { registerUser, loginUser };
```



### login 에러처리

> 실제로는 에러처리를 잘하는게 중요함
>
> 에러가 떴을 떄 네트워크 패널로 들어가서 어떤점이 문제인지 확인할 줄 알아야한다.
>
> 에러가 났을 때는 사용자가 알수있게 화면에 표시를 해줘야된다!

- `components` > `LoginForm.vue`

```vue
<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="username">id:</label>
      <input id="username" type="text" v-model="username" />
    </div>
    <div>
      <label for="password">pw:</label>
      <input id="password" type="text" v-model="password" />
    </div>
    <!-- disabled가 isUsernameValid가 true가 아닐때 효과가 나타나고, valid해야 선택가능함 -->
    <!-- ||는 or 둘중 하나라도 없다면 로그인 버튼 누를 수 없음 -->
    <button :disabled="!isUsernameValid || !password" type="submit">
      로그인
    </button>
    <p>{{ logMessage }}</p>
  </form>
</template>

<script>
import { loginUser } from '@/api/index';
// email이 맞는지 확인하는 코드 가져옴
import { validateEmail } from '@/utils/validation';

export default {
  data() {
    return {
      // form values
      username: '',
      password: '',
      // log
      logMessage: '',
    };
  },
  // data의 변화에 따라서 자동으로 계산해줌
  computed: {
    // Username이 유효한지 확인, 유효하면 True, 유효하지 않으면 false
    isUsernameValid() {
      // username이 valid한지 validateEmail이 확인해줌, username에 한글자한글자 변화가나타날때마다 computed의 isUsernameValid가 실행됨
      return validateEmail(this.username);
    },
  },
  methods: {
    // 에러를 잘 처리해야됨!! -> 에러가 나면 화면에 표시를 해줘야된다
    async submitForm() {
      // try-비즈니스로직, catch-에러 핸들링할 코드
      try {
        // 비즈니스 로직
        const userData = {
          username: this.username,
          password: this.password,
        };
        // 타입스크립트를 이용해 userData인자의 타입도 지정해 줄 수 있음
        const { data } = await loginUser(userData);
        console.log(data.user.username);
        this.logMessage = `${data.user.username} 님 환영합니다`;
        // this.initForm();
        // 에러가 error객체에 담겨서 catch로 넘어옴
      } catch (error) {
        // 에러 핸들링할 코드
        // error.response.data를 하면 어떤것이 문제있는지 잘못된 곳에 접근함(백엔드에서 에러를 넘겨줌)
        console.log(error.response.data);
        // error메세지를 담아줌
        this.logMessage = error.response.data;
        // this.initForm();
        // 폼초기화를 끝나면 다 일어나게 finally에 넣어줌
      } finally {
        this.initForm();
      }
    },
    initForm() {
      this.username = '';
      this.password = '';
    },
  },
};
</script>

<style></style>

```

#### (참고) id가 email인지 아닌지 확인하는법 email validation

> [Email Validation 정규 표현식 코드](https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript)

- id가 email인지 아닌지 확인하기 위해서는 signup에서부터 확인을 해야됨!!
- `src` 폴더 아래에 `utils`폴더를 만들어 `validation.js` 파일을 만듦

```js
function validateEmail(email) {
  var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

export { validateEmail };
```

![image-20201214171744551](Vue-til-끝장내기.assets/image-20201214171744551.png)

### (참고) styling

- `App.vue`에 `style`태그 아래에 css파일 import

```vue
<template>
  <div class="app">
    <AppHeader></AppHeader>
    <div class="app-contents">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import AppHeader from '@/components/common/AppHeader.vue';

export default {
  components: {
    AppHeader,
  },
};
</script>

<style>
@import './css/reset.css';
@import './css/common.css';
</style>
```

- `src`>`css`>`common.css` , `reset.css`

```css
body {
  background: #F7F6F9;
}
.app {
	position: relative;
	width: 100%;
	height: 100%;
  font-size: 1.4rem;
}
.app-contents {
  height: calc(100% - 64px - 102px);
}
h1 {
	text-align: center;
	font-weight: 100;
}

/*--- LINK ---*/
a {
  color: #364f6b;
  text-decoration: none;
}
a:hover {
  color: #3fc1c9;
}

/*--- LAYOUT ---*/
.contents {
  max-width: 1020px;
  margin: 0 auto;
  padding: 0 5px;
  width: 100%;  
}
/*--- HEADER ---*/
.page-header {
  font-size: 45px;
	font-weight: 600;
	color: #456155;
	padding: 30px 5px 15px;
}

/*--- FORM ---*/
.form-container {
  display: flex;
  align-items: center;
}
.form-wrapper {
  background: white;
  -webkit-box-shadow: 0 20px 20px rgba(0, 0, 0, 0.08);
  box-shadow: 0 20px 20px rgba(0, 0, 0, 0.08);
  border-radius: 3px;
  padding: 15px 15px;
}
.form-wrapper.form-wrapper-sm {
  max-width: 500px;
  margin: 40px auto;
}
.form-wrapper-sm .page-header {
  padding: 0px 0 20px;
}
.form {
	width: 460px;
	height: 100%;
}
.form .validation-text {
	margin-top: -0.5rem;
	margin-bottom: 0.5rem;
	font-size: 1rem;
	display: flex;
	flex-direction: row-reverse;
	justify-content: space-between;
}
.form label {
  width: 100%;
  display: block;
  margin-bottom: 0.5rem;
  color: #364f6b;
  font-size: 90%;
}
.form input,
.form textarea {
  font-family: inherit;
  font-size: 100%;
  width: 100%;
  border: 1px solid #dae1e7;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.1);
  padding: 0.5rem 0.75rem;
  margin-bottom: 1rem;
}
.form input.valid {
  border: 1px solid #21b314;
}
.form input.invalid {
  border: 1px solid red;
}
.form div:nth-last-child(2) {
  margin-bottom: 0.5rem;
}
.btn {
  background: #FE9616;
  padding: 0.5rem 1.5rem;
  font-weight: 700;
  border-radius: .25rem;
  border: 0 solid #dae1e7;
}
.btn.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.log {
  color: #ff4057;
  font-size: 1rem;
  text-align: center;
}
.warning {
  color: #ff4057;
}

/*--- LIST ---*/
.list-container {
	padding-top: 13px;
}
.list-container.sticky {
	margin-top: 76px;
}
.list-container > ul {
	display: flex;
	flex-wrap: wrap;
}
.list-container > ul > li {
	position: relative;
	flex-grow: 1;
	width: 320px;
	height: 250px;
	margin: 7px;
	padding: 10px 20px;
	background: white;
	box-shadow: 0 20px 20px rgba(0, 0, 0, 0.08);
	border-radius: 3px;
}
.post-title {
	font-size: 24px;
	font-weight: 600;
	margin-bottom: 0.5rem;
}
.post-contents {
	height: 160px;
	overflow-y: auto;
	font-size: 18px;
}
.post-time {
	position: absolute;
	bottom: 4px;
	right: 5px;
	font-size: 14px;
	color: #9e9e9e;
}
.icon {
	font-size: 1.3rem;
	cursor: pointer;
	color: #364f6b;
	padding-right: 0.4rem;
}
.icon:hover {
	color: #3fc1c9;
}
.icon:active {
	color: #fc5185;
}
.ion-md-create {
	padding-left: 0.1rem;
}
```

```css
html,
body {
	height: 100%;
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
	font-family: 'Spoqa Han Sans', 'Sans-serif';
}

h1,
p,
ul {
	margin: 0;
	padding: 0;
}

input,
select,
textarea {
	border: 0;
	padding: 0;
	margin: 0;
	background: transparent;
	resize: none;
}

li {
	list-style: none;
}

button {
	font-family: inherit;
	font-size: 90%;
	margin: 0;
	cursor: pointer;
}

*,
*:after,
*:before {
	box-sizing: border-box;
	font-family: 'Spoqa Han Sans', 'Sans-serif';
}
```



## Main page

### 컴포넌트간 데이터 전달 방법 3가지

> [뷰 라우터 Programmatic Navigation 문서](https://router.vuejs.org/guide/essentials/navigation.html#programmatic-navigation)
>
> 1.  event올리고 porps로 data내림
> 2. event bus를 보냄
> 3. Vuex의 store이용

![image-20201214173507921](Vue-til-끝장내기.assets/image-20201214173507921.png)

#### 3. Vuex이용

> `package.json`에 dependencies에 들어감
>
> - dependencies : 애플리케이션 로직과 관련된 라이브러리 목록
> - devDependencies에 포함된 라이브러리는 `npm run build` 했을 떄 포함되지 않음(배포할 때 포함되지 않음) 
>
> [개발용 라이브러리와 배포용 라이브러리 구분하기 문서](https://joshua1988.github.io/webpack-guide/build/npm-module-install.html#개발용-라이브러리와-배포용-라이브러리-구분하기)

```sh
$ npm i vuex
```

- `src` > `store` > `index.js`

```js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: '',
  },
  // state값이 변경됐을 때 특정 상태를 보여줌 -> computed라고 생각하면됨(return값이 있어야됨)
  getters: {
    isLogin(state) {
      // username의 값이 빈문자열이 아닐때 로그인이 됐다! -> true로 나옴
      return state.username !== '';
    },
  },
  // state를 바꿈
  mutations: {
    // username(setUsername을 호출할때 보내줄 인자)을 받아서 그 값을 state의 username에 담아줌
    setUsername(state, username) {
      state.username = username;
    },
    // logout기능, username을 비워줌, store의 기준은 username이 채워져있냐 없냐의 여부로 로그인을 알게해놨음(getters isLogin)
    clearUsername(state) {
      state.username = '';
    },
  },
});

```

- `main.js`

```js
import Vue from 'vue';
import App from './App.vue';
import router from '@/routes/index';
// vuex의 store를 쓰기 위해 가져옴
import store from '@/store/index';

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router,
  // store 연결
  store,
}).$mount('#app');
```

- AppHeader.vue

```vue
<template>
  <header>
    <div>
      <!-- logo를 누르면 기본/로 가서 login페이지로 감 -->
      <router-link to="/" class="logo">
        TIL
        <!-- username을 store에서 가져옴 -->
        <span v-if="isUserLogin">by {{ $store.state.username }}</span>
      </router-link>
    </div>
    <div class="navigations">
      <!-- 1 분기처리함 -->
      <!-- login이 됐을 때(true일때) 보임 -->
      <template v-if="isUserLogin">
        <!-- 클릭을 했을 때 로그아웃이 되게 만듦 -->
        <a href="javascript:;" @click="logoutUser" class="logout-button">
          Logout
        </a>
      </template>
      <!-- 2 -->
      <!-- 그렇지 않으면 이게 보임 -->
      <template v-else>
        <router-link to="/login">로그인</router-link>
        <router-link to="/signup">회원가입</router-link>
      </template>
    </div>
  </header>
</template>

<script>
export default {
  computed: {
    isUserLogin() {
      // store가 인스턴스에 연결돼있어서 this로 접근 가능, getters에 islogin을 가져옴
      return this.$store.getters.isLogin;
    },
  },
  methods: {
    // 로그아웃 메서드, clearUsername이란 mutation을 호출, login페이지로 넘어감
    logoutUser() {
      this.$store.commit('clearUsername');
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.username {
  color: white;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #927dfc;
  z-index: 2;
  box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.05);
}
a {
  color: #dedede;
  font-size: 18px;
}
a.logo {
  font-size: 30px;
  font-weight: 900;
  color: white;
}
.logo > span {
  font-size: 14px;
  font-weight: normal;
}
.navigations a {
  margin-left: 10px;
}
.fixed {
  position: fixed;
  top: 0;
  width: 100%;
}
.logout-button {
  font-size: 14px;
}
a.router-link-exact-active {
  color: white;
  font-weight: bold;
}
</style>
```

- `MainPage.vue`

```vue
<template>
  <div>
    <div class="main list-container contents">
      <h1 class="page-header">Today I Learned</h1>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
```

- router등록 `index.js`

```js
 //routes에 코드추가
	{
      // code spliting을 이용해서 import
      path: '/main',
      component: () => import('@/views/MainPage.vue'),
    },
```

- `LoginForm.vue`수정

```vue
<template>
  <div class="contents">
    <div class="form-wrapper form-wrapper-sm">
      <form @submit.prevent="submitForm" class="form">
        <div>
          <label for="username">id:</label>
          <input id="username" type="text" v-model="username" />
          <p class="validation-text">
            <span class="warning" v-if="!isUsernameValid && username">
              Please enter an email address
            </span>
          </p>
        </div>
        <div>
          <label for="password">pw:</label>
          <input id="password" type="text" v-model="password" />
        </div>
        <button
          :disabled="!isUsernameValid || !password"
          type="submit"
          class="btn"
        >
          로그인
        </button>
      </form>
      <p class="log">{{ logMessage }}</p>
    </div>
  </div>
</template>

<script>
import { loginUser } from '@/api/index';
import { validateEmail } from '@/utils/validation';

export default {
  data() {
    return {
      // form values
      username: '',
      password: '',
      // log
      logMessage: '',
    };
  },
  computed: {
    isUsernameValid() {
      return validateEmail(this.username);
    },
  },
  methods: {
    async submitForm() {
      try {
        // 비즈니스 로직
        const userData = {
          username: this.username,
          password: this.password,
        };
        const { data } = await loginUser(userData);
        console.log(data.user.username);
        // commit, store의 mutations의 setUsername을 호출, 응답한 data의 username을 인자로 보내줌
        this.$store.commit('setUsername', data.user.username);
        // url로 이동시켜줌 '/main' 그 페이지로 이동함!
        this.$router.push('/main');
        // this.logMessage = `${data.user.username} 님 환영합니다`;
        // this.initForm();
      } catch (error) {
        // 에러 핸들링할 코드
        console.log(error.response.data);
        this.logMessage = error.response.data;
        // this.initForm();
      } finally {
        this.initForm();
      }
    },
    initForm() {
      this.username = '';
      this.password = '';
    },
  },
};
</script>

<style>
.btn {
  color: white;
}
</style>

```

