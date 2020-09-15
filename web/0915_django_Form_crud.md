# Django CRUD

> form

1. 가상환경 만들기

```sh
$python -m venv venv
```

2. `.gitignore`만들기

```txt
venv/
.vscode/
```

3. django 설치

```sh
$pip install django
```

4. 현재 폴더(`.`)에 `crud_form`이라는 프로젝트 만들기

```sh
$django-admin startproject crud_form .
```

5. 앱만들기

```sh
$python manage.py startapp articles
```

6. settings에 installed_app에 앱이름 추가
7. urls.py에 import모듈 path옆에 include 추가하고 articles앱에 urls분리를 함!

```python
path('articles/', include('articles.urls'))
```

8. articles에 urls.py를 만들고,  아래와 같은 세팅을 만듦

> 다른 앱과 혼동되지 않도록 구분하기 위해 `app_name`을 만듦!

```python
from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('',views.index, name='index')
]
```

9. models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
```

10. views.py

```python
def index(request):
    #모든 articles를 보여준다
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html',context)
```

11. 메인 프로젝트 폴더에 `templates`폴더를 만든 뒤 `base.html`을 만들고, settings.py의 templates에 `'DIRS': [BASE_DIR/'templates'],`를 적음

> 메인프로젝트 폴더 안에 넣으면 안됨! manage.py랑 같은 위치에 templates폴더를 만들어야됨!

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRUD_FORM</title>
</head>
<body>
  {% block content %}
  {% endblock content %}
</body>
</html>
```

12. app폴더 안에 `templates`폴더 안에 `articles`폴더를 만든 뒤 아래에 해당 앱의 템플릿을 만듦

```html
{% extends 'base.html' %}
{% block content %}
<h1>메인페이지</h1>
<hr>
{% for article in articles %}
<h1>{{article.title}}</h1>
<hr>
{% endfor %}
{% endblock content %}
```

13. migrate한뒤 서버를 연다

```sh
$python manage.py makemigrations
$python manage.py migrate
$python manage.py runserver
```

14. 해당 앱에 `forms.py`를 만듦

```python
#forms.py
from django import forms
from .models import Article
#모델을 기반으로 만들거야
#forms는 장고에 있는 모듈
class ArticleForm(forms.ModelForm):
    class Meta:
        #괄호안붙임, Article이라는 모델 자체의 정보를 넘김(인스턴스 만드는 것 아님)
        model = Article
        fields = '__all__'
```

15. create를 만들어보쟈

```python
#urls.py
path('create/',views.create,name='create'),
```

- views.py

```python
#views.py
from .forms import ArticleForm
def create(request):
    #쓸수있는 페이지를 보여주고,
    #받은 데이터를 db에 저장
    if request.method == 'POST':
        #request.POST에서 저장된 데이터를 다 불러옴, files이거 다시!!!!!(image추가 떄문에 넣음)
        form = ArticleForm(data=request.POST,files=request.FILES)
        if form.is_valid(): #유효성검사 후 폼을 통해 저장, return 값이 생겨 변수에 저장, 그냥 save()만해도 되지만 나중에 쓸려고 변수에 저장
            article = form.save() #해당 article_pk의 데이터를 article에 저장해서 redirect에서 article.pk를 통해 아이디를 가져옴
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm() #인스턴스를 만듦
    #유효성검사를 통과하지 못했다면! form에 에러메세지가 들어있다
    context = {
        'form' : form,
    }
    return render(request,'articles/create.html',context)
```

- create.html

> form.as_p : form을 p태그로 감싸줌

```html
{% extends 'base.html' %}
{% block content %}
<h1>글쓰기 페이지</h1>
<form action="">
{{form.as_p}}
</form>
{% endblock content %}
```

16. detail만들기

- urls.py

```python
#dynamic routing, article_pk라는 이름은 내가 정하기 나름, views.py에 적는 이름과 동일하면 됨
    path('<int:article_pk>/',views.detail,name='detail'),
```

- views.py

```python
def detail(request,article_pk):
    #상세페이지, article_pk에따른 article을
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article,
    }
    return render(request,'articles/detail.html',context)
```

- detail.html

> 여기서 imag가 있으면 img src를 쓰게 하려면 if article.imag 아래에 img src를 두면 됨!
>
> 이미지가 있을 때만 img태그를 사용!!
>
> 만약에 없다면 오류가 뜬다! alt는 이미지가 없을때 불러오는 이미지 파일인데, 그 파일이 없으면 에러가 남!
>
> 모듈에서 image를 추가해서 공백도 괜찮다고 설정은 했지만 아마 이미지파일이 없기 때문에 에러가 나는 것이 아닐까...싶당.....if문에 넣어주자!

```html
{% extends 'base.html' %}
{% block content %}
<h1>상세페이지</h1>
<h1>{{article.title}}</h1>
<p>{{article.content}}</p>
{% comment %} 이미지가 있으면 이미지뜨게함..? {% endcomment %}
{% if article.image %}
  <img src="{{article.image.url}}" alt="{{article.image}}">
{% endif %}
<ul>
  <li>{{article.created_at}}</li>
  <li>{{article.updated_at}}</li>
</ul>
<a href="{% url 'articles:index' %}">메인 페이지</a>
<a href="{% url 'articles:update' article.pk%}">수정하기</a>
<form action="{% url 'articles:delete' article.pk %}" method='POST'>
{% csrf_token %}
<button>삭제하기</button>
</form>
{% endblock content %}
```

17. update만들기

- urls.py

```python
path('update/<int:article_pk>/',views.update,name='update'),
```

- views.py

```python
def update(request,article_pk):
    #업데이트 할 수 있는 페이지 보여줘야됨
    #내가 이미 썼던 정보가 포함되어 보여야 됨
    #데이터 받아서 업데이트 실제로 수행
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        #수정을 해주기 위해서는 원래의 데이터 값을 받아와야됨! 그래서 instance를 추가해야됨, 없으면 새로운 글을 계속 등록함
        form = ArticleForm(data=request.POST, files=request.FILES, instance=article)
        if form.is_valid():
            form.save()
            #pk값을 넘겨주기 위해 article변수에 form.save()를 담아 같이 인자로 보냄, 근데, 위에 article을 이미 정의했기 때문에 안적어도 됨!
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        #뭘 수정할지 알아야되기때문에, update에서는 article을 안넘겨주면 html에서 article.pk값을 받을 수 없음 그래서 적어 줘야됨
        'article':article
    }
    return render(request,'articles/update.html',context)
```

- update.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>수정 페이지</h1>
<form action="{% url 'articles:update' article.pk %}" method='POST' enctype="multipart/form-data">
  {% csrf_token %}
  {{form.as_p}}
  <button>수정하기</button>
</form>
<a href="{% url 'articles:index' %}">메인페이지</a>
{% endblock content %}
```

18. delete만들기

- urls.py

```python
path('delete/<int:article_pk>/',views.delete,name='delete'),
```

- views.py

```python
@require_POST
def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')
```



#### 아래 추가된 새로운 개념 설명!

19. static 설정

**settings.py**

- 맨 아래에 아래와 같은 구문 추가하여 커스텀 경로 만들기

```python
#그냥두면 장고가 static파일을 인식하지 못하기 때문에 앱별로 static도 인식하고, 기본 static도 인식하게 함
#실제위치는 따로 있지만 그냥 /static/으로 별칭을 두겠다(제일 바깥 폴더)
STATIC_URL = '/static/'
#이거 작성
STATICFILES_DIRS =  [BASE_DIR/'static']
```

- **개발 단계에서 사용하는 실제 정적 파일이 위치한 경로를 지정하는 설정**
- django는 기본적으로 app 내부의 static 파일을 찾을 수 있는데, 프로젝트 내부의 static 파일을 찾기 위해 위와 같이 경로를 작성해 줘야 한다.
-  `STATIC_URL = '/static/'` 의 의미(기본적으로 `setting.py` 에 작성되어 있음.)
  - 실제 파일이나 디렉토리가 아니고 URL 로만 존재하는 단위.



**1) image upload**

> 실제 db에는 이미지가 저장된게 아니라 이미지의 주소가 저장돼있음

- 이미지 파일 업로드하기
- `models.py`에 `image = models.ImageField()` 구문 추가
- 하지만 이미 테이블이 만들어져 있으므로 image 컬럼을 그냥 추가하면 `NOT NULL` 무결성 조건에 위배된다.
- 그러므로 `blank=True`를 추가해야 에러가 발생하지 않는다. (`image = models.ImageField(blank=True)`)

>참고
>
> **`NULL` vs `blank`**
>
>- `NULL`
>  - 기본 값 : `False`
>  - **DB**와 관련되어 있다.(Databased-related)
>  - 주어진 컬럼이 NULL 값을 가질 것인지를 결정.
>- `blank`
>  - 기본 값 : `False`
>  - **데이터 유효성**과 관련되어 있다.(Validation-related)
>  - `full_clean()` / `is_valid()` 처럼 유효성 검사 메서드가 호출될 때 유효성 검사에 사용
>- `null=True, blank=False`: DB 내에서는 해당필드가 NULL을 사용하지만, 웹 사이트에서는 HTML INPUT 태그에 `required`속성이 필요하다라는 것을 의미한다.
>  - `required` 속성 : 반드시 입력해야 다음 단계로 넘어갈 수 있음을 의미
>
>
>
>**주의사항**
>
>- **문자열 기반 필드(CharField, TextField 등)에는 `null=True` 금지(`blank=True`를 차라리 주자)**
>- 이렇게 정의하게 되면 문자열 기반 필드는 `데이터 없음`에 대한 값이 2가지가 된다. **None과 빈 문자열**을 갖게 된다.
>- 데이터 없음에 대한 조건이 2가지이면 중복이기 때문에 문자열 기반 필드는 NULL이 아닌 빈 문자열을 사용하는게 django의 convention이다.
>
>```python
>class Person(models.Model):
>    name = models.TextField(blank=True) # null=True는 금지
>    birth = models.DateField(null=True, blank=True)
>    # 문자열 기반 필드가 아닌 숫자 필드이기 때문에 가능.
>```



- 단, 이미지를 쓸 때 `Pillow`를 설치해야 한다.
  - image 필드를 사용할 때 필수로 필요한 패키지이다.

```sh
$ pip install Pillow
```

- `models.py`의 내용이 수정되었으므로 `migration` 과정을 다시 해줌!!!

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #빈칸이어도 괜찮다는 뜻 blank=true
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
```

- views.py

> `files = request.FILES` 추가
>
> - 이미지도 edit을 통해 새로운 이미지로 수정할 수는 있지만, text 와는 다르게 수정할 때 이미지를 무조건 업로드하지 않으면 에러가 발생한다. (글만 수정하는 건 안 된다는 의미.)
>   - 이미지는 바이너리 데이터(하나의 덩어리)라서 텍스트처럼 **일부만 수정하는게 불가능.**
>   - 그렇기 때문에 html input 태그의 value 속성으로 수정하는 방식이 아니고, 새로운 사진으로 덮어 씌우는 방법을 사용.
>   - `<input type="file">` 가 `value=""` 를 지원하지 않는다.
>   - 정말 글만 수정하고 싶다면 이전과 똑같은 이미지를 업로드하면 된다.
>
> `views.py`의 `update` 함수에 `files = request.FILES` 추가
>
> `update.html` 에도 두 줄 추가

```python
def create(request):
    #쓸수있는 페이지를 보여주고,
    #받은 데이터를 db에 저장
    if request.method == 'POST':
        #request.POST에서 저장된 데이터를 다 불러옴, files이거 다시!!!!!(image추가 떄문에 넣음)
        form = ArticleForm(data=request.POST,files=request.FILES)
        if form.is_valid(): #유효성검사 후 폼을 통해 저장, return 값이 생겨 변수에 저장, 그냥 save()만해도 되지만 나중에 쓸려고 변수에 저장
            article = form.save() #해당 article_pk의 데이터를 article에 저장해서 redirect에서 article.pk를 통해 아이디를 가져옴
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm() #인스턴스를 만듦
    #유효성검사를 통과하지 못했다면! form에 에러메세지가 들어있다
    context = {
        'form' : form,
    }
    return render(request,'articles/create.html',context)

def update(request,article_pk):
    #업데이트 할 수 있는 페이지 보여줘야됨
    #내가 이미 썼던 정보가 포함되어 보여야 됨
    #데이터 받아서 업데이트 실제로 수행
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        #수정을 해주기 위해서는 원래의 데이터 값을 받아와야됨! 그래서 instance를 추가해야됨, 없으면 새로운 글을 계속 등록함
        form = ArticleForm(data=request.POST, files=request.FILES, instance=article)
        if form.is_valid():
            form.save()
            #pk값을 넘겨주기 위해 article변수에 form.save()를 담아 같이 인자로 보냄, 근데, 위에 article을 이미 정의했기 때문에 안적어도 됨!
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        #뭘 수정할지 알아야되기때문에, update에서는 article을 안넘겨주면 html에서 article.pk값을 받을 수 없음 그래서 적어 줘야됨
        'article':article
    }
    return render(request,'articles/update.html',context)
```

- create.html

> 파일을 올릴 때는 `enctype="multipart/form-data"`를 반드시 추가해줘야 한다.

```html
{% extends 'base.html' %}
{% block content %}
<h1>글쓰기 페이지</h1>
<form action="{% url 'articles:create' %}" method='POST' enctype="multipart/form-data">
  {% csrf_token %}
  {{form.as_p}}
  <button class='btn btn-primary'>제출하기</button>
</form>
<a href="{% url 'articles:index' %}">메인페이지</a>
{% endblock content %}
```

- detail.html

> `<img src="{{ article.image.url }}" alt="{{ article.image }}">` 구문 추가
>
> 하지만 이 상태에서는 업로드한 이미지가 나오지 않는다. 미디어 파일 경로를 설정해 줘야 한다.
>
> <문제점!>
>
> 이미지 필드 설정 이전에 작성했던 게시글의 detail 페이지가 동작하지 않는다.
>
> - `article.image.url` 을 불러오지 못하기 때문이다.
>
> 해결방법1
>
> - static 파일로 이미지가 없을 때 대신 사용할 이미지를 미리 넣어둠.
> - `static` > `articles` > `images` 에 대체 이미지 저장
>
> 해결방법2
>
> - 템프릿에서 `{% if %}` 문으로 `article.image` 가 존재하는 경우(True인 경우)만 이미지를 출력하도록 설정

```html
{% extends 'base.html' %}
{% block content %}
<h1>상세페이지</h1>
<h1>{{article.title}}</h1>
<p>{{article.content}}</p>
{% if article.image %}
  <img src="{{article.image.url}}" alt="{{article.image}}">
{% endif %}
<ul>
  <li>{{article.created_at}}</li>
  <li>{{article.updated_at}}</li>
</ul>
<a href="{% url 'articles:index' %}">메인 페이지</a>
<a href="{% url 'articles:update' article.pk%}">수정하기</a>
<form action="{% url 'articles:delete' article.pk %}" method='POST'>
{% csrf_token %}
<button>삭제하기</button>
</form>
{% endblock content %}
```

- update.html

> `enctype="multipart/form-data"`추가

```html
{% extends 'base.html' %}
{% block content %}
<h1>수정 페이지</h1>
<form action="{% url 'articles:update' article.pk %}" method='POST' enctype="multipart/form-data">
  {% csrf_token %}
  {{form.as_p}}
  <button>수정하기</button>
</form>
<a href="{% url 'articles:index' %}">메인페이지</a>
{% endblock content %}
```



**2) 미디어 파일 경로 설정**

- settings.py(맨 아래에 추가!)

```python
# STATIC_URL 과 비슷한 역할을 한다.
# 업로드 된 파일(stored files)의 URL 주소를 만들어주는 역할.
# 주의사항 : STATIC_URL 과 값이 달라야 한다.
MEDIA_URL = '/media/'

# STATICFILES_DIRS 와 비슷한 역할을 한다.
# 실제 파일이 업로드 되면 어디에 저장될 지 정하는 실제 경로.
# 주의사항 : STATICFILES_DIRS 와 값이 달라야 한다.
# 개발 단계에서 사용하는 경로이므로 실제 배포 단계에서는 다른 경로 설정을 해야 한다.
MEDIA_ROOT = BASE_DIR/'media'
```

- 본 프로젝트(crud_form)의 `urls.py`

> 첫 번째 인자(settings.MEDIA_URL) : 어떤 url을 정적으로 추가할지 (Media file url)
>
> 두 번째 인자(document_root=) : 실제 해당 미디어 파일이 어디에 존재하는지
>
> static은 url을 설정을 해주는 녀석인데, 어떤일을 할거냐면 MEDIA_URL로 url을 만들건데 MEDIA_ROOT에 있는 파일을 가지고 url을 만들거야
> list더하기를 이용함, MEDIA_URL과 실제 url이 어떻게 될지 작성하고 실제 파일들은 MEDIA_ROOT에 담겨있다고 알려주는 느낌
> 이 두가지 정보를 가지고 실제 url을 만듦

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```









------------------

## Static

> html,js,css,image,video 정적 static

- settings.py에서 INSTALLED_APPS 제일 밑에 적힌 것이 static을 관리함

```python
INSTALLED_APPS = [
 #(생략)
    'django.contrib.staticfiles',
]
```



- base.html에 `block css`를 만들어서 static모듈을 관리하게 함!

```html
{% load static %}
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRUD_FORM</title>
  <link rel="stylesheet" href="{% static 'base.css' %}">
  <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
  {% block css %}
  {% endblock css %}
</head>
<body>
  {% block content %}
  {% endblock content %}
  <script src="{% static 'js/bootstrap.bundle.js' %}"></script>
</body>
</html>
```



- articles앱에 static폴더를 만든 뒤, articles폴더를 만든 뒤, `index.css`를 만든다

```css
/* 가상선택자 종류, 클릭하면 바뀌는 것! visited는 클릭했다는 뜻, 눌렀을때 빨개짐*/
a:visited {
  color:crimson;
}
```

- index.html

> extends는 항상 최상단에 위치하고 아래에 `{% extends 'base.html' %}`을 써서 static을 쓰기 위해 씀
>
> base.html에서 설정한 block css를 써서 articles폴더안에 들어있는 index.css를 불러옴

```html
{% extends 'base.html' %}
{% load static %}
{% block css %}
  <link rel="stylesheet" href="{% static 'articles/index.css' %}">
{% endblock css %}

{% block content %}
<h1>메인페이지</h1>
<a href="{% url 'articles:create' %}">글쓰기</a>
<hr>
{% for article in articles %}
<a href="{% url 'articles:detail' article.pk%}">
  <h1>{{article.title}}</h1>
</a>
<hr>
{% endfor %}
{% endblock content %}
```



#### 부트스트랩 static 다운받아 쓰기

> 왜 굳이 다운받는걸 택했을까?
>
> CDN으로 파일을 관리하게 되면 의존성이 더 커짐! 만약 이 서버가 무너져서 못쓰게 된다면, 내 프로그램도 영향이 크게 생김, 서비스의 신뢰성이 중요하게 생각되는 경우 의존성을 줄이기 위해 직접 다운받아 넣는다

- 부트스트랩 다운받아 static폴더에 넣고, css는 head에, js는 body 젤 밑에 script src에 폴더 위치를 적음

> base.html
>
> head에 `<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">`추가
>
> body에 `<script src="{% static 'js/bootstrap.bundle.js' %}"></script>`추가

```html
{% load static %}
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRUD_FORM</title>
  <link rel="stylesheet" href="{% static 'base.css' %}">
  <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
  {% block css %}
  {% endblock css %}
</head>
<body>
  {% block content %}
  {% endblock content %}
  <script src="{% static 'js/bootstrap.bundle.js' %}"></script>
</body>
</html>
```

- 위와 같이 하면 부트스트랩 적용가능
- 예시, create.html

> `<button class='btn btn-primary'>제출하기</button>` 이렇게 해서 제출하기 버튼 파랗게 만듦

```html
{% extends 'base.html' %}
{% block content %}
<h1>글쓰기 페이지</h1>
<form action="{% url 'articles:create' %}" method='POST' enctype="multipart/form-data">
  {% csrf_token %}
  {{form.as_p}}
  <button class='btn btn-primary'>제출하기</button>
</form>
<a href="{% url 'articles:index' %}">메인페이지</a>
{% endblock content %}
```







-------------------

#### image resizing

> 이미지가 너무 큼!
>
> 썸네일 이미지는 적당한 크기면 됨 너무 크면 돈이 많이 든다!
>
> 이런것들을 내 필요에 맞게 적당히 잘라서 저장할 필요가 있음

- `pillow`, `pilkit`, `django-imagekit`를 미리 설치해야 한다.
  - **설치 순서 : `pillow` -> `pilkit` -> `django-imagekit` (반드시 지키자!!)**
  - `pilkit` : `pillow` 를 쉽게 쓸 수 있도록 도와주는 라이브러리
  - `django-imagekit` : 이미지 helper를 제공하는 dango app
  - `settings.py` 에 `django-imagekit` app 등록 => `'imagekit',` 추가



> 순서 맞춰서 설치해야됨! 아니면 에러가 날 수 있음

```sh
$pip install pilkit
$pip install django-imagekit
```

- settings.py

```python
INSTALLED_APPS = [
    'articles',
    'imagekit',
```

- models.py

```python
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #빈칸이어도 괜찮다는 뜻 blank=true
    # image = models.ImageField(blank=True)
    #다시 이미지 필드 씀->이미지 크기 조절(width,height)
    image = ProcessedImageField(
        blank=True, 
        #사용자가 올린 이미지 가공을 해서 원본그대로가 아니라 썸네일처럼 잘라서 올림
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90},
        upload_to='%Y/%m/%d',
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
```



#### (1) html 태그로 직접 사이즈 조정

- 원본은 그대로 저장되어 있고 보여지는 사이즈만 조정하는 것이기 때문에 근본적인 해결책이 아니다.



#### (2) 업로드 할 때 이미지 자체를 resizing 해서 저장

##### ① 원본 X / 썸네일 O

> `models.py`
>
> - 맨 위에 두 줄 추가
>
> ```python
> from imagekit.models import ProcessedImageField
> from imagekit.processors import Thumbnail
> ```
>
> - ImageField 대신 다음 구문으로 작성
>   - `Thumbnail`은 이미지를 잘라서 저장되는 것이므로 원본 비율을 유지한채 작게 저장하고 싶으면 다른 것을 찾아서 쓰면 된다.
>
> ```python
> 	image = ProcessedImageField(
>         # ProcessedImageField 에 인자로 들어가 있는 값들은 migrations 이후에
>         # 추가되거나 수정되더라도 makemigrations 를 하지 않아도 된다.
>         processors=[Thumbnail(200, 300)], # processors : 처리할 작업 목록
>         format='JPEG', # 저장 포맷 (JPEG가 퀄리티를 낮췄을 때 이미지가 덜 깨진다.)
>         options={'quality': 90}, # 추가 옵션들
>         upload_to='articles/images', # 저장 위치(MEDIA_ROOT/articles/images)
>     )
> ```

##### ② 원본 O / 썸네일 O

> `models.py`
>
> - import 구문 수정
>
> ```python
> from imagekit.models import ProcessedImageField, ImageSpecField
> ```
>
> - image 필드 내용 수정
>   - 썸네일을 쓰겠다고 호출하는 순간에만 썸네일로 저장된다.
>   - 이 때는 image 필드를 다시 추가했으므로 migrations 과정을 다시 해줘야 한다.
>
> ```python
> 	image = models.ImageField(blank=True)
>     image_thumbnail = ImageSpecField( # detail.html에서 썸네일을 호출할 때만 불러온다.
>         source='image', # 원본 ImageField 이름 (upload_to 대신 source를 사용)
>         processors=[Thumbnail(200, 300)],
>         format='JPEG',
>         options={'quality': 90},
>     )
> ```

> `detail.html`
>
> - `{% block content %}` 내부에 아래 구문 추가
>
> ```
> <img src="{{ article.image_thumbnail.url }}" alt="썸네일">
> ```





[참고,출처, 이분 정리 진짜 잘하심..](https://github.com/wally-wally/TIL/blob/master/04_django/%5BSSAFY%5Ddjango_%232.md)