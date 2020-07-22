# Python 이론(2020-07-22)

>함수

## 1. 함수 선언과 호출

- 가독성, 재사용성, 유지보수를 위해 함수를 사용함
- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있음
- 동작 후 `return`을 통해 결과값 전달
- `return`값이 없으면, `None`을 반환(=결과값이 없다.)
- 함수의 호출은 `func()`/ `func(val1,val2)`

```python
def <함수이름>(parameter1,parameter2):
    <코드>
    return value
```

```python
#함수정의하기
def cube(num): #cube라는 함수이름으로 정의하겠다
    #num이라는 이름으로 쓰겠다 :파라미터(매개변수) 정의
    cubed = num**3
    return cubed
    #return num**3도 넣을 수 있음
#함수는 반드시 결과값을 뱉어내야됨, return이 없더라도 None으로 output됨
#return문에는 하나의 값 뿐만아니라 하나의 값으로 환원 될 수 있는 표현식도 올수있다.
#함수는 입력은 여러개지만 output은 하나의 것(객체)(한개가 아닐 수 있음ex)리스트, 튜플 등)이 나옴
```

- print의 return값은 None.

```python
# 우리가 활용하는 print문도 파이썬에 지정된 함수입니다. 
# 아래에서 'hi'는 argument이고 출력을 하게 됩니다.
result=print('hi')
print(result)
type(result)
#**매우 중요한 것***print의 return값은 None임
#return되는 것과 printing되는 것이 다름
#jupyter로 봤을 때 결과 옆에 out이 돼있는 것은 아웃풋이 있는거임
#print는 return문이 없다.**몇몇 함수는 return값이 없다.
#return이 되고 안되고가 중요하다
sorted_list=[5,2,3,4,1].sort()
print(sorted_list)
#값이 None
#why? 리턴하지 않는 함수이기 때문
```

- 반환하라=> return을 꼭 해주기!

```python
def my_max(a,b):
    if a>=b:
        return f'{a}(이)가 더 큽니다.' 
#후에 결정되는 것을 하겠다.->interpolation, f스트링사용
        print(f'{a}(이)가 더 큽니다.') 
#print로 하면 return을 했을 때와 완전 다른 함수 (**return값이 설정 됐냐 아니냐에 따라 크게 다름)
#my_max는 return값이 있는 함수인데 print를 한다면 output이 없어 None이 됨(같아보이지만 다름)
    else:
        return f'{b}(이)가 더 큽니다.'
```

- 내장함수 목록

```python
dir(__builtins__) 
#이렇게 쓰면 내장함수 목록을 알 수 있음, 이건 함수이름으로 쓰면 안됨
```



## 2. Output

### 1) return

- 함수는 반환값이 있으며, 어떤 종류(객체)라도 관계없음
- But, `오직 한개의 객체`만 반환됨
- 함수가 `return`되거나 종료되면, 함수를 호출한 곳으로 돌아감

```python
def my_list_max(a,b): #매개변수는 a,b로 정의
      #sum함수 활용
    if sum(a)>=sum(b):
        return a
    else:
        return b
```



## 3. Input

### 1) 매개변수(parameter)

- 입력을 받아 함수 내부에서 활용할 `변수`

### 2) 인자(argument)

- 전달인자=실제로 전달되는 `입력값`

#### (1) 위치 인자

- 함수는 기본적으로 인자를 위치(`순서`)로 판단

```python
def cylinder(r,h): 
#나중에 파라미터(r,h)를 명확하게 적어주는 것이 좋다. 
#순서가 중요하기 때문에 봤을 때 위치를 알 수 있게 적는 습관이 중요
    area= r*r*3.14 #밑면의 넓이
    volume=area*h #원기둥 부피
    return volume
print(cylinder(5,2))
print(cylinder(2,5)) 
# 순서를 바꾸면 다른 값이 나옵니다.//인자의 위치가 중요함
```

#### (2) 기본인자 값

- parameter 옆에 `=(기본인자)`로 지정
- **단, 기본인자값을 가지는 인자 다음에 기본값이 없는 인자를 사용할 수 없음

```python
def greeting(name='익명',grade):#기본인자값을 가진다면 파라미터가 순서가 중요함
    return f'{grade}학년, {name}님, 환영합니다.' 
#왜 에러나냐? 컴퓨터를 헷갈리게 만들기 때문
#예) greeting(4)를 한다면 이게 name인지 grade인지 헷갈림
#순서를 바꾸면 rule이 생김, 앞(기본값이 없는것)에 있는건 반드시 필요
#greeting(grade, name='익명')이러면 오류가 나지 않음
```

#### (3) 키워드 인자

- 직접 변수의 이름으로 특정 인자를 전달할 수 있음

```python
def greeting(age,name='익명'):
    return f'{age}세 {name}님 환영합니다.'
greeting(name='홍길동',age=20) 
#이렇게 매개변수를 이용해서 쓴다면 위치를 제대로 연결시켜줌
greeting(age=20,name='홍길동')
#20세 홍길동님 환영합니다
```

- **단, `키워드 인자`를 활용한 다음, `위치 인자`를 활용할 수 없음

```python
#greeting(name='홍길동',20) 
#부분만 keyword argument를 쓰고 싶다면 가장 뒤에 적어줘야 오류 없이 작동
greeting(20, name='홍길동') 
#keyword는 다 쓰던지, 뒤에만 쓰던지! 원칙을 지켜주세용
```

#### (4) 가변인자

- `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트 `*args`를 활용(`*`이 중요 `args`라는 이름은 달라져도 됨, but 주로 이렇게 사용)
- 가변 인자 리스트는 `tuple`형태로 처리 되며, 매개변수에 `*`로 표현(`list`아님)

```python
def func(a,b,*args):
#*args:임의의 개수의 위치인자를 받음, 주로 매개변수 목록의 마지막에 옴
```

- max, min을 구할 때 sys의 가장 작은값, 큰값을 기본값으로 둠

```python
import sys 
#print(sys.maxsize)#가장 큰것/ 앞에 -붙이면 가장작은수

def my_max(*args):#함수에 인자를 여러개 넣어도 알아서 인식(가변인자이기 때문)
    #1.max라는 함수를 리턴하는 my_max 이렇게 그냥 쓸수도 있고
    #return max(args) 
    #max를 쓰는 것이 비효율적일 때가 있어서 바닥부터 알고리즘짜는 걸 아는게 중요
        
    #2. 기본적방법 : 큰값구할때 가장 작은것을 기본값으로 둠
    max_value=-sys.maxsize 
    for i in args:
        if max_value<i:
            max_value=i
    return max_value
```

#### (5) 가변 키워드 인자

- 정해지지 않은 키워드 인자들은 `dict`형태로 처리 됨
- `**`러 표현, 보통 `kwargs` 이름 사용

```python
def func(**kwargs):
#**kwargs : 임의의 개수의 키워드 인자를 받음
```

- 딕셔너리 생성 함수

```python
hi = dict(한국어='안녕',영어='hi')
hello=dict(독일어='guten tag', 프랑스어='bon jour')
#이건 함수, 우리가 정의하지않은 키워드를 핸들링하는것 가변 키워드인자이기 때문
#몇개를 넣든 키워드와 함께 적으면 딕셔너리가 완성됨
#keyword인자에는 ''쓰면 안됨, 하나의 파라미터이기 때문
print(hi)
print(hello)
greeting= {'한국어':'안녕','영어':'hi'} #이건 그냥 기본적는것
#hi와 greeting은 같게 나오지만 다른것
```



## 4. 스코프(scope)

- 함수는 코드 내부에 공간(`scope`)를 생성함
- 전역 스코프(`global scope`) : 코드 어디에서든 참조할 수 있는 공간
- 지역 스코프(`local scope`) : 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
- 전역 변수(`global variable`) : 전역 스코프에 정의된 변수
- 지역 변수(`local variable`) : 로컬 스코프에 정의된 변수

```python
# 들여쓰기에 맞춰 각 공간이 정해져 있음

## **지역스코프에서는 전역으로 조회가 가능하지만 전역스코프에서는 지역스코프를 조회 못함
#로컬은 중2병히키코모리 막내동생...자기만 조회가능

# 전역 스코프(global scope)
a = 10 # 전역 변수(global)

def func(b):
    # 지역 스코프(local scope)
    c = 20 # 지역 변수(local variable)
    print(a) #10을 가리키고 있음(지역스코프에서 전역스코프 조회는 가능)
    print(b)#func파라미터를 가리킴
    

# 변수 c는 접근 불가합니다.
#func함수 안에 있는 것(지역스코프를)을 밖(전역스코프)에서 조회하는 것은 불가

#print(c)
```

- `func()`함수에 `a변수`를 추가하면?

```python
a = 10 # 전역 변수(global)

def func(b):
    # 지역 스코프(local scope)
    c = 20 # 지역 변수(local variable)
    a=30
    print(a) # 안에서 바깥으로 조회해나감(안에a가 있기때문에 안에서 정의된 a를 사용)
    print(b)

func(50)
#30
#50
```

- 식별자 검색(resolution) 규칙
  - 식별자들은 이름공간(namespace)에 저장돼 있음
  - `LEGB Rule`
    - `L`ocal scope : 정의된 함수
    - `E`nclosed scope : 상위 함수
    - `G`lobal scope : 함수 밖의 변수 혹은 import된 모듈
    - `B`uilt-in-scope : 파이썬 안의 내장되어 있는 함수 또는 속성

```python
print = 'hello' #이러면 내장함수가 아니라 문자가 되기 때문에 에러가남
print(3)
del print #print를 못쓰는 것이 아니라 global에 있는 print를 지움, 빌트인에는 남아있음
#1. `print()` 코드가 실행되면
#2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,
#3. `print`라는 식별자를 Global scope에서 찾아서 `print = hello`를 가져오고, 
#4. 이는 함수가 아니라 문자열이기 때문에 `not callable`하다라는 오류를 내뱉게 됨.
#5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문
```

```python
a = 10  # 전역 변수
b = 20  # 전역 변수

def enclosed():
    a = 30  # enclosed함수의 지역 변수
    
    def local():
        c = 40 # local함수의 지역 변수
        print(a, b, c)#순차적으로 보기 때문에 'a= enclosed에 있는 30', 'b=global에 있는 20'
    
    local()#이건 enclosed에 포함됨
    
    a = 50  # enclosed함수의 지역 변수이며, local함수에서는 Enclosed Scope

#전역에서 local()함수 호출?
enclosed() #enclosed에 local()을 실행하라고 돼있기 때문
#local()을 쓰면 안됨
# 이건 따로 호출 불가, enclosed 안에 들어있는 것이기 때문에 global에서는 호출 불가
#히키코모리 동생방을 볼수 없다.
```

- 전역변수를 바꿀 수 있는가?

```python
global_num = 3
def local_scope():
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())#이건 local_scope를 불렀기 때문
print('global_num:', global_num) #밖에서 불렀기때문에 3

#전역변수를 바꾼다면
###global문법을 가져와 전역변수와 함께 바뀜
#하지만 이렇게 프로그래밍 하면 좋지 않음 
#되도록이면 안의 데이터는 밖의 것을 수정하지 않게 해야됨
#오류가 났을 때 고치기 쉬우려면 다 분리해서 알고리즘 해야됨
#하지만 global을 썼을 때 상당히 편하기 때문에 많이 쓰기도함..(개발과정에선 금지)
#알고리즘 테스트에서는 해도 됨(테스트 통과만 하면 되기 때문)

global_num = 3
def local_scope():
    global global_num 
    global_num= 5 
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num) 

```

- 변수의 수명 주기
  - `built-in scope` : 파이썬이 실행된 이후부터 영원히 유지
  - `global scope`(전역스코프) : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날때까지 유지
  - `local scope`(지역(함수)스코프) : 함수가 호출될 때 생성, 함수가 종료될 때까지 유지(함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)

## 5. 재귀함수(recursive function)

- **알고리즘에서 꼭 알아야됨
- 컴퓨터 프로그래밍에서 매우 중요한 개념
- 함수 내부에서 자기 자신을 호출하는 함수

### 1) 팩토리얼 계산

- 반복문을 통한 팩토리얼
  - n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소
  - 마지막에 ndl 1이면 더 이상 반복문 돌지 않음

```python
def fact(n):
    result=1 #누적곱은 1부터 시작
    for i in range(1,n+1):
        result*=i
    return result
```

- 재귀를 이용한 팩토리얼 계산
  - 재귀함수를 호출하며, n은 1씩 감소
  - 마지막에 n이 1이면 더 이상 추가 함수 호출 안함
  - 반드시 `base case`가 존재
  - `base case` : 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳
  - 코드가 더 직관적이고 이해하기 쉬운 경우 있음
  - But, 함수가 호출될 때마다 메모리 공간에 쌓임-> 메모리 스택이 넘쳐(Stack overflow) 프로그램 실행 속도가 늘어남
  - 파이썬에서는 1,000번이 넘어가면 더이상 함수 호출 안함

```python
#재귀는 큰문제를 잘게 쪼개 작은문제부터 해결해나가는 것에 사용함
#반복되는 하부구조를 가짐
#문제가 부분 문제로 치환이 가능 2!=1!*2, 
#3!(factorial(3))=3*2!(factorial(2)=2*1!(factorial(1)))
#무한으로 불러옴 종료조건이 필요함
def factorial(n):
    if n==1:
        return 1 #문제가 분할됐다가 작은답으로부터 큰문제의 답이 도출됨
    return n * factorial(n-1)

#3!(factorial(3))=3*2!(factorial(2)=2*1!(factorial(1)))
#factorial(1)=1로 치환을 한다는 식을 넣어줘야됨(종료조건=base step=기본식)
#수열 점화식(점점변해가는식,recurrence relation)=재귀식
#문제가 분할됐다가 작은답으로부터 큰문제의 답이 도출됨
#!(factorial(3))=3*2!(factorial(2)=2*1!(factorial(1)))
#여기서 factorial(1)은 return 1이 되면서 다시 위로 값이 합쳐지면서 답이 도출됨
#작게 분해가 됐다가 작은 값(basestep)의 답을 얻은뒤 원래 구하고자한 큰 값이 도출됨
```



### 2) 피보나치 수열

- 반복문

```python

```

- 재귀함수 사용

```python
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
```



### 3) 반복문과 재귀함수 차이

- 알고리즘 자체가 재귀적 표현이 자연스러운 경우 재귀함수 사용
- 재귀호출은 `변수 사용`을 줄여줌

```python
#재귀로 가능한 것
def sum_recur(n):
    if n==0:
        return 0
    return n+sum_recur(n-1)
```



