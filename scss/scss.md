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

