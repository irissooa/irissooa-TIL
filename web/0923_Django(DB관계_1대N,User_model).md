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



#### Abstract base classes

- 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
- 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨

![image-20200923144115871](0923_Django(DB관계_1대N,User_model).assets/image-20200923144115871.png)



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

- `settings.py`

```python
AUTH_USER_MODEL = 'accounts.User'
```

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
fields = ['title', 'content',] # 구문 수정
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

> 하나의 모델에는 여러 외래키가 있어도됨

```python
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #(생략)
```

- `forms.py`

> exclude 수정

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        #제외할 것을 적어줘도됨, 이건 foreign key이기 때문에 안보여지게 할거야
        exclude = ['article','user',]
```



1. comments_create logic 수정
   - `views.py` > `comments_create` view

> user에 대한 정보를 받아옴, 사실상 들어가는 정보는 user_id임 클래스변수 user에 객체 자체를 넣어줌

```python
comment.user = request.user # 구문 추가
```

- `comments_create`뷰함수

```python
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
        comment.article = 
        #user에 대한 정보를 받아옴, 사실상 들어가는 정보는 user_id임 클래스변수 user에 객체 자체를 넣어줌
        comment.user = request.user
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

- `detail.html`

  > ` {{ comment.user }}`댓글 작성자 표시

```html
{% for comment in comments %}
  <ul>
    {{ comment.user }}<li>{{comment.content}}</li>
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method='POST' class='d-inline'>
    {% csrf_token %}
    <input type="submit" value='DELETE'>
    </form>
  </ul>
    {%empty%}
    <p>댓글이 아직 없어요.</p>
  {% endfor %}
```



2. 비로그인 유저 댓글 작성 form 숨기기

- `views.py`

```python
@require_POST
def comments_create(request,pk):
     #댓글작성은 detail 페이지에서 보여짐
    # article = Article.objects.get(pk=pk)
    if request.user.is_authenticated: #이 구문 추가(인증된 유저만!)
        article = get_object_or_404(Article,title__startswith='A',pk=1)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = 
            comment.user = request.user
            comment.save()
            return redirect('articles:detail',article.pk)
        context = {
            'comment_form':comment_form,
            'article':article,
        }
        return render(request,'articles/detail.html',context)
    #로그인하지 않았을때
    return reirect('accounts:login')
```



- `detail.html`

```html
{% if request.user.is_authenticated %}
    <h4>댓글작성</h4>
    <form action="{% url 'articles:comments_create' article.pk %}" mehtod='POST'>
    {% csrf_token %}
    {{comment_form}}
    <input type="submit">
    </form>
    {% else %}
    <a href="{% url 'acoounts:login' %}">[댓글을 작성하려면 로그인 하세요.]</a>
{% endif %}
```



3. 내가 작성한 게시글에서만 DELETE 보이기

- detail.html

> `{% if request.user == comment.user %}`

```html
<ul>
    {{ comment.user }}<li>{{comment.content}}</li>
    {% if request.user == comment.user %}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method='POST' class='d-inline'>
      {% csrf_token %}
      <input type="submit" value='DELETE'>
      </form>
    {% endif %}
  
```

- `views.py` > `comments_delete` view

```python
@require_POST
def comments_delete(request,article_pk,comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    if request.user.is_authenticated: # 이 구문 추가(인증된 유저만!)
        comment = get_object_or_404(Comment,pk=comment_pk)
        if request.user == comment.user: # 이 구문 추가(작성한유저만!)
            comment.delete()
    return redirect('articles:detail',article_pk)
```



#### 1. ModelForm Custom

- `accounts` > `forms.py`

```python
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
```

- `signup` view
  - 기존에 import 했던 `UserCreationForm` 삭제, `CustomUserCreationForm` 추가
  - `UserCreationForm` -> `CustomUserCreationForm` 변경





------------

### Model relationships(M : N) 

- **User : Article = M : N**
  - User는 여러 개의 Article에 LIKE 할 수 있고
  - Article은 여러 User 로 부터 LIKE 받을 수 있다.

- **모델링은 현실 세계를 최대한 유사하게 반영하기 위해서 해야한다.**

- 일상에 가까운 예시를 통해 db를 모델링하고, 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있는지에 대해 고민

**환자와 의사의 예약 시스템을 구축하라는 프로젝트**

- 모델링(`models.py`)

  ```python
  from django.db import models
  
  class Doctor(models.Model):
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
  
  
  class Patient(models.Model):
      name = models.TextField()
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```



#### 1. 1:N의 한계 (shell_plus로 객체 생성 후 확인)

- 불필요한 필드(같은 환자 이름을 가진 필드)를 또 만들어야 하는 문제점이 발생한다.
- 수정을 할 수 없고 계속 추가해야됨!
- 문제점
  - 방문 예약을 바꾸는 것이 불가능(새로운 객체 생성)
  - 다른 의사를 방문한 기록을 남길 수 없음

- `python manage.py shell_plus`

```sh
In [1]: doctor1 = Doctor.objects.create(name='justin')

In [2]: doctor2 = Doctor.objects.create(name='eric')

In [3]: patient1 = Patient.objects.create(name='tony', doctor=doctor1)

In [4]: patient2 = Patient.objects.create(name='harry', doctor=doctor2)

In [5]: doctor1
Out[5]: <Doctor: 1번 의사 justin>

In [6]: doctor2
Out[6]: <Doctor: 2번 의사 eric>

In [7]: patient1
Out[7]: <Patient: 1번 환자 tony>

In [8]: patient2
Out[8]: <Patient: 2번 환자 harry>

#환자가 의사를 바꾸고싶은데 수정을 못하고 다시 추가로 만들어줘야됨!
In [9]: patient3 = Patient.objects.create(name='tony', doctor=doctor2)

In [10]: patient3
Out[10]: <Patient: 3번 환자 tony>

In [11]: patient3.doctor.name
Out[11]: 'eric'

In [12]: patient4 = Patient.objects.create(name='harry', doctor=doctor1)

#하나의 patient가 여러 의사를 지정받을 수 없음!
In [13]: patient4 = Patient.objects.create(name='harry', doctor=doctor1, doctor=doctor2)
  File "<ipython-input-13-2775590f4f3f>", line 1
    patient4 = Patient.objects.create(name='harry', doctor=doctor1, doctor=doctor2)
                                                                   ^
SyntaxError: keyword argument repeated
```



#### 2. 중개모델 생성 - `models.py`에 Reservation model 추가

[![중개 모델](0923_Django(DB관계_1대N,User_model).assets/67262400-9c610880-f4df-11e9-9904-a8ebb314966b.JPG)](https://user-images.githubusercontent.com/52685250/67262400-9c610880-f4df-11e9-9904-a8ebb314966b.JPG)

- 1 : N 의 한계점을 해결하기 위해 중개모델을 생성하여 어느 의사가 어느 환자와 매칭되는지 알 수 있다.
- `hospitals` > `models.py`

```python
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

- 기존의 `db.sqlite3`, `0001_initial.py` 삭제 후(`__init__`이건 삭제하면 안됨) 다시 migration 과정 진행

- 중개 모델이 생겼으므로 `doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)` 이 구문은 필요가 없게 된다.

```sh
In [1]: doctor1 = Doctor.objects.create(name='justin')

In [3]: patient1 = Patient.objects.create(name='tony')

#진료예약을 하나 만든것과 같은 것
In [4]: reservation1 = Reservation.objects.create(doctor=doctor1, patient=patient1)

IN[5] : reservation1
Out[5]: <Reservation: 1번 의사의 1번 환자>

#역참조 '_set.all()'
In [6]: doctor1.reservation_set.all()
Out[6]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

In [7]: patient1.reservation_set.all()
Out[7]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

In [8]: patient2 = Patient.objects.create(name='harry')

In [9]: reservation2 = Reservation.objects.create(doctor=doctor1, patient=patient2)

IN[10]: reservation2
Out[10]: <Reservation: 1번 의사의 2번 환자>

#오늘 내 환자 몇명이었지?
In [11]: doctor1.reservation_set.all()
Out[11]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>

In [12]: for reservation in doctor1.reservation_set.all():
    ...:     print(reservation.patient.name)
    ...: 
tony
harry
```



#### (3) 중개 모델을 직접 거치지 않고 바로 가져오기 - `Through` option

- `Through option`
  - 중개 모델을 거치지 않고 직접 서로 테이블을 참조하는 option
  - `ManyToManyField`는 **실제적인 물리적인 필드가 DB에 생기는 것이 아니다.**
    - 보통 복수형을 적는다! (외래키는 보통 단수형)
- `models.py`

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.models.ManyToManyField(Doctor,through='Reservation')
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- `shell_plus`

```sh
In [1]: patient1 = Patient.objects.get(pk=1)

In [2]: patient1
Out[2]: <Patient: 1번 환자 tak>

#진료를 조회함
In [3]: patient1.reservation_set.all()
Out[3]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

#의사만 출력, 내가 진료받는 의사로 patient에서 바로 접근(through option을 통해!)
In [4]: patient1.doctors.all()
Out[4]: <QuerySet [<Doctor: 1번 의사 justin>]>

In [5]: doctor2 = Doctor.objects.create(name='eric')

In [6]: Reservation.objects.create(doctor=doctor2, patient=patient1)
Out[6]: <Reservation: 2번 의사의 1번 환자>

In [7]: patient1.reservation_set.all()
Out[7]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 2번 의사의 1번 환자>]>

#나를 진료해주는 의사가 누구인지 바로 조회
In [8]: patient1.doctors.all()
Out[8]: <QuerySet [<Doctor: 1번 의사 justin>, <Doctor: 2번 의사 eric>]>

In [10]: doctor2
Out[10]: <Doctor: 2번 의사 eric>

In [11]: doctor2.patient_set.all()
Out[11]: <QuerySet [<Patient: 1번 환자 tony>]>
```



#### 4. Doctor도 patients 를 참조할 수 없을까? - `related_name` option

> 역참조! 필드가 있는곳에서 참조하는건 참조, 필드가 없는 곳에서 자기를 참조하는 것을 참조하는 것이 역참조!

- `related_name`

  - 참조되는 대상이 참조하는 대상을 찾을 때(역참조), 어떻게 불러 올지에 정의한다.
  - MTOM(ManyToMany) 필드가 없는 테이블이 있는 테이블을 참조할 때 사용한다.
  - 필수적으로 사용하는 건 아니지만 필수적인 상황이 발생할 수 있다.

  ```python
  doctors = models.ManyToManyField(Doctor, related_name='patients') # 구문 추가
  # through='reservation'는 삭제
  ```

- `models.py` 

  ```python
  class Doctor(models.Model):
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
  
  
  class Patient(models.Model):
      name = models.TextField()
      #through='Reservation'(삭제)->중개모델을 지웠기 때문에 없앰
      #역참조 related_name인자가 있다->중개모델 클래스 지워도 괜춘
      doctors = models.ManyToManyField(Doctor, related_name='patients')
  
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  
  '''
  Doctor가 Patient참조 역참조
  중개모델을 앞으로는 직접만들지 않을거야!
  '''
  
  # class Reservation(models.Model):
  #     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  #     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      
  #     def __str__(self):
  #         return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

- shell_plus로 확인

  ```sh
  In [1]: doctor1 = Doctor.objects.create(name='justin')
  
  In [3]: patient1 = Patient.objects.create(name='tony')
  
  In [4]: doctor1
  Out[4]: <Doctor: 1번 의사 justin>
  
  In [5]: patient1
  Out[5]: <Patient: 1번 환자 tony>
  
  In [6]: doctor1.patients.add(patient1)
  
  In [8]: doctor1.patients.all()
  Out[8]: <QuerySet [<Patient: 1번 환자 tony>]>
  
  In [9]: patient1.doctors.all()
  Out[9]: <QuerySet [<Doctor: 1번 의사 justin>]>
  
  In [10]: patient1.doctors.remove(doctor1)
  
  In [11]: patient1.doctors.all()
  Out[11]: <QuerySet []>
  
  In [12]: doctor1.patients.all()
  Out[12]: <QuerySet [<Patient: 1번 환자 tony>,<Patient: 2번 환자 harry>]>
  ```

- 위와 같은 상황일 때 `manytomany_patient_doctors` 테이블이 새로 생성된다.

- 중개 모델을 생성하지 않고 `doctor`에서는 `patients.all()`로, `patients`에서는 `doctors.all()`로 서로 접근할 수 있다.(ManytoMany 필드의 특징!)



- 그렇다면 중개모델은 필요가 없는가??? => **아님!!!!**
  - 예약한 시간 정보를 담는다거나 하는 경우(= 추가적인 필드가 필요한 경우)에는 반드시 중개모델을 만들어서 진행을 해야되는 상황도 있다.
  - 다만 그럴 필요가 없는 경우 위와 같이 해결할 수 있다.

