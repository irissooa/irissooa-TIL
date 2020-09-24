# Django

> Model_Relationship

## Model Relationship

- 모델 간 관계를 나타내는 필드
- Many to one(1:N)
  - `ForeignKey()` 외래키
- Many to Many(M:N)
  - `ManyToManyField()`
- One to One(1:1)
  - `OneToOneField()`



### A many-to-one relationship in RDBMS

> 관계형 데이터베이스 관리 시스템
>
> 댓글 구현! 1(article):N(comments)
>
> 1은 참조 되는 테이블, N은 참조하는 테이블
>
> 외래키는 참조무결성 원칙! 따름 : 반드시 유일한 값을 골라야됨! 그래서 확실한 유일한 값인 부모 테이블의 id로 외래키를 지정함

- Foreign Key(외래키)
- 외래키는 참조하는 테이블에서 1개의 키(속성 또는 속성의 집단)에 해당하고 참조하는 측의 관계 변수는 참조되는 측의 테이블의 키를 가리킴
- 참조하는 테이블의 속성의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응
- 하나의 테이블이 여러 개의 외래 키를 포함할 수 있음
- 이러한 외래 키들은 각각 서로 다른 테이블을 참조 할 수 있음
- 참조하는 테이블과 참조되는 테이블이 동일할 수 있음(재귀적 외래 키)
  - 자기자신을 참조하는것! ex) 대댓글! 



#### Foreign Key

> django에서 A many-to-one relationship을 표현하기 위한 클래스
>
> 2개의 위치인자 필요
>
> 1. 참조하는 모델
> 2. on_delete 옵션
>    - 외래키가 참조하고 있는 부모객체가 삭제되었을 때 연결된 N의 애들을 어떻게 처리할거냐?
>    - 만약 게시글이 삭제되고 댓글이 8개가 달렸다면 그 8개의 댓글은 어떻게 처리할거냐? 
>
> 댓글은 articles의 models.py에 만들자!

- `articles` > `models.py`

  > Article class가 1, Comment class가 N
  >
  > 클래스변수인 외래키는 참조하는 테이블 이름의 소문자 단수형으로 작성!
  >
  > 나중에 관리하기 편하기 위해!
  >
  > =>외래키 필드이름:`클래스이름(외래키로 지정한 변수 이름)_id`이기 때문에 참조하는 테이블 이름의 소문자 단수형으로 작성!

```python
class Comment(models.Model):
    #article(외래키) 필수 인자: 참조하는 클래스,on_delete옵션!
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```

- 모델을 추가하면, `migrate`를 다시 해줘야됨!

- migration한 뒤, 테이블(`앱이름_모델이름`)에서 보면 외래키(필드이름:`클래스이름(외래키로 지정한 변수 이름)_id`)는 가장 아래(우측)에 기록되기 때문에 어디에 적든 순서 상관 없음!

  



##### ForeignKey's Arguments on_delete

- **CASCADE**
  - 보통 이거 적음
  - **부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제**
- PROTECT
  - 참조가 되어 있는 경우 오류 발생
- SET_NULL
  - 부모 객체가 삭제 됐을 때 모든 값을 NULL로 치환(NOT NULL 조건 시 불가능)
- SET()
  - 특정 함수 호출
- DO_NOTHING
  - 아무것도 하지 않음
  - 다만, 데이터베이스 필드에 대한 SQL ON DELETE제한 조건을 설정
- RESTRICT(new in 3.1)
  - RestrictedError를 발생시켜 참조된 객체의 삭제를 방지



## DB 댓글 쓰기

```sh
$pip install ipython
$python manage.py shell_plus
```

- 

```sh
In[1] : comment = Comment() #comment라는 이름의 인스턴스 만들기
IN[2] : comment.content = 'first comment'
IN[3] : comment.content
Out[3]: 'first comment'
IN[4] : comment.save() #이렇게 쓰면 에러 뜸!!!!! 데이터 베이스에 Null이 들어가려고 하기 때문 
```

- `IntegrityError: NOT NULL constraint failed: articles_comment.article_id` 이 에러가 뜸

```sh
IN[5]: article = Article.objects.get(pk=1)
In[6] : article
Out[6] : <Article:첫번째 제목>
In[7] : comment
Out[7] : <Comment: first comment>
In[8]: comment.content
Out[8] : 'first comment'
In[9]: comment.article = article #객체(article.pk를 안넣어도 알아서 id값을 저장함)
In[10]: comment.save()
In[11]: comment
Out[11]: <Comment:first comment>
In[12] : comment.pk
Out[12] : 1
In[13]: comment.article
Out[13]: <Article:첫번째 제목>
In[14]: comment.article.pk
Out[14]:1
In[15]:comment.article_id
Out[15]:1
In[16] :comment.article_pk #이런건 없다고 뜸!(주의!)
In[17] : commet.article.title
Out[17]: '첫번째 제목'
```

![image-20200921141438963](0921_Django_Model_Relationship,SQL(ORM).assets/image-20200921141438963.png)

- 두번째 댓글

```sh
In[18]:comment = Comment(content='second comment',article=article)
In[19]: comment
Out[19]: <Comment:second comment>
In[20]: comment.save()
In[21] : comment.pk
Out[21]:2
In[22] : exit()#shell_plus 종료
```

- `admin`관리자 등록

```sh
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'sooa'): admin  
이메일 주소:  
Password: 
Password (again):
비밀번호가 사용자 이름와 너무 유사합니다.
비밀번호가 너무 일상적인 단어입니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

- `admin`페이지에 보이게 하기 위해 아래와 같이 설정해야됨!

- `articles` > `admin.py`

```python
from django.contrib import admin
from .models import Article,Comment # 명시적 상대경로 표현

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
```







#### 1번 게시글에 달린 모든 댓글을 어떻게 조회하냐?

> `foreign key`는 N(comment)에 저장돼있음
>
> 물리적으로 DB테이블에 Article에는 어떤 변화도 없음!
>
> 그러면 article은 어떻게 자기 아래에 달린 댓글을 알수있을까? 
>
> 역참조!(참조되는애가 참조하는 애를 참조하는 것!) - >명령어 manager`자식_set`
>
> `comment.article`는 comment가 article을 참조할떄!
>
> `article.comment_set` 로 역참조 article이 comment를 참조

```sh
#외래키를 가지지 않은 참조되는 대상이 자신을 참조하는 대상을 참조하는 역참조!!!
In[1] : article = Article.objects.get(pk=1)
In[2] : article.pk
Out[2] : 1
In[3] : article.comment_set.all()#쿼리셋으로 나옴
Out[3]: QuerySet <[<Comment:first comment>,<Comment:second comment>]> #list처럼 사용 가능
In[4]: comments=article.comment_set.all()
In[5]: comments
Out[5]:QuerySet <[<Comment:first comment>,<Comment:second comment>]>
In[6]: comments.first()
Out[6]:<Comment:first comment>
In[7]: comments.first().content
Out[7]:'first comment'
In[8]: comments[0].content
Out[8]:'first comment'
```





## 1:N  model manager

- Comment가 Article을 참조
  - **article**
- Article이 Comment을 참조(역참조)
  - **comment_set**
  - django에서는 역참조시 `소문자모델이름_set`형식의 manager를 만든다



## related_name

> 외래키 3번쨰 인자 related_name='comments'역참조시 원하는 이름으로 바꿀 수 있음 이렇게 하면 comment_set 명령어는 더이상 못씀
>
> `models.py`

`article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='comments')`







------------------

## 댓글 CRUD

- `articles` > `forms.py`

> 모델폼을 만들거에욤

```python
from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'

#detial페이지에서 보여져야됨->detail view에 적힘
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        #제외할 것을 적어줘도됨, 이건 foreign key이기 때문에 안보여지게 할거야
        exclude = ['article']
```



- `articles` > `views.py`

  > `forms.py`에 추가된 form을 detail view함수에 추가
  >
  > 이제 폼이름 여러개니까 구분지어줌 comment_form

```python
from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form':comment_form,
    }
    return render(request, 'articles/detail.html', context)
```



#### create

- `articles` > `urls.py`

```python
 path('<int:pk>/comments/',views.comments_create,name='comments_create'),
```



- `articles` > `views.py`

>  기본값은 true인데 `comment_form.save(commit=False)`이거는 commit을 하지 않음 save는 하긴 할건데 아직 db에 작성하지말고 인스턴스만 만들어주되 저장은 좀만 기다려달라
>
> 그러면 db에 저장이 안됐기 때문에 인스턴스에 값을 추가로 넣을 수 있음        

```python
@require_POST
def comments_create(request,pk):
     #댓글작성은 detail 페이지에서 보여짐
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # Create, but don't save the new comment instance.
        comment = comment_form.save(commit=False)
        comment.article = article
        #넣을 거 다 넣었으니 이제 save, data를 받을 떄 내용+외래키를 받아와야되기 때문에 잠시 시간을 준거임
        comment.save()
        return redirect('articles:detail',article.pk)
    context = {
        'comment_form':comment_form,
    }
    #에러메세지를 담고 detail페이지로 넘어감
    return render(request,'articles/detail.html',context)
```



- detail.html

```html
<h4>댓글작성</h4>
  <form action="{% url 'articles:comments_create' article.pk %}" mehtod='POST'>
  {% csrf_token %}
  {{comment_form}}
  <input type="submit">
  </form>
```



- 여기서 댓글에 공백을 넣고 제출했더니! `NoReverseMatch`가 뜸 

> 이건 해당 page에서 url태그만 보면 됨!!!
>
> detail 은 article이 필요한데, article이 뷰함수에 존재하지 않아서 그럼! article을 추가해줌

```python
@require_POST
def comments_create(request,pk):
     #댓글작성은 detail 페이지에서 보여짐
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        #기본값은 true인데 comment_form.save(commit=False)이거는 commit을 하지 않음 save는 하긴 할건데 아직 db에 작성하지말고 인스턴스만 만들어주되 저장은 좀만 기다려달라
        comment = comment_form.save(commit=False)
        #그러면 db에 저장이 안됐기 때문에 인스턴스에 값을 추가로 넣을 수 있음
        comment.article = article
        #넣을 거 다 넣었으니 이제 save, data를 받을 떄 내용+외래키를 받아와야되기 때문에 잠시 시간을 준거임
        comment.save()
        return redirect('articles:detail',article.pk)
    context = {
        'comment_form':comment_form,
        'article':article,
    }
    #에러메세지를 담고 detail페이지로 넘어감
    return render(request,'articles/detail.html',context)
```



#### read

> 댓글 조회

- detail에서 출력돼야함 -> `detail`의 뷰함수에 추가

> 역참조 일어남, pk게시글이 가진 모든 댓글 가져옴
>     `comments = article.commet_set.all()`

```python
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    #역참조 일어남, pk게시글이 가진 모든 댓글 가져옴
    comments = article.commet_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)
```

- detail.html

```python
  <h4>댓글 목록</h4>
  {% for comment in comments %}
  <ul>
    <li>{{comment.content}}</li>
  </ul>
  {% endfor %}
  <hr>
  <h4>댓글작성</h4>
  <form action="{% url 'articles:comments_create' article.pk %}" mehtod='POST'>
  {% csrf_token %}
  {{comment_form}}
  <input type="submit">
  </form>
{% endblock  %}

```



#### Update

> 이건 javascript배워야 할 수 있음-> 건너뛴다





#### Delete

- `urls.py`

```python
path('<int:article_pk>/comments/<int:comment_pk>/delete/',views.comments_delete,name='comments_delete'),
```

- `views.py`

```python
from .models import Article,Comment

@require_POST
def comments_delete(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    #인자로 받은 article_pk를 가져옴
    #만약 article=comment.article로 받아온다면-> article.pk로 받아도되지만 최적화....를 위해...인자로 받아라??
    return redirect('articles:detail',article_pk)
```

- length가 보통 최적화..얼마나 db에 적게 보내냐?
- detail.html

```html
<ul>
    <li>{{comment.content}}</li>
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method='POST' class='d-inline'>
    {% csrf_token %}
    <input type="submit" value='DELETE'>
    </form>
  </ul>
```



- 필터

> `  {{comments.count}} 개`와 ` {{comments|length}}`는 같은 뜻이지만 나중에 최적화를 할때 length가 보통 더 좋다!

```html
<h4>댓글 목록</h4>
  {% if comments|length %}
    {{comments|length}} 개의 댓글이 있습니다.
  {% endif %}

  {% for comment in comments %}
  <ul>
    <li>{{comment.content}}</li>
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method='POST' class='d-inline'>
    {% csrf_token %}
    <input type="submit" value='DELETE'>
    </form>
  </ul>
    {%empty%}
    <p>댓글이 아직 없어요.</p>
  {% endfor %}
  
```





## get_object_or_404

> `get_list_or_404()`이건 `all()`대신 사용! 자주쓰진 않음..그냥알아두기

- 주어진 model manager에서 .`.get()`을 호출하지만 모델의`DoesNotExist`예외 대신 `HTTP404`를 발생시킴
- 예를 들어 해당 객체가 있다면 `objects.get(pk=pk)`을 실행하고 없으면 `ObjectDoesNotExist`예외가 아닌 `Http404(HttpResponseNotFound)`를 raise함
- 클라이언트에게 정확한 에러로 처리해주기 위해 사용

```python
from django.shortcuts import render, redirect,get_object_or_404

def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,pk=pk)
    
@require_POST
def comments_delete(request,article_pk,comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)
    
#아래와 같이 필터도 적용 가능
@require_POST
def comments_create(request,pk):
     #댓글작성은 detail 페이지에서 보여짐
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,title__startswith='A',pk=1)
```

- `article = Article.objects.get(pk=pk)`와 `article = get_object_or_404(Article,pk=pk)`는 같지만 앞으로 없는 글 조회를 할 때 에러 페이지가 500에러가 아니라 404에러가 뜸!(Page not found)가 떠서 사용자가 알기 쉽게 해줌
- 꼭 할필요는 없지만 사용자에게 친화적인 홈페이지를 만들기 위해 사용!!!

- `shortcut`이 없으면 `try, except`를 이용해서  아래와 같이 길게 써야되지만 짧게 쓸 수 있게 해줌!

![image-20200921155127804](0921_Django_Model_Relationship,SQL(ORM).assets/image-20200921155127804.png)







---------------

## 댓글 CRUD

- `articles` > `models.py`

```python
from django.db import models

# Create your models here.
class Article(models.Model): # 상속
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    #article(외래키) 필수 인자: 참조하는 클래스,on_delete옵션!,  related_name='comments'역참조시 원하는 이름으로 바꿀 수 있음 이렇게 하면 comment_set 명령어는 더이상 못씀
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```

- `articles`>`forms.py`

```python
from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'

#detial페이지에서 보여져야됨->detail view에 적힘
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        #제외할 것을 적어줘도됨, 이건 foreign key이기 때문에 안보여지게 할거야
        exclude = ['article']
```

- `articles` > `urls.py`

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
    path('<int:pk>/comments/',views.comments_create,name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/',views.comments_delete,name='comments_delete'),
]
```

- `articles`> `views.py`

```python
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article,Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

#이제 폼이름 여러개니까 구분지어줌 comment_form
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,pk=pk)
    comment_form = CommentForm()
    #역참조 일어남, pk게시글이 가진 모든 댓글 가져옴
    comments = article.commet_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,pk=pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        # article = Article.objects.get(pk=pk)
        article = get_object_or_404(Article,pk=pk)
    
        article.delete()
    return redirect('articles:index')


@require_POST
def comments_create(request,pk):
     #댓글작성은 detail 페이지에서 보여짐
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,title__startswith='A',pk=1)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        #기본값은 true인데 comment_form.save(commit=False)이거는 commit을 하지 않음 save는 하긴 할건데 아직 db에 작성하지말고 인스턴스만 만들어주되 저장은 좀만 기다려달라
        comment = comment_form.save(commit=False)
        #그러면 db에 저장이 안됐기 때문에 인스턴스에 값을 추가로 넣을 수 있음
        comment.article = article
        #넣을 거 다 넣었으니 이제 save, data를 받을 떄 내용+외래키를 받아와야되기 때문에 잠시 시간을 준거임
        comment.save()
        return redirect('articles:detail',article.pk)
    context = {
        'comment_form':comment_form,
        'article':article,
    }
    #에러메세지를 담고 detail페이지로 넘어감
    return render(request,'articles/detail.html',context)


@require_POST
def comments_delete(request,article_pk,comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    #인자로 받은 article_pk를 가져옴
    #만약 article=comment.article로 받아온다면-> article.pk로 받아도되지만 최적화....를 위해...인자로 받아라??
    return redirect('articles:detail',article_pk)
```



- `detail.html`

```html
{% extends 'base.html' %}

{% block content %}
  <h2 class="text-center">DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
  <hr>
  <h4>댓글 목록</h4>
  {% if comments|length %}
    {{comments|length}} 개의 댓글이 있습니다.
  {% endif %}
  {{comments.count}} 개
  {% for comment in comments %}
  <ul>
    <li>{{comment.content}}</li>
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method='POST' class='d-inline'>
    {% csrf_token %}
    <input type="submit" value='DELETE'>
    </form>
  </ul>
    {%empty%}
    <p>댓글이 아직 없어요.</p>
  {% endfor %}
  <hr>
  <h4>댓글작성</h4>
  <form action="{% url 'articles:comments_create' article.pk %}" mehtod='POST'>
  {% csrf_token %}
  {{comment_form}}
  <input type="submit">
  </form>
{% endblock  %}

```

