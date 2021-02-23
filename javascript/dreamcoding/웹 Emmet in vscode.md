# 웹 Emmet in vscode

- `!` tab하면 기본 html 스켈레톤 코드 자도완성

#### 자식 요소: `>`

`>`를 사용하여 **자식 요소**를 생성할 수 있다. :

```html
div>ul>li
```

결과 :

```html
<div>
    <ul>
        <li></li>
    <ul>
<div>
```

------

#### 형제 요소: `+`

`+`를 사용하여 한 요소와 **같은 단계**에 위치한 요소를 생성할 수 있다.

```html
div+p+bq
```

결과 :

```html
<div></div>
<p></p>
<blockquote></blockquote>
```

------

#### 한 단계 올리기: `^`

`^`를 사용하여 **한 단계 위**에 요소를 배치할 수 있다.

```html
div+div>p>span+em^bq
```

*span+em은 p태그의 하위 단계에 위치하지만 bq는 ^로 인해 p태그와 같은 단계에 위치하게 된다.*

결과 :

```html
<div></div>
<div>
    <p>
        <span></span>
        <em></em>
    </p>
    <blockquote></blockquote>
</div>
```

#### 반복하기 `*`

```html
div>ul>li*3
<div>
    <ul>
        <li></li>
        <li></li>
        <li></li>
    </ul>
</div>
```

#### 그룹화 `()`

```html
div>(header>ul>li*2)+footer
<div>
    <header>
        <ul>
            <li></li>
            <li></li>
        </ul>
    </header>
    <footer></footer>
</div>
```

#### 클래스 `.class`

```html
div.class
<div class="class"></div>
```

#### 아이디 `#id`

```html
div#id
<div id="id"></div>
```

#### 속성 `[attr]`

```html
td[title="hello" colspan=5]
<td title="hello" colspan="5"></td>
```

#### 넘버링 `$`

```html
ul>li.item$*5
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
</ul>
ul>li.item$@5*5
<ul>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
    <li class="item8"></li>
    <li class="item9"></li>
</ul>
```

#### 텍스트 `{}`

```html
.fruit{banana}
<div class="fruit">banana</div>
.container>ul.list>li.list-item*5>a{list$}
<div class="container">
    <ul class="list">
        <li class="list-item"><a href="">list1</a></li>
        <li class="list-item"><a href="">list2</a></li>
        <li class="list-item"><a href="">list3</a></li>
        <li class="list-item"><a href="">list4</a></li>
        <li class="list-item"><a href="">list5</a></li>
    </ul>
</div>
```

------



# CSS

- `w100` 입력 후 `Tab`

```css
  width: 100px; (기본이 px단위)
```

####  단위

p → %
e → em
x → ex

- `w50p` `h100p`

```css
  width: 50%;
  height: 100%;
```



- `m10p30e5x`

```css
  margin: 10% 30em 5ex;
```