# Django

> DB 데이터베이스 관계(1:N)
>
> [출처_이분대단행...](https://github.com/wally-wally/TIL/blob/master/04_django/%5BSSAFY%5Ddjango_%234.md)

## User

> Subsituting a custom User model(커스텀 유저 모델로 대체하기)

- 일부 프로젝트에서는 Django의 내장 유저 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있다
- 유저 지정 모델을 참조하는 AUTH_USER_MODEL(`settings.py`) 설정 값을 변경해 기본 유저 모델을 재정의(override) 할 수있음
- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도 커스텀 유저 모델을 설정하는 것을 강력하게 권장(**그냥 커스텀유저모델을 사용해라**)
- 커스텀 유저 모델은 기본 유저 모델과 동일하게 동작하지만 필요한 경우 나중에 맞춤 설정할 수 있기 때문
- **(중요!!!!!) 단, 프로젝트의 첫 migrate를 실행하기 전에 완료해야함**



### AUTH_USER_MODEL

> [settings.py_AUTH_USER_MODEL](https://docs.djangoproject.com/en/3.1/ref/settings/)

- User를 나타내는데 사용하는 모델
- 기본값은 'auth.User'
- 주의사항
  - 프로젝트가 진행되는 동안 AUTH_USER_MODEL 값을 변경할 수 없음(종속된 모델을 만들고 마이그레이션 된 후/ 변경하기 위해서는 많은 시간과 절차가 필요)
  - **프로젝트 시작 시 설정**하기 위한 것이고 custom User로 대체하는 법을 [참고(Substituting a custom User model)](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/)해서 설정



### AbstractBaseUser & AbstractUser

- AbstractBaseUser
  - password와 last_login만 기본적으로 제공
  - 자유도가 높지만 다른 필요한 필드는 모두 작성해야 함
- AbstractUser
  - 관리자 권한과 함께 완전한 기능을 갖춘 유저 모델을 구현하는 기본 클래스
  - 여기서 상속받은 User를 사용하고 있었음!(실제로 모든 일을 다함, User는 유저를 표현하기 위한 것일 뿐!)







### Custom users and the built_in auth forms

- AbstractBaseUser의 모든 subclass와 호환되는 forms
  - AuthenticationForm, SetpasswordForm, PasswordChangeForm, AdminpasswordChangeForm
- User와 연결되어 있어 커스텀 유저모델을 사용하려면 다시 작성하거나 확장해야하는 forms(**다시 커스텀유저모델로 작성할거야!**)
  - UserCreationForm
  - UserChangeForm



### Referencing the User model(유저 모델 참조하기)

- settings.AUTH_USER_MODEL(문자열로됨)

  - 유저 모델에 대한 외래 키 또는 다 대 다 관계를 정의 할 때 사용

  - **즉, models.py에서 유저 모델을 참조할 때 사용**
  - `accounts`에 User모델이 있는데 articles가 끝난다음에 accounts가 실행되기 때문에 오류가 뜰 수 있음, 그래서 모델에서는 객체가 등장하는게 아니라 문자열로 됨 AUTH_USER_MODEL을 써야됨

- get_user_model()

  - django는 유저 모델을 직접 참조하는 대신 get_user_model()을 사용하여 유저 모델을 참조하라고 권장
  - 현재 활성(active) 유저 모델(지정된 커스텀 유저 모델, 그렇지 않은 User)을 반환
  - **즉, models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용**



### User - Article 관계(1 : N 관계)

1. `settings.AUTH_USER_MODEL`

> `앱이름.모델이름`-> 장고가 auth모델을 쓰는것이 아니라 대체를 함!
>
> 중간에 바꿀 수 없음, 그렇기 때문에 데이터베이스를 초기화 해야됨 migrations를 다 지우고 db도 다 지움!
>
> 마이그레이션 초기화할때 `__init__`을 지우면안되고 숫자로 돼있는거만 지우고, dbsqlite3파일도 지움!

- `articles` > `models.py`
  - `settings.py`에 `AUTH_USER_MODEL`에 대해 나와 있지 않음
  - `AUTH_USER_MODEL = 'auth.User'`가 기본값이기 때문이다.
  - 여기는 `get_user_model`을 참고하지 못하고 `AUTH_USER_MODEL`을 적어야됨, user_id를 defalut를 1로 설정할 수도 있음 

```python
from django.conf import settings

# Article 클래스에 추가
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

- `forms.py` > `ArticleForm`

```python
fields = ('title', 'content',) # 구문 수정
```

- `get_user_model()` : return 값이 `class`
- `settings.AUTH_USER_MODEL` : return 값이 `str`



>  **django가 서버가 켜질 때 초기화 순서로 보는 `models.py`에서 `get_user_model()`을 사용하지 못하는 이유?????**

① `INSTALLED_APPS`의 각 항목을 imports 한다. (단, 순서는 **`위에서 아래로`**)

- 이 과정에서 직접적, 간접적으로 모델을 import 해선 안 된다.
- ①번 단계에서 app을 import 하는 동안에 불필요한 제약들을 피하기 위해 이 단계에서는 모델을 가져오지 않는다.

② 각 어플리케이션의 `models.py`를 import 한다.

- **②번 단계가 완료가 되면**, `get_model()`과 같은 모델에서 작동하는 API들을 사용할 수 있게 된다.
- 그러므로 `models.py`에서 외래키 추가할 때 `get_user_model()`을 사용하지 못한다.

③ `AppConfig`의 ready() 메서드를 실행한다.

- **②번 단계가 완료된 후에야 `get_user_model()`을 사용할 수 있는데 아직 `accounts` app이 `INSTALLED_APP`의 작성 순서 때문에 아직 import가 되지 완료되지 않은 상황이라 `get_user_model()`이 어떤 `User` model을 return해야 하는지 django가 알 수 없는 상태이다.**



> (중요!!)
>
> **모든 곳**에서 User model을 호출할 때는 **`get_user_model()`**
>
> 단, **`models.py`**에서만 **`settings.AUTH_USER_MODEL`**



- DB는 기본으로 `NOT NULL` 조건을 지켜야 하므로 새로운 컬럼 추가시 현재 이미 만들어져 있는 레코드에 대해 `user_id`의 기본값을 어떻게 설정할지 물어보는 구문이 다음과 같이 표시된다.
  - 아래와 같은 상황은 `user_id`를 `1`로 선택한 예시화면이다.

[![model](0923_Django(DB관계_1대N,User_model).assets/67252556-7111f580-f4ae-11e9-9c8d-ac9586a3fd39.JPG)](https://user-images.githubusercontent.com/52685250/67252556-7111f580-f4ae-11e9-9c8d-ac9586a3fd39.JPG)



2.  Create Logic 수정

- 글의 작성자가 누구인지를 알기 위해 설정
  - `views.py` > `create` view (구문 수정)

```python
article = form.save(commit=False)
article.user = request.user
article.save()
```



3. Update, Delete Logic 수정

- 자신의 게시글이 아니면 UPDATE, DELETE를 하지 못하도록 설정
- `detail.html` (구문 수정)

> requst없이 사용할수 있지만 명확하게 하기 위해서 써주는 편! 

```html
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  {% endif %}
```

- `views.py` > `update` view

> 수정하는 유저와,게시글 작성 유저가 같은지 확인

```python
@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user: # 큰 if ~ else문 추가
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
                article = form.save()
                return redirect(article)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form, 
        'article': article,
    }
    return render(request, 'articles/form.html', context)
```

- `views.py` > `delete` view

```python
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user: # 이 구문 추가
            article.delete()
        else:
            return redirect(article)
    return redirect('articles:index')
```



### User - Comment(1 : N 관계)

- `articles` > `models.py` > `Comment` Class

```python
# 구문 추가
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```



1. comments_create logic 수정
   - `views.py` > `comments_create` view

```python
comment.user = request.user # 구문 추가
```



2. 비로그인 유저 댓글 작성 form 숨기기

```html
detail.html
{% if user.is_authenticated %}
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit" value="submit">
  </form>
  <hr>
{% else %}
  <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요]</a>
  <hr>
{% endif %}
```



3. 내가 작성한 게시글에서만 DELETE 보이기

- detail.html

```html
{% if request.user == comment.user %}
  <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" style="display: inline;">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
{% endif %}
```

- `views.py` > `comments_delete` view

```python
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user: # 이 조건 추가됨
            comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)
```



### 프로필 이미지 기능 추가(gravatar 프로필 이미지)

#### 1. ModelForm Custom

> ```
> accounts` > `forms.py
> from django.contrib.auth.forms import UserCreationForm
> 
> class CustomUserCreationForm(UserCreationForm):
>     class Meta(UserCreationForm.Meta):
>         fields = UserCreationForm.Meta.fields + ('email',)
> ```

> `signup` view
>
> - 기존에 import 했던 `UserCreationForm` 삭제, `CustomUserCreationForm` 추가
> - `UserCreationForm` -> `CustomUserCreationForm` 변경



> `index` view
>
> ```
> import hashlib
> 
> def index(request):
>     if request.user.is_authenticated:
>         gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
>     else:
>         gravatar_url = None
>     visits_num = request.session.get('visits_num', 0)
>     request.session['visits_num'] = visits_num + 1
>     request.session.modified = True
>     articles = Article.objects.all()
>     context = {'articles': articles, 'visits_num': visits_num, 'gravatar_url': gravatar_url,}
>     return render(request, 'articles/index.html', context)
> ```

> `base.html` (구문 추가)
>
> ```
> <img src="https://s.gravatar.com/avatar/{{ gravatar_url }}?s=80" alt="프로필이미지">
> ```



#### (2) Custom template tags and filters (django custom template tag 공식 문서)

**모든 페이지에서 이미지가 나오도록 수정한다.**

> `accounts` app > `templatetags` folder 생성
>
> - 폴더 내부에 `__init__.py`, `gravatar.py` 생성

> ```
> gravatar.py
> import hashlib
> from django import template
> 
> register = template.Library()
> 
> @register.filter # 기존의 템플릿 라이브러리에 아래의 함수(custom filter)가 추가된다는 의미인 decorator
> def makemd5(email): # {{ email | ssafy }} 와 같은 경우 필터 앞에 있는 왼쪽에 있는 값
>     return hashlib.md5(email.encode('utf-8').lower().strip()).hexdigest()
> ```

> ```
> base.html
> {% load gravatar %} <!-- 가장 맨 위에 코드 추가 -->
> 
> <img src="https://s.gravatar.com/avatar/{{ request.user.email|makemd5 }}?s=80" alt="프로필이미지"> <!-- 코드 수정-->
> ```

> `index` view
>
> - (1)에서 새로 작성했던 코드가 굳이 있을 필요가 없다.
> - django custom template tag를 사용했기 때문이다.