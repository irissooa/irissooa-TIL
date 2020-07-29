# Python(2020-07-29)

> 모듈

- 모듈 : 특정 기능을 `.py` 파일 단위로 작성
- 패키지 : 특정 기능과 관련된 여러 모듈들의 집합 패키지 안에는 또 다른 서브 패키지를 포함 할수도 있음
- 파이썬 표준 라이브러리 : 파이썬에서 기본적으로 설치된 모듈과 내장함수를 묶어서 파이썬 표준 라이브러리(Python Standard Library, PSL)라 불림
- 패키지 관리자(pip) : `PyPl`에 저장된 외부 패키지들을 설치하도록 도움

## 1. 모듈(Module)

```python
import module
from module import var, function, Class
from module import *
```



- 특정 기능을 하는 코드를 담고 있는 파일
- 모듈 생성(ex `check.py`) 후 활용

### 1.1 모듈 활용

- `import`

  - 모듈을 활용하기 위해서 반드시 `import`문으로 내장 모듈을 이름 공간으로 가져와야 함

  ```python
  import check
  ```

  - 함수를 자주 사용할거라면, 변수에 할당해서 사용할 수 있음

  ```python
  check_odd = check.check_odd
  ```

## 2. 패키지(Package)

```python
from package import module
from package.module import var, function, Class
```



- 패키지는 점(`.`)으로 구분된 모듈 이름 (`package.module`)을 써서 모듈을 구조화하는 방법
- 패키지 생성 -> 폴더구조 생성

```sh
my_package/
    __init__.py
    math/
        __init__.py
        tools.py  
    statistics/
        __init__.py
        tools.py
```

- 모듈 이름 `my_package.math`는 `my_package`라는 이름의 패키지에 있는 `math`라는 이름의 하위 패키지를 가리킴
- `__init__.py`
  - 이 파일은 비워둠

- `tool.py`에 `standard_deviation()`함수를 넣음

```python
import math # math를 불러와야됨
def standard_deviation(values):
    mean = sum(values) / len(values)
    sum_var = sum(pow(value - mean, 2) for value in values) / len(values)
    std_dev = math.sqrt(sum_var)
    return std_dev
```

### 2.1 패키지 활용

- `from`패키지 `import`모듈
  - `import`는 `from`과 함께 사용

```python
from my_package.statistics import tools
dir(tools)#내가 안에 뭐를 넣어놨는지 볼 수 있다.
type(tools.standard_deviation) #function 호출할 수 있는지 확인(혹시 모를때)
tools.standard_deviation([1,2,3,4,5])
```

- `from`패키지.모듈 `import` 데이터
  - 특정한 함수 혹은 어트리뷰트만 활용하고 싶을 때

```python
#from 패키지.하위패키지 import 모듈
from my_package.statisics.tools import standard_diviation
standard_diviation([1,2,3,4,5])
```

- `from` 모듈 `import *`
  - 해당하는 모듈 내의 모든 변수, 함수, 클래스 가져옴

```python
#*은 모두를 가져옴
from my_package.math.tools improt *
print(e)
print(pi)
```

- `from` 모듈 `import` 데이터 `as` 별명
  - 내가 지정하는 이름을 붙여 가져옴

```python
#as뒤에 함수의 별명을 붙여줌
from my_package.statistics.tools import standard_deviation as sd
sd([1,2,3,4,5])
```



## 3. OOP

- 객체(Object)
- 객체지향프로그래밍(Object Oriented Programming)

- Class 와 객체

### 3.1 객체(Object)

- Python에서 모든 것은 객체
- 모든 객체는 type, 속성(attribute), 조작법(method)을 가짐
  - type : 어떤 연산자(operator)와 조작(method)이 가능한가
  - attribute  : 어떤 상태(데이터)를 가지는가
  - method : 어떤 행위(함수)를 할 수 있는가

#### 1) Type과 Instance

- Type : 공통된 속성과 조작법을 가진 객체들의 분류
- 파이썬에서 모든 것은 객체이고, 모든 객체는 특정 타입의 instance이다.
- Instance : 특정 타입의 실제 데이터 예시

```python
#isinstance(데이터, 타입)
a=5
isinstance(a,int) #True
```



| type |        instance        |
| :--: | :--------------------: |
| int  |         0,1,2          |
| str  | `''`,`'hello'`,`'123'` |
| list |     [], ['a','b']      |
| dict | {}, {'key' : 'value'}  |

### 3.2 속성(Attribute)과 메서드(Method)

- 객체의 속성(상태, 데이터)과 조작법(함수) 구분

| type    | attributes       | methods                               |
| ------- | ---------------- | ------------------------------------- |
| complex | `.real`, `.imag` |                                       |
| str     | -                | `.capitalize()`,`.join()`, `.split()` |
| list    | -                | `.append()`, `.reverse()`, `.sort()`  |
| dict    | -                | `.keys()`, `.values()`, `.items()`    |

- 속성은 객체의 상태/데이터를 뜻함

```python
#<객체>.<속성>
(3+4j).real #3
```

- 메서드는 특정 객체에 적용할 수 있는 행위를 뜻함

```python
#<객체>.<조작법>()
[3,2,1].sort() #.sort()는 None이 리턴되기 때문에 할당해야됨
a = [3,2,1]
a.sort()
print(a) #[1,2,3]
```



### 3.3 객체 지향 프로그래밍(Object-Oriented Programming)

- Object가 중심이 되는 프로그래밍
- 컴퓨터 프로그래밍의 패러다임의 하나
- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 '객체'들의 모임으로 파악하고자 하는 것
- 절차중심 VS Object중심 => 어떻게 프로그램을 정돈(organize)할 것인가
- Object중심 장점
  - 코드의 직관성
  - 활용의 용이성
  - 변경의 유연성

### 3.4 클래스와 객체

- type : 공통 속성을 가진 객체들의 분류(class)

- class : 객체들의 분류(class)를 정의할 때 쓰이는 키워드, type을 만드는 type
- class 생성 

```python
class ClassName:
    methods
```

- 인스턴스 생성
  - 정의된 클래스에 속하는 객체를 해당 클래스의 instance라고 함
  - person1은 사용자가 정의한 `Person`이라는 데이터타입의 인스턴스

```python
# 인스턴스 = 클래스()
person1 = Person()
```

- 메서드 정의
  - 특정 데이터 타입(클래스)의 객체에 공통적으로 적용 가능한 행위들을 의미

```python
class Person:
    # 메서드(method)
    def talk(self):    # 인자로 self를 붙여줍니다.
        return '안녕'
```

