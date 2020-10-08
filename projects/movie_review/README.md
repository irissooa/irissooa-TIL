# README

> 근영이와의 프젝:)
>
> 여태까지 배웠던 1:N까지의 관계를 처음부터 만들었다!!
>
> 그리고 부트스트랩을 이용해 좀 더 이쁘게 꾸며봤당

- 프로젝트명을 `pjt05`를 만들고, `accounts`, `community`앱을 만듦
- `pjt05` > `urls.py`

> 명세와는 다르게 추가로 runsever를 하자마자 review의 전체 페이지를 보이게 만들었다.

```python
from django.contrib import admin
from django.urls import path,include
from community import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.review_list),
    path('accounts/',include('accounts.urls')),
    path('community/',include('community.urls')),
]
```

- `base.html`

> `bootstrap4`를 이용해 form을 보기 좋게 하기위해 추가로 설치했다.

```html
{% load bootstrap4 %}
<!doctype html>
<html lang="ko">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    {% bootstrap_css %}
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

    <title>MOVIE COMMUNITY</title>
  </head>
  <body>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">MOVIE_REVIEW</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="{% url 'community:review_list' %}">REVIEW</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'community:create' %}">NEW</a>
          </li>
          {% if user.is_authenticated %}
            <li class="nav-item">
              <form action="{% url 'accounts:logout' %}" method='POST'>
              {% csrf_token %}
              <button class="btn btn-link text-muted text-decoration-none">LOGOUT</button>
              </form>
            </li>
          {% else %}
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:signup' %}">SIGNUP</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:login' %}">LOGIN</a>
            </li>          
          {% endif %}
        </ul>
      </div>
    </nav>
    {% block content %}
    {% endblock content %}
  </div>
 
 
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {% bootstrap_javascript jquery='full' %}
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </body>
</html>
```



- `accounts` > `urls.py`

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]

```

- `accounts` > `forms.py`

> 명세에 나온대로 UserCreationForm을 이용해서 CustomCreationForm을 만듦!

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
```



- `accounts` > `views.py`

```python
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.

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


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:review_list')
```

- `accounts` > `signup.html`

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

- `accounts` > `login.html`

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

- `community` > `models.py`

```python
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)



class Comment(models.Model):
    content = models.CharField(max_length=100)
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
```

- `community` > `admin.py`

> Review, Comment는 관리자 페이지에서 데이터의 생성, 조회, 수정, 삭제 가능하게 만듦

```python
from django.contrib import admin
from .models import Review,Comment
# Register your models here.
admin.site.register(Review)
admin.site.register(Comment)
```



- `community` > `forms.py`

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

- `community` > `urls.py`

```python
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('',views.review_list,name='review_list'),
    path('create/',views.create,name='create'),
    path('<int:review_pk>/',views.review_detail,name='review_detail'),
    path('<int:review_pk>/comments/',views.comments,name='comments'),
]
```

- `community` > `views.py`

```python
from django.shortcuts import render,redirect,get_object_or_404
from .models import Review,Comment
from .forms import ReviewForm,CommentForm
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()[::-1]
    context ={
        'reviews':reviews,
    }
    return render(request,'community/review_list.html',context)


@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method =='POST':
        form = ReviewForm(request.POST)
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

- `community` > `review_list.html`

```html
{% extends 'base.html' %}
{% block content %}
<table class="table">
  <thead class="thead-dark">
    <tr>
      <th scope="col">ID</th>
      <th scope="col">TITLE</th>
      <th scope="col">MOVIE</th>
      {% comment %} <th scope="col">내용</th> {% endcomment %}
    </tr>
  </thead>
  <tbody>
    {% for review in reviews %}
    <tr>
      <th scope='row'>{{review.user}}</th>
      <td><a href="{% url 'community:review_detail' review.pk %}" class='text-info'>{{review.title}}</a></td>
      <td>{{review.movie_title}}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock content %}
```

- `community` > `form.html`

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

- `community` > `review_detail.html`

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
<h1 class = 'text-center'>REVIEW</h1>
<hr>

<h3>{{review.title}}</h3>
<br>
<p>영화제목 : {{review.movie_title}}</p>
<p>내용 : {{review.content}}</p>
<p>RANK : {{review.rank}}</p>
<p>작성일 : {{review.created_at}}</p>
<p>수정일 : {{review.updated_at}}</p>
<hr>
<form action="{% url 'community:comments' review.pk %}"method='POST'>
{% csrf_token %}
{% comment %} {{comment_form.as_p}} {% endcomment %}
{% bootstrap_form comment_form %}
<button type="button" class="btn btn-outline-secondary btn-sm">COMMENT</button>
</form>
<hr>
<h5>COMMENT</h5>
{% for comment in comments %}
  <p>작성자 : {{comment.user}}</p>
  <p>댓글 : {{comment.content}}</p>
{% endfor %}
{% endblock content %}
```



### 어려웠던 점

> 아직 각자 다른 컴퓨터로 작업해서 하나로 합치는 과정이 어려운 것 같다!
>
> 좀 더 연습이 필요함...ㅎㅎ
>
> 그리고 부트스트랩으로 좀 더 이쁘게 꾸미고 싶었는데 review_detail페이지가 깔끔하게 표현안된것 같아서 아쉽다
>
> 다른 방법을 써봐야될 것 같다
>
> 그리고 LOGOUT만 버튼모양이 달라서 같은 모양으로 맞춰줘도 다른 버튼과 위치가 균일하지 않았다. 더 연구해봐야겠다ㅠㅠ 

