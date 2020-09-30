# Django M:N관계

> 지난 시간
>
> A many to one relationship
>
> User-Article/ User-Comment
>
> User 대체 -> Custom user model
>
> 대체 후 회원가입 이뤄지지 않음, 대체한 후 회원가입 진행 안됨-> 회원가입에 대한 useer creationform이 기본적으로 장고가 user를 대체하기 전인 기본 user model로 만들어진 모델폼이기 떄문
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

![image-20200928093941422](0928_Django(DB관계_N대M).assets/image-20200928093941422.png)

> 한계 : 환자가 다른 의사한테 또 진료를 받고 싶다면 필드를 한번 더 사용해야되고, harry라는 환자가 두명의 의사한테 동시에 진료를 받을 수 없었음!
>
> 그래서 중개모델을 작성!



![image-20200928094442508](0928_Django(DB관계_N대M).assets/image-20200928094442508.png)

> 각각의 모델과 1:N의 관계를 맺음, 지금 1번의사한테 두명의 환자가 예약되어있는 것을 보여줌 
>
> 데이터를 조회할 때 아래와 같이 shell_plus에 입력했음
>
> ![image-20200930185919266](0928_Django(DB관계_N대M).assets/image-20200930185919266.png)



![image-20200928094500784](0928_Django(DB관계_N대M).assets/image-20200928094500784.png)

> 의사가 환자들을 조회를 하고 싶다!
>
> 환자도 내가 진료를 받을 의사들을 조회하고 싶다!
>
> 여기서 ManyToManyField가 등장
>
> 두 모델간 종속관계가 없어 둘중 어느 모델에 써도 관계 없음! Doctor에 적어도 상관없음
>
> ![image-20200928094531785](0928_Django(DB관계_N대M).assets/image-20200928094531785.png)
>
> 참조되는 모델의 복수형으로 적으면 됨!
>
> 조회할때의 명령어는 이렇게 씀!
>
> ![image-20200930190154615](0928_Django(DB관계_N대M).assets/image-20200930190154615.png)
>
> 1번환자를 조회하고
>
> 1번환자의 모든 예약을 역참조로 불러옴
>
> 내가 오늘 진료를 받을 의사만 보여줌! Patient가 바로 의사를 참조하는 것처럼 보이게 함 
>
> ![image-20200928094722487](0928_Django(DB관계_N대M).assets/image-20200928094722487.png)
>
> 하지만 여전히 Doctor는 Reservation을 통해서만 Patient를 참조할 수 있음!
>
> ManyToManyField는 종속관계는 없지만 역참조를 하면 Doctor도 patient를 참조할 수 있음!
>
> ![image-20200928094732248](0928_Django(DB관계_N대M).assets/image-20200928094732248.png)
>
> `related_name=`역참조시 사용하는 `manager`를 변경함
>
> ![image-20200930191025532](0928_Django(DB관계_N대M).assets/image-20200930191025532.png)
>
> `related_name`을 설정하고 나면 이전에 사용했던 명령어 `patient_set`은 쓸 수 없음!





![image-20200928095013372](0928_Django(DB관계_N대M).assets/image-20200928095013372.png)

>![image-20200930191833211](0928_Django(DB관계_N대M).assets/image-20200930191833211.png)





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
> ![image-20200930230608193](0928_Django(DB관계_N대M).assets/image-20200930230608193.png)
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
> ![image-20200930235216291](0928_Django(DB관계_N대M).assets/image-20200930235216291.png)

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

    <--FontAwesome을사용할수있게추가해줌-->
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
> `{{ article.likes }} ` 개수를 구할 때 `|length` or `.count()`를 적으면 개수를 구할 수 있다

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

<--아래 구문 추가-->
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
<--여기까지-->
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}
```









--------------

## GIT

![image-20200928125050746](0928_Django(DB관계_N대M).assets/image-20200928125050746.png)

![image-20200928125225667](0928_Django(DB관계_N대M).assets/image-20200928125225667.png)

![image-20200928125249043](0928_Django(DB관계_N대M).assets/image-20200928125249043.png)

2. .git 폴더를 삭제한 다음 다시 gitinit을 하면 됨,(프로젝트를 새로 만든 다음에)