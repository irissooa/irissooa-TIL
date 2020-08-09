# Python(20-07-27)

> 에러 & 예외 처리, 데이터구조

## 에러

### 1. 문법 에러

- 문법 에러가 있는 프로그램은 실행되지 않음
- 에러 발생 시 `SyntaxError`라는 키워드와 함께, 에러의 상세 내용을 보여줌
- `파일이름`, `줄번호`, `^` 문자로 `paser`(파이썬이 코들르 읽어 들일 때) 문제가 발생한 위치 표현
- `paser` 는 `^`로 줄에서 에러가 감지된 가장 앞의 위치를 가리킴

```python
if True:
    print('참')
else #:이 없기 때문에 line4에 옳지 않은 문법이라고 뜸
    print('거짓')
File "<ipython-input-1-e832de0e3f84>", line 4
    else
        ^
SyntaxError: invalid syntax
```

```python
#EOL(End Of Line) 따옴표가 닫히지 않았는데 문자가 끝나버림
print('hi)
File "<ipython-input-2-2ca46bac34ce>", line 2
    print('hi)
              ^
SyntaxError: EOL while scanning string literal
```



### 2. 예외

- 실행 도중 예상하지 못한 상황을 맞이하면, 프로그램 실행을 멈춤
- 문법적으로는 옳지만, 실행시 발생하는 에러

```python
# 0으로 나눌수는 없습니다.
# =====
10 * (1/0) #0으로 무언가를 나눌때 나타남
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-6-d0937ce0240b> in <module>()
      1 # 0으로 나눌수는 없습니다.
      2 # =====
----> 3 10 * (1/0)

ZeroDivisionError: division by zero
```

```python
# 지역 혹은 전역 이름 공간내에서 유효하지 않는 이름
# 즉 정의되지 않은 변수를 호출 하였을 경우
# =====
print(abc)
NameError                                 Traceback (most recent call last)
<ipython-input-7-fe943a5bc5e3> in <module>()
      2 # 즉 정의되지 않은 변수를 호출 하였을 경우
      3 # =====
----> 4 print(abc)

NameError: name 'abc' is not defined
```

```python
# 자료형에 대한 타입 자체가 잘못 되었을 경우
# =====
1 + '1' # 데이터 타입이 다른데 연산을 할 수 없다. int+str은 더할수 없다
TypeError                                 Traceback (most recent call last)
<ipython-input-8-2260977fb592> in <module>()
      1 # 자료형에 대한 타입 자체가 잘못 되었을 경우
      2 # =====
----> 3 1 + '1'

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

```python
#반올림을 하는 함수인데 안에 문자가 들어갈 수 없다.
round('3.5')
TypeError                                 Traceback (most recent call last)
<ipython-input-9-17d9b5be2b9b> in <module>()
      1 #
----> 2 round('3.5')

TypeError: type str doesn't define __round__ method
```

```python
#sample은 몇개를 비복원추출할건지 적어야되는데 정해진 인자 수 보다 적게 입력되면 뜸
#(1) 필수 argument 누락
import random
random.sample([1, 2, 3])
TypeError                                 Traceback (most recent call last)
<ipython-input-10-e90809572e13> in <module>()
      1 #
      2 import random
----> 3 random.sample([1, 2, 3])

TypeError: sample() missing 1 required positional argument: 'k'
      
    
#(2) argument 개수 초과
#인자가 1개만 있어야되는데 2개가 들어가 있음// 왜 2개를 넣었는데 3개라고 하지?=>수요일에 할거
random.choice([1, 2, 3], 6)
TypeError                                 Traceback (most recent call last)
<ipython-input-11-697869171877> in <module>()
      1 #
----> 2 random.choice([1, 2, 3], 6)

TypeError: choice() takes 2 positional arguments but 3 were given
```

```python
# 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우
# =====
int('3.5') 
ValueError                                Traceback (most recent call last)
<ipython-input-12-532e5a67e8aa> in <module>()
      1 # 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우
      2 # =====
----> 3 int('3.5')

ValueError: invalid literal for int() with base 10: '3.5'
```

```python
# 존재하지 않는 값을 찾고자 할 경우
numbers = [1, 2]
numbers.index(3) #3은 안에 없어요!
ValueError                                Traceback (most recent call last)
<ipython-input-13-cbc1c8e40b60> in <module>()
      1 # 존재하지 않는 값을 찾고자 할 경우
      2 numbers = [1, 2]
----> 3 numbers.index(3)

ValueError: 3 is not in list
    
    
# 존재하지 않는 index로 조회할 경우
empty_list = []
empty_list[-1] # 내가 가진 index보다 그 밖의 값을 줬어..
IndexError                                Traceback (most recent call last)
<ipython-input-14-80c75c6ef006> in <module>()
      1 # 존재하지 않는 index로 조회할 경우
      2 empty_list = []
----> 3 empty_list[-1]

IndexError: list index out of range
```

```python
# 딕셔너리에서 Key가 없는 경우 
# =====
songs = {'sia': 'candy cane lane'}
songs['queen']
KeyError                                  Traceback (most recent call last)
<ipython-input-15-db616501ca9c> in <module>()
      2 # =====
      3 songs = {'sia': 'candy cane lane'}
----> 4 songs['queen']

KeyError: 'queen'
```

```python
# 모듈을 찾을 수 없는 경우 # 존재하지 않는 모듈을 가지고 오려고 할때
# =====
import reque
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-16-1f4d180ba434> in <module>()
      1 # 모듈을 찾을 수 없는 경우
      2 # =====
----> 3 import reque

ModuleNotFoundError: No module named 'reque'
 

# 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 (존재하지 않는 클래스/함수 호출)
# ====오타가 날때
from random import sampl
ImportError                               Traceback (most recent call last)
<ipython-input-17-666b31f7f91a> in <module>()
      1 # 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 (존재하지 않는 클래스/함수 호출)
      2 # =====
----> 3 from random import sampl

ImportError: cannot import name 'sampl'
```

```python
# 주피터 노트북에서는 정지 버튼이지만, 실제로 우리가 돌릴 때는 ctrl+c를 통해 종료하였을 때 발생한다.
# =====keyboard를 통해 실행되던 코드가 종료됐다// 계속 반복되는 잘못된코드일때 계속 코드가 돌아서 강제로 멈출때 뜸
while True:
    continue
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-18-8b9466abc919> in <module>()
      2 # =====
      3 while True:
----> 4     continue

KeyboardInterrupt: 
```



## 예외 처리

- `try`&`except`

```python
try:
    <코드> # 예외가 발생하지 않으면 except없이 실행 종료
except(예외):
    <코드> #예외가 발생하면, 남은 부분을 수행하지 않고, except 실행
```



### 1. 에러 메시지 처리 `as`

```python
try:
    <코드>
except 예외 as err:#예외인 어떤 에러가 나온다면 err라는 곳에 저장해두었다가 print(err)해줘
    <코드>
```



### 2. 복수의 예외 처리

- 하나 이상의 예외 모두 처리 가능
- 괄호가 있는 튜플로 여러 개의 예외 지정 가능

```python
try:
    <코드>
except(예외1,예외2):#except 예외1//except 예외2로 쭉 적는 것과 같음, 코드가 동일할때 사용
    <코드>
```

- except를 여러 개 쓸 때 중요한 점 : `순차적`으로 수행됨! 가장 작은 범주부터 시작해야 됨

#### 1) else

- 에러가 발생하지 않는 경우 실행 시킴
-  `except` 뒤에 와야 됨
- `try`코드가 예외를 일으키지 않았을 때 실행됨

```python
try: #여기에 여러 데이터가 있을 가능성이 있기 때문에 어떤 에러가 나오더라도 else는 반드시 일어나게 하려고 사용
    numbers = [1, 2, 3]
    number = numbers[2]
except IndexError:
    print('오류 발생')
else:
    print(number) #오류가 없다면 print하겠다.잘 된 상황에 맞춰서 코드를 실행
   
# 3
```



#### 2) finally

- 모든 경우에든 반드시 실행되는 코드
- 예외의 발생 여부와 관계 없음

```python
try:
    languages = {'python': 'good'}
    languages['java']
except KeyError as err:
    print(f'{err}는 딕셔너리에 없는 키입니다.')
finally: #잘풀리든 아니든 무조건 실행되는 코드
    print('감사합니다.')
    
# 
'java'는 딕셔너리에 없는 키입니다.
감사합니다.
```



### 3. 예외 발생 시키기

#### 1) raise

- 예외를 강제로 발생시킴

```python
def my_div(num1, num2):
    try:
        return (num1 // num2)
    except TypeError:
        raise ValueError('숫자를 넣어주세요')
    except ZeroDivisionError:
        # raise ZeroDivisionError
        print('division by zero 오류가 발생하였습니다.')
       
    
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-685efa17a266> in my_div(num1, num2)
      2     try:
----> 3         return (num1 // num2)
      4     except TypeError:

TypeError: unsupported operand type(s) for //: 'str' and 'str'

During handling of the above exception, another exception occurred:

ValueError                                Traceback (most recent call last)
<ipython-input-3-38d53e68908a> in <module>
----> 1 my_div('1', '5')

<ipython-input-1-685efa17a266> in my_div(num1, num2)
      3         return (num1 // num2)
      4     except TypeError:
----> 5         raise ValueError('숫자를 넣어주세요')
      6     except ZeroDivisionError:
      7         # raise ZeroDivisionError

ValueError: 숫자를 넣어주세요
```



#### 2) assert

- 예외를 발생시키는 다른 방법
- 상태를 검증하는데 사용
- 무조건 `AssertionError`발생
- 검증식이 거짓일 경우 발생

```python
def my_div(num1, num2):
    assert type(num1) == int,AssertionError
    assert type(num2) == int,AssertionError
    moc = num1//num2
    remain = num1 % num2
    return moc, remain
my_div(1, 2) #(0, 1)
my_div('1', '2') 
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-41-cd1e2b9ba8ef> in <module>
----> 1 my_div('1', '2')

<ipython-input-39-73825cc14978> in my_div(num1, num2)
      1 def my_div(num1, num2):
----> 2     assert type(num1) == int,AssertionError
      3     assert type(num2) == int,AssertionError
      4     moc = num1//num2
      5     remain = num1 % num2

AssertionError: <class 'AssertionError'>
```





## 데이터 구조

> 데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법
>
> Program = Data Structure + Algorithm

### 1. 문자열

- immutable(변경할 수 없고)
- ordered(순서가 있고)
- iterable(순회 가능)

#### 1.1 조회/탐색

##### 1) `.find(x)`

- x의 첫번째 위치 반환, 없으면 `-1`을 반환

```python
'apple'.find('p') #1
#없으면 -1 find와 index는 없을 때의 결과값이 다름
'apple'.find('f') #-1
```

##### 2) `.index(x)`

- x의 첫번째 위치 반환
- 없으면, 오류 발생
- return  값이 없음

```python
# return값이 없다. 오류가 뜸 substring=>글자 중 일부 =>handling해줌 try, except를 이용하여 결과값을 줌
try: 
    'apple'.index('k')
except ValueError:
    print('해당하는 값이 없습니다.')

#해당하는 값이 없습니다.
```



#### 1.2 값 변경

##### 1) `.replace(old,new[, count])`

- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
- count를 지정하면 해당 갯수만큼 시행

```python
#return값이 있다 없다는 조작법의 결과를 특정변수에 넣었을 때 변수안의 값을 볼수 있다 없다의 차이
#return하지 않으면 print()했을 때 None을 줌
'yay!'.replace('a', '_') # y_y!
'wooooowoo'.replace('o', '', 2) #'wooowoo'
```

##### 2) `.strip([chars])` (**중요)

- 특정한 문자들을 지정, 양쪽을 제거
- `.lstrip([chars])`: 왼쪽을 제거
- `.rstrip([chars])`: 오른쪽을 제거
- 지정하지 않으면 공백을 제거

```python
'    oh!\n'.strip() #'oh!
'    oh!\n   '.lstrip() #'oh!\n   '
'hehehihihihihi'.rstrip('hi') #'hehe'
```

##### 3) `.split()`

- 문자열을 특정한 단위로 나누어 리스트로 반환
- return 값이 있음

```python
inputs = input().split() #5 3 2 3 5 3 2 3 5 
print(inputs)#['5', '3', '2', '3', '5', '3', '2', '3', '5']
```

##### 4) `'separator'.join(iterable)`

- 특정한 문자열로 만들어 반환
- iterable(반복가능) 컨테이너의 요소들을 separator를 구분자로 합쳐(` join()`)문자열로 반환

```python
word = '배고파' #글자 iterable(순회가능)
words = ['안녕', 'hello']
'!'.join(word) #'배!고!파'
# 구분자를 한칸띄움으로 하겠다.
' '.join(words) #'안녕 hello'
```



#### 1.3 문자 변형

- `.capitalize()`: 앞글자를 대문자로 만들어 반환
- `.title()` : `'`'나 공백 이후를 대문자로 만들어 반환
- `.upper()` : 모두 대문자로 만들어 반환
- `.lower()` : 모두 소문자로 만들어 반환
-  `.swapcase()` : 대<->소문자로 변경하여 반환

-  기타 문자열 관련 검증 메소드 : 참/거짓 변환 -> 그때그때 구글링으로 찾기...ㅎㅎ

- `.isalpha()`: 문자열이 문자인지 아닌지를 True,False로 리턴

- `.isdecimal()`:주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수이기 때문에 특수문자 중 숫자모양을 숫자로 치지않는다.

- `.isdigit()`: 단일 글자가 '숫자' 모양으로 생겼으면 무조건 True를 반환하는 함수. 즉, 숫자처럼 생긴 '모든 글자'를 숫자로 친다.

- `.isnumeric()`:숫자값 표현에 해당하는 문자열까지 인정한다. 제곱근 및 분수, 거듭제곱 특수문자도 isnumeric() 함수는 True를 반환하는 것을 알 수 있다.

- `.isspace()`:문자열에 공백이 포함되어 있음 True 아니면 False

- `.isupper()`:모두 대문자라면 True 아니면 False

- `.istitle()`:모든 단어의 첫 문자열이 대문자이면 True 아니면 False

- `.islower()`:모두 소문자라면 True 아니면 False

### 2. 리스트(List)

- mutable(변경 가능)
- ordered(순서 있고)
- iterable(순회 가능)
- 원본 변경O => retrun None
- 원본 변경X => 변경된 Data Return 이런 경우가 많음

#### 2.1 값 추가 및 삭제

-  `.append(x)` 
  - 리스트에 값을 추가
  - 원본을 조작하고 return값이 없음 (return이 있고 없고는 매우 중요!!!)

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.append('banapresso')
print(cafe) #['starbucks', 'tomntoms', 'hollys', 'banapresso']
new_cafe=cafe.append('banapresso')
print(new_cafe) #None => 원본 변경이 아니라 변경된 Data Return
```

- `.extend(iterable)`
  - 리스트에 iterable(list, range, tuple, string) 값을 붙일 수 있음
  -  `.append(x)` 와 달리 iterable에 그냥 추가하고 싶은 것 넣으면 안됨 list라면 `[iterable]`이렇게 넣어줘야 됨

- `.insert(i,x)`
  - 정해진 위치 `i`에 값을 추가
  - 매우 유연, 리스트의 길이를 넘어서는 인덱스는 마지막에 아이템이 추가됨

```python
cafe.insert(len(cafe)+100, '!')
print(cafe) 
#['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'end', '!']
```

- `.remove(x)`
  - 리스트에서 값이 x인 것을 삭제
  - 원본 변경이면 return이 없는 경우가 많음
  - 값이 없으면 오류가 발생

```python
numbers = [1, 2, 3, 1, 2]
#중복된 값 1 삭제
numbers.remove(1)
print(numbers) #[2, 3, 1, 2] #한개만 삭제됨

numbers.remove(1)
print(numbers) #[2, 3, 2]
```

-  `.pop(i)`
  - 정해진 위치 `i`에 있는 값을 삭제, 그 항목을 반환
  - `i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줌
  - 값이 return된다는 것은 별도의 변수에 저장할 수 있다는 것

```python
a = [1, 2, 3, 4, 5, 6]
print(a.pop(0))#1
print(a)#[2, 3, 4, 5, 6]
```

-  `.clear()`
  - 리스트의 모든 항목을 삭제

```python
numbers = list(range(1, 10))
print(numbers) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.clear()
print(numbers)#[]
```



#### 2.2 탐색 및 정렬

- `.index(x)`
  - x값을 찾아 해당 index값을 반환
  - 없을 시 오류가 발생(ValueError)

```python
a = [1, 2, 3, 4, 5]
a.index(3) #2
a.index(100)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-19-1547ad15da79> in <module>
      2 # 앞서 remove 역시도 같은 에러가 발생하였습니다. (ValueError)
      3 # =====
----> 4 a.index(100)

ValueError: 100 is not in list
```

- `.count(x)`
  - 원하는 값의 개수를 확인

```python
#원하는 값을 모두 삭제하려면
a = [1, 2, 1, 3, 4]
target_value = 1
for i in range(a.count(target_value)):
    a.remove(target_value)
print(a) #[2, 3, 4]
```

- `.sort()`
  - 정렬을 함
  - 내장함수`sorted()`와 다르게 원본 list를 변형
  - None을 리턴
  - `sorted()`
    - 내장함수, return값이 있다.
    - 원본은 변화가 없다.

```python
import random
lotto = random.sample(range(1, 46), 6)
print(lotto) #[35, 45, 40, 33, 16, 8]
```

-  `.reverse()`
  - 반대로 뒤집기(정렬 아님)

```python
classroom = ['Tom', 'David', 'Justin']
classroom.reverse()
print(classroom) #['Justin', 'David', 'Tom']
```



#### 2.3 리스트 복사

```python
#mutable해서 같음
a = [1,2,3,4,5]
b = a
a[2] = 5
print(a) #[1,2,5,4,5]
print(b) #[1,2,5,4,5]

#잘 복사를 하려면!
a = [1,2,3,4,5]
b = a[:] #a의 처음부터끝까지 복사하겠다
#or b = list(a)
a[2] = 5
print(a) #[1,2,5,4,5]
print(b) #[1,2,3,4,5]
```

- 2차원 배열은 복사를 slicing으로 할 수 없음

```python
a=[1,2,3,4,[1,2,3]]
b=a[:]
```

- 이 경우라면 제일 뒤 [1,2,3]은 slicing으로 완전히 다른 list가 될수 없고 [1,2,3]은 연결돼있음

- 이해가 안되면 `python tutor`로 눈으로 확인



#### -  리스트 복사 방법

##### 1) `slice`연산자 사용 [`:`]

```python
a = [1, 2, 3]
b = a[:] #새로운값을 retrun/원본변경 아님

b[0] = 5 #b를 변경해도 a는 변경안됨
print(a) #[1, 2, 3]
```



##### 2) `list()`활용

```python
a = [1, 2, 3]
b = list(a)

b[0] = 5
print(a)
```

- BUT 1),2) 둘다 일부 상황에만 `서로 다른 얕은 복사(shallow copy)`이다.
- 2차원 배열 복사

``` python
a = [1, 2, [1, 2]]
b = a[:]

b[2][0] = 3
print(a) #python tutor를 통해 왜 이렇게 됐는지 그림으로 보여줌
#[1, 2, [3, 2]]
```

- 만일 중첩된 상황에서 복사를 하고 싶다면, `깊은 복사(deep copy)`를 해야함
- 내부에 있는 모든 객체까지 새롭게 값이 변경됨

```python
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)

b[2][0] = 3
print(a) #[1, 2, [1, 2]]
```



#### 2.4 List Comprehension

```python
[식 for 변수 in iterable if 조건식]

[식 if 조건식 else 식 for 변수 in iterable]

# elif 는 다음과 같이 사용해야 합니다. (if else 열거)
[식 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable]

```

- 짝수리스트
- 반복문 사용

```python
even_list = []
for number in range(1,11):
    if number % 2==0:
        even_list.append(number)
```



### 3. 데이터 구조에 적용가능한 Built-in Function

- 순회가능한(iterable) 데이터 구조에 적용가능
- list, dict, set, str, bytes, tuple, range

#### 1) `map(function, iterable)`

- 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 결과 돌려줌
- return은 `map_object`형태
- 입력값을 처리할 때 자주 활용

#### 2) `filter(function, iterable)`

- iterable에서 fuction의 반환된 결과가 `True`인 것들만 구성하여 반환
- `filter object`를 반환

#### 3) `zip(*iterables)`

- 복수의 iterable 객체를 모음
- 결과는 튜플의 모음으로 구성된 `zip object`를 반환

### 4. 세트(Set)

- mutable(변경가능)
- unordered(순서 없고)
- iterable(순회 가능한)

#### 4.1 추가 및 삭제

- `.add(elem)` :  elem을 세트에 추가를 함, 중복을 제거하고 return하는 값이 없다

- `.update(*others)` : 여러가지 값을 추가, 인자로는 반드시 iterable 데이터 구조를 전달

- `.remove(elem)` : elem을 세트에서 삭제하고, 없으면 KeyError가 발생

- `.discard(elem)` : elem을 세트에서 삭제하고 없어도 에러가 발생하지 않음

- `.pop()` : 임의의 원소를 제거해 반환

#### 4.2 딕셔너리(Dictionary)

- mutable
- unordered
- iterable
- `Key : Value`페어의 자료구조

##### 1) 조회

- `.get(key[, default])` 
  - key를 통해 value를 가져옴, 절대로 KeyError가 발생하지 않고, default는 기본적으로 None

##### 2) 추가 및 삭제

- `.update()`
  - 값을 제공하는 key, value로 덮어씀

##### 3) 딕셔너리 순회(반복문 활용)

- 딕셔너리에 `for`문을 실행

```python
# 0. dictionary 순회 (key 활용)
for key in dict:
    print(key)
    print(dict[key])


# 1. `.keys()` 활용
for key in dict.keys():
    print(key)
    print(dict[key])


# 2. `.values()` 활용    
for val in dict.values():
    print(val)


# 3. `.items()` 활용
for key, val in dict.items():
    print(key, val)
```

- `get(key[,default])`
  - key가 딕셔너리에 있는 경우 key에 대응하는 값을 돌려주고, 그렇지 않음 default돌려줌

##### 4) Dictionary comprehension

- `iterable`에서 `dict`를 생성할 수 있음

```python
{키: 값 for 요소 in iterable}

dict({키: 값 for 요소 in iterable})

# elif 는 다음과 같이 사용해야 합니다. (if else 열거)
{키: 값 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable}
```

