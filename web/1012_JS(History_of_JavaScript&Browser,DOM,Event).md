# JavaScript

> [kakao tech](https://tech.kakao.com/2020/09/21/kakao-fe-platform-team/)

> History of JavaScript & Browser,
>
> DOM(Document Object Model),
>
> Event(Listener))

> **API Server**
>
> - Request & Response
> - 데이터 응답(JSON)
>
> **DRF(Django REST Framework)**
>
> - API Server 개발을 위한 프레임워크
>
> **RESTful**
>
> - 자원(URI)
>   - 자원을 표현
>   - 계층 구조
> - 행위(HTTP Method)
>   - GET,POST,PUT/PATCH,DELETE
> - 표현(Representations)
>   - Data, Metadata of data
>   - 응답 데이터(JSON)
>
> **JSON(JavaScript Object Notation)**
>
> - JavaScript의 자료구조 중 하나인 object의 표기법을 따른 데이터 교환 포맷
> - key와 value의 조합
>   - {'key':'value'}
> - 데이터를 교환할 때 사용하는 양식(약속)
> - 단순 문자열
> - 개발 환경에 맞는 자료형으로 변환 후 활용



## History of JavaScript & Browser

> WHY JavaScript??
>
> 브라우저 화면을 **동적**으로 만들기 위해서!!
>
> 브라우저 조작을 위한 것
>
> Browser : 문자열에 불과한 것을 보기좋게 보여줌
>
> 두 아버지
>
> - 팀 버너스리(www,http,uri)
>
> - 브랜던 아이크(javascript)

- 1994년 네스케이프사의 Netscape Navigator(NN) 브라우저가 표준
- 정적인 HTML을 동적으로 표현하기 위한 언어 도입을 결정
- 1995년 브랜던 아이크 주도로 개발된 'Mocha'를 자체 브라우저에 도입(10일만에 만듦)
- 이후 LiveScript라는 이름을 거쳐 지금의 JavaScript로 변경(`!=java`)

- MS의 폭발적 성장, IE(Internet Explore)3에서 자체적인 JScirpt를 지원, 호환성 문제로 크로스 브라우징 등의 이슈 발생(1차브라우저전쟁 :`IE vs NN` 이후에는 2차 `IE vs Chrome`)
- 이후 Netscape 후계자들은 모질라 재단 기반의 Firefox를 개발

- 계속되는 파편화를 방지하고 모든 브라우저에서 동일하게 동작하기 위한 표준의 필요성 제기
- Netscapte는 ECMA 인터네셔널에 기술 규격을 제출한 이후 표준 제정에 대한 논의 지속
  - Ecma 인터내셔널은 정보와 통신 시스템을 위한 국제적 표준화 기구
- Google Chrome등장
  - 왜 크롬이 빠른가?
  - JavaScript의 문제가 아니라 **엔진**이 문제!

- JS의 한계
  - 브라우저를 조작하는 언어이기 때문에 브라우저 밖을 벗어날 수 없음!
  - `Node JS` 라는 새로운 Runtime 환경이 등장 -> 브라우저 밖에서도 쓸 수 있음!
- Chrome등장 이후 여러 과정을 거쳐 자바스크립트의 고질적 문제를 많이 해결한 ES2015(ES6)등장
- ECMAScript6(ES6)는 기존 코드를 간결하게 작성할 수 있는 새로운 문법들이 추가되면서 더욱 발전할 수 있는 발판을 만듦
  - Arrow function
  - const, let
  - Promise
  - Object 축약 문법

- **Cross Browsing Issue**
  - jQuery
    - 다양한 브라우저를 신경쓸것없이 알아서 대응을 해줌!
  - Vanilla JavaScript
    - 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장(대표적 jQuery)
    - 최근 표준화된 브라우저, ES6 이후의 다양한 도구의 등장으로 순수 자바스크립트 활용의 증대
    - 브라우저에 내장돼있기 때문에 설치가 필요없고 굉장히 빠름

### 결론

> 1. 브라우저 전쟁
> 2. **파편화 & 표준화의 투쟁**
> 3. 브라우저 전재의 여파
> 4. **Cross Browsing Issue**
> 5. **표준화(통합)을 위한 노력(**ex. jQuery)
> 6. **Vanilla JavaScript**

#### (1) Summery

- Javascript는 브라우저를 동적으로 사용하기 위해 고안된 언어다.
- Java와 Javascript는 서로 완전히 다른 언어다. 즉, 둘은 전혀 관련/유사성이 없다.
- ECMA Script(ES)는 브라우저마다 파편화 되어가는 JS 생태계를 묶기 위해 ECMA가 제시한 표준안이다. 즉 ES6는 ECMA가 제안하는 JS의 표준 Ver.6 라는 의미!
- 현재 Javascript는 ES5(2009)에서 ES6+(2015~)로 넘어가는 중이다.(아직도 ES5 표준으로 작성된 참고자료가 많다.)
- IE는 HTML5 표준과 ES6 표준 두 가지 모두 매우 안 지킨다.
- 브라우저 콘솔에서 바로 사용할 수 있는 JS를 Vanilla JS라고 부른다.(Vanilla 아이스크림 === 순정)
- Vanilla JS는 프로그래밍을 통해 BOM 조작, DOM 조작을 할 수 있다.
- 브라우저라는 제한된 환경을 넘어 브라우저 밖(컴퓨터)에서 JS를 구동할 수 있는 새로운 실행 환경인 `Node.js`가 등장한다. (Node.js 환경에서는 당연히 DOM, BOM 조작 불가능)



#### (2) Vanilla JS vs Node.js

- Vanilla JS
  - 브라우저 콘솔 환경에서 사용하는 가장 순정의 JS를 의미
  - 어떠한 라이브러리/프레임워크에도 의존하지 않는 Original Browser JS라고 할 수 있다.
  - BOM(Browser Object Model) 조작, DOM(Document Object Model) 조작, 프로그래밍 가능
- Node.js
  - 브라우저 밖에서 JS를 구동할 수 있는 새로운 JS 실행환경(runtime environment)인 `Node.js`가 등장
  - V8 엔진을 기반으로 제작되었으며, Node.js의 등장을 통해 JS 만으로 클라이언트-서버 를 모두 제작할 수 있게 되었다.



### 브라우저에서 할 수 있는 일

- DOM조작
  - 문서(HTML)조작
- BOM 조작
  - navigator, screen,location,frames,history,XHR
- JavaScript Core(ECMAScript)
  - Data Structure(Object,Array), Conditional Expression, Iteration



----------

## DOM(Document Object Model)

> 문서 객체 모델
>
> 무언가를 객체처럼 다뤄서 조작(속성,메소드)
>
> ![image-20201012104916399](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012104916399.png)
>
> **DOM TREE**
>
> ![image-20201012104950106](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012104950106.png)

- HTML, XML 등과 같은 문서를 다루기 위한 언어 독립적인 문서 모델 인터페이스

- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 도우며, 구조화된 노드와 오브젝트로 문서를 표현

- 주요 객체

  - **window : DOM을 표현하는 창, 가장 최상위 객체(`모든 객체의 부모`)**

  - document :  페이지 콘텐츠의 Entry Point 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen

- 브라우저마다 각자의 방법으로 DOM을 구현
- 모든 문서의 노드들은 'DOM Tree'라고 불리는 트리 구조의 모습을 나타냄
- 브라우저 사이에 DOM구현이 호환되지 않음에 따라, W3C에서 DOM표준 규격을 작성
- DOM은 문서의 기반이 되는 데이터 구조에 제한을 두지 않지만, 잘 구조화된 문서는 DOM을 사용해 트리 구조를 얻어낼 수 있다(마크업의 중요성)
- 스크립트를 작성할 때 문서 조작을 위해 document혹은 window객체를 사용할 수 있음
  - **window 객체는 생략 가능**

![image-20201012105501664](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012105501664.png)

![image-20201012105523547](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012105523547.png)

![image-20201012105548252](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012105548252.png)



### DOM 조작

#### Selection

> 여기서 우리는 아래 두개를 주로 사용할거얌
>
> 1개 : querySelector()
>
> 여러개 : querySelectorAll()
>
> (참고)
>
> getElementById는 왜 안쓰냐?
>
> 여러가지 이유가 있지만, 이건 id로 밖에 못잡음, 하지만 querySelector는 복합선택자이고 유연성이 있음 그래서 querySelector를 주로 사용할거얌
>
> querySelector 했을때 해당되는 class가 여러개 있을 때는 제일 첫번째 것을 가져옴

- **단일 Node**

  - document.getElementById(id)

  - document.querySelector(selector)

- **HTMLCollection(live)**

  - document.getElementsByTagName(tagName)
  - document.getElementsByClassName(class)

- **NodeList(non-live)**

  - document.querySelectorAll(selector)

![image-20201012110605668](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012110605668.png)

#### Manipulation

- **innerText**
  - 텍스트
- **innerHTML**
  - XSS공격에 취약점이 있으므로 사용시 주의
- **Node attribute**
  - element.style.backgroundColor
  - setAttribute(attributeName,value)
  - getAttribute(attributeName)

![image-20201012110440269](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012110440269.png)

- **특정 태그를 생성**
  - Document.createElement(tagName)
- **마지막 자식 요소로 추가**
  - ParentNode.appendChild(Node)
- **해당 요소를 제거**
  - ParentNode.removeChild(child Node)

![image-20201012110811068](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012110811068.png)



##### innerText vs innerHTML

![image-20201012110851134](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012110851134.png)![image-20201012110911695](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012110911695.png)



#### 정리

1. 선택한다
   - querySelector()
   - querySelectorAll()
2. 변경한다
   - innerText
   - innerHTML
   - etc..



### DOM 조작

#### basic DOM Manipulation

> javascript는 script로 조작함
>
> 자바스크립트 주석은 `//` 여러줄은 `/* 여기사이에 적으면 됨 */`

```html
<body>
  <h1 id="header">DOM Manipulation</h1>
  <h2 id="langHeader">Programming Languages</h2>
  <ul>
    <li class="lang">Python</li>
    <li class="lang">Java</li>
    <li class="lang" id="specialLang">JavaScript</li>
  </ul>

  <h2 id="frameHeader">Frameworks</h2>
  <ul>
    <li class="framework" id="specialFrame">Django</li>
    <li class="framework">Spring</li>
    <li class="framework">Vue.js</li>
  </ul>
```

##### 1. Selection - querySelector / querySelectorAll
###### 1-1. window & document

```javascript
  <script>
    
    //console.log(console에 log찍어줘)는 print와 같은 기능
    console.log(window)
    console.log(document)
    // window는 생략가능
    console.log(window.document)

```

![image-20201012123047929](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012123047929.png)



###### 1-2. querySelector

```javascript
    const mainHeader = document.querySelector('h1')
    // # 은 id
    const langHeader = document.querySelector('#langHeader')
    const frameHeader = document.querySelector('#frameHeader')
    console.log(mainHeader, langHeader, frameHeader)
```

![image-20201012123113363](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012123113363.png)



###### 1-3. querySelectorAll

```javascript
    // . 은 class// 그리고 여러개 요소라면 제일 첫번째 요소를 반환
    const langLi = document.querySelectorAll('.lang')
    const frameworkLi = document.querySelectorAll('.framework')
    console.log(langLi, frameworkLi)
```

![image-20201012123310568](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012123310568.png)



###### 1-4. 여러 개의 요소 -> 첫 번째로 일치하는 요소

```javascript
    const selectOne= document.querySelector('.lang')
    console.log(selectOne)
```

![image-20201012123623179](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012123623179.png)



###### 1-5. 복합 선택자

> querySelector

```javascript
    // 자손선택자
    const selectDescendant = document.querySelector('body li')
    // 자식선택자
    const selectChild = document.querySelector('body > li')
    console.log(selectDescendant) 
    console.log(selectChild) 
```

![image-20201012123757023](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012123757023.png)

> querySelectorAll

```javascript
    // 자손선택자
	const selectDescendant = document.querySelectorAll('body li')
    // 자식선택자
    const selectChild = document.querySelector('body > li')
    console.log(selectDescendant) 
    console.log(selectChild) 
```

![image-20201012123844086](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012123844086.png)

###### 1-6. getElementById, getElementByClassName 

```javascript
    const selectSepcialLang = document.getElementById('specialLang')
    const selectAllLangs = document.getElementsByClassName('framework')
    const selectAllLiTags = document.getElementsByTagName('li')
    console.log(selectSepcialLang, selectAllLangs, selectAllLiTags)
```

![image-20201012123921514](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012123921514.png)



##### 2. Manipulation
###### 2-1. Creation

```javascript
    // 태그만 나옴
    const browserHeader = document.createElement('h2')
    const ul = document.createElement('ul')
    const li1 = document.createElement('li')
    const li2 = document.createElement('li')
    const li3 = document.createElement('li')
    console.log(browserHeader, li1, li2, li3) 
```

![image-20201012124056070](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124056070.png)

  ###### 2-2. innerText & innerHTML / append & appendChild

```javascript
    // 태그안에 속성을 바꿔 내용을 적음
    browserHeader.innerText = 'Browsers'
    li1.innerText = 'IE'
    // innerText는 <strong>이거까지 다 나오지만 HTML은 chrome만 나옴
    li2.innerText = '<strong>FireFox</strong>'
    li3.innerHTML = '<strong>Chrome</strong>'
    console.log(browserHeader, li1, li2, li3)
```

![image-20201012124147037](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124147037.png)

###### 2-3. append DOM 

> ul태그에 li1, li2 li3을 붙임

```javascript
    // 문서에 붙여넣는 과정
    const body = document.querySelector('body')
    body.appendChild(browserHeader)
    body.appendChild(ul)
	
    ul.append(li1, li2, li3) 
```

![image-20201012124238777](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124238777.png)

> 이건 여러개 붙여도 가장 앞에 하나만 붙임

```javascript
    const body = document.querySelector('body')
    body.appendChild(browserHeader)
    body.appendChild(ul)
    
    ul.appendChild(li1, li2, li3) 
```



![image-20201012124341891](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124341891.png)

###### 2-4. Delete

```javascript
    // 잡아서 삭제를 함
    // removeChild
    // ul에 li1을 removeChild를 이용해서 삭제함
    ul.removeChild(li1) 
```

![image-20201012124656366](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124656366.png)

```javascript
    ul.removeChild(li2)
```

![image-20201012124718732](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124718732.png)

>   이건 안에 넣는 인자 없이 해당요소를 전부 날림, ul태그 밑을 다 날림

```javascript
     ul.remove()
```

![image-20201012124826709](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124826709.png)

>  body태그 밑을 다 날림

```javascript
    body.remove()
```

![image-20201012124906585](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012124906585.png)

###### 2-5. Element Styling

```javascript
    // 객체 안의 속성에 접근해서 style을 적용한거
    li1.style.cursor = 'pointer'
    li2.style.color = 'blue'
    li3.style.background = 'red'
```

![image-20201012125001383](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012125001383.png)

>  setAttribute

```javascript
    // 세팅
    // id속성을 king으로 넣겠다, 실제 속성값을 style할 수 있음
    li3.setAttribute('id', 'king')
```



![image-20201012125041374](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012125041374.png)

>  getAttribute

```javascript
      // li태그 style을 가져옴
    const getAttr = li1.getAttribute('style')
    // const getAttr2 = li3.getAttribute('style')
    console.log(getAttr)
    // console.log(getAttr2)
```



![image-20201012125223807](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012125223807.png)

> getAttribute

```javascript
    // li태그 style을 가져옴
    const getAttr = li1.getAttribute('style')
    const getAttr2 = li3.getAttribute('style')
    console.log(getAttr)
    console.log(getAttr2)
```



![image-20201012125426207](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012125426207.png)



--------

### DOM 조작 practice

> Before
>
> ![image-20201012135304054](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012135304054.png)
>
> After
>
> ![image-20201012135249303](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012135249303.png)

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>my first markup</title>
  <style>
	  #main {
	    background-color: rgba(197, 255, 251)
	  }
	
	  .box-container {
	    display: flex;
	    justify-content: center;
	    align-items: center;
	  }
	
	  .box-item {
	    margin: 20px;
	    padding: 30px;
	    border-radius: 10px;
	    width: 600px;
	    background-color: white;
	  }
	
	  .button {
	    background-color: rgba(45, 166, 153);
	    border-radius: 4px;
	    color: white;
	    padding: 10px 20px;
	    margin: 20px;
	    cursor: pointer;
	    font-size: 15px;
	  }
	
	  .footer {
	    margin-top: 14vh;
	  }
	</style>
</head>
<body>
  <header>
    <a href="https://www.ssafy.com">
      <img src="ssafy.png" alt="싸피 이미지" width="300px">
    </a>
    <h1>SSAFY 4기 학생 건강설문</h1>
  </header>
  <section>
    <form action="#" method="GET">
      <div>
        <label for="name">이름을 기재해주세요.</label><br>
        <input type="text" id="name" placeholder="실명을 작성해주세요." autofocus>
      </div>
      
      <div>
        <label for="region">지역을 선택해주세요.</label>
        <select name="region" id="region" required>
          <option value="">선택</option>
          <option value="서울" disabled>서울</option>
          <option value="대전">대전</option>
          <option value="광주">광주</option>
          <option value="구미">구미</option>
        </select>
      </div>
      
      <div>
        <p>오늘의 체온을 선택해주세요.</p>
        <input type="radio" name="body-heat" id="normal" value="normal" checked>
        <label for="normal">37도 미만</label>
        <input type="radio" name="body-heat" id="warning" value="warning">
        <label for="warning">37도 이상</label>
      </div>

      <input type="submit" value="제출하기">
    </form>
  </section>

  <!-- <footer>
    Google 설문지를 통해 비밀번호를 제출하지 마시오.
  </footer> -->
  
  <script>
    // const로 지정된 것은 재할당이 불가능 함, mainBackground라는 변수에 body를 가져와 넣음
    const mainBackground = document.querySelector('body')
    //console은 파이썬의 print
    console.log(mainBackground)
    // mainBackground의 id 선택자로 main을 적용함
    mainBackground.id = 'main'
    // 변수 설정시 const가 오고 쿼리셀렉터(딱하나만 가져옴, header가 여러개더라도 위에서 부터 읽어서 젤처음 만나는 것을 가져옴)뒤에 tag이름 적음
    // 여러개를 가져오는 것은 queryselectorall
    const header = document.querySelector('header')
    const section = document.querySelector('section')
    console.log(header)
    console.log(section)
    // header와 section에 class container를 적용해줄거야
    header.className = 'box-container'
    section.className = 'box-container'
    // 보통을 className보다(원래있는 class를 안건드리기 위해) classList.add를 통해 class를 추가
    header.classList.add('my-class')
    // display column으로 하면 display flex로 그림과 글이 옆으로 표시되는것을 아래위로 바꿀 수 있음
    header.style.flexDirection = 'column'
    
    // 각 div에 class지정, 
    // const mainFormDivList = document.querySelector('div') 
    // 이렇게만 하면 맨 처음 div만 적용
    // console.log(mainFormDivList)
    // 모든 div를 가져오려면 queryselectall 사용
    const mainFormDivList = document.querySelectorAll('div') 
    console.log(mainFormDivList)
    // js에도 for문 사용 가능 
    // forEach는 각각의 item에 이 function을 각각 실행한다
    mainFormDivList.forEach(function (div){
      // 중괄호 안에 할일을 적으면 됨(className을 사용하면 이전에 있던 class도 다 지워지고 className으로 적용한 class만 적용됨)
      // className = 'box-item footer' 이렇게 적으면 두개 다 적용은 되지만 이전에 있던class는 지워짐
      div.classList.add('box-item')
    })
    // 다른 input은 form태그 직계 자손이 아님
    // 제일 마지막 제출 버튼은 form태그 직계자손임 이렇게 해도 되고
    const submitButton = document.querySelector('form > input')
    // 이렇게 적어도 됨
    // const submitButton = document.querySelector('input[type="submit"]')
    submitButton.classList.add('button')

    // class통한 것 말고 직접적으로 style변화를 줄 수도 있음
    // id로 가져올 수 있음 ex) id='name'
    const nameInput = document.querySelector('#name')
    // css에서는 margin-top이렇게 썼지만 js는 - 를 허용하지 않기 때문에 그부분을 대문자로 바꿔 marginTop이렇게 씀
    nameInput.style.marginTop = '7px'
    nameInput.style.padding = '10px'
    // nameInput.style.paddingLeft = '15px'

    const regionSelect = document.querySelector('#region')
    // 선택하는것을 밑으로 깔고 싶다
    regionSelect.style.display = 'block'
    regionSelect.style.marginTop = '7px'
    regionSelect.style.padding = '10px'

    // 이미지를 바꾸고싶음
    const image = document.querySelector('img')
    image.src = 'https://zzu.li/ssafy-image'
    // console.dir(image)을 쓰면 image속성이 어떤 것들이 있는지 전부 보여줌
    // console.dir(image)
    // 이미지 크기를 키우자
    image.width = 600
    // image.style.widty = '600px'

    //footer 꾸미기
    // js를 통해 태그를 만들어 Dom에다가 붙이는 것을 하고 싶음
    // 태그를 js로 만들고, dom(쉽게 생각하면 body태그, ul태그..etc)에다가 
    // 태그를 만들 땐 createElement('태그이름')를 쓰면됨
    const footer = document.createElement('footer')
    // text 어떻게 붙여넣을 수 있는가?
    footer.innerText = 'Google 설문지를 통해 비밀번호를 제출하지 마시오.'
    // js에서만 존재하는 태그(아직까진)
    // DOM에는 어떻게 붙이냐? 붙일 위치를 먼저 찾아와야됨
    const body = document.querySelector('body')
    // console.dir(body) body태그속성 :  childnodes(body태그 자식들), children(태그들만!)
    // body에 자식으로 footer태그를 만듦
    body.appendChild(footer)
    // footer를 수정하고 싶다면
    footer.classList.add('box-container','footer')
    // body 자식 태그들이 나옴
    // console.log(body.children)
    // class명을 빼고싶다면
    // footer.classList.remove('box-container')

  </script>
</body>
</html>
```



----------

### basic JavaScriptCore

> 내일 더 자세하게 할 예정

> 밖에 index.js 파일을 만든 뒤, script에 넣는 코드를 넣음
>
> `<!-- js를 불러오고싶다면 이런식으로도 불러올 수 있음-->
>   <!-- <script src='index.js'></script> -->` 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Basic JavaScript Core Things</title>
</head>
<body>
  <!-- js를 불러오고싶다면 이런식으로도 불러올 수 있음-->
  <!-- <script src='index.js'></script> -->
  <script>
    // Conditional Expression
    // var, let있지만 var는 안씀
    const myName = 'ssafy 4th'

    // 중괄호 사용
    // == 동등비교연산자(자동변환, 그래서 의도치않은 결과가 나타날 수 있음), ===일치비교연산자(권장)
    if (myName === 'ssafy 4th') {
      console.log('ssafy 4th님 환영합니다.')
    } else if (myName === 'ssafy 3th') {
      console.log('ssafy 3th님 환영합니다.')
    } else {
      console.log('환영합니다.')
    }

    // Iteration 
    // + for ... in / for ... of
    // 0,1,2,3,4,5
    for (let i = 0; i < 6; i++) {
      console.log(i)
    }

    // 핵심!
    // Function Declaration & Call
    //1. 함수 선언
    // 함수 선언식
    function add (num1, num2) {
      // console.log(num1 + num2)
      return num1 + num2
    }

    // 함수 표현식
    // 함수는 어떤 변수에 담길수 있다는 js의 특징을 이용
    const sub = function (num1, num2) {
      // console.log(num1 - num2)
      return num1 - num2
    }

    // arrow function
    const multi = (num1, num2) => {
      return num1 * num2
    }

    //2. 함수 호출
    // () 함수 호출 순간
    // js는 인자에 자유로움
    const result1 = add(2, 7)
    const result2 = sub(7, 2)
    const result3 = multi(7, 2)

    console.log(result1, result2, result3)
  </script>
</body>
</html>
```

![image-20201012141603238](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012141603238.png)







---------

## EventListener

> ```javascript
> // 기본 틀
> EventTarget.addEventListener('click',function <함수이름> (){})
> EventTarget.addEventListener('keydown',function (){})
> ```
>
> ![image-20201012145335914](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012145335914.png)

### Event

> [공식문서](https://developer.mozilla.org/ko/docs/Web/Events)

> click, submit, keydown(키가 눌려짐), mouseover(마우스올라감)
>
> ![image-20201012141945656](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012141945656.png)

### addEventListener

> **`~가 ~하면 ~한다`**
>
> '클릭**하면** 경고 **창을 띄운다**'
>
> '특정 이벤트(click,keydown,mouseover)가 발생하면, 할 일(function)을 등록하자'
>
> `EventTarget.addEventlistener(type,listener)`
>
> ![image-20201012142353800](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012142353800.png)

#### onclick

> 이렇게 inline으로 쓰는 것 권장하진 않지만 이렇게 할 수 있다는걸 보여주기 위해 적음!
>
>  function <함수이름> (){} 함수이름을 그냥 안적고 넘기면 익명함수! 이름을 적지 않아도 됨
>  event를 e라고도 줄여서 통상 많이 적음 

```html
<body>
  <!-- 1. onclick event handler-->
  <button onclick="alertMessage()">나를 눌러봐!</button>
```

```javascript	
<script>
    // 1.onclick 를 정의한 뒤 위에 onclick으로 적어서 호출
    const alertMessage = function(){
      alert('안녕하세요!')
    }
  </script>
```

![image-20201012142829867](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012142829867.png)

#### **addEventListener(중요!!!!!)**

> 이렇게 사용하는 것을 권장

##### click

```html
<body>
<!-- 2. addEventListener -->
  <button id="myButton">나를 눌러봐!!</button>
  <hr>
```

```javascript
    // 1)eventtarget가져오기
    const myButton = document.querySelector('#myButton')
    // 2) eventtarget.addeventlinster()
    // myButton.addEventListener('click')
    // 3) listener함수 넣기
    // alertMessage는 명시적 호출()이 아님 그냥 알아서 호출되기 때문에 괄호 안적음
    myButton.addEventListener('click',alertMessage)
```

##### keydown

```html
<body>
<!-- 3. addEventListener2 -->
  <p id="myParagraph"></p>

  <form action="#">
    <label for="myTextInput">내용을 입력하세요.</label>
    <input id="myTextInput" type="text">
  </form>
  <hr>
```

```javascript
    const myTextInput = document.querySelector('#myTextInput')
    
    myTextInput.addEventListener('keydown',function (event){
      // console.log(event)
      // console.log(event.target.value)
      const myParagraph = document.querySelector('#myParagraph')
      // 이렇게 하면 바로 적을 수 있음
      myParagraph.innerText = event.target.value
    })
```



![image-20201012144543316](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012144543316.png)

- 색 바꿈

```html
<body> 
<!-- 4. addEventListener3 -->
  <h2>Change My Color</h2>
  <label for="changeColorInput">원하는 색상을 영어로 입력하세요.</label>
  <input id="changeColorInput"></input>
  <hr>
```

```javascript
   // 4.addEventListener - keydown
    const changeColorInput = document.querySelector('#changeColorInput')
    changeColorInput.addEventListener('keydown',function (event) {
      // h2를 가져옴
      const h2 = document.querySelector('h2')
      // h2의 style의 color로 입력값으로 바꾸겠다!
      h2.style.color = event.target.value
    })
```

![image-20201012145155005](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012145155005.png)



### preventDefault

> Default(기본값)를 막는다
>
> 기본값 : 어떠한 태그가 가진 기본 event

#### submit

> 제출을 눌렀을 때 어디로 안갔으면 좋겠다!
>
> `cancelable = True` 이건 기본 event 취소가능하다는 말

```html
  <!-- 2. submit -->
  <!-- form은 submit이 기본 event 이런 기본 값을 막아야되는 상황이 있음 -->
  <form action="/articles/" id="myForm">
    <input type="text">
    <input type="submit">
  </form>
  <hr>
```

```javascript
   // 2. submit
    const  form = document.querySelector('#myForm')
    // target.addEL('어떤event',할일)
    form.addEventListener('submit',function (event){
      // 작성하고 제출을 하면 console에 찍혀야되는데 안찍힘
      console.log(event)
      // 기본 event를 막아준다는 의미
      event.preventDefault()
    })
```

![image-20201012151238882](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012151238882.png)





------

## todoCRUD

> Console에는 이렇게 직접 적을 수 있음
>
> ![image-20201012152139878](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012152139878.png)

### Create / Read

> console에 입력했던 것 처럼 입력을 했지만 입력이 되지 않는다 -> 함수화 해야됨

```javascript
    // 이렇게 해도 입력이 안됨 그래서 함수화 해야됨
    const input = document.querySelector('input')
    const content = input.value

    const li = document.createElement('li')
    li.innerText = content

    const ul = document.querySelector('ul')
    ul.appendChild(li)
```

- 함수 선언형 
  - console에 호출(`addTodo()`)하면 뜸!

```javascript
    function addTodo () {
      const input = document.querySelector('input')
      const content = input.value
  
      const li = document.createElement('li')
      li.innerText = content
  
      const ul = document.querySelector('ul')
      ul.appendChild(li)
    }
```



![image-20201012152559742](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012152559742.png)

- 함수에 인자를 넘겨주게 만들어봄

```javascript
    function addTodo (todo) {
      const input = document.querySelector('input')
      // const content = input.value
  
      const li = document.createElement('li')
      li.innerText = todo
  
      const ul = document.querySelector('ul')
      ul.appendChild(li)
    }
```

![image-20201012152813586](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012152813586.png)

- Todo를 클릭했을 때 함수가 호출되게 만들고 싶다!

> - addEL은 todo를 event객체로 넘겨줌! 그래서 [object MouseEvent]라고 찍힘
> - 그래서 content에 input.value를 넣어서  li.innerText로 content를 넣어줌!
>
> ![image-20201012153251231](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012153251231.png)

```javascript
    const button = document.querySelector('button')
      // 익명 함수 function 뒤에 addTodo 이름 지움
      
    // button.addEventListener('click', function (todo) {
    button.addEventListener('click', function () {
      // console.log(todo)
      const input = document.querySelector('input')
      const content = input.value
  
      const li = document.createElement('li')
      // li.innerText = todo
      li.innerText = content
  
      const ul = document.querySelector('ul')
      ul.appendChild(li)
      // 입력했을 때 글자가 안지워지는게 아쉬워
      input.value = ''
    })
```





- function로직을 다른곳에서 또 쓰려면 또 써야되나?

> 그냥 이름을 붙여서 함수(기명함수)를 만들고 함수를 호출해주자!(주의! 괄호를 적지 않음)

```javascript
    const button = document.querySelector('button')
    function addTodo () {
      // console.log(todo)
      const input = document.querySelector('input')
      const content = input.value
  
      const li = document.createElement('li')
      // li.innerText = todo
      li.innerText = content
  
      const ul = document.querySelector('ul')
      ul.appendChild(li)
      // 입력했을 때 글자가 지워지게 함
      input.value = ''
    }
    button.addEventListener('click',addTodo)
```

- 여기서 엔터를 눌렀을 때 제출되게 하고싶다

> ```javascript
>       if (event.code === 'Enter') {
>         addTodo()
>       }
> ```
>
> 위 코드가 없다면 아래 그림처럼 하나하나 값이 입력됨
>
> ![image-20201012154117852](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012154117852.png)
>
> 
>
> `event.code==='Enter'`값을 조건으로 적는다면 Enter키를 눌렀을 때 값이 입력됨
>
> ![image-20201012153530020](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012153530020.png)

```javascript
    const button = document.querySelector('button')
    const input = document.querySelector('input')

    function addTodo () {
      // console.log(todo)
      // const input = document.querySelector('input')
      const content = input.value
  
      // 빈값이 들어갈 수 없게 만듦
      // if (content !== '') {
      if (contnet) {
        const li = document.createElement('li')
        // li.innerText = todo
        li.innerText = content
    
        const ul = document.querySelector('ul')
        ul.appendChild(li)
        // 입력했을 때 글자가 지워지게 함
        input.value = ''
        })


      } else {
        alert('빈 값 안됨!!!!')
      }

    }
    button.addEventListener('click',addTodo)
    // input.addEventListener('keydown',addTodo)
    input.addEventListener('keydown',function (event) {
      // event의 code속성이 Enter라면 addTodo함수를 호출(직접호출이라 ()적어줌)할래!
      if (event.code === 'Enter') {
        addTodo()
      }
    })
    
```







### Update / Delete

> [text-decoration](https://developer.mozilla.org/ko/docs/Web/CSS/text-decoration)
>
> - 누르면 취소선 나왔다가 다시 누르면 지워지고
> - X 버튼을 누르면 삭제가 됨
>
> ![image-20201012160206489](1012_JS(History_of_JavaScript&Browser,DOM,Event).assets/image-20201012160206489.png)

```javascript
   const button = document.querySelector('button')
    const input = document.querySelector('input')

    function addTodoUpdateDelete () {
      const content = input.value
  
      // 빈값이 들어갈 수 없게
      // if (content !== '') {
      if (contnet) {
        const li = document.createElement('li')
        // li.innerText = todo
        li.innerText = content
    
        const ul = document.querySelector('ul')
        ul.appendChild(li)
        // 입력했을 때 글자가 안지워지는게 아쉬워
        input.value = ''

    // Update(취소선을 만들어보자)
        // li.style.textDecoration = 'line-through'
        li.addEventListener('click', function (event) {
        //방법 
        //1. length
        //   if (event.target.classList.length===0) {
        //     event.target.classList.add('done')
        //   } else {
        //     event.target.classList.remove('done')
        //   }

        // })
        // 2.contains 그 클래스 존재 true/false
        //   if (event.target.classList.contains('done')) {
        //     event.target.classList.remove('done')
        //   } else {
        //     event.target.classList.add('done')
        //   }

        // })
        // 3. toggle : done이 class에 있으면 제거하고 없으면 추가해라
        event.target.classList.toggle('done')
        })
          
        // Delete
        // 조건이 없음! li에 remove가 들어감과 동시에 삭제가됨
        // li.remove()
        // button을 만듦
        const deleteButton = document.createElement('button')
        deleteButton.innerText = 'X'
        // 속성으로 될때는 margin-left가 marginLeft로 대문자로 바뀜
        deleteButton.style.marginLeft = '10px'
        li.appendChild(deleteButton)
        // 이 버튼이 클릭됐을 때 삭제되게 만듦!
        deleteButton.addEventListener('click', function () {
          li.remove()
        })


      } else {
        alert('빈 값 안됨!!!!')
      }

    }
    button.addEventListener('click',addTodoUpdateDelete)
    // input.addEventListener('keydown',addTodo)
    input.addEventListener('keydown',function (event) {
      // event의 code속성이 Enter라면 addTodoUpdateDelete함수를 호출(직접호출이라 ()적어줌)할래!
      if (event.code === 'Enter') {
        addTodoUpdateDelete()
      }
    })
```



