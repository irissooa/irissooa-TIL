#  WEB 과목평가 정리

## HTML

- Hyper
  - 정보가 동일선상이 아닌 다중으로 연결된 상태
  - Hyper Text
    - 하이퍼링크를 통해 사용자가 한문서에서 다른문서로 즉시 접근 할 수 있는 텍스트이며 http, html 등이 있음
- Markup Language
  - '마크업을 한다' : 특정 텍스트에 역할을 부여함, 제목, 본문등을 마킹
  - h1tag는 단순히 글자가 커지는 것이 아니라 의미론적으로 그 페이지에서 각 핵심 주제를 의미

### 기본구조

- DOM
  - 웹 페이지의 객체 지향 표현
  - 문서의 구조화된 표현을 제공
  - 프로그래밍 언어가 DOM구조에 접근할 수 있는 법 제공하여 문서구조, 스타일, 내용 등 변경할 수 있게 도움
  - 동알한 문서를 표현하고, 저장하고, 조작하는 방법 제공

- 요소
  - HTML요소는 시작태그, 종료태그, 태그사이 내용으로 구성
    - 태그는 그 정보의 성격과 의미를 정의함
    - 내용 없는 태그 : br, hr, img, input, link, meta
  - 중첩 가능
  - HTML은 오류를 뿜지않고 그냥 레이아웃이 깨져 디버깅이 힘듦
- 속성
  - 태그의 부가적인 정보가 들어옴
  - 요소는 속성을 가질 수 있으며 추가적 정보(이미지 파일의 경로,크기)를 제공
  - 태그와 관계없이 사용가능한 속성도 있음
  - 시작 태그에 위치해야하며 `이름`과 `값`의 쌍을 이룸
- HTML head
  - 페이지를 열 때 브라우저에 표시되는 `body`요소와 달리 표시되지 않음
  - 페이지에 대한 metadata를 포함
- 제목 달기
  - h1요소는 페이지당 한번씩 사용됨
  - 제목이나 뉴스의 헤드라인 표시
  - `title`은 HTML문서 전체의 타이틀을 표현하기 위한 메타데이터임
- 메타 데이터
  - 많은 `<meta>`요소가 `name`과 `content`속성을 가짐
  - `name`은 메타 요소가 어떤 정보의 형태를 갖고 있는지 알려줌
  - `content`는 실제 메타데이터의 컨텐츠임
- 기본과 단락
  - 각 단락은 `<p>`요소 안에 둘러싸여 있어야 함
  - 제목도 heading요소 안에 둘러싸여 있어야 함
  - 메인제목이 `<h1>`, 소제목이 나머지 `<h2>`~`<h6>`
- List
  - Unordered
    - 순서 없는 리스트를 정렬
    - `<ul>`태그로 감싸줌
    - 그 안의 리스트 항목을  `<li>`(list item)태그로 감싸줌
  - Ordered
    - `<ol>`태그로 감싸는 것을 제외하거는 마크업 구조는 순서 없는 리스트(`<ul>`)과 동일함

- table
  - `<table>` : 테이블을 만드는 태그
  - `<th>` : 테이블의 헤더부분을 만드는 태그
  - `<tr>` : 테이블의 행을 만드는 태그
  - `<td>` : 테이블의 열을 만드는 태그
  - `<colspan>` : 가로 합병(열 합병)
  - `<rowspan>` : 세로 합병(행 합병)
  - 각 열의 의미에 따라 thead, tbody, tfoot 태그로 구분지을 수 있음
- Form
  - 사용자가 입력한 정보를 서버로 전송하기 위한 컴포넌트를 의미
  - 서버에서 처리될 데이터를 제공하는 역할
  - 기본속성은 action/method임
  - action : 어디로 보낼지 결정
  - method : GET , POST
  - GET
    - 데이터 조회용
    - 서버의 데이터를 변경할 목적이 아니고, 조회만!
    - 전송할 데이터를 문자열 형태로 URL 뒤에 인수로 붙여서 전송(쿼리셋형태로 보냄)
    - 보안성이 없어 누구나 전송의 내용을 볼 수 있다!! 
    - `<a>`태그를 이용할 경우 일반적으로 GET방식 전송만 가능하나 자바스크립트를 이용하면 POST방식으로 전송이 가능하다! 
  - POST
    - 데이터 수정용,
    - 서버의 데이터를 변경할 목적!
    - 파일의 형태로 전송됨으로써 url 상에 나타나지 않아 보안성이 있음(body로 보냄)
    - 일반적으로 from은 POST형식으로 전송된다! 

#### TEXT관련요소

- `<a>`: 하이퍼링크
  - href속성
- `<b>` vs `<strong>` : 글자를 굵게 만들어줌(b는 그냥 굵게, strong은 굵게+강조)
- `<i>` vs `<em>` : 글자 기울림(i는 그냥 이탤릭체, em은 이탤릭체+강조)
- `<br>` : 줄바꿈



#### 시멘틱 태그

> 브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확히 설명하는 태그

- `<header>` 
- `<nav>` : navigation bar
- main content : `<main>`, `<article>`, `<section>`, `<div>` 등 
- aside: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
- footer 하단에 표시

#### `<div>` vs `<span>`

- `<span>`

  - 아무 의미가 없고
  - 태그 안에 컨텐츠가 없다면 해당 부분은 아무 변화가 없지만
  - 태그 내 객체가 들어간다면, 그 객체의 크기만큼 공간이 할당 됨

- `<div>`

  - 포함하고 있는 컨텐츠가 어떠한 의미도 갖지 않음을 의미
  - 논리적인 구분을 정의하는 태그, 각각의 블록을 가짐
  - 주로 레이아웃을 잡는 용도
  - class속성을 같이 사용함

  

#### 사용 이유?

- 의미부여
  - 문서에 의미를 부여해주는 행위
  - 의미있는 정보의 그룹을 태그로 표현

### 장점

1.  읽기 쉬워짐 (개발자)
   - 의도한 요소의 의미가 명확히 드러남
   - 코드의 가독성을 높임
   - 유지보수를 쉽게 함
2.  접근성이 좋아짐
   - ex) 검색엔진 및 보조기술 → 시력장애용 스크린리더 → 더 나은 경험 제공
   - HTML 문서는 html 언어 + 사람이 읽을 수 있는 content의 조합
   - 검색 엔진은 HTML 코드만 잘 읽음
   - 시맨틱 태그 사용이 권장, 검색 엔진도 무슨 내용인지 이해할 수 있게 됨

### 시멘틱 웹

- 기존의 단순한 데이터 집합이었던 웹페이지를 '의미'와 '관련성'을 가지는 거대한 데이터베이스로 구축



### 각  기능 설명

- `label` 입력란 앞에 정보를 적음

- `for`에 name을 적고 아래 `input`에서 `id`로 name을 주면 실제 web에서 label글을 클릭했을 때 input창에 커서가 감

- `input`사용자로부터 정보를 입력받을 수 있음

  - `name`에 fullname이라는 `key`로 내가 적은 이름(input값)이 value로 전달됨
  - ex. `http://naver.com/?fullname=내가적은이름&class-no=2&temp=37.5미만` 이런식으로 됨
  - 태그사이에 있는 이름은 화면에 표시될 text
  - `value`에 적은 것은 정보가 전달될 때 사용됨
  - `id`를 `label`과 같게 주면 글자를 클릭했을 때 체크가 됨(label의 글을 눌러도 input 값이 눌러짐-input형태가 버튼이다)
  - `name`을 똑같이 주면 여러개 중 하나가 선택됨(input type이 체크하는 형태인데 여러개 모두 선택되지 않고 한개만 선택되게 하기 위해 사용)
  
  ```sh
  <body>
  	<form~>
  		<div> 
              <label for="name">이름을 적어주세요</label>
              <input type="text" id="name" name="fullname" value="초기값이 설정됨"> 
  </div>        
  </body>
  ```
```
## CSS

- Inline Style Sheet : HTML태그의 style속성에 CSS코드를 넣는 방법

  ```sh
  <p style= "color: blue">
      Lorem ipsum dolor.
  </p>
```

  - 해당 태그(`<p>`)가 선택자가 되고, CSS코드에는 속성과 값이 만들어짐, 꾸미는데 한계가 있고, 재사용이 불가능함

- Internal Style Sheet : HTML 문서 안의 `<style>`과 `</style>`안에 CSS코드를 넣는 방법

  ```sh
  <style>
  h1 {
      color: blue;
      }
  </style>
  ```

  - `<style>`과 `</style>`안에 CSS코드를 넣음
  - 위 같은 경우 문서 안의 모든 h1요소는 파란색이 됨
  - HTML문서 안의 여러 요소를 한번에 꾸밀 수 있다는 장점이 있으나, 또 다른 HTML 문서에는 적용할 수 없다는 단점이 있음
  - class를 지정할때 밑에 있을 수록 우선적용

- Linking Style Sheet : 별도의 CSS파일을 만들고 HTML문서와 연결하는 방법

  ```sh
  h1 {
  	color:red;
  }
  ```

  - 별도의 CSS파일을 만들고 HTML문서와 연결하는 방법
  - h1 요소의 글자를 빨간색으로 하고싶다면 별도의 style.css를 만든 뒤, HTML문서에 아래의 코드를 추가함

  ```sh
  <link rel="stylesheet" href="style.css">
  ```

  

### CSS Selector

> 선택자는 스타일을 지정할 웹 페이지의 HTML 요소를 대상으로 하는 데 사용

#### 전체 선택자

- `*` 사용, 전체에 적용하겠다라는 뜻

#### class 선택자

- 마침표(`.`)문자로 시작하며 해당 클래스가 적용된 문서의 모든 항목 선택
- 클래스를 생성(다중표기가능, 공백을 주고 연달아 적으면 됨
- 왠만하면 클래스 선택자를 이용해 스타일 지정

#### id선택자

- `#`문자로 시작하며 기본적으로 클래스 선택자와 같은 방식으로 사용
- BUT!! id는 문서 당 한 번만 사용할 수 있으며 요소에는 단일 id값만 적용
- 문서에서 동일한 id여러번 사용가능하지만 그러면 안됨!!!!!!!

#### 복합선택자

- 자손(하위의 모든 요소) : 셀렉터a `공백`셀렉터b
  - `.box p {` 클래스 안의 모든 p태그를 바꿔줌

- 자식(바로 아래의 요소) : 셀렉터a`>`셀렉터b
  - `.box > p {` box클래스 바로 안에 있는 p태그, 두단계이상 아래는 안되고, 바로 아래!! 직계자손만

#### 적용 우선순위

1. `!important`
   - 다른 사람들의 코드에서 발견할 때 그 의미를 알 수 있는 것은 조지만 반드시 필요한 경우가 아니라면 사용하지 마라!!
   - cascading이 정상적으로 작동하는 방식을 변경하므로, CSS스타일 문제를 해결하기 어렵

2. inline style
3. id 선택자(`#`)
   - 대부분 다른 선택자보다 우선순위가 높아 다루기 어려움
   - `class`선택자로 작성하는 것이 좋음
   - 만약 문서 내 `링크이동`이나 `for`를 사용하는 특별한 경우에만 아이디 사용
4. class 선택자(`.`)
5. 요소 선택자
   - 전체선택자(`*`)
6. 소스 순서



### CSS상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속함

- 속성 중에는 상속이 되는 것과 되지 않는 것들이 있음

- 상속 되는 것

  - TEXT관련 요소 등

- 상속되지 않는 것

  - Box model관련 요소(width, height, margin, padding, border, display)
  - position 관련 요소

  

### CSS 단위

#### (상대) 크기 단위

**px**

- 모니터 해상도의 한 화소인 '픽셀'을 기준
- 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

**%**

- 백분율 단위
- 가변적인 레이아웃에서 자주 사용

**em**

- em은 상속의 영향 받음, rem은 최상위 요소(html)를 기준으로 결정됨.
- 상황에 따라 각기 다른 값을 가짐
- 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

**rem**

- 최상위 요소인 html(root em)을  절대 단위를 기준으로 삼음. 상속의 영향을 받지 않음.
- 상속에 영향을 받지 않기 때문에 대부분의 경우 `rem` 을 많이 사용
- 배수 단위를 가짐

##### em VS rem

```html
(전략..)
  <style>
    .em {
      font-size: 1.5em;
    }
    .rem {
      font-size: 1.5rem; 
    }
  </style>
</head>
<body>
  <ul class="em"> 
    <li class="em">em</li>
    <li class="rem">rem</li>
    <li>no class</li>
  </ul>
</body>
</html>
```

- 둘 다 사이즈를 같게 설정했지만 실제 출력값은 다름
- 위 코드의 `.em`은 실제 폰트가 36px(`16(html의 기본폰트)*1.5*1.5(부모사이즈)`)
  - 부모에 사이즈가 em으로 설정돼있음, em을 쓰면 고정이 안될 수 있음 rem을 쓰면 내가 원하는 값 나옴 em은 부모와 상대적 크기비교 때 사용
- 위코드 `.rem` : 24px(`16*1.5`)

**viewport**

- (스크롤을 내리지 않은 상태에서) 웹 페이지를 방문한 유저에게 현재 보이는 웹 컨텐츠의 영역
- viewport를 기준으로한 상대적인 사이즈
- 주로 스마트폰이나 테블릿 디바이스의 화면을 일컫는 용어로 사용됨
- vw, vh



**색상 표현 단위**

1. 색상 키워드
   - 색상 키워드는 대소문자를 구분하지 않는 식별자로
   - red, blue, black처럼 특정 색을 나타냄
2. RGB 색상
   - 빨강, 초록, 파랑을 통해 특정 색을 표현
   - 16진수 표기법이나 함수형 표기법으로 사용
   - a는 alpha(투명도)가 추가된 것
3. HSL 색상
   - 색상, 채도, 명도를 통해 특정 색상을 표현
   - a는 alpha(투명도)가 추가된 것



## Box Model

> 웹 디자인은 contents를 담을 box model을 정의하고 CSS 속성을 통해 스타일(배경, 폰트와 텍스트 등)과 위치 및 정렬을 지정하는 것.

![image-20200822202125048](WEB 과목평가 정리.assets/image-20200822202125048.png)

- 모든 HTML 요소는 box 형태
- 하나의 박스는 네 부분(영역)으로 이루어 진다.
  - content / padding / border / margin

1. Content
   - 글이나 이미지, 비디오 등 요소의 실제 내용
   - `width`와 `height`와 같은 속성을 사용해서 정할 수 있음
2. Padding (안쪽 여백)
   - Border(테두리) 안쪽의 내부 여백
   - 배경색, 이미지 지정 가능
   - 콘텐츠 주변을 마치 공백처럼 자리잡음
3. Border(테두리)
   - 콘텐츠와 패딩까지 둘러쌈
     - 테두리의 크기와 스타일은 `border`와 관련 속성을 사용하여 제어할 수 있음
4. Margin (바깥쪽 여백)
   - 테두리 바깥의 외부 여백
   - 배경색 지정 불가

**마진 상쇄**

- block의 top 및 bottom margin이 결합되는 마진 중 크기가 가장 큰 한 마진으로 결합(상쇄)됨

##### Box model 구성

- 상하좌우

```
.margin-1{
margin:10px;
}
```

- 상하/좌우

```
.margin-2{
margin:10px 20px;
}
```

- 상/좌우/하

```
.margin-3{
margin:10px 20px 30px;
}
```

- 상/우/하/좌(시계방향)

```
.margin-4{
margin:10px 20px 30px 40px;
}
```

#### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box의 크기!
  - padding을 제외한 순수 contents영역만을 box로 설정
- 일반적으로 영역을 볼 때는 border까지의 너비를 100px보는 것을 원함
  - 그 경우 box-sizing을 border-box로 설정
  - 이 말은 border까지의 box 크기를 정한다는 말.
- 보통 CSS최상단에서 보더박스를 전체선택자(`*`)로 다 적용해주고 시작

## Display

> display CSS 속성은 요소를 블록과 인라인 요소 중 어느 쪽으로 처리할지와 함께 자식 요소를 배치할 때 사용할 레이아웃을 설정

**block**

- 위에서 밑으로 쌓이는 박스
- 요소는 블록 요소 상자를 생성하여 일반 흐름에서 요소 앞뒤에 줄 바꿈을 생성
- 블록 레벨 요소안에 인라인 레벨 요소가 들어갈 수 있음
- width와 height가 적용됨
- 한 줄에 적용됨
- div / ul, ol, li/ p/ hr/ form 등

**inline**

- 줄바꿈이 일어나지 않는 행의 일부 요소
- content 너비만큼 가로 폭을 차지
- width, height, margin-top, margin-bottom을 지정할 수 없음
- 상하 여백은 line-height로 지정
- 옆으로 쌓임
- **```**은 인라인이기 떄문에 전체 문단이 끊기지 않고 하나로 그려짐
- 보통 인라인 요소는 데이터와 다른 인라인 요소만 포함할 수 있으며, 블록 요소는 포함할 수 없음
- 링크용`<a>`요소와 `<span>`, `<em>` 및 `<strong>`요소는 모두 기본적으로 인라인으로 표시됨
- ex) span / a / img / input, label / b , em, i, strong 등

**inline-block**

- inline 처럼 텍스트 흐름대로 나열, block처럼 박스 형태이기 block 속성 사용가능.
- 옆으로 쌓이는데 block의 특성도 갖춰 width와 height가 적용됨
- `padding`, `margin`과 `border`속성으로 인해 다른 요소가 상자에서 밀려남

**none**

- 해당 요소를 화면에서 사라지게 하며 요소의 공간조차 사라지게 함
- `visibility: hidden;`은 해당 요소를 화면에서 사라지게는 하나 공간은 사라지지 않음

| 속성에 따른 수평 정렬 | block                               | inline             |
| --------------------- | ----------------------------------- | ------------------ |
| 왼쪽 정렬             | margin-right:auto;                  | text-align:left;   |
| 오른쪽 정렬           | margin-left:auto;                   | text-align:right;  |
| 가운데 정렬           | margin-right:auto;margin-left:auto; | text-align:center; |



## Position

- 문서 상에서 요소를 배치하는 방법을 지정

  

**박스의 위치 속성 & 값**

- position
  - static / absolute / relative / fixed
  - z-index

**기본 개념**

1. static (기본 위치)
   - 모든 태그의 기본
   - 태그의 default 값
2. relative (상대 위치)
   - 기본 위치(static)를 기준으로 좌표 속성을 사용해 위치 이동
   - top과 bottom은 원래 위치에서의 세로축 거리
   - left와 right는 원래 위치에서의 가로축 거리를 지정
   - 이전의 기존 위치도 기억(static)하고 있어, 다른 것들의 위치는 바뀌지 않음
3. absolute (절대 위치)
   - static 이 아닌 가장 가까운 부모/조상 요소를 기준으로 좌표 속성 만큼 이동
   - 부모 요소를 찾아가고 나아가 없다면 body에 붙는다
   - top, right, bottom, left는 요소의 컨테이닝 블록 모서리로부터 거리를 지정
     - 요소의 크기와 위치는 컨테이닝 블록의 영향을 자주 받음
     - 백분율 값을 사용한 width, height, padding, margin 속성의 값과 절대적 위치로 설정된 요소의 오프셋 속성 값은 자신의 컨테이닝블록으로부터 계산됨
     - height와 width가 auto로 지정된 절대 위치 지정 요소는 내용에 맞도록 크기를 조절
   - 비대체 절대위치 지정요소는 top과 bottom을 지정하고, height는 지정하지 않음(auto)으로 사용 가능한 수직 공간을 채울 수 있음
   - `left`와 `right`를 지정하고, `width`는 `auto`로 두면, 사용 가능한 모든 수평 공간을 채움
   - `top`과 `bottom`을 지정한 경우(`auto`가 아니라면), `top`이 우선 적용
   - 요소가 바깥 여백을 가진다면 거리에 더함
   - 절대 위치 지정요소는 새로운 블록 서식 맥락을 생성
4. fixed (고정 위치)
   - 부모/조상 요소와 관계없이 브라우저의 viewport를 기준으로 좌표 속성 만큼 이동
   - 스크롤을 내리거나 올려도 화면에서 사라지지 않고 항상 같은 곳에 위치

**absolute**

- `absolute`는 원래 위치해 있었던 과거 위치에 있던 공간은 더 이상 존재하지 않는다는 점이 특징
- 다른 모든 것과는 별개로 독자적인 곳에 놓임
- 언제 쓸까?
  - 페이지의 다른 요소의 위치와 간섭하지 않는 격리된 사용자 인터페이스 기능을 만들 수 있음
  - 팝업 정보 상자 및 제어 메뉴, 롤오버 패널, 페이지 어느 곳에서나 끌어서 놓기할 수 있는 유저 인터페이스 페이지 등

```css
##relative인 bigbox기준으로 아래의 absolute인 box들이 위치함
.big-box {
  position: relative;
  margin: 100px auto 500px;
  border: 5px solid black;
  width: 500px;
  height: 500px;
}

.small-box {
  width: 100px;
  height: 100px;
}

#red {
  background-color: red;
  position: absolute;
  bottom: 0px;
  right: 0px;

  /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
  
}

#gold {
  background-color: gold;
  position: fixed;
  right: 50px;
  bottom: 50px;
  /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
  
}

#green {
  background-color: green;
  position:absolute;
  top: 0;
  left: 0;
  bottom:0;
  right:0:
  margint:auto;
  
}

  /* 큰 사각형의 가운데 위치시키기 */


#blue {
  background-color: blue;
  position: absolute;
  top: 100px;
  left: 100px;
  /* 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 */

}

#pink {
  background-color: pink;
  /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
  position: absolute;
}
```





### CSS styling

- `border-box` VS `content-box`
  - `border-box`는 테두리와 안쪽 여백의 크기도 요소의 크기로 고려
  - 너비를 100 픽셀로 설정하고 테두리와 안쪽 여백을 추가하면, 콘텐츠 영역이 줄어들어 총 너비 100 픽셀을 유지
  - 대부분의 경우 이 편이 크기를 조절할 때 쉬움
  - `content-box`는 기본 CSS 박스 크기 결정법을 사용
  - 요소의 너비를 100 픽셀로 설정하면 콘텐츠 영역이 100 픽셀 너비를 가지고, 테두리와 안쪽 여백은 이에 더해짐
- `font-family` : 글꼴 설정
- `border-style` : 테두리 스타일
- `text-aline` : 인라인 정렬
- `width : 100%`
  - 크기를 꽉 채우게 줌

### CSS layout

> 웹페이지에 포함되는 요소들을 취합하고 그것들이 어느 위치에 놓일 것인지 제어하는 기술

### float

- float된 이미지 좌, 우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입
- 이미지가 아닌 다른 요소들에도 적용해 웹 사이트의 전체 레이아웃을 만드는데까지 발전
- 기본값 : none
- `left` 요소를 왼쪽으로 띄움, `right` 오른쪽으로 띄움 ( 우리 얼굴방향으로 띄운다고 생각하면 됨)

#### floatclear 방법

- float를 했을 때 위로 떠서 그 아래공간으로 다른 요소들이 치고 들어가 겹쳐질 수 있음
- 해결하려면 여러 방법이 있지만
- 가장 정석 float로 띄운 것 뒤에 가상의 박스를 둔다고 생각하면 됨
- float는 인라인 요소, 텍스트 요소를 감싸는 것, 그래서 그렇지 않은 것들이 겹쳐 질 수 있음
- 가상 높이를 만들어 부모가 만든 높이를 만들어줌

1. 항상 float속성을 적용한 요소의 부모 요소에 적용함
2. 보통 이런 현상을 해결하기 위한 스타일 이름은`.clearfix`라고지음
3. `header `태그 다음에 가상요소(`::after`)로 내용이 빈 블럭을 만들고
4. 이 가상요소는 `float left, right(both)`를 초기화 한다(무시한다=띄운거를 무시함)
5. 내용이 빈 컨택트를 만듦
   - (참고)content에 단어를 적는다면 content하나하나의 뒤에 들어감
6. 다른요소가 올라오지 못하게 블락으로 설정
7. 오른쪽 왼쪽 둘다 오지못하게 막음

```html
<style>
    .left {
      float: left;
    }
    .clearfix::after {
      content: "";
      display: block;
      clear: both;
    }
</style>
<body>
 
  <header class="clearfix">
    <div class="box1 left">div</div>
  </header>
  <div class="box2">div</div>
</body>
```



### flexbox(CSS flexible box layout)

- float는 flexbox나 grid 가 나오기 전에 나옴
- 단순히 텍스트를 감싼다는 기본적 목적으로 주로 많이 쓰임
- 그 원인이 flexbox라는 기술이 나왔기 때문
- 요소 간 공간 배분과 정렬 기능을 위한 1차원(단방향)레이아웃
- 뷰포트나 요소의 크기가 불명확하거나 동적으로 변할 때 효율적으로 요소를 배치, 정렬, 분산할 수 있는 방법을 제공하는 레이아웃 방식
- 복잡한 계산 없이 요소의 크기와 순서를 유연하게 배치할 수 있음
- 정렬, 방향, 순서, 크기 등을 유연하게 조절할 수 있기 때문에 별도의 분기 처리를 줄일 수 있음
- 복수의 자식요소인 `flex item`과 그 상위 부모 요소인 `flex container`로 구성됨
- 반드시 알아야할 것! 요소, 축
- 요소
  - flex container(부모 요소)
  - flex item(자식요소)
- 축
  - main axis(메인축)
  - cross axis(교차축)

- [자세한 내용은 `0812_web`정리 참고](https://github.com/irissooa/irissooa-TIL/blob/master/web/0812_web.md)

```html
<style>
      /* 부모한테 display flex를 주는 것이 시작 */
    .flex-container {
      display: flex;
/* 부모가 정한 너비를 넘치지 않게함, 넘으면 떨어뜨림 */
      flex-wrap: wrap;
      /* 기본값  row */
      flex-direction: row;
      /* 쌓이는 방향이 바뀜 321 */
      flex-direction: row-reverse;
      /* 메인이 y축으로 바뀜 */
      flex-direction: column;
      /* 아래에서 위로 쌓아 올라가는 모습 */
      flex-direction: column-reverse;
      /* flex-direction과 flex-wrap의 약어 */
      flex-flow: column wrap;
</style>
```



```html
<style>
	/* 정렬시작 */
    /* 메인축 정렬 */
    /* 이게 기본값 */
    justify-content: flex-start;
    /* 흐름의 방향은 바뀌지 않고 정렬만 바꼈기 때문에 순서는 그대로, 우측정렬됨 */
    justify-content: flex-end;
    /* 메인축 기준으로 가운데로 옴 */
    justify-content: center;
    /* 처음과 끝을 각 끝으로 보내고 가운데 것들을 균등하게 나눔 */
    justify-content: space-between;
    /* 균등 좌우 정렬 내부요소의 여백이 외부요소의 여백의 2배 */
    justify-content: space-around;
    /* 균등정렬 균등하게 띄워져 있음 내부요소 여백과 외부요소 여백이 같음*/
    justify-content: space-evenly;

</style>
```



```html
<style>
/* 크로스축 정렬(현재 y축) */
    /* 원래 div 크기대로 줄어듬 위쪽이 스타트기 때문에 붙어있음*/
    align-items: flex-start;
    /* 크로스축 기준 아래 */
    align-items: flex-end;
    /* 상하기준으로 중간 */
    align-items: center;
    /* 글자들의 크기가 달라져야 바뀜 (baseline 구글 사진 찾기)*/
    align-items: baseline;
</style>
```



## Flexbox 용어정리

#### justify-content

- flex-start: 요소들을 컨테이너의 왼쪽으로 정렬
- flex-end: 요소들을 컨테이너의 오른쪽으로 정렬
- center: 요소들을 컨테이너의 가운데로 정렬
- space-between: 요소들 사이에 동일한 간격을 둠
- space-around: 요소들 주위에 동일한 간격을 둠

#### align-items

- flex-start: 요소들을 컨테이너의 꼭대기로 정렬
- flex-end: 요소들을 컨테이너의 바닥으로 정렬
- center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬
- baseline: 요소들을 컨테이너의 시작 위치에 정렬
- stretch: 요소들을 컨테이너에 맞도록 늘림

#### flex-direction

- row: 요소들을 텍스트의 방향과 동일하게 정렬
- row-reverse: 요소들을 텍스트의 반대 방향으로 정렬
- column: 요소들을 위에서 아래로 정렬
- column-reverse: 요소들을 아래에서 위로 정렬

#### order

- 때때로 컨테이너의 row나 column의 순서를 역으로 바꾸는 것만으로는 충분하지 않음
- 이러한 경우에는 order 속성을 각 요소에 적용가능
- order의 기본 값은 0이며, 양수나 음수로 바꿀 수 있음

#### flex-wrap

- nowrap: 모든 요소들을 한 줄에 정렬
- wrap: 요소들을 여러 줄에 걸쳐 정렬
- wrap-reverse: 요소들을 여러 줄에 걸쳐 반대로 정렬

#### flex-flow

- flex-direction + flex-wrap

#### align-content

- 여러 줄들 사이의 간격을 지정
- `align-items`는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정
- 한 줄만 있는 경우, `align-content`는 효과를 보이지 않음

## Bootstrap

- 다양한 브라우저에서 동일한 모양으로 페이지를 보이게 함

- fixed top : z-index 얼굴쪽으로 쏘는 방향이 z축 위에 와야되니까 그냥 큰값을 준거임

- sticky top..fixed처럼 브라우저에 고정이 되는데 계속 그자리에서 대체되지 않는것이 아니라 다음 sticky top을 만나면 바뀜

- 부트스트랩 공식문서를 보며 익히기...

## Grid system

- 반드시 기억해야할 2가지
- 12개의 column
- 12는 약수가 가장 많다
- 1,2,3,4,6,12 비율을 나눌때 다양하게 레이아웃을 나눌 수 있음
- 5개의 grid breakpoints
- class="row" -> display :flex가 선언이 돼있음
- google news는 정돈이 잘돼있음, 시멘틱태그, 그리드시스템 잘씀
- 12개의 column으로 나뉘어져 있음

**offset**

- `offset-*` 은 지정한 만큼의 column 공간을 무시하고 다음 공간부터 컨텐츠를 적용한다.



