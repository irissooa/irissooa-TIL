# django

- `dtl_example`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dtl-example</title>
</head>
<body>
  {% comment %} 그냥 이런 기능들이 있다는 것만 알기..ㅎ {% endcomment %}
  <h3>1.lorem ipsum</h3>
  {% comment %} 아무태그없이 그냥 텍스트 쓴것처럼 한 문단 만들어줌 {% endcomment %}
  {% lorem %}
  <hr>
  {% comment %} 3단어 {% endcomment %}
  {% lorem 3 w %}
  <hr>
  {% comment %} 5개 랜덤 단어 {% endcomment %}
  {% lorem 5 w random %}
  <hr>
  {% comment %} p태그로 감싼 두개의 문단이 만들어짐 {% endcomment %}
  {% lorem 2 p %}
  <hr>
  <h3>2.글자 수 제한</h3>
  {% comment %} char 3{% endcomment %}
  <p>{{my_sentence|truncatechars:3}}</p>
  {% comment %} char n-3개(...3포함)이후 ... {% endcomment %}
  <p>{{my_sentence|truncatechars:10}}</p>
  {% comment %} word3개 {% endcomment %}
  <p>{{my_sentence|truncatewords:3}}</p>

  <h3>3.글자 관련 필터</h3>
  {% comment %} 글자길이 {% endcomment %}
  <p>{{'abc'|length}}</p>
  {% comment %} 글자 소문자 {% endcomment %}
  <p>{{'abc'|lower}}</p>
  {% comment %} 각 앞글자 대문자 {% endcomment %}
  <p>{{my_sentence|title}}</p>
  {% comment %} 제일 앞글자만 대문자 {% endcomment %}
  <p>{{'abc def'|capfirst}}</p>
  {% comment %} menus 중 random 1개 {% endcomment %}
  <p>{{menus|random}}</p>
  
  <h3>4.연산</h3>
  {% comment %} 연산을 제공하긴 하지만 논리는 view.py에서 하고, 여기서는 단지 보여주는 것들만 기록한다 {% endcomment %}
  <p>{{4|add:6}}</p>

  <h3>5. 날짜표현</h3>
  {% comment %} 파이썬에서 만든 시간(컴퓨터시간)2020년 8월 18일 10:03 오전  {% endcomment %}
  {{ datetimenow }} <br>
  {% comment %} 2020년 8월 18일 1:03 오전 {% endcomment %}
  {% comment %} 위 날짜와 차이가 나는 이유, 장고의 시간 : setting.py에서 기준시간이 UTC(영국시간)이기 때문, 이걸 한국시간 ASIA/SEOUL로 바꿔주면 같아짐 {% endcomment %}
  {% now "DATETIME_FORMAT" %} <br>
  {% comment %} 2020-8-18 01:03 {% endcomment %}
  {% now "SHORT_DATETIME_FORMAT" %} <br>
  {% comment %} 2020년 8월 18일 {% endcomment %}
  {% now "DATE_FORMAT" %} <br>
  {% comment %} 2020-8-18. {% endcomment %}
  {% now "SHORT_DATE_FORMAT" %}
  <hr>
  {% comment %} 2020년 08월 18일 (화요일) 01:03 {% endcomment %}
  {% now "Y년 m월 d일 (D) h:i" %}
  <hr>
  {% comment %} Copyright 2020 {% endcomment %}
  {% now "Y" as current_year %}
  {% comment %} 2020-8-18. {% endcomment %}
  Copyright {{ current_year }}
  <hr>
  {{ datetimenow|date:"SHORT_DATE_FORMAT" }}
  <hr>
</body>
</html>
```



## app이 여러개 일때

> 각 app에 `url.py`를 만들어줌

- url이 앱별로 겹치니까 app별로 `urls.py`를 만듦
- 적당히 import해주고 `urlpatterns`(반드시 이 이름이어야 장고가 인식함) 리스트를 선언
  - 원래 프젝에 작성했던 url 중 articles관련 url은 articles의 url.py로 옮김
  - `include('앱이름.urls(.py생략)')`

```python
#본 url.py 
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # 서브url로 'articles/' 나 'pages/'를 등록해 앱별 url.py를 연결시킴
    #ex) http://127.0.0.1:8000/articles/
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

- articles(앱)의 url.py
  - 반드시 `urlpatterns`를 가지고 있어야 장고가 인식함
  - 원래 프젝에 작성했던 url 중 articles관련 url 이동시킴
  - 가장 마지막에 keyword인자를 적어줌

```python
from django.urls import path #장고.urls에서 path를 가져오겠다
from . import views # articles 내부의 views에 접근해서 가져오겠다


urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('dtl-practice/', views.dtl_practice,name='dtl_practice'),
    path('throw/', views.throw,name='throw'),
    path('catch/', views.catch,name='catch'),
    path('dtl-example/', views.dtl_example,name='dtl_exmaple'),
]
```

- throw.html 
  -  사용자의 데이터를 어딘가(action)으로 보내고 싶을 때 사용
  - `url.py`에 적은 `keyword인자`를 action에 `{% url 'keyword인자' %}` 적어주면 자동으로 보낼 주소를 적어줌 

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
  <form action="{% url 'catch' %}" method="GET">
    <label for="name">데이터 입력 : </label>
    <input type="text" id="name" name="name">
    <input type="submit">
  </form>
</body>
</html>
```

- catch.html
  - `url.py`에 적은 keyword인자를 action에 `{% url 'keyword인자' %}` 적어주면 자동으로 보낼 주소를 적어줌

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
{% comment %} client가 GET방식 , POST방식으로 보냈냐에 따라 다름 {% endcomment %}
  <h1>Catch 페이지</h1>
  <h2>throw 에서 보낸 데이터는 {{ message }} 입니다.</h2>
  <a href="{% url 'throw' %}">back</a>
</body>
</html>
```



#### 장고는 모든것을 한곳에 모아서 파일 관리함, settings에 앱 등록 순서별로 먼저 찾는다

- index가 이름이 같을 때 articles의 이름이 먼저 적었기 때문에 articles의 index가 먼저 뜸

```python
#본 프젝 url app등록 순서 1)article, 2)pages
INSTALLED_APPS = [
    # 1. local apps
    'articles',
    'pages',
    # 2. 3rd party apps
    # 3. django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

##### 앱별로 템플릿이 따로 인식될 수 있도록 설정해줌

- templates안의 폴더에 앱이름과 같은 폴더(예 `templates/articles`)를 만들어 해당 앱의 html파일을 모두 넣음
  - 앱이 두개 이상일 경우 먼저 등록한 템플릿의 파일을 먼저 읽어와 발생하는 문제를 대비하기 위해
  - 해당 앱의 views.py에서 return render를 할 때 앞에 `앱이름폴더/`를 적어줌
  - `return render(request, 'articles/index.html')`



#### 반복되는 html을 모두 쓰지 않아도 되도록 설정

- 본 프로젝트 폴더에 `templates` 폴더를 만든 뒤 `base.html`을 만들어 반복되는 html 틀을 만들어줌
- 여기 block사이는 각 만드는 html마다 들어갈 내용
- endblock뒤엔 content가 안들어가도 되지만 block뒤엔 무조건 들어가야됨!
- `templates/base.html`

```html
#부트스트랩의 html 가져옴
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <title>first project</title>
  </head>
  <body>
 
  {% block content %}
  {% endblock %}
 
    <script src="code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </body>
</html>
```

- `pages/index.html`
  - `{% extends 'base.html' %}` 써 준 뒤 `{% block content %}`~`{% endblock content %}` 사이에 본 내용을 써주고 `content`는 원하는 content를 적음
  - 본 프젝의 `templates/base.html`에 써둔 block사이에 쓰여짐
  - 이런식으로 블락을 여러개 사용할 수 있음
  - ` {% extends 'base.html' %}`는 반드시 제일 상단에 적어야 됨

```html
{% extends 'base.html' %}

{% block title %}
<title>pages/index 용 타이틀</title>
{% endblock title %}

{% block content %}
<h1>이건 content 블락 안의 내용!</h1>
{% endblock content %}
```

##### setting.py에 base.html 등록

- `BASE_DIR`은 프로젝트의 최상위 경로를 표시함
- `TEMPLATES`에
- `'DIRS': [BASE_DIR / 'first_project' / 'templates'],` 
  - 별도 템플릿 폴더를 읽어오고 싶을 때 사용
  - BASE_DIR(최상위 폴더) 그 아래의/first_project폴더 그아래의/ templates 폴더에 있는 것을 불러올것임
  - 하나의 경로를 적어줌 경로를 추가하고 싶다면 `,` 뒤에 또 적어주면됨
- `APP_DIRS` 앱별 템플릿 폴더를 읽어오는 속성

```python
#프로젝트 최상위 경로(__file__)를 표시
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
#...(중략)
TEMPLATES = [ 
    {
		#(...전략)
        'DIRS': [BASE_DIR / 'first_project' / 'templates'], 
        'APP_DIRS': True, 
#(...후략)
]
```

##### 같은 이름 방지

- `name(키워드인자)`이 같은 것을 방지

- 해당 앱의 `urls.py`에 `app_name='앱이름' `적어줌 (반드시 `app_name`이름으로 변수 설정)

- 앱이름을 설정하면 모든 url 수정해줘야됨 `'앱이름:html'`
- url `'articles:index'`를 적어주면 앱이름 구별 가능

```html
#예시
<a href="{% url 'articles:throw' %}">back</a>
<a href="{% url 'articles:index' %}">홈으로</a>
```





##  Practice

## practice/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
```

## pages/views.py

```python
import random
from django.shortcuts import render

# Create your views here.
def lotto(request):
    #로또 당첨 번호
    numbers = range(1,46)
    lotto = random.sample(numbers,6)
    #보너스 번호
    bonus = random.sample(numbers,1)

    #로또 1000회분량
    lotto_1000 = [random.sample(numbers,6) for _ in range(1000)]

    #각 등수 별 cnt세기
    #1등 lotto랑 같음, 2등 lotto 5개 +보너스1개 3등 lotto 5개(보너스포함안함) 4등 4개 5등 3개 이후 꽝
    
    first, second, third, fourth, fifth, death = 0,0,0,0,0,0
    for i in lotto_1000:
        cnt = 0
        for j in i: #로또_1000안의 리스트들을 본다
            for k in lotto: #뽑은 lotto의 번호와 비교함
                if j == k:
                    cnt += 1
        #순위별로 cnt 분배
        if cnt == 6:
            first += 1
        elif cnt == 5 and (bonus in i):
            secnd += 1
        elif cnt == 5 and (bonus not in i):
            third += 1
        elif cnt == 4:
            fourth += 1
        elif cnt ==3:
            fifth += 1
        else:
            death += 1
        

    context = {
        'lotto' : sorted(lotto),
        'bonus' : bonus,
        'first' : first,
        'second' : second,
        'third' : third,
        'fourth' : fourth,
        'fifth' : fifth,
        'death' : death,
    }
    return render(request,'lotto.html',context)
```

## templates/lotto.html

- `ul`아래에 `li`로 하나씩 묶어주면 리스트를 만들 수 있음

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lotto</title>
</head>
<body>
  <h1>로또 당첨 횟수를 알아보자.</h1>
  <hr>
  <h2>이번 회차 당첨 번호 : {{ lotto }} + {{ bonus }}</h2>
  <ul>
  <li>1등 : {{ first }}번</li>
  <li>2등 : {{ second }}번</li>
  <li>3등 : {{ third }}번</li>
  <li>4등 : {{ fourth }}번</li>
  <li>5등 : {{ fifth }}번</li>
  <li>꽝 : {{ death }}번</li>
  </ul>
</body>
</html>
```



