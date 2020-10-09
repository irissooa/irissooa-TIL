# README

> 근영이와의 프젝:)
>
> 여태까지 배웠던 1:N까지의 관계를 처음부터 만들었다!!
>
> 그리고 부트스트랩을 이용해 좀 더 이쁘게 꾸며봤당

### 어려웠던 점, 우리가 좀 더 추가해본 것!

> 아직 각자 다른 컴퓨터로 작업해서 하나로 합치는 과정이 어려운 것 같다!
>
> 좀 더 연습이 필요함...ㅎㅎ
>
> 그리고 부트스트랩으로 좀 더 이쁘게 꾸미고 싶었는데 review_detail페이지가 깔끔하게 표현안된것 같아서 아쉽다
>
> 다른 방법을 써봐야될 것 같다
>
> 그리고 LOGOUT만 버튼모양이 달라서 같은 모양으로 맞춰줘도 다른 버튼과 위치가 균일하지 않았다. 더 연구해봐야겠다ㅠㅠ 

> 늘 만들던 기능과는 달리 새롭게  부트스트랩으로 꾸미고 애니메이션도 넣어봤당
>
> 제일 처음 열자마자 보이는 에러가 싫어서 바로 index페이지로 가게 꾸며놨다.
>
> 이미지 넣고 static, media, css를 이용해서 더 이쁘게 꾸미고 싶었지만 아직 잘하지 못해서 검색해가며 했지만 그것도 또다른 재미가 있었다
>
> 그리고 제일 힘들었던 점은 깃을 이용해서 다른 곳에 있는 근영이와 협업하는 것이었는데 자꾸 merge에러가 떠서 pycahe를 지워가며 했다.....이건 좀 더 배우고 익숙해져야 될 것 같다....!

--------

- 프로젝트명을 `pjt05(=pjt06)`를 만들고, `accounts`, `community`앱을 만듦

- `urls.py`

> runserver를 하자마자 바로 보여줄 페이지를 만들기 위해 community앱의 views를 불러와 index페이지로 가게 만듦
>
> `+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)` 이건 static, media를 활용해보려다가...실패....ㅠ

```python
from django.contrib import admin
from django.urls import path,include
from community import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('accounts/',include('accounts.urls')),
    path('community/',include('community.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

- `community` > `views.py`

```python
def index(request):
    return render(request,'community/index.html')
```

- `community` > `index.html`

> 이건 무료 템플릿에서 가져옴
>
> 거기에 추가로 우리롱이 사진을 넣으려고 static을 써봤다
>
> ## Static
>
> - 제일 밖에 `static`폴더를 만든 뒤, 넣고싶은 이미지 파일을 넣음
> - `settings.py`
>
> > 여기서 오류!!!!  `STATICFILES_DIRS`로 적었어야 되는데 `STATIC_DIR`라고 적어서 이미지가 자꾸 뜨지 않았다..ㅠ제대로 찾아보고 적자....!
>
> ```python
> STATIC_URL = '/static/'
> STATICFILES_DIRS = [BASE_DIR/'static']
> ```

```html
{% extends 'base.html' %}
{% load static %}
  {% comment %} <div style = 'background-size : cover; background-repeat:no-repeat; background-image: url({% static 'Love.jpg' %});'> {% endcomment %}


{% block content %}
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css" integrity="sha384-vp86vTRFVJgpjF9jiIGPEEqYqlDwgyBgEF109VFjmqGmIY/Y4HV4d3Gp2irVfcrp" crossorigin="anonymous">
<link href="static/community/vendor/fontawesome-free/css/all.min.css" rel="stylesheet">
{% comment %} <link href="community\static\community\vendor\simple-line-icons\css\simple-line-icons.css" rel="stylesheet" type="text/css"> {% endcomment %}
<link href="https://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">
<link href="static/community/css/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

<link href="community/css/landing-page.min.css" rel="stylesheet">
<br>
<link rel="stylesheet" type="text/css" href="{% static 'community/css/landing-page.css' %}">
<!-- Icons Grid -->
<section class="features-icons bg-light text-center">
  {% comment %} <div class="container"> {% endcomment %}
    <div class="row">
      <div class="col-lg-4">
        <div class="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
          <div class="d-flex align-items-center justify-content-center">
            <a href="{% url 'community:review_list'%}"><i class="fas fa-list-ul fa-5x" style="color:black"></i></a>
          </div><br>
          <h3>Review List</h3>
          <p class="lead mb-0">World's <mark>Best</mark> Reviews</p>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
          <div class="d-flex align-items-center justify-content-center">
            <a href="{% url 'community:create'%}"><i class="fas fa-edit fa-5x" style="color:black"></i></a>
          </div><br>
          <h3>Create New Review</h3>
          <p class="lead mb-0"><mark>Stack</mark> Your Reviews</p>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="features-icons-item mx-auto mb-0 mb-lg-3">
          <div class="d-flex align-items-center justify-content-center">
            <a href="{% url 'accounts:signup'%}"><i class="fas fa-users fa-5x" style="color:black"></i></a>
          </div><br>
          <h3>Sign Up</h3>
          <p class="lead mb-0"><mark>A small step</mark> <br>to Become reviewer</p>
        </div>
      </div>
    </div>
  {% comment %} </div> {% endcomment %}
</section>
<br>
<img src="{% static 'Love2.jpg' %}" class='d-inline-block'>

{% endblock content %}
```



## 1. AUTH_USER_MODEL

- User모델을 커스터마이징 하기 위해 `accounts`앱에 User모델을 만듦

> follow하는 기능을 만들기 위해 만든 필드
>
> 근데 아래의 nickname과 profile_photo는 User의 프로필 페이지를 만들때 nickname과 profile사진을 넣을 수 있게 구현하려고 했지만 실패..다음에 시도해 봐야겠다!

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self',symmetrical=False,related_name='followers')
    # nickname = models.CharField(max_length=64)
    # profile_photo = models.ImageField(blank=True)
```

- `settings.py`

> 이제부터 사용할 User모델위 위치를 적어줌

```python
AUTH_USER_MODEL = 'accounts.User'
```



## 2. Accounts

### (1) Index페이지

> user들의 목록을 보여주는 페이지를 만들어봤다

- `urls.py`

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.index,name='index'),
]
```

- `views.py`

> 유저를 `get_user_model()`로 불러와서 users에 대한 정보를 표시 

```python
from django.contrib.auth import get_user_model

def index(request):
    User = get_user_model()
    users = User.objects.all()[::-1]
    context = {
        'users':users,
    }
    return render(request,'accounts/index.html',context)
```

- `index.html`

```python
{% extends 'base.html' %}
{% block content %}
<h1 class='text-center'>Users</h1>
{% for new_user in users %}
  <a href="{% url 'accounts:profile' new_user.username %}">
  <h3>{{new_user.username}}</h3>
  </a>
  <hr>
{% endfor %}
{% endblock content %}
```



### (2) SignUp

> User모델을 재정의 했으니 django에서 가져오는 UserChangeForm도 다시 커스터마이징 해줘야된다.

- `accounts` > `forms.py`

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
```

- `accounts` > `urls.py`

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
]
```

- `views.py`

```python
from django.views.decorators.http import require_http_methods,require_POST
from .forms import CustomUserCreationForm

@require_http_methods(['GET','POST'])
def signup(request):
    #이미 인증된 사용자 전체리뷰페이지로
    if request.user.is_authenticated:
        return redirect('community:review_list')
    #POST일때 -> user정보를 usercreationform에 저장해서 회원가입!
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #유효성 검사후 맞으면 저장!
            user = form.save()
            #그리고 로그인!
            auth_login(request,user)
            return redirect('community:review_list')
     
    #GET일때는 -> 회원가입폼을 보여줌!
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)
```

- `signup.html`

> form을 이쁘게 보여주기 위해 `bootstrap4`를 가져와 썼다.
>
> `settings.py`의 `INSTALLED_APPS`에 추가함
>
> ```python
> INSTALLED_APPS = [
>     'accounts',
>     'community',
>     'bootstrap4',
> ```

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
  <h1 class='text-center'>SIGNUP</h1>
  <form action="" method='POST'>
    {% csrf_token %}
    {% comment %} {{form.as_p}} {% endcomment %}
    {% bootstrap_form form %}
    <button class = 'btn btn-outline-secondary btn-sm'>SIGNUP</button>
  </form>
  
{% endblock content %}
```



### (2) Login

- `urls.py`

```python
    path('login/',views.login,name='login'),
```

- `views.py`

```python
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

@require_http_methods(['GET','POST'])
def login(request):
    #이미 인증된 사용자 전체리뷰페이지로
    if request.user.is_authenticated:
        return redirect('community:review_list')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'community:review_list')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)
```

- `login.html`

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
  <h1 class='text-center'>LOGIN</h1>
  <form action="" method = 'POST'>
  {% csrf_token %}
  {% comment %} {{form.as_p}} {% endcomment %}
  {% bootstrap_form form %}
  <button class = 'btn btn-outline-secondary btn-sm'>LOGIN</button>
  </form>
  {% endblock content %}
```



### (3) Logout

- `urls.py`

```python
    path('logout/',views.logout,name='logout'),
```

- `views.py`

```python
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:review_list')
```



### (4) Profile

> User의 프로필페이지에 follow도 같이 표현해주고, User가 쓴 review, comment, 좋아요한 review를 표시하는 것을 만듦

- `urls.py`

```python
    path('<user_id>/',views.profile,name='profile'),
    path('<int:user_id>/follow/',views.follow,name='follow'),
```

- `views.py`

> follow는 내가 나를 follow하면 안됨, 그리고 follow돼있다면 follow를 취소하고, 아니라면 추가함

```python
def profile(request,user_id):
    User = get_user_model()
    person = get_object_or_404(User,username=user_id)
    context = {
        'person':person,
    }
    return render(request,'accounts/profile.html',context)

@require_POST
def follow(request,user_id):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(),pk=user_id)
        me = request.user

        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile',you.username)
    return redirect('accounts:login')
```

- `profile.html`

> profile페이지에 User가 쓴

```html
{% extends 'base.html' %}
{% block content %}
<h1 class='text-center'>{{person.username}}'s Profile</h1>
<hr>
{% include 'accounts/_follow.html' %}
<hr>
<h5>{{person.username}}'s REVIEW</h5>
{% for review in person.review_set.all %}
  <div><a href="{% url 'community:review_detail' review.pk %}">{{review.title}}</a></div>
{% endfor %}
<hr>
<h5>{{person.username}}'s Comments</h5>
{% for comment in person.comment_set.all %}
  <div>{{comment.content}}</div>
{% endfor %}
<hr>
<h5>{{person.username}}'s LIKE</h5>
{% for review in person.like_reviews.all %}
  <div><a href="{% url 'community:review_detail' review.pk %}">{{review.title}}</a></div>
{% endfor %}
{% endblock content %}
```

- `_follow.html`

> templates분리!
>
> 용도별로 templates을 분리하면 관리하기 편함
>
> follow버튼을 `font awesome`에서 아이콘을 가져옴

```html
<!-- 팔로워 수 / 팔로잉 수 -->
<div class="jumbotron">
    <!-- 팔로우 버튼 / 언팔로우 버튼 -->
    <!--나를 follow하면 안되니까! 나한테는 이 버튼들이 안보이게 함-->
    {% if request.user != person %}
      <form action="{% url 'accounts:follow' person.pk %}" method="POST" class='d-inline'>
        {% csrf_token %}
        <!--팔로우가 돼있다면 unfollow버튼을 보여주고 아니면 Follow를 보여줌-->
        {% if request.user in perosn.followers.all %}
          {% comment %} <button class="btn btn-secondary">Unfollow</button> {% endcomment %}
          <button class='btn btn-link' style='color:secondary;'>
            <i class="fas fa-user-plus"></i>
          </button>
        {% else %}
          {% comment %} <button class="btn btn-primary">Follow</button> {% endcomment %}
          <button class='btn btn-link' style='color:primary;'>
            <i class="fas fa-user-plus"></i>
          </button>
        {% endif %}
      </form>
    <p class="lead d-inline">
      팔로워 수 : {{ person.followers.all|length }} / 팔로잉 수 : {{ person.followings.all|length }} 
    </p>
    {% endif %}
</div>
```



## 3. Community

### (1) Model

> Review, Comment의 모델을 만들어 db를 저장하게 만듦
>
> 주석처리된 `image`필드는 이미지를 가공해서 써보려고 했지만 시간이 부족해 하지 않았다.

```python
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_reviews')
    # image = ProcessedImageField(
    #     blank=True, 
    #     #사용자가 올린 이미지 가공을 해서 원본그대로가 아니라 썸네일처럼 잘라서 올림
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality':90},
    #     upload_to='%Y/%m/%d',
    # )
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=100)
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like_comment = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_comments')

    def __str__(self):
        return self.content
```



### (2) form

> 새로운 Review, Comment를 적을 폼을 만듦

```python
from django import forms
from .models import Review,Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title','movie_title','rank','content',)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
```



### (3) Review_list

- `urls.py`

```python
	path('reviews/',views.review_list,name='review_list'),
```

- `views.py`

```python
def review_list(request):
    reviews = Review.objects.all()[::-1]
    context ={
        'reviews':reviews,
    }
    return render(request,'community/review_list.html',context)
```

- `review_list.html`

> 여기서 static으로 css를 활용해 봤다
>
> - `community` > `static` > `community`폴더에 `index.css`파일을 만들어 클릭을 한번 하면 빨갛게 되게 만듦
>
> ```css
> /* 가상선택자 종류, 클릭하면 바뀌는 것! visited는 클릭했다는 뜻, 눌렀을때 빨개짐*/
> a:visited {
>   color:crimson;
> }
> ```

```html
{% extends 'base.html' %}
{% load static %}
{% block css %}
  <link rel="stylesheet" href="{% static 'community/index.css' %}">
{% endblock css %}

{% block content %}
<table class="table">
  <thead class="thead-dark">
    <tr>
      <th scope="col">ID</th>
      <th scope="col">TITLE</th>
      <th scope="col">MOVIE</th>
      <th scope="col">LIKE</th>
    </tr>
  </thead>
  <tbody>
    {% for review in reviews %}
    <tr>
      <th scope='row'><a href="{% url 'accounts:profile' review.user.username  %}">{{review.user}}</a></th>
      <td><a href="{% url 'community:review_detail' review.pk %}" class='text-info'>{{review.title}}</a></td>
      <td>{{review.movie_title}}</td>
      <td>
      <form action="{% url 'community:like' review.pk %}" method='POST'>
      {% csrf_token %}
      {% if request.user in review.like.all %}
     <button class='btn btn-link' style='color:crimson;'>
        <i class="fas fa-heart"></i>
      </button>
      {% else %}
       <button class='btn btn-link' style='color:black;'>
        <i class="far fa-heart"></i>
      </button>
      {% endif %}
      </form>
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock content %}
```



### (4) Create

- `urls.py`

```python
    path('reviews/create/',views.create,name='create'),
```

- `views.py`

> review 모델에 있는 user필수 키를 입력하기 위해 form저장을 잠시 미루고(`commit=False`) request.user를 넣고, 다시 저장

```python
from django.shortcuts import render,redirect,get_object_or_404
from .models import Review,Comment
from .forms import ReviewForm,CommentForm
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method =='POST':
        form = ReviewForm(request.POST,files=request.FILES)
        if form.is_valid():
            #user인자에다가 request의 user정보를 담는다
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_detail',review.pk)
    else:
        form = ReviewForm()
    context = {
        'form':form,
    }
    return render(request,'community/form.html',context)

```

- `form.html`

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}

<h1 class='text-center'>CREATE REVIEW</h1>
<form action=""method='POST'>
{% csrf_token %}
{% comment %} {{form.as_p}} {% endcomment %}
{% bootstrap_form form %}
<button class = 'btn btn-outline-secondary btn-sm'>WRITE</button>
</form>
{% endblock content %}
```



### (5) Detail

- `urls.py`

```python
  path('reviews/<int:review_pk>/',views.review_detail,name='review_detail'),
```

- `views.py`

> review정보와 comment를 적을 폼, detail에 표시할 comment들을 역참조로 불러와서 context로 template에 보내줌

```python
def review_detail(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    comments = review.comment_set.all()[::-1]
    comment_form = CommentForm()
    context = {
        'review':review,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'community/review_detail.html',context)


```

- `review_detail.html`

> detail페이지를 이쁘게 꾸미기가 제일 힘들었다... 다시 도전해 봐야겠다!
>
> comment를 달고 추가로 comment도 좋아요를 할 수 있는 기능을 만들었다.

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
<h1 class = 'text-center'>REVIEW</h1>
<hr>
<h3><strong>{{review.title}}</strong></h3>
<p>Movie {{review.movie_title}} Rank {{review.rank}}  Posted by
  <a href="{% url 'accounts:profile' review.user.username %}">{{review.user}}</a></p>
<p>create : {{review.created_at|date:'Y M D'}} / update : {{review.updated_at|date:'Y M D'}}</p>
<br>
<p>{{review.content}}</p>
<hr>
<h5>댓글 목록</h5>
<form action="{% url 'community:comments' review.pk %}"method='POST'>
{% csrf_token %}
{% bootstrap_form comment_form %}
<button class="btn btn-outline-secondary btn-sm">COMMENT</button>
</form>
<hr>
{% for comment in comments %}
  <p class='d-inline'>{{comment.user}} : {{comment.content}}</p>
  <form action="{% url 'community:like_comment' review.pk comment.pk %}" method='POST' class='d-inline'>
    {% csrf_token %}
    {% if request.user in comment.like_comment.all %}
     <button class='btn btn-link' style='color:crimson;'>
        <i class="fas fa-heart"></i>
      </button>
    {% else %}
      <button class='btn btn-link' style='color:black;'>
        <i class="far fa-heart"></i>
      </button>
    {% endif %}
  </form>
  <p class='d-inline'>{{comment.like_comment.all|length}}명이 이 댓글을 좋아합니다.</p>
  <br>
{% endfor %}
{% endblock content %}
```





### (6) Comment

- `urls.py`

```python
 path('reviews/<int:review_pk>/comments/',views.comments,name='comments'),
```

- `views.py`

> comment도 마찬가지로 review와 user필드가 외래키로 지정돼있어서 저장해줌
>
> detail페이지에 폼과 comment들을 표시함

```python
@require_POST
def comments(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
    return redirect('community:review_detail',review.pk)
```





### (7) Like

- `urls.py`

> review를 좋아요하는 기능과 like를 좋아요하는 기능을 만듦

```python
 path('reviews/<int:review_pk>/like/',views.like,name='like'),
    path('reviews/<int:review_pk>/like/<int:comment_pk>',views.like_comment,name='like_comment'),
```

- `views.py`

> review_list 페이지에 like기능 넣음

```python
@require_POST
def like(request,review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review,pk=review_pk)
        if review.like.filter(pk=request.user.pk).exists():
            review.like.remove(request.user)
        else:
            review.like.add(request.user)
        return redirect('community:review_list')
    return redirect('accounts:login')


@require_POST
def like_comment(request,review_pk,comment_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment,pk=comment_pk)
        if comment.like_comment.filter(pk=request.user.pk).exists():
            comment.like_comment.remove(request.user)
        else:
            comment.like_comment.add(request.user)
        return redirect('community:review_detail',review.pk)
    return redirect('accounts:login')
```





## 3. Admin

- `community` > `admin.py`

> Review와 Comment를 관리자 페이지에서 관리하게 만듦

```python
from django.contrib import admin
from .models import Review,Comment
# Register your models here.
admin.site.register(Review)
admin.site.register(Comment)
```

- `accounts` > `admin.py`

> 관리자 페이지에서 User도 관리하게 만들려고 했으나 실패... 시간 더 있을 때 해봐야겠다

```python
from django.contrib import admin
# from .models import User

# # Register your models here.
# class Profileinline(admin.StackedInline):
#     model = User
#     con_delete = False
# admin.site.register(User)
```





## 4. Base.html

> 모든 템플릿에 기본이 되는 base.html
>
> 다양한 시도를 해보려고 했고,
>
> 기본 전체 배경에는 색을 넣었다
>
> 다음에는 더 디자인을 깔끔하게 해봐야겠다

```python
{% load bootstrap4 %}
{% load static %}
<!doctype html>
<html lang="ko">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    {% bootstrap_css %}
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/5dcb1cc34c.js" crossorigin="anonymous"></script>
    {% comment %} <link rel="stylesheet" href="{% static 'base.css' %}">
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}"> {% endcomment %}
    {% block css %}
    {% endblock css %}
    <title>MOVIE COMMUNITY</title>
  </head>
  <body style = 'background-size : cover; background-repeat:no-repeat;' class='bg-light'>

    <nav class="navbar navbar-expand-lg navbar-light"style="background-color: #faedd9;">
      <div class="collapse navbar-collapse d-flex justify-content-between" id="navbarSupportedContent">
      <a class="navbar-brand" href="{% url 'community:index' %}"><i class="fas fa-chess-board fa-spin fa-2x" style = "color:black"></i></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="{% url 'community:review_list' %}"><i class="fas fa-list fa-2x"></i>REVIEWS</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'community:create' %}"><i class="fas fa-pen-nib fa-2x"></i>NEW</a>
          </li>
          {% if user.is_authenticated %}
            <li class="nav-item">
              <form action="{% url 'accounts:logout' %}" method='POST'>
              {% csrf_token %}
              <button class="btn btn-link text-muted text-decoration-none"><i class="fas fa-sign-out-alt fa-2x"></i>LOGOUT</button>
              </form>    
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:index' %}"><i class="fas fa-users fa-2x"></i>USERS</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:profile' request.user.username %}"><i class="fas fa-user-cog fa-2x"></i>MY PAGE</a>
            </li>
          {% else %}
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:signup' %}"><i class="fas fa-plus-circle fa-2x"></i>SIGNUP</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:login' %}"><i class="fas fa-sign-in-alt fa-2x"></i>LOGIN</a>
            </li>          
          {% endif %}
        </ul>
      </div>
    </nav>
    {% comment %} <div class="container"> {% endcomment %}
    {% block content %}
    {% endblock content %}
    {% comment %} </div> {% endcomment %}
 
 
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {% bootstrap_javascript jquery='full' %}
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </div>
  <br>
  <footer>
    <div class = container>
        <p class="font-weight-lighter font-italic text-center">Created by ⓒ Sooa | geun0 </p>
        <p class="font-weight-lighter font-italic text-center">2020 / 10 / 08</p>
      </div>
    </div>
  </footer>
  <br>
</html>
```

