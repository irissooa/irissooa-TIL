# Vue Single File Component 와 Vue router

[toc]



## Single File Component

> 화면의 특정 영역에 대한 HTML,CSS, JavaScript코드를 **하나의 파일(.vue)에서 관리**
>
> Vue 컴포넌트 === Vue 인스턴스  === .vue File



### Component

> **다시 사용할 수 있는** 범용성을 위해 개발된 소프트웨어 구성 요소
>
> Vue => 가장 강력한 기능 중 하나, 기본 HTML엘리먼트를 확장하여 **재사용 가능한 코드**, Vue 컴포넌트(**new Vue**)는 **Vue 인스턴스**다.
>
> 1. 유지
> 2. 보수
> 3. 재사용성

- "소프트웨어 개발에서 독립적인 단위 모듈"
- 대체로 컴포넌트는 특정 기능이나 관련된 기능의 조합으로 구성되는데, 프로그래밍 설계에서 시스템은 모듈로 구성된 컴포넌트로 나뉜다.
- Vue 공식문서에 적힌 내용
  - 기본 HTML 엘리먼트를 확장하여 **재사용 가능한 코드로 캡슐화 하는 것**
- **모든 Vue 컴포넌트는 Vue 인스턴스다.** 그러므로, 모든 options 객체를 사용할 수 있다.(단, root에서만 사용할 수 있는 옵션은 제외)
- 한 Vue app 안에서 각 컴포넌트들은 Root 인스턴스를 시작으로 부모-자식 컴포넌트의 관계를 가진다.
- Vue cli 환경에서 사용하는 방법과 일반적인 HTML, JS 에서 사용하는 방법이 다르다.
- Component 에서 활용되는 속성들
  - `name` : 컴포넌트 사용 시, 해당 컴포넌트의 이름을 정의
  - `components` : 부모 컴포넌트에서 사용할 자식 컴포넌트의 이름(`name`)들을 작성
  - `props` : 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때 사용



### props

- 컴포넌트를 재생산할 때 컴포넌트에서 사용할 변수를 부모에게 내려주게 되는데 이를 `props`라고 한다.

- `props`는 반복되는 컴포넌트에서 서로 다른 정보가 들어가야 할 때 사용

- 하위(자식)에서 상위(부모) 데이터를 직접 참조해선 안되고 실제로도 안된다.

  - 자식 컴포넌트에서 부모 컴포넌트를 움직이게 하려면, 이벤트를 발생(`emit`)시켜야 한다.
  - 모든 Vue 컴포넌트들은 `.$emit` 메서드를 통해 부모 컴포넌트가 들을 수 있는 이벤트를 발생시킬 수 있다.

- `props` 옵션을 통해 부모 -> 자식으로 데이터를 전달

- 전달하려고 하는 **데이터의 이름을 태그 내의 속성**으로, **내용을 속성 값**으로

- props 예제

  `type` : `String`, `Number`, `Boolean`, `Array`, `Object`, `Date`, `Function`, `Symbol`

  `default` : `any`

  `required` : `Boolean`

  `validator` : `Function`

  ```js
  // 단순한 구문
  Vue.component('props-demo-simple', {
    props: ['size', 'myMessage']
  })
  
  // 유효성 검사를 포함한 객체 구문
  Vue.component('props-demo-advanced', {
    props: {
      // 타입 체크만 합니다.
      height: Number,
      // 타입 체크와 유효성 검사를 합니다.
      age: {
        type: Number,
        default: 0,
        required: true,
        validator: function (value) {
          return value >= 0
        }
      }
    }
  })
  ```

## Vue CLI(Command line interface)

> 어떻게 컴포넌트 기반으로 개발을 할까?
>
> Node.js -> 런타임 환경은 프로그래밍 언어가 동작하는 환경을 의미함
>
> 브라우저에서만 동작하던 Javascript는 일반 컴퓨터에서도 활용할 수 있게 됨
>
> npm(노드 패키지 매니저)은 자바스크립트 프로그래밍 언어를 위한 패키지 관리자이다. 자바 스크립트 런타임 환경(Node.js)의 기본 패키지 관리자



## Babel & Webpack

> JS -> **파편화 & 표준화**
>
> Babel -> 파편화된 Js문법을 변환하기위해 존재하는 도구(최신문법을 이전문법으로 번역해준다.)
>
> Webpack -> **bundler** 
>
> JS는 기본적으로 모듈이 없음 근데 필요하니까 모듈에 대한 개념을 가지고 들어옴 
>
> **모듈간의 의존성 문제를 해결하기 위해 존재하는 도구**

### Node.js

- JavaScript Runtime Environment
- JavaScript를 브라우저 밖에서 실행할 수 있는 새로운 환경



### Babel

- Compiler
- 신버전의 JavaScript코드를 구버전의 JavaScript로 바꿔주는 도구



### Webpack

- Bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 서로 연관 있는 모듈 간의 관계를 해석하여 정적인 자원으로 변환해주는 변환 도구
- 파일 간의 연관관계를 파악하여 하나의 자바스크립트 파일로 변환해주는 변환 도구
- 웹팩은 현재 가장 널리 쓰이는 모듈 번들러.
- JS 뿐만 아니라 CSS, IMAGE 파일 등 리소스의 의존성들도 관리한다.

#### webpack의 구성

| 요소    | 내용                                                         |
| ------- | ------------------------------------------------------------ |
| entry   | 여러 js 파일들의 시작점 => 웹팩이 파일을 읽어 들이기 시작하는 부분전체 애플리케이션 설치, 필요 라이브러리를 로딩하는 로직을 포함웹팩으로 빌드(변환)할 대상 파일을 지정 |
| module  | 웹팩은 JS 만 변환 가능하기 때문에 HTML, CSS 등은 모듈을 통해서 웹팩이 이해할 수 있도록 변환이 필요하다.변환 내용을 담는 곳 |
| plugins | 웹팩을 통해 번들된 결과물을 추가로 처리하는 부분ex) 결과물의 사이즈를 줄이거나 결과물(기본적으로 JS)을 기타 CSS, HTML 파일로 분리하는 기능 등이 있음 |
| output  | 여러 js 파일을 **하나로 만들어 낸 결과물**결과물의 위치, 파일명 등 세부 옵션을 설정 |

















-----------------------



template - component를 만들거다라고 생각하면서



1. 자식이 부모한테 데이터를 직접 전달할 수 없다.(전제조건)

2. 부모가 자식한테 데이터를 보내는 것은 가능!(appData)

3. parentData는 직접적으로 app에 데이터를 보낼 수 없어서 선택한 것이 app에 parentdata를 만들고 parentdata를 변경할 수 잇는 방법 -> emit을 하는데 onParentdatachange라는 이벤트를 발생시키기만 하면 내가 app에서 parentdata를 변경시켜줄게!라고 부탁함

   그 알려주는 코드가 app에 @onparentdatachange임 이 함수가 실행되면 method에 parentdata가 바뀜 그 버튼을 누르는건 ㅈ자식쪽에서this.$emit이라는 함수를 통해 그 버튼을 누를 ㅅ수 잇음!

   

   부모는 버튼을 전달하고,

   부모는 이벤트리스너를 달고

   

    자식은 버튼을 누른다

   자식은 이벤트를 발생시킨다.