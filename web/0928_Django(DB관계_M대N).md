# Django M:N관계

> 지난 시간
>
> A many to one relationship
>
> User-Article/ User-Comment
>
> User 대체 -> Custom user model
>
> 대체 후 회원가입 이뤄지지 않음, 대체한 후 회원가입 진행 안됨-> 회원가입에 대한 user creationform이 기본적으로 장고가 user를 대체하기 전인 기본 user model로 만들어진 모델폼이기 떄문
>
> 그래서 custom model로 만들어서 바꿔줘야됨(Userchangeform도 마찬가지)
>
> - user참조
>   - get_user_model() : models.py가 아닌 모든 곳
>   - AUTH_USER_MODEL  : models.py에서만!(문자열), 실행순서 때문
>
>   
>
> 1. 커스텀유저모델을 쓰기로 결정했다
> 2. model을 accouts에 만듦
> 3. 장고한테 내가 만든 user모델을 쓰겠다고 알려줘야됨!-> settings.py에 적어줘야됨, django한테 내가 만든 유저모델을 기본 유저모델로 쓸거라고 알려줌(Auth_User_model='accounts.User'):내가 만든 user모델 위치
> 4. 사용을 할 때 기준이 있음 model에서 사용할 때 settings.AUTH_USER_MODEL을 사용함, 다른 곳에서 사용할 때 get_user_model(get_user_model을 모두 써도 최신장고 버전에서는 관계없다고 공식문서에 적혀있지만 관례상 나눠서 쓴다!)
>
>    

## A many-to-many relationship

![image-20200928093941422](0928_Django(DB관계_M대N).assets/image-20200928093941422.png)

> 한계 : 환자가 다른 의사한테 또 진료를 받고 싶다면 필드를 한번 더 사용해야되고, harry라는 환자가 두명의 의사한테 동시에 진료를 받을 수 없었음!
>
> 그래서 중개모델을 작성!



![image-20200928094442508](0928_Django(DB관계_M대N).assets/image-20200928094442508.png)

> 각각의 모델과 1:N의 관계를 맺음, 지금 1번의사한테 두명의 환자가 예약되어있는 것을 보여줌 
>
> 데이터를 조회할 때 아래와 같이 shell_plus에 입력했음
>
> ![image-20200930185919266](0928_Django(DB관계_M대N).assets/image-20200930185919266.png)



![image-20200928094500784](0928_Django(DB관계_M대N).assets/image-20200928094500784.png)

> 의사가 환자들을 조회를 하고 싶다!
>
> 환자도 내가 진료를 받을 의사들을 조회하고 싶다!
>
> 여기서 ManyToManyField가 등장
>
> 두 모델간 종속관계가 없어 둘중 어느 모델에 써도 관계 없음! Doctor에 적어도 상관없음
>
> ![image-20200928094531785](0928_Django(DB관계_M대N).assets/image-20200928094531785.png)
>
> 참조되는 모델의 복수형으로 적으면 됨!
>
> 조회할때의 명령어는 이렇게 씀!
>
> ![image-20200930190154615](0928_Django(DB관계_M대N).assets/image-20200930190154615.png)
>
> 1번환자를 조회하고
>
> 1번환자의 모든 예약을 역참조로 불러옴
>
> 내가 오늘 진료를 받을 의사만 보여줌! Patient가 바로 의사를 참조하는 것처럼 보이게 함 
>
> ![image-20200928094722487](0928_Django(DB관계_M대N).assets/image-20200928094722487.png)
>
> 하지만 여전히 Doctor는 Reservation을 통해서만 Patient를 참조할 수 있음!
>
> ManyToManyField는 종속관계는 없지만 역참조를 하면 Doctor도 patient를 참조할 수 있음!
>
> ![image-20200928094732248](0928_Django(DB관계_M대N).assets/image-20200928094732248.png)
>
> `related_name=`역참조시 사용하는 `manager`를 변경함
>
> ![image-20200930191025532](0928_Django(DB관계_M대N).assets/image-20200930191025532.png)
>
> `related_name`을 설정하고 나면 이전에 사용했던 명령어 `patient_set`은 쓸 수 없음!





![image-20200928095013372](0928_Django(DB관계_M대N).assets/image-20200928095013372.png)

>![image-20200930191833211](0928_Django(DB관계_M대N).assets/image-20200930191833211.png)





## ManyToManyField

> [Django공식문서](https://docs.djangoproject.com/en/3.1/ref/models/fields/#manytomanyfield)

- M:N관계를 나타내기 위해 사용하는 필드
- 하나의 필수 위치 인자(M:N 관계로 설정할 모델 클래스)가 필요하다

> DB Reperesentation(데이터베이스에서의 표현)

- django는 M:N관계를 나타내는 **중개 테이블**(intermediary join table)을 만든다
- 테이블 이름은 ManyToManyField의 이름과 이를 포함하는 모델의 이름을 조합하여 생성함

> Arguments

- 모두 optional 하며 관계가 작동하는 방식을 제어함

- `related_name`
  
  - ForeignKey의 related_name과 동일
  
- `through`
  - 중개 테이블을 **직접** 작성하려는 경우 지정
  - 일반적으로 **추가 데이터**를 M:N 관계와 연결하려는 경우에 사용
  
- `symmetrical`(대칭적임)
  - ManyToManyField가 동일한 모델(self)을 가리키는 정의에서만 사용
  - 재귀적 정의(대댓글 관계)
  
  ![image-20201001132426350](0928_Django(DB관계_M대N).assets/image-20201001132426350.png)
  
  - 예시처럼 동일한 모델을 가리키는 경우 Person 클래스에 person_set 매니저를 추가 하지 않는다.
  - 대신 대칭적(symmetrical)이라고 간주하며, source인스턴스(참조하는)가 target 인스턴스(참조되는)를 참조하면 target 인스턴스도 sourxe인스턴스를 참조하게 됨
  - self와 M:N관계에서 대칭을 원하지 않는 경우 **`semmetrical`를 `False`로 설정함**(기본값이 True)
  - Folllow도 마찬가지! 내가 팔로우 한다고 상대도 팔로우 되는게 아님! 그래서 False로 바꿔야됨!
  
- etc.....





## LIKE(좋아요) 구현

> 하나의 article에는 여러user가 좋아요를 할 수 있다
>
> 한명의 user는 여러 article에 좋아요를 누를 수 있다
>
> Article - User M:N관계!

- `articles` > `models.py`

> `like_users` : ManyToManyField를 맺는 첫번째 필수인자, user(user모델 참조는 models.py에서는 `settings.AUTH_USER_MODEL`) 나머지 인자는 옵션인데 역참조 명령어를 `related_name='like_article'`로 줌!
>
> 그냥 like_users도 users, related_name도 원래 기본대로 할래! 라고 했을 때 아래와 같은 역참조시 충돌됐다는 오류가 남!
>
> ![image-20200930230608193](0928_Django(DB관계_M대N).assets/image-20200930230608193.png)
>
> related_name을 더해라! 이상황에서는 이 인자가 필수가 돼버림!
>
> WHY??
>
> **1:N**
>
> Article은 User랑 이미 1:N 관계가 설정 돼있음!
>
> -  article이  user를 참조할 때 / `article.user`
> - article이 user를  역참조할때 / `user.article_set`(유저가 작성한 게시글들 조회)
>
> **M:N**
>
> 여기서 M대 N관계가 `users`라는 필드명으로 추가됨!
>
> - article이 user를 참조할 때 / `article.users`
> - article이 user를 역참조할 때/ `user.article_set`(유저가 좋아요한 게시글들 조회)
>
> 의도는 다른데 역참조 명령어가 겹쳐서 충돌이 일어남!!
>
> ERROR HINT대로 related_name을 필수로 바꿔줘야되는 상황이 생김!
>
> **M:N 필드명 수정!**
>
> - article이 user를 참조할 때 users-> like_users/ `article.like_users`(이 게시글에 좋아요를 누른 유저들을 조회)
> - article이 user를 역참조할 때 `related_name = 'like_articles'`/ `user.like_articles`(유저가 좋아요한 게시글들 조회)
>
> M:N관계 필드를 추가해 models.py가 변경이 됐으니 migration해줌! 이거는 필드값이 추가된것처럼 보이지만 1:N관계필드를 추가했을 때는 default값을 물어보는게 나왔었는데, ManyToManyField는 실제 물리적 필드가 아니기 때문에 Aricile과 User에 필드가 새로 생기는 것이 아니라 테이블 하나가 더 생기는 것일 뿐!
>
> 이것은 핵심이 중개모델을 만드는 것! 그래서 필드의 변화가 없고 그래서 defalut값이 필요없다!
>
> 이 테이블의 이름 규칙 `articles_article_like_users(앱이름_그 필드가 참조하는 모델의 이름_그모델에 작성된 필드 이름)` 각각의 모델에 대한 외래키를 가지고 있음!
>
> ![image-20200930235216291](0928_Django(DB관계_M대N).assets/image-20200930235216291.png)

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #like_users 키 추가
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

```



- `articles` > `urls.py`

> 좋아요를 누를 수 있는 url이 필요함
>
> 좋아요는 게시글에 있음! 그래서 articles앱에 적을거야
>
> 어떤 게시글에 좋아요를 눌렀는지 동적라우팅이 필요함

```python
from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    
    # 추가
    path('<int:article_pk>/like/', views.like, name='like'),
]
```

- `articles` > `views.py`

> DB의 테이블값에 변화가 있음,  중개모델 테이블이 달라지기 때문!
>
> 그래서 POST로 데이터를 받음!
>
> `add`와 `remove`를 통해 추가와 삭제를 할 수 있음
>
> (참고) 삭제된 pk는 재사용되지 않는다
>
> `article.like_users.filter(pk=request.user.pk).exists()`
>
> 장고는 in(포함)의 개념보다는 존재하는지(`exists()`) 묻는 것을 더 권장함! 전체에서 하나를 찾아야되는 상황에서 `exixts()`를 사용해라!(in보다 내부적으로 더 빠르게 잘 작동할 수 있음)
>
> WHY! `.get()`이 아니라 왜 `.filter()`를 썼냐?
>
> `.filter()` : 해당조건을 만족하는 쿼리셋을 리턴함! 0개,1개,2개,,,등 에러를 발생시키지 않음
>
> 하지만 `.get()`은 값이 없다면 에러가남!

```python
@require_POST
def like(request, article_pk):
    # 인증된 사용자만 가능
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # user가 article에 좋아요를 눌렀는지 안눌렀는지
        
        # 1-1. user가 article을 좋아요 누른 전체유저에 포함이 되어있는지 안되어있는지.
        # if request.user in article.like_users.all():
        
        
        #1-2가 장고가 권장한대로 작성한 것!
        # 1-2. user가 article을 좋아요 누른 전체유저에 존재하는지.
        # 해당 게시글에 좋아요를 누른 사람들 중에서 현재 접속유저가 있다면 좋아요를 취소
        if article.like_users.filter(pk=request.user.pk).exists():
            # 좋아요 취소(중개테이블에서 좋아요를 빼겠다)
            article.like_users.remove(request.user)
        else:
            # 좋아요
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

- `base.html`

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

<!--FontAwesome을 사용할 수 있게 추가해줌-->
  <script src="https://kit.fontawesome.com/dacf7dcd9c.js" crossorigin="anonymous"></script>
  <title>Document</title>
</head>
```

- `articles` > `index.html`

> `<i class="fas fa-heart"></i>` 하트이미지 추가
>
> button태그는 default가 submit임!, 하트의 이미지를 누르면 좋아요 설정, 삭제를 하게 만들기 위해!
>
> submit을 바꾸기를 위해 버튼은 활용하는 것이 스타일링하기 편함!
>
> 버튼 모양 바꾸기 -> 부트스트랩 Link class를 주면 버튼 모양 사라짐, `style="color: black;"`을 주면 색도 바뀜
>
> `{{ article.like_users.all }} ` 개수를 구할 때 `|length` or `.count()`를 적으면 개수를 구할 수 있다

```html
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">NEW</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인 하세요]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p><b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b></p>
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>

<!--아래 구문 추가-->
    <form action="{% url 'articles:like' article.pk %}" method="POST" class="d-inline">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <button class="btn btn-link" style="color: crimson;">
          <i class="fas fa-heart"></i>
        </button>
      {% else %}
        <button class="btn btn-link" style="color: black;">
          <i class="fas fa-heart"></i>
        </button>
      {% endif %}
    </form>
    {{ article.like_users.all|length }} 명이 이 글을 좋아합니다.
    <br>
<!--여기까지-->
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}
```





## Profile

> 프로필페이지를 만든 뒤 그안에 follow를 만듦
>
> 계정에 관계가 있으니 accounts앱에! articles에 만들어도 관계없음 자기가 구성하기 나름

- `accounts` > `urls.py`

> `path('<username>/'`에서 `str:`은 기본값이기 때문에 생략가능!
>

```python
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_password, name='change_password'),

    #아래구문 추가
    path('<username>/', views.profile, name='profile'),
]

```

- `accounts` > `views.py`

> `username`도 중복이 되는것이 아니기 때문에 pk값과 같음
>
> `user`라는 변수는 템플릿으로 넘어갔을 때 다른 변수와 겹칠 확률이 높음 그래서 view에서는 `person`이라는 변수로 정함
>
> `views.py`에서 User모델을 참조하려면 `models.py`가 아닌 곳에서는 `get_user_model()`로 참조를 함

```python
from django.contrib.auth import get_user_model

def profile(request, username):
    #직관적으로 쓰려면 이렇게!
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    #한줄로 아래와 같이 작성해도 됨
    #perosn = get_object_or_404(get_user_model(),username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

- `accounts` > `profile.html`

> 이 유저가 작성한 모든 게시글을 쿼리셋으로 받으려면 역참조를 이용함!
>
> `person.article_set.all`을 이용!
>
> 이 user가 작성한 댓글도 `person.commnet_set.all`역참조 이용
>
> 좋아요한 것들을 모두 출력하려면 `related_name`을 변경했던 것을 이용해 `person.like_articles.all`을 사용

```html
{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">{{ person.username }}의 프로필</h1>
<hr>
<!--팔로우/언팔로우 버튼/팔로워수/팔로잉 수-->
{% include 'accounts/_follow.html' %}

<hr>

<h2>{{ person.username }}이 작성한 게시글</h2>
<!--이 user가 작성한 게시글을 쿼리셋으로 받아 출력-->
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>

<h2>{{ person.username }}이 작성한 댓글</h2>
<!--이 user가 작성한 댓글을 쿼리셋으로 받아 출력-->
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}
<hr>

<h2>{{ person.username }}이 좋아요 한 게시글</h2>
<!--이 user가 좋아요한 게시글을 쿼리셋으로 받아 출력-->
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>

<a href="{% url 'articles:index' %}">[back]</a>

{% endblock %}
```

- `articles` > `index.html`

> `article.user.username` : 이게시글을 작성한 user의 username의 url로 이동!

```html
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">NEW</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인 하세요]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
<!--작성자의 profile로 이동하게 만듦-->
    <p><b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b></p>


    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <form action="{% url 'articles:like' article.pk %}" method="POST" class="d-inline">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <button class="btn btn-link" style="color: crimson;">
          <i class="fas fa-heart"></i>
        </button>
      {% else %}
        <button class="btn btn-link" style="color: black;">
          <i class="fas fa-heart"></i>
        </button>
      {% endif %}
    </form>
    {{ article.likes }} 명이 이 글을 좋아합니다.
    <br>
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

- 내프로필로 이동
- `base.html`

> `request.user.username`을 통해 눌렀을 때 내프로필로 이동하는 링크 만듦

```html
<h3>Hello, {{ user.username }}</h3>
    {% if request.user.is_authenticated %}
<!--내프로필로 이동 추가-->
      <a href="{% url 'accounts:profile' request.user.username %}">내프로필</a>
      <a href="{% url 'accounts:update' %}">정보수정</a>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
```



### Follow

- `accounts` > `models.py`

> follow는 우리가 custom한 User에 적을거야! 그래서 프젝 처음 시작부터 User대체 작업을 해놔야 필드를 추가하기 편하다!
>
> 내가 팔로잉을 했을 때 상대방도 팔로잉 하게 대칭되지 않게 `symmetrical=False`로 인자를 줌
>
> `related_name='followers'`와 필드이름 `followings`는 이름이 어차피 `self`같은 것을 참조하기 때문에 바꿔 적어도 상관없지만 생각하기 편하게 내가 참조할때는 following이라는 단어를 쓰는게 편하니까 이렇게 적음
>
> 이렇게 하면 User에 followings라는 필드가 생가나요?
>
> -> 아니요! ManyToManyField이기 때문에 아예 새로운 중개테이블이 생기는 것이지 필드가 추가되는 것은 아님!!
>
> 아래는 Like의 중개모델 
>
> **만약 source모델과 target모델이 다르다면** 필드는 아래처럼 만들어짐
>
> `source_id`->`target_id`
>
> ![image-20201001135409568](0928_Django(DB관계_M대N).assets/image-20201001135409568.png)
>
> 그럼 Followings의 중개모델은? source와 target모델이 같음!
>
> **만약 source와 target이 같은 경우라면?**
>
> `from_모델_id`,` to_모델_id`
>
> id는 기본적으로 있음
>
> ManyToManyField가 정의된 필드가 먼저 나옴
>
> 그리고 target모델이름이 뒤쪽에 other_model로 나옴 
>
> self를 참조하는 경우 아래와 같이 중개테이블이 만들어짐
>
> | id   | `from_user_id` | `to_user_id` |
> | ---- | -------------- | ------------ |
> |      | 1              | 2            |
> |      | 2              | 1            |
>
> 1번유저가 2번유저를 참조(첫번째 줄)
>
> 만약 맞팔이 되려면 2 1도 새로 추가돼야함(2번째 줄)
>
> User모델이 변경됐기 때문에 migration해야됨!
>
> ![image-20201001180217457](0928_Django(DB관계_M대N).assets/image-20201001180217457.png)

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- `accounts` > `urls.py`

> follow는 user_pk를 알아야됨!

```python
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

- `accounts` > `views.py`

> 두명의 user가 필요함(follow하는 상대방, 나)
>
> **주의**
>
> 나자신을 follow할 수 없도록 해야됨! ` if me != you:` 이거 설정을 먼저 해야됨!

```python
@require_POST
def follow(request, user_pk):
    # 상대방(user_pk로 정보를 가져와야됨)
    you = get_object_or_404(get_user_model(), pk=user_pk)
    # 나(요청안에 들어있음)
    me = request.user
	
    if me != you:
        #user(내가) 어떤 사람을 following하려함, person의 입장에서 이사람의 followers(이 사람을 following하고있는 사람)의 안에 내가 있다면 이미 following 하고 있단 뜻! 그렇다면 언팔
        # if user in person.followers.all():
        	#person.followers.remove(me)
         #else:
        	#person.followers.add(me)
        
        #만약 .exists 쿼리셋 API로 바꾼다면 아래처럼 바뀜!
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
        else:#없다면 following
            you.followers.add(me)
    #프로필로 redirect할건데 상대방의 username을 가지고 그 사람의 profile로 가야됨!
    return redirect('accounts:profile', you.username)
```

- 부트스트렙의 `jumbotron`을 가져다 follow로 쓸거야!
- 팔로워수`person.followers.all|length`, 팔로잉수`person.followings.all|length`
- `detail view함수`

```python
detail view에 다음 두 줄 구문 추가

person = get_object_or_404(get_user_model(), pk=article.user_id) # template에서 person을 사용하기 위해 추가함
context = {
    'article': article,
    'comment_form': comment_form,
    'comments': comments,
    'person': person,
}
```



- 템플릿을 분할하는 것이 좋음!
  - 나중에 따로 사용할만하거나 해당페이지에서 정리가 좀 필요하다면 분할을 하는 것도 좋음!

- `accounts` > `_follow.html`

> 개인적으로 앞에 `_`하는 것이 분할된 템플릿이라는 걸 표시해주기 위해 적음
>
> 분할한 페이지를 적는 것은 `accounts`> `profile.html`에 `{% include "accounts/_follow.html" %}`을 적으면 분할된 템플릿을 해당 위치에 넣을 수 있음!

```html
<!-- 팔로워 수 / 팔로잉 수 -->
<div class="jumbotron">
    <p class="lead">
      팔로워 수 : {{ person.followers.all|length }} / 팔로잉 수 : {{ person.followings.all|length }} 
    </p>
    <!-- 팔로우 버튼 / 언팔로우 버튼 -->
    <!--나를 follow하면 안되니까! 나한테는 이 버튼들이 안보이게 함-->
    {% if request.user != person %}
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        <!--팔로우가 돼있다면 unfollow버튼을 보여주고 아니면 Follow를 보여줌-->
        {% if request.user in perosn.followers.all %}
          <button class="btn btn-secondary">Unfollow</button>
        {% else %}
          <button class="btn btn-primary">Follow</button>
        {% endif %}
      </form>
    {% endif %}
</div>
```





-------------------

정규수업과정 끝

아래는 그냥 추가로 한 것

## 쿼리 최적화, DB 최적화

**주의사항**

- **성급한 조기 최적화는 프로그래밍에서 악의 근원이다.**
- **코드는 코드 자체적으로도 빨라야 하지만, 더 중요한 것은 다른 개발자들이 읽기 쉬워야한다.**

- html에서 중복된 쿼리들을 변수화 할 수 있음

> `person.follwers.all`이나 `person.followings.all` 이런것들이 계속 반복돼서 쓰이고 있음
>
> 이때 `with` template tag가 있음! 기능상으로 바뀐건 없음! 
>
> - 복잡한 변수를 더 간단한 이름으로 저장(캐시)하며, 여러 번 DB를 조회할 때(특히 비용이 많이 드는) 유용하게 사용가능하다.
>
> `with 변수=반복되는코드 변수=반복되는코드` 그리고 이 변수들을 사용할 범위를 정하고 `endwith`으로 닫아주면 됨!
>
> ` {% with followers=person.followers.all followings=person.followings.all %}`

```html
<!-- 팔로워 수 / 팔로잉 수 -->
<div class="jumbotron">
  {% with followers=person.followers.all followings=person.followings.all %}
    <p class="lead">
      팔로워 수 : {{ followers|length }} / 팔로잉 수 : {{ followings|length }} 
    </p>
    <!-- 팔로우 버튼 / 언팔로우 버튼 -->
    <!--나를 follow하면 안되니까! 나한테는 이 버튼들이 안보이게 함-->
    {% if request.user != person %}
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        <!--팔로우가 돼있다면 unfollow버튼을 보여주고 아니면 Follow를 보여줌-->
        {% if request.user in followers %}
          <button class="btn btn-secondary">Unfollow</button>
        {% else %}
          <button class="btn btn-primary">Follow</button>
        {% endif %}
      </form>
    {% endif %}
  {% endwith %}
</div>
```



#### Django Debug Toolbar

- 쿼리의 최적화, 지연시간 최적화를 어떻게 해야될까?
- 라이브러리의 힘을 빌려야됨 `Django Debug Toolbar`

> 설치법 외우는 것이 아니라 [공식문서](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) 보고 적기

```sh
$ python -m pip install django-debug-toolbar
```

- `settings.py`

> `'debug_toolbar',` 추가

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    # ...
    'debug_toolbar',
]

MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]
STATIC_URL = '/static/'

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
```

- project의 `urls.py`에 아래 구문 추가해서

```python
import debug_toolbar
from django.conf import settings

urlpatterns = [
    ...
    path('__debug__/', include(debug_toolbar.urls)),
]
```

- 최종 프로젝트의 urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
#아래 추가
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
```

- runserver를 했을 때 오른쪽에 Debug를 할 수있는 bar가 생김
- 데이터베이스 최적화는 중복되는 것을 알려주고 그것을 줄여나가는 것



#### annotate

> Count라던지 평균값 등 값을 계산해서 하는 경우는 `annotate`를 주로사용
>
> 1:N, 1:1 -> `select_related`
>
> `1:N(역참조)`, `M:N` -> `prefetch_related`

- `articles` > `views.py` > `index`

> Article에 있는 필드만 가져오는게 아니라 이 Article에 좋아요 하고있는 개수 컬럼(필드명:`likes`)을 하나를 더 만들겠다
>
> `like_users`의 값을 셀거야! Count를 import해옴(aggregation function)
>
> 이렇게 하면 index페이지에서 like_users한 사람들을 불러오는것을 중복해서 처리하지 않게되고 view에서 한번에 처리함!

```python
from django.db.models import Count
def index(request):
    articles = Article.objects.annotate(likes=Count('like_users')).order_by('-pk')
```

| Article          | likes                                                        |
| ---------------- | ------------------------------------------------------------ |
| 원래 Article필드 | 이 Article에 좋아요를 하고 있는(`like_users`) 개수 필드 추가 |

- `index.html`

> 여기서 `article.like_users.all|length`이게 계속 중복되고 있음!
>
> 최적화하려면 이걸 바꿔야됨
>
> 이거를 새로만든 필드면 `likes`를 이용해서 줄임
>
> **주의사항! **
>
> 실제 article에 영원히 이 `likes`라는 필드가 계속 붙어있는 것은 아님!
>
> 조회를 하면서 붙여온 것일 뿐!
>
> 이렇게 하면 단순히 조회만 하는 것! 쿼리를 다시 날리지 않음
>
> 중복이었던 SQL이 줄어듬

```html
<!--before-->
    </form>
    {{ article.like_users.all|length }} 명이 이 글을 좋아합니다.
<!--after-->
    </form>
    {{ article.likes }} 명이 이 글을 좋아합니다.
```



#### select_realated

> 각 게시글이 한번 로드될 때 이 게시글의 작성자를 load함
>
> Article이 User를 참조함 (N:1) -> 이게 계속 중복됨
>
> DB에서 쿼리를 좀 줄여서 한번에 가져온다고 생각하면 됨...ㅎ

- `articles` > `vies.py` > `index`

```python
def index(request):
    articles = Article.objects.select_related('user').annotate(likes=Count('like_users')).order_by('-pk')
```

![image-20201001215321072](0928_Django(DB관계_M대N).assets/image-20201001215321072.png)



#### prefetch_related

> M:N관계 때문에 일어나는 것들을 최적화 할 때 사용
>
> 매 게시글마다 like_users를 계속 새로 호출하지 않게 만듦

- `articles` > `views.py` > `index`

```python
def index(request):
    articles = Article.objects.prefetch_related('like_users').select_related('user').annotate(likes=Count('like_users')).order_by('-pk')
```





--------------

## GIT

![image-20200928125050746](0928_Django(DB관계_M대N).assets/image-20200928125050746.png)

![image-20200928125225667](0928_Django(DB관계_M대N).assets/image-20200928125225667.png)

![image-20200928125249043](0928_Django(DB관계_M대N).assets/image-20200928125249043.png)

2. .git 폴더를 삭제한 다음 다시 gitinit을 하면 됨,(프로젝트를 새로 만든 다음에)