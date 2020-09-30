# Django N:M관계

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

- django는 M:N관계를 나타내는 중개테이블(intermediary join table)을 만든다
- 테이블 이름은 ManyToManyField의 이름과 이를 포함하는 모델의 이름을 조합하여 생성함

> Arguments

- 모두 optional 하며 관계가 작동하는 방식을 제어함
- `related_name`
  - ForeignKey의 related_name과 동일
- `through`
  - 중개 테이블을 직접 작성하려는 경우 지정
  - 일반적으로 추가 데이터를 M:N 관계와 연결하려는 경우에 사용
- `symmetrical`(대칭적임)
  - ManyToManyField가 동일한 모델(self)을 가리키는 정의에서만 사용
  - 재귀적 정의(대댓글 관계)
- etc.....

---------

하나의 article에는 여러user가 좋아요를 할 수 있다

한명의 user는 여러 article에 좋아요를 누를 수 있다





-------------

## GIT

![image-20200928125050746](0928_Django(DB관계_N대M).assets/image-20200928125050746.png)

![image-20200928125225667](0928_Django(DB관계_N대M).assets/image-20200928125225667.png)

![image-20200928125249043](0928_Django(DB관계_N대M).assets/image-20200928125249043.png)

2. .git 폴더를 삭제한 다음 다시 gitinit을 하면 됨,(프로젝트를 새로 만든 다음에)