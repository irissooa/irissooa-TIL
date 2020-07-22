# Python 이론

# 1. 문법

- 주석

  - 한 줄 : 앞에 #으로 표시
  - 여러 줄 : 한 줄 씩 #을 사용 또는 `'''` 또는 `"""`으로 표현 가능
    - multiline은 주로 함수/클래스 설명을 위해 활용

- 코드라인

  - 1줄에 1문장이 원칙

  - 문장은 파이썬이 실행 가능한 최소한의 코드 단위

  - 한 줄로 표기할 때 `;`를 작성하여 표기할 수 있지만 기본적으로 `;`을 작성하지 않는다.

    ```python
    print('hello');print('world')
    ```

  - 여러 줄을 작성할 때는 역슬래쉬`\`(원화표시)를 사용

    ```python
    print('\
    안녕\
    나는\
    python이야\
    ')
    # (출력) 안녕나는python이야 
    #// 가능은 하지만 자주 사용안함
    ```

  - `[]`,`{}`,`()`는 `\` 없이도 가능

    ```python
    menu=[
    '김밥','라면','떡볶이'
    ]
    #되도록 공백 없이 쓰는 것 추천
    ```

### 1. 저장

> 무엇을(어떤 data type), 어떻게('='), 어디에(variable, container)로 나뉜다.

#### 1.1 변수(varibale)

##### 1)  할당 연산자

- 변수는 `=`로 할당됨
- `type()` : 데이테 타입을 확인 가능
- `id()` : 메모리 주소 확인 가능

```python
x='hello'
type(x)
id(x)
# (출력) str
```

- 같은 값을 동시에 할당 가능

```python
x=y='hello' #error가 안남, x에도 y에도 'hello'가 담김
print(x)
print(y)
# hello
# hello
```

- 다른 값을 동시에 할당 가능

``` python
a=2020
b=4
a,b=2020,4 # 한줄로 줄이기 위해 이렇게 표현도 가능
print(a)
print(b)
#2020
#4
#파이썬은 동시할당을 통해 변수 없이 바꿈 가능
#ex) 
a,b=b,a
print(a)
print(b)
#4
#2020
```

- 변수의 개수가 더 많거나 적으면 에러가 남(too many values, not enough values)

##### 2) 식별자(Identifiers)

- 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름

- 영문알파벳(대문자, 소문자/ 구분필요), 밑줄(_), 숫자로 구성됨

- 길이에 제한 없음

- 예약어는 사용할 수 없음

  ```python
  #예약어 직접 확인 가능
  import keyword
  print(keyword.kwlist)
  ```

- 내장함수(built-in fuction)이나 모듈 등도 이름 사용 안됨(오류남)

#### 1.2 데이터타입

##### 1) 숫자타입

(1) `int`(정수,ingteger)

- 파이썬은 다른 프로그래밍 언어(C계열)와 다르게 정수 자료형에서 오버플로우가 없다.(데이터 타입 별로 사용할 수 있는 메모리 크기가 제한되어 있지 않다.)

- 2진수 : `0b` / 8진수 : `0o` /16진수 : `0x` 로 표현 가능

  ```python
  binary_number=0b10 #2진수는 0과 b를 합쳐서 표현할 수 있다.
  print(binary_number) #tab키 누르면 자동완성 가능
  #2
  octal_number=0o10 #8진수
  print(octal_number)
  #8
  hexadecimal_number=0x10 #16진수
  print(hexadecimal_number)
  #16
  ```

(2)`float`(부동소수점, 실수, floating point number)

- **실수를 컴퓨터가 표현하는 과정에서 항상 같은 값으로 일치되지 않기 때문에 값이 같은지 비교하는 과정에서 문제가 발생할 수 있다.

  ```python
  3.5-3.2 ==0.3 #false나옴***무심코 썼다가 우리가 해석하는 것과 컴퓨터가 해석하는 방식이 다름 그래서 실수의 연산에서 오류가 자주 발생 조심해야됨
  ```

- 두개의 값이 같은지 확인 할 때

  -  `round()`이용

  ```python
  print(3.5-3.2)
  #0.2999999999999999999998
  print(0.3)
  #0.3
  round(3.5-3.2,2)==0.3 #그래서 실수 연산에 매우 조심해야됨.
  #True
  ```

  - `epsilon`이용

  ```python
  import sys
  print(sys.float_info.epsilon) #매우작은 숫자를 써서 처리할 것임 두수의 차이가 큰지 작은지 확인할때 사용
  #2.220446049250313e-16
  abs(a-b)<=1e-10 # 인위적이지 않고, 공식적으로 사용하는 것은 sys.float_info.epsilon이다. 비교를 기준으로 사용하는 숫자임
  #True
  ```

  - `math`모듈 이용(가장 많이 이용)

  ```python
  import math #이젠 sys.float_info.epsilon을 안써도 math.isclose를 쓰면 됨
  math.isclose(a,b) #실제 실수 연산에서 가장 많이 사용
  #True
  ```

- 컴퓨터식 지수 표현 방식 : e

  ```python
  b=314e-2 #e는 지수를 표현하는 방식
  print(b)
  #3.14
  ```

(3) `complex`(복소수, complex number)

- 실수부+허수부(`j`로 표현, 공백을 포함하면 안됨)

##### 2) 문자(String)타입

- 문자열은 `'`나 `"`을 활용하여 표현 가능

- 단, 문자열을 묶을 때 동일한 문장부호를 활용

- 사용자에게 받은 입력은 기본적으로 str->숫자로 사용하고 싶을 땐 형변환을 해줘야 됨

- 문자열 안에 문장부호를 넣고 싶다면 `\`를 앞에 표기

  ```python
  "he's cool"
  '그의 이름은 "ssafy"였다.'
  "그의 이름은 \"ssafy\"였다." #\를 사용하면 같은 부호를 사용하더라도 글자로 인식함
  #'그의 이름은 "ssafy"였다.'
  ```

- 여러줄에 걸친 문장은 `'''`를 사용해야 됨

- 문자열은 `+`로 이어붙이고, `*`로 반복 가능

- `\`활용

  | 예약문자 | 내용(의미) |
  | :------: | :--------: |
  |   `\n`   |  줄 바꿈   |
  |   `\t`   |     탭     |
  |   `\r`   | 캐리지리턴 |
  |   `\0`   |  널(Null)  |
  |   `\\`   |     \      |
  |   `\'`   |     '      |
  |   `\"`   |     "      |

  ```python
  print('안녕\n나는\npython\t이야') #\n을 이용해 줄 바꿈을 해줌 \t는 탭, 쓰다보면 외워짐
  #안녕
  #나는
  #python	이야
  ```

  ```python
  print('\\-$ 환율') #'\'(백슬래쉬 자체를 나타내고싶다.)는 앞에\를 붙여줌
  print("이건 \"python\"입니다.") #"를 문자열 자체로 표시하고 싶을 때
  #\-$환율
  #이건 "python"입니다.
  ```

- end 옵션 변경 가능

  ```python
  print('hello',end=' ') #\n이 기본값으로 들어가있기 때문에 ' ' 공백을 줄수도 있고, 수정가능,\t 등
  print('world')
  #hello world
  ```

1) String interpolation(**자주 사용)

- `%formatting`

  ```python
  print('내 이름은 %s 입니다.'%name) 
  #고전적 스타일:c언어 스타일 %s %특정한값
  ```

- `str.format()`

  ```python
  print('내 이름은 {} 입니다.'.format(name)) 
  #{} 구멍뚫어주고 .format(변수)로 적어줌
  ```

- `f-strings`

  ```python
  print(f'내 이름은 {name} 입니다.') 
  #신식문법 앞에 'f'를 붙여줌 {변수} 입력
  ```

  - 형식 지정 가능

    ```python
    import datetime #시간과 날짜를 알려줌
    now=datetime.datetime.now() 
    #현재시간 알려주는 now함수
    print(now) #이 서버가 한국시간이 아님
    print(f'올해는 {now:%Y}년, 이번달은 {now:%m}월, 오늘은 {now:%d}일' 
    #{now:%_}출력형식 지정은':'로 표시 %y는 20 %Y는 2020')
    #올해는 2020년, 이번달은 07월, 오늘은 20일'
    ```

  - 연산도 가능

    ```python
    pi=3.141592
    r=10
    print(f'{pi:.3} 넓이는 {pi*r*r:.3}')
    #:.3은 3번째 자리에서 반올림
    ```

##### 3) 참/거짓(Boolean)타입

- True/False

- 비교/논리 연산을 수행 등에서 활용

- 0 또는 데이터가 없으면 `False`로 변환(**중요)

  ```python
  bool({})
  #0,{},(),[],'' 등 비어있으면 False
  ```

- `None` 타입

  ```python
  type(None) #None은 자기만의 타입이 있음
  #NoneType
  a=None
  bool(a)
  #False
  ```

##### 4) 형변환

​	(1) 암시적 형변환

- 사용자가 의도하지 않고, 파이썬 내부에서 자동으로 형변환

- bool, Numbers(int,float,complex)

  ```python
  True + 3 #True는 1로 자동 형변환
  False + 3 #False는 0
  result=None
  result + 3 #None은 int로 변환할 수 없다.
  ```

- 값과 값을 더할 때 제일 좋은 건 타입을 일치시키는 것이 좋지만 그렇지 못할 때 파이썬이 암시적으로 형변환해줌

- 정수<실수<복소수 큰단위로 형변환 됨

  ```python
  int_number=2020
  float_number=3.14
  complex_number=2+3j
  type(int_number+ complex_number) #complex로 형변환됨
  ```


​	(2) 명시적 형변환

- 암시적 형변환은 제외하고는 모두 명시적(직접)으로 형변환을 해줘야됨

  - string->intger : 형식에 맞는 숫자만 가능

    ```python
    str(1)+'등' #int와 string은 덧셈으로 연산되지 않음
    #1등
    #string은 글자가 숫자일때만 형변환이 가능
    ```

  - integer->string : 모두 가능

    ```python
    int('3.5') #error
    #숫자에 맞는 데이터 타입이어야 문자에서 숫자로 변환 가능
    int(float('3.5')) #3
    int(3.5) #숫자면 바로 int로 변환 가능
    ```

    

  - `int()`, `float()` : 문자(string), 숫자(float)를 int, float로 변환 

  - `str()` : 숫자, list, tuple, dictionary를 문자열로 변환

    

#### 1.3 연산자(Operator)

##### 1) 산술연산자

| 연산자 |      내용      |
| :----: | :------------: |
|   //   |   몫(정수부)   |
|   %    | 나머지(modulo) |
|   **   |    거듭제곱    |

- 기본 수학 연산자 사용 : `+`, `-`, `/`, `*`

- 나눗셈(`/`)은 항상 `float`

- `divmod` 함수

  ```python
  a,b=divmod(5,2) #몫과 나머지를 할당
  print(a) #2
  print(b) #1
  ```

##### 2) 비교연산자 

| 연산자 |          내용          |
| :----: | :--------------------: |
|   !=   |       같지 않음        |
|   is   |    객체 아이덴티티     |
| is not | 부정된 객체 아이덴티티 |

- `<`(미만),`<=`(이하),`>`(초과),`>=`(이상),`==`(같음)

  ```python
  3!=3.0 #정수와 float로 표현된 정수 값은 같음
  #False
  3.0==3.0
  #True
  ```

##### 3) 논리연산자(***중요)

| 연산자  |            내용            |
| :-----: | :------------------------: |
| a and b |  a와 b 모두 True시만 True  |
| a or b  | a와 b 모두 False시만 False |
|  not a  |  True->False, False->True  |

- `&`와 `|`은 파이썬에서는 비트 연산자

- 단축평가

  ```python
  vowels = ['a','e','i','o','u'] #모음의 모음들
  ('a' and 'b') in vowels #a와 b가 함께 있니
  ('a' and 'b') #b가 출력
  ('a' or 'b') #a가 출력
  ('a' or 'b') in vowels #True
  # 이유 : 글자 중에 빈것 빼고 다 True로 출력 그래서 단축평가로 뒤 True인 b가 출력
  # or은 앞이 true이기 때문에 a가 출력
  ```

1. and/or를 포함한 식에서
2. 먼저, 연산자 양 쪽이bool로 형변환이 일어남
   1. and 경우에는 첫번째가 F일 경우 두번째 항목과 관련 없이 무조건 F
   2. 이 경우에는 두번째 항목을 고려하지 않고
   3. 첫번째 항목을 다시 원래대로 형변환한 결과를 돌려줌
   4. 첫번째 항목이 T인 경우 두번째 항목도 살펴봐야 총 결과를 알 수 있으므로, 두번재 항목이 키플레이어가 됨
1. 표현식의 양 변을 형변환해서 출력되는 결과를 좌지우지하는 키플레이어를 형변환하여 출력해줌

##### 4) 복합연산자

- 연산과 대입이 함께 이루어짐

- 반복문을 통해서 개수를 카운트 할 때 사용

- `a+=b` ==`a=a+b` 이런식으로 사용

  ```python
  cnt=0
  while cnt<5:
    print(cnt)
    cnt+=1 #cnt=cnt+1을 대입과 할당을 한번에 하는 연산자 +=1로 바꿈
  #출력
  0
  1
  2
  3
  4
  ```

##### 5) 기타 주요 연산자

- 숫자가 아닌 자료형은 `+` 연산자를 통해 합쳐질 수 있음(문자열, list 등)

- `in` 연산자를 통해 요소가 속해있는지 확인 가능(문자열, list, range 등)

- `is` 연산자를 통해 동일한 `object(것)`인지 확인 가능

  ```python
  a=[1,2,3]
  b=[1,2,3]
  print(a is b) #==는 True지만 각각을 정의했기 때문에 id는 다름 
  ```

- Indexing/Slicing

  - `[]`사용, `[:]`을 통해 리스트 슬라이싱 가능

    ```python
    [1,2,3,4,5][1:3] #1이상 3이하 위치 슬라이싱
    #[2,3]
    ```

##### 6) 연산자 우선순위

- 굳이 안외워도 됨
- 우선순위를 모르겠으면 `()`을 통한 grouping 해줌
  0. `()` grouping
  1. Slicing
  2. Indexing
  3. 제곱연산자 `**`
  4. 단항연산자 `+`,`-`(음수, 양수 부호)
  5. 산술연산자 `*`,`/`,`%`
  6. 산술연산자 `+`,`-`
  7. 비교연산자 `in`, `is`
  8. `not`
  9. `and`
  10. `or`

##### 7) 표현식&문장

1) 표현식(expression) : 하나의 값(value)로 환원될 수 있는 문장

- 식별자, 값,연산자로 구성
- 표현식을 만드는 문법은 일반적인 수식과 유사
- 하나의 값, 수식, 문장 등이지만 하나의 값으로 평가 될 수 있어야 됨
- 할당문은 표현식이 아님, 그래서 환원되지 않음

2) 문장 (statement): 실항가능한 최소한의 코드 단위

- 하나의 값, 표현식



#### 1.4 컨테이너(Container)

##### 1) 순서가 있는 데이터

- 순서대로 내열된 것이 정렬되었다(sorted)는 아니다.
- 순서를 가질 수 있고, 특정 위치 데이터를 가리킬 수 있다.

###### (1) 리스트([])

###### (2) 튜플(())

- 리스트와 유사, ()로 묶어서 표현
- 수정 불가능

###### (3) range(n,m,s)

- 기본값 : 0부터 n-1까지 값을 가짐
- 범위 : n부터 m-1까지 +s만큼 증가

###### (4) 연산자/함수

| operation     | 설명                    |
| ------------- | ----------------------- |
| x in s        | containment test        |
| x not in s    | containment test        |
| s1+s2         | concatenation           |
| s*n           | n번만큼 반복하여 더하기 |
| s[i]          | indexing                |
| s[i:j]        | slicing                 |
| s[i:j:k]      | k간격으로 slicing       |
| len(s)        | 길이                    |
| min(s),max(s) | 최솟값, 최댓값          |
| s.count(x)    | x의 개수                |



##### 2) 순서가 없는 데이터

###### (1) set({})

- 수학에서의 집합과 동일

- `{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.

- 빈 집합을 만들려면 `set()`을 사용(`{}`는 불가능)

  

###### (2) dictionary

- `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조

- `{}`를 통해 만들며, `dict()`로 만들 수 있음

- `key`는 변경 불가능한 데이터만 가능)(str, int, float, bool, tuple, range)

- `value`는 `list`, `dictionary` 등 모든 것이 가능

  

##### 3) 형변환(O변환가능/X변환불가능)

|    구분    | string |   list   |  tuple   | range |   set    | dictionary |
| :--------: | :----: | :------: | :------: | :---: | :------: | :--------: |
|   string   |   -    |    O     |    O     |   X   |    O     |     X      |
|    list    |   O    |    -     |    O     |   X   |    O     |     X      |
|   tuple    |   O    |    O     |    -     |   X   |    O     |     X      |
|   range    |   O    |    O     |    O     |   -   |    O     |     X      |
|    set     |   O    |    O     |    O     |   X   |    -     |     X      |
| dictionary |   O    | O(KEY만) | O(KEY만) |   X   | O(KEY만) |     -      |

##### 4) 데이터 분류(**중요)

###### (1) 변경 불가능한 데이터

- 단일 데이터 : 숫자, 글자, 참/거짓
- range, tuple, frozenset

###### (2) 변경 가능한 데이터

- list, dict, set, 사용자가 만든 데이터타입



### 2. 제어문

#### 1.1 조건문

> `if`문은 반드시 참/거짓을 판단할 수 있는 조건과 함께 사용

##### 1) if 조건문

```python
if <참/거짓 조건>:
    <코드>#앞에 스페이스 4번 띄움
else :
    <코드>
```

```python
if (num%2)==1: #우선순위가 애매하면 ()를 써줌
#if (num%2): 이값이 1 혹은 0이되기 때문에 1이되면 True라서 홀수, 0은 F라서 짝수
  print('홀수입니다.')
else :
  print('짝수입니다.')
```

##### 2) elif 복수 조건

```python
if score>=90:
  print('A')
elif score>=80:
  print('B')
elif score>=70:
  print('C')
elif score>=60:
  print('D')
else :
  print('F')
```

##### 3) 중첩 조건문

```python
if score>=90:
  print('A')
  if score>=95:
    print('참 잘했어요!')
elif score>=80:
  print('B')
elif score>=70:
  print('C')
elif score>=60:
  print('D')
else :
  print('F')
```

##### 4) 조건 표현식

- 조건에 따라 값을 정할 때 활용
- =삼항 연산자

```python
true_value if <조건식> else false_value
```

```python
num = int(input('숫자를 입력하세요 : '))
value = num if num >= 0 else -num
print(value)#절댓값
```



#### 1.2 반복문

##### 1) while 반복문

- 조건식이 참인 경우 반복적으로 코드 실행
- 조건식 뒤에 콜론(`:`)이 반드시 필요, 코드는 `4spaces`를 들여쓰기 함
- 반드시 종료조건 설정 필요

```python
while <조건식>:
    <코드>
```

```python
while True:
    print('조건식이 참일 때까지')
    print('계속 반복')
```

##### 2) for문

- 시퀀스(String,Tuple,List,Range)나 다른 순회가능한  객체((iterable)의 요소들을 순회함
- 정해진 시퀀스 내에서 반복 시 사용, 가지고 있는 모든 것을 꺼냄

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드>
```

 ```python
#enumerate(iterable,start=0)
lunch = ['짜장면', '초밥', '피자', '햄버거']
for idx, menu in enumerate(lunch):
  print(idx,menu) #알고리즘테스트에서 활용도가 높다.
#출력
0 짜장면
1 초밥
2 피자
3 햄버거
 ```



##### 3) 반복제어

###### (1) break

- `for`나 `while`문에서 빠져나감

```python
n=0
while True:
  if n>=3:
    print('브레이크걸리는 시점',n)
    break
  print(n)
  n+=1
print('반복문 탈출!')
```

```python
for i in range(10):
  if i>1:
    print('break할거야')
    break
  print(i)
```

###### (2) continue

- `continue` 이후의 코드를 수행하지 않고, 다음 요소부터 계속하여 반복 수행

```python
for i in range(6):
#i=2,continue를 만나면 continue이후의(밑의) 코드 2개는 실행하지 않고 바로 n=3으로 넘어감
  if i %2==0:
    continue
    print(f'{i}는 짝수다.')
  print(f'{i}는 홀수다.')
```

```python
for age in ages:
  if age<20:
    continue
  else:
    print(f'{age} 살은 성인입니다.')

for age in ages:
  if age>=20:
    print(f'{age} 살은 성인입니다.')
##둘다 맞다. continue쓰고 안쓰고 차이 둘 다 표현 할 줄 알아야 함
```

###### (3) for-else

- 끝까지 반복문을 시행한 후 실행
- 반복에서 리스트의 소진이나(`for`문) 조건이 거짓이 돼서(`while`문) 종료할 때 실행
- 반복문이 `break`문으로 종료될 때는 실행되지 않음(`break`를 통해 중간에 종료되지 않은 경우만 실행)

```python
for i in range(3):
  print(i)
  if i==100:
    break
else:
  print('break 실행 안됨') ## for와 같은 라인에 else를 써줌
#
0
1
2
break 실행 안됨
```

```python
for i in range(3):
  print(i)
  if i==1:
    break
else:
  print('break 실행 안됨') ## for와 같은 라인에 else를 써줌
#
0
1
```

```python
numbers=[1,4,6,8,10]
for number in numbers:
  print(number)
  if number==5:#numbers에 5가 있다면 True만 출력
    print('True')
    break
else :#5가 없다면 False만 출력
  print('False')


#하나라도 있으면 뭐하고, 아니면 뭐하고 이런 문제에서 사용 break를 만나고 안만나고의 차이
```

###### (4) pass

- 아무것도 하지 않음
- 문법적으로 문장이 필요하지만, 아직 코딩이 완성되지 않았을 때 자리 채우는 용도로 사용 가능

```python
# pass
for i in range(5):
  if i==3:
    pass #왜 쓰냐? if에 들어올 코드를 아직 잘 모를때 비워두면 에러를 발생시키기 때문에 사용
    print('요건 패스')
  print(i)
#
0
1
2
요건 패스
3
4
```

```python
# continue
for i in range(5):
  if i==3:
    continue #밑의 코드는 실행하지 않고 지나감
    print('요건 패스')
  print(i)
#
0
1
2
4
```

