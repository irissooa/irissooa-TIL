# SCSS

[toc]

## emit

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <!-- emit -->
    
  <!-- div*5 -->
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
    
  <!-- div.box*3 -->
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
    
  <!-- ul>li.list*5 -->
  <ul>
    <li class="list"></li>
    <li class="list"></li>
    <li class="list"></li>
    <li class="list"></li>
    <li class="list"></li>
  </ul>
</body>
</html>
```

## VS code

> 해당 프로젝트 설정만 바꾸고 싶다면 작업영역(workspace)에서 설정 바꿔주면 된다

### Live Sass Compiler 설치

>  예를들어 `test.scss`파일을 만들어 아래의 코드를 작성한 뒤
>
> ```scss
> $fs:16px;
> 
> body {
>   font-sixe:$fs;
> }
> ```
>
> ![image-20210110160844294](scss.assets/image-20210110160844294.png)
>
> `Watch my Sass`를 누르면 ![image-20210110161001764](scss.assets/image-20210110161001764.png) 이렇게 `test.css`, `test.css.map`파일이 생긴다.
>
> ```css
> /* test.css */
> body {
>   font-size: 16px;
> }
> /*# sourceMappingURL=test.css.map */
> 
> /* test.css.map */
> {
>     "version": 3,
>     "mappings": "AAEA,AAAA,IAAI,CAAC;EACH,SAAS,EAHP,IAAI;CAIP",
>     "sources": [
>         "test.scss"
>     ],
>     "names": [],
>     "file": "test.css"
> }
> ```
>
> 같은 폴더에서 변환되는것을 바꾸고 싶다면 `Live Sass Compiler`확장에 들어가면 바꾸는 법이 적혀있음
>
> ![image-20210110161307440](scss.assets/image-20210110161307440.png)
>
> ```json
> {
>   "liveSassCompile.settings.formats": [
>     {
>       "format": "expanded",
>       "extensionName": ".css",
>       "savePath": "/css"
>     },
>   ],
>   "liveSassCompile.settings.excludeList": [
>     "**/node_modules/**",
>     ".vscode/**"
>   ],
>   "liveSassCompile.settings.generateMap": true,
>   "liveSassCompile.settings.autoprefix": [
>     "> 1%",
>     "last 2 versions"
>   ]
> }
> ```
>
> 사용자 설정으로 `setting.json`파일에 위처럼 복붙!
>
> 여기서 `liveSassCompile.settings.formats`를 붙여넣고, `savePath`의 경로를 `null`이 아니라 
>
> `"/"` 이렇게 하면 프로젝트의 root에 저장이되고 아니면 
>
> `"/css"`라고하면 root아래의 css폴더를 만들어 그안에 저장, 
>
> `"~/css"` 해당 sass파일 아래의 css라는 폴더안에 저장
>
> `"~/../css"` `~`는 해당 sass파일 위치 `..`는 해당 폴더의 위에 `/css`css폴더

##  Sass

> CSS작성(생성)을 위한 작고 가벼운 언어이고, Sass와 SCSS가 있다.
>
> **Sass**
>
> SCSS와 작성하는데 있어서 구조적 차이가 있고 작성이 번거롭고 복잡할 수 있다.
>
> **SCSS**
>
> 기존에 알던 CSS와 유사하게 작성할 수 있기 때문에 친근하게 느껴져 배우기가 쉽다

![image-20210110164049993](scss.assets/image-20210110164049993.png)

`test.scss`파일을 `watching`을 이용해 바뀐 코드를 자동을 `test.css`로 변환됨

그리고 `sass-test.html`의 head에 `<link rel="stylesheet" href="sass/test.css">`로 연결하면 `live-server`에 의해 자동으로 변환된 값이 새로고침됨

`$원하는 이름:원하는설정`하면 아래에 변수처럼 적용시킬 수 있다

![image-20210110165027190](scss.assets/image-20210110165027190.png)

![image-20210110165012138](scss.assets/image-20210110165012138.png)



## Scss 문법

### vars

> (참고) html body에 `div#box$*5`를 쓰면 id가 box1부터 box5인 div가 자동 생성
>
> 처음 배울 때는 css랑 똑같이 적어도됨! 그러다가 익숙해지면 개선!
>
> 반복되는 코드가 나올때 예를들어 아래의 글자색, 배경색, width 등
>
> ```scss
> body {
>   background-color: #ddd;
> }
> 
> #box1 {
>   color:#ff0;
>   background-color: #00f;
>   width:100px;
> }
> 
> #box2 {
>   color:#f00;
>   background-color: #00f;
>   width:100px;
> }
> 
> #box3 {
>   color:#ff0;
>   background-color: #00f;
>   width:300px;
> }
> 
> #box4 {
>   color :#f00;
>   background-color: #00f;
>   width:300px;
> }
> 
> #box5 {
>   color:#0f0;
>   background-color: #00f;
> }
> ```
>
> 이렇게 적으면 파란색을 노란색으로 고치고 싶다면 다 바꿔줘야됨! 이걸 변수로 처리하면 한번만 바꾸면 된다!
>
> ```scss
> $bg-color:rgb(73, 83, 221);
> 
> body {
>   background-color: #ddd;
> }
> 
> #box1 {
>   color:#ff0;
>   background-color: $bg-color;
>   width:100px;
> }
> 
> #box2 {
>   color:#f00;
>   background-color: $bg-color;
>   width:100px;
> }
> 
> #box3 {
>   color:#ff0;
>   background-color:$bg-color;
>   width:300px;
> }
> 
> #box4 {
>   color :#f00;
>   background-color:$bg-color;
>   width:300px;
> }
> 
> #box5 {
>   color:#0f0;
>   background-color:$bg-color;
> }
> ```
>
> ![image-20210110201210584](scss.assets/image-20210110201210584.png)

- 변수 이름 규칙

  - `변수 : css에 들어갈 수 있는 모든 값;`

  - `$영문`으로 시작, 영문,숫자,`-`,`_`이렇게만 들어갈 수 있다 

### Nesting

> 포함관계

- `sass-basic.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="/css/sass-basic.css">
</head>
<body>
  <div id="box1">
    box1<br>
    <a href="#">button1</a>
    <div id="box2">
      box2<br>
      <a href="#">button2</a>
    </div>
  </div>
</body>
</html>
```

- `sass-basic.scss`

```scss
html {
  font-size: 18px; 
}

body {
  margin: 20px;
  background-color: #fff4ef;
}

div {
  color: #333;
  padding: 20px;
}

a {
  display: inline-block;
  margin: 10px 0;
}

#box1 {
  font-size: 40px;
  background-color: #ffcccc;
  // 모서리둥글게함
  border-radius: 20px;
  // 모서리,테두리
  border: 3px solid #f00;
  // 그림자
  box-shadow: 0px 3px 11px 0px rgba(0, 0, 0, 0.75);
}

#box1 > a {
  color: #a22;
  text-decoration: none;
}

#box1 > a:hover {
  color: #000;
  text-decoration: underline;
}

#box1:hover {
  background-color: #ccc;
}

#box1 #box2 {
  font-size: 20px;
  background-color: #e9e9e9;
  
  border-radius: 20px;
  border: 3px solid #f00;
  box-shadow: 0px 3px 11px 0px rgba(0, 0, 0, 0.75);
}

#box1 #box2 > a {
  color: #ee6633;
  text-decoration: none;
}

#box1 #box2 > a:hover {
  color: #a22;
  text-decoration: underline;
}
```

![image-20210110202010119](scss.assets/image-20210110202010119.png)

- 여기서 scss는 포함관계를 나타낼 수 있는데 만약 아래처럼 `box1`id 아래에 `a`를 적고 css를 적는다면, 변환된 css파일에는 box1id아래 모든 a태그를 가리키는 css로 변환된다!

- scss파일

```scss
#box1 {
  font-size: 40px;
  background-color: #ffcccc;
  // 모서리둥글게함
  border-radius: 20px;
  // 모서리,테두리
  border: 3px solid #f00;
  // 그림자
  box-shadow: 0px 3px 11px 0px rgba(0, 0, 0, 0.75);
  a {
  color: #a22;
  text-decoration: none;
  };
  a:hover {
  color: #000;
  text-decoration: underline;
  };
}
```

- css파일

```css
#box1 a {
  color: #a22;
  text-decoration: none;
}

#box1 a:hover {
  color: #000;
  text-decoration: underline;
}
```

- 하지만 이렇게 하면 box1id아래 모든  `a`가 해당되기 때문에 바로 아래의 a만 적용하고 싶다면 `&`를 이용!

#### `&`(자기자신)

> `&`를 이용하면`#box1` 아래에 
>
> `&:hover`는 `#box1:hover`
>
> `& > a` 는 `#box1 > a`, 그 아래 또 `&:hover`를 한다면 `#box1 > a:hover`

- scss

```scss
#box1 {
  &:hover {
    background-color: #ccc;
  }
  & > a {
  color: #a22;
  text-decoration: none;
  &:hover {
      color: #000;
      text-decoration: underline;
    }
  };
}
```

- css

```css
#box1:hover {
  background-color: #ccc;
}

#box1 > a {
  color: #a22;
  text-decoration: none;
}

#box1 > a:hover {
  color: #000;
  text-decoration: underline;
}
```

