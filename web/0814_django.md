# django

> 파이썬으로 작성된 오픈소스 웹 어플리케이션 프레임워크로, 모델-뷰-컨트롤러 모델 패턴(소프트웨어 디자인 패턴)을 따름

- dynamic web Vs Static web
- python web framework
  - 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적

|         구분         | MVC(소프트웨어 디자인 패턴) | django(MTV) |
| :------------------: | :-------------------------: | :---------: |
|      데이터관리      |            Model            |    Model    |
|   인터페이스(화면)   |            View             |  Template   |
| 중간 관리(상호 동작) |         Controller          |    View     |

- django how?

![image-20200814095003024](0814_django.assets/image-20200814095003024.png)

## django 다루는 법

#### 1. startproject

- project를 만들 때 하이픈, python, django 쓰는 이름 안됨

```sh
$ django-admin startproject {원하는이름}
```



#### 2. startapp

- django를 다룰때 이렇게 적어줌

```sh
$ python manage.py {동작하길 원하는 것}
```

- 방금 만든 프로젝트 파일로 vscode를 다시 연 뒤
  - 이거를 쓰면 서버가 열림

```sh
$ python manage.py runserver
```



#### 3. 앱등록 시 순서를 잘 지켜야 됨

1. **앱 생성**

```sh
$ python manage.py startapp {원하는 앱이름}
```

- 만들어진 앱 폴더의`models.py`는 Model이고, `views.py`는 View 이다.

2. **앱 등록**

- django에서 만든 프로젝트 폴더의 `settings.py`에 만든 앱을 `INSTALLED_APPS`에 적어줌
  - django에서는 마지막에 `,`가 들어감 안들어가도 오류가 나진 않지만 적어줘야됨

```python
# Application definition

INSTALLED_APPS = [
    #1. local apps
    'articles',
    #2. 3rd party apps
    
    #3. django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



- 언어를 바꾸고 싶다면 `settings.py`의 `LANGUAGE_CODE`를 바꿔줌

```python
LANGUAGE_CODE = 'ko-kr'
```



#### 4. 코드작성 순서(데이터 흐름과 동일)

#### 1) urls.py

- django의 기본 설정 중 `admin`(관리자 페이지)가 있다.

```sh
django의 열린 서버 뒤에 /admin 을 적어주면 관리자페이지로 감
```

- 

```sh
from 함수있는장소 import views(원하는 파이썬 이름)
path('url주소/',가져올 뷰함수 적기)
```



- `index`라는 주소를 요청했을 때 articles app의 views.py의 특정함수(뷰함수)를 가져올거야

```python
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```



#### 2) vies.py(동작)

- 장고와의 약속 뷰함수는 첫번째 인자로 무조건 request를 받아야됨
- 랜더링할 준비를 끝남(사용자에게 보여지기 위해서 render라는 함수가 필요함) 
- templates라는 이름이라는 약속이 있음
  - 저 폴더 안을 쓰는 것을 다 알고 있으니 추가경로를 쓰지 않고 템플릿 이름을 써도 돼 대신 폴더이름은 반드시 templates여야돼

```sh
render(반드시첫번째인자로 request를 적어줌,'템플릿 이름')
```



```python
from django.shortcuts import render #뷰함수 쓸거면 너 반드시 render함수를 써야될거야

# Create your views here.
def index(request): 
    return render(request,'index.html') 
```

- 파이썬 가이드라인 함수간 공백은 `2enter`가 있어야 됨

#### django imports style guide 순서

1. standard library

2. 3rd party( ex: request)

3. Django

4.  local django(내장함수가아니라 다른 모듈에서 가져오거나 내가 만든 것)



#### 3) templates(폴더이름은 반드시 이렇게!)(어떤 모습으로?)

- 앱 안에 `templates`폴더를 만들어 안에 `template`을 만듦(ex `index.html`)

- 메인페이지에 보여질 홈페이지를 꾸밀 곳, 아래 예시처럼 꾸며주면 됨

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>안녕하세요! 반갑습니다!</h1>
</body>
</html>
```



### 예시

- 저녁 메뉴 추천 서버 만들기
-  이름을 다 맞춰주는게 좋음
  -  url, views함수, template 이름
     

#### 1. urls.py

- url에 `dinner` 적으면 `views`에서 `dinner`함수를 가져올거야

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dinner/',views.dinner),
]
```



#### 2. views.py

- 같이 렌더링할 값을 딕셔너리로 적어줌

```python
import random 
from django.shortcuts import render #뷰함수 쓸거면 너 반드시 render함수를 써야될거야

# Create your views here.
def index(request):
    return render(request,'index.html') 


def dinner(request):
    menus = ['족발','김치찜','햄버거','연어덮밥','초밥']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'pick': pick,})
```

- `context`라는 dict를 만들어 여러 키값들을 넣어줘되 됨

```python
def dinner(request):
    menus = ['족발','김치찜','햄버거','연어덮밥','초밥']
    pick = random.choice(menus)
    context = {
        'pick' : pick,
    }
    return render(request, 'dinner.html', context)
```



#### 3.templates/ dinner.html

- 사용할 `key` 이름을 적고 싶다면 중괄호 두개로 감싸줌

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>오늘 저녁은 {{ pick }} 입니다.</h1>
</body>
</html>
```





## Django Template Language(DTL)

- django template system에서 사용하는 built-in template system이다
- 조건, 반복, 치환, 필터, 변수 등의 기능을 제공
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- 파이썬처럼 if, for를 사용할 수 있지만 이거는 단순히 python code로 실행되는 것이 아님
- 공식문서에 들어가서 설명들을 보기! 자세한 내용은 링크로 또 들어가야됨!



#### syntax:

- variable : `{{ }}`
  - views.py에서 context 딕셔너리를 만들어
- filter
  - `|`뒤에 filter를 적어준다 
  - :  `{{ variable|filter }}`

```html
{% if messages|length >= 100 %}
   You have lots of messages today!
{% endif %}
```

- tags : `{% tag %}`





### variable routing

- url의 변수화

```html
path('hello/<str(변수의 type):name(변수이름)>/', views.hello)
```

- `view.py`

```python
def hello(request, name): #path에 적은 변수의 이름과 같아야됨
    context ={
        'name' : name
    }
    return render(request, 'hello.html', context)
```

- `hello.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>안녕하세요, {{ name }}님</h1>
</body>
</html>
```



### tags

- 파일명말고, 이름 설정할 떄 html은 `-`, python에는 `_`사용




##### `for`

```html
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
```



##### `for ...empty` 예시

- 

```python
 path('dtl-practice/', views.dtl_practice),
```

- 

```python
def dtl_practice(request):
    menus = ['짜장면', '탕수육', '짬뽕']
    empty_list = []
    context = {
        'menus' : menus,
        'empty_list' : empty_list
    }
    return render(request, 'dtl_practice.html', context)
```

- 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>DTL for, if tags 연습</h1>
  <h2>1.for tag</h2>
  {% for menu in menus %}
    {{ menu }}
  {% endfor %}
  <hr>
  {% for menu in menus %}
    {{ forloop.counter }} : {{ menu }}
  {% endfor %}
  <hr>
  {% for x in empty_list %}
    {{x}}
  {% empty %}
    <p>아무것도 없어요!!</p>
  {% endfor %}

</body>
</html>
```





##### `if`

- python의 operator 사용가능 : >, <, ==, is, in, not in ..등

```html
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```





## 템플릿 시스템 설계 철학

- 장고는 템플릿 시스템이 **표현**을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각함
- 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안됨





## 주고받을때 view함수는 2개 필요함

1. form을 받을 페이지

   - throw/

   - form- 검색할 수 있는 action

2. 결과를 보내줄 페이지

   - catch/
   - 클라이언트가 보낸 정보를 받아서 그대로 화면에 출력

##### 순서

1. throw.html-form태그를 통해 요청 보냄
2. /catch/로 요청받음
3. catch view -data를 받아
4. 최종적으로catch.html에서 출력



##### 1) urls.py

```python
    path('throw/', views.throw),
    path('catch/',views.catch),
```



##### 2. view.py

```python
#url로 받지 않고 사용자 입력만 받으면 됨
def throw(request):
    return render(request, 'throw.html')


#throw에서 보낸 form 데이터(request.GET)를 받기
def catch(request):
    # request.GET['name'] #여기에 데이터가 존재//이렇게 쓰는 방식은 만약 없으면 keyerror가 됨->서버가 에러 날 수있음 그래서 .get을 쓰는게 낫다
    message = request.GET.get('name') #여기에 데이터가 존재 // 없으면 none이 반환
    context = {
        'message' : message,
    }
    return render(request,'catch.html', context)
```



##### 3. throw.html

- `form`태그의 `action`을 `/데이터를 보낼곳/`이렇게 적어야됨
- method의 default값은 원래 `GET`이지만 적어두는게 좋다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Throw 페이지</h1>
  <form action="/catch/" method="GET">
    <label for="name">데이터 입력 : </label>
    <input type="text" id="name" name="name">
    <input type="submit">
  </form>
</body>
</html>
```



##### 4. catch.html

````html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Catch 페이지</h1>
  <h2>throw에서 보낸 데이터는 {{ message }}입니다.</h2>
</body>
</html>
````



## http method

- GET
  - 단순 조회할 때만 사용
  - 쿼리스트링으로 넘어감
  - 딕셔너리 안에 input data가 들어있는데 `key(input name) : value(input vlaue)` 이렇게 들어가게 됨
  - `{'name' : '내가 보내는 데이터'}`
  - url의 `?`뒤에 key=value&key=value...형태로 들어옴
  - `http://127.0.0.1:8000/catch/?name=헤이즈`

- POST
  - 데이터 변경
  - URL에 나타나지 않음
  - Body로 넘어감..
  - 추후 자세하게 할 예정