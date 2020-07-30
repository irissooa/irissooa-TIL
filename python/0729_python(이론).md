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
  - `< 클래스 이름>`은 `PascalCase`로 정의(PascalCase = 시작 중간 대문자로 표시한다는 말)
  - 클래스 내부에는 데이터와 함수를 정의할 수 있고, 메스드(method)로 불림
  - 하나의 탑입을 만들 때 사용

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
#
class Person:
    """
    이것은 Person 클래스(class)입니다.
    """
```

```python
person1 = Person() 
person2 = Person()
print(type(person1)) #class는 새로운 type이기 때문에 Person type이 나옴
print(type(person2))
print(person1.__doc__) #doc는 document의 줄임말 Person에 정의한 말이 나옴(보통 설명 적어놓음)
print(person2.__doc__)
#random도 파이썬이 class로 만들어 놓고 doc로 자세하게 어떤 것인지 설명해 놓음

#출력
<class '__main__.Person'>
<class '__main__.Person'>

    이것은 Person 클래스(class)입니다.
    

    이것은 Person 클래스(class)입니다.
    
```

- 메서드 정의
  - 특정 데이터 타입(클래스)의 객체에 공통적으로 적용 가능한 행위들을 의미

```python
class Person:
    # 메서드(method)
    def talk(self):    # **인자로 self를 붙여줍니다.(중요)
        return '안녕'
```

```python
p1 = Person() 
p1.talk() #객체.메서드() 객체는 목적어 메서드는 행위// P1에 talk()를 해라 
#호출되는 시점에 없어도 왜 돌아가지? (self) 일단 이렇게 쓴다고 알고 넘어감

#'안녕'
```

- 생성자 메서드
  - 인스턴스 객체가 생성될 때 호출되는 함수

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```

- 소멸자 메서드
  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 함수

```python
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```

```python
class Person:
    def __init__(self): #호출되면 자동으로 나옴
        print('응애!')
        
    def __del__(self):
        print('갈게..')
        
p1 = Person()
p1 = 'hello' # 이러면 p1 객체가 사라지는 것과 같음
#파이썬 내부 청소부 garbage collector가 있는데 p1이 다른걸 할당하면 이전의 p1을 del함
#응애!
#갈게..
```





- 속성 정의
  - 특정 데이터 타입(클래스)의 객체들이 가지게 될 상태/데이터 의미

```python
class Person:
    def __init__(self, name): #name 위치인자를 추가함 
        self.name = name #self는 객체 스스로임 self.name은 객체의 name이고, =name은 인자임 다른거다.
        
    def talk(self):
        return f'안녕, 나는 {self.name}'

me = Person('홍길동') #'홍길동'이 없으면 name이라고 하는 위치인자가 없어서 오류가 뜸
print(me.name) #이 객체는 '홍길동'이라는 이름을 가짐
```



#### <매직메서드>

- 더블인더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드
- `__init__` (self)
  - 생성자
  - 클래스 생성시 초기화 작업을 위한 메서드
  - 인스턴스 객체가 생성될 때 자동으로 호출
  - 인스턴스 객체 생성시 초기화할 멤버 변수 값을 전달 할 수 있음
- `__del__` (self)
  - 소멸자
  - 메모리 해제등의 종료 작업을 위한 메서드
  - 인스턴스 객체의 참조 카운터가 0이 될 때 호출
  - 명시적으로 del구문을 사용한다고 클래스 객체의 소멸자 함수가 항상 호출 되는 것은 아님
  - 인스턴스 객체를 생성한 이후 참조 카운터가 1이상 존재한다면 del구문을 사용하여도 소멸자는 호출 되지 않음

- `__str__` (self)
  - 문자열 표현 반환
  - 객체에서 `print()` 또는 `str()` 함수가 호출될 때 호출됨
  - 이 메소드는 string 객체를 반환해야 함
- `__repr__` (self)
  - tuple, dictioary, string 등과 같은 유효한 파이썬 표현식
  - 이 메소드는 `repr()`객체에서 함수가 호출될 때 호출
  - 문자열을 반환해야 됨 그렇지 않으면 오류 발생
- `self` : 인스턴스 자신
  - 호출 시 첫번째 인자로 인스턴스 자신이 전달됨
  - 보통 매개변수명으로 첫번째 인자로 설정



### 3.5 인스턴스 변수

- 인스턴스의 속성
- 각 인스턴스들의 고유한 변수(데이터)
- 메서드 정의에서 `self.변수명` 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당

```python
class Person:

    def __init__(self, name):    # 인스턴스 메서드 (생성자) 
        self.name = name         # 인스턴스 변수
```

#### 3.6 클래스 변수

- 클래스의 속성
- 해당 클래스의 모든 인스턴스가 공유
- 클래스 정의 내부에서 선언
- `클래스.변수명` 또는 `인스턴스.변수명`으로 접근(할당)

```python
#
class Person:
    species = 'human' #class 변수 // species는 john eric 둘다 조회하면 human이 나옴/ 클래스변수 클래스가 가지면서 모두 같은 값을 가짐
    
    def __init__(self, name): #instance변수
        self.name = name
        
#class는 독자적인 이름공간을 만듬, 중2병 히키코모리 막내동생방/ 밖에서는 안에들어갈수 없고 안의 데이터는 밖의 데이터를 조회할 수 있다.
#global에서 species하면 조회가 불가능하고, class이름인 Person.species라고 하면 조회가 가능해짐
print(Person.species)
Person.talk()#Person공간 안의 talk를 부른 것과 동일함
```

### 3.7 인스턴스 & 클래스간의 이름공간

##### 1) 이름 탐색 순서

- 인스턴스와 클래스 모두에서 같은 속성 이름이 등장하면, 속성 조회는 인스턴스를 우선

```python
class Person:
    name = '홍길동' # 이경우 instance가 .name을 했을 때 어떤 name을 가져올까// p1.name을 했을 때 p1이 이름이 없다면 홍길동이 나오고 이름이 있다면 Gildong가 나옴

    def __init__(self, name='Gildong'):
        self.name = name
    
    def talk(self):
        return f'안녕, 나는 {self.name}'
```

##### 2) 이름 공간 원칙

- 인스턴스에서 변수의 이름을 조회할 수 없다면, 클래스 객체의 데이터 조회
- 인스턴스=>클래스(=>상위 클래스) 순 탐색

### 3.8 인스턴스&클래스 메서드(+스태틱 메서드)

##### 1) 인스턴스 메서드

- 인스턴스가 사용할 메서드
- 클래스 내부에서 정의되는 메서드의 기본값은 인스턴스 메서드
- 호출시, 첫번째 인자로 인스턴스 자기자신 `self` 전달됨
- 인스턴스는, 3가지 종류의 메서드 모두에 접근할 수 있다.
- 하지만 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않아야 한다. (가능하다 != 사용한다)
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계한다.

##### 2) 클래스 메서드

- 클래스가 사용할 메서드
- `@classmethod`를 위에 쓰고 정의
- 호출시, 첫번째 인자로 클래스 `cls`가 전달됨
- 클래스 또한 3가지 종류의 메서드 모두에 접근할 수 있다.
- 하지만 클래스에서 인스턴스 메서드는 호출하지 않는다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계한다. (클래스 메서드와 정적 메서드)
  - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 **클래스 메서드**로 정의한다.
  - 클래스와 클래스 속성에 접근할 필요가 없다면 **정적 메서드**로 정의한다.
  - 클래스 메서드와 정적 메서드는 인스턴스 없이 호출할 수 있다는 점은 같다.
  - 하지만 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용하며 그렇지 않을 경우 정적 메서드를 사용한다.

```python
class Puppy:
    population = 0 #클래스변수
    
    def __init__(self, name, breed): # 인스턴스메서드
        self.name = name #인스턴스변수
        self.breed = breed
        Puppy.population += 1 #클래스변수
        
    def __del__(self):
        Puppy.population -= 1 #클래스변수
    
    def bark(self):
        return f'왈왈! 나는{self.name}, {self.breed}(이)야' #self붙은건 모두 인스턴스변수
    
    @classmethod #클래스메서드
    def get_population(cls):#cls는 self와 같이 클래스메서드에서 변수로 쓰임, 꼭 이거 아니어도 되지만 보통 cls라 씀
        return f'현재 강아지 마리수: {cls.population}'
     
	@staticmethod  #클래스와 인스텐스에 벗어남
    def info():
        return '이것은 Puppy 클래스입니다!'
```

##### 3) 스태틱 메서드

- 클래스가 사용할 메서드
- `@staticmethod`를 위에 적어 사용
- 호출시, 어떠한 인자도 전달되지 않음

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2, ...):
```



### 3.10 상속

- 클래스에서 가장 큰 특징
- 부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높아짐
- 코드를 중복하여 정의하지 않을 수 있음
- 공통된 속성이나 메서드를 부모 클래스에 정의하고 상속하면서 적은 코드로 다양한 형태 객체를 만들 수 있음
- 상속관계에서 이름공간
  - 기존의 `인스턴스->클래스` 순 // `인스턴스->자식클래스->부모클래스->전역`

```python
class ChildClass(ParentClass):
    <code block>
```

- `super()`
  - 자식클래스 메서드를 추가로 구현
  - 부모 클래스의 내용을 사용하고자 할때

```python
class ChildClass(ParentClass):
    def method(self, arg):
        super().method(arg) 
        
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id

#위 Student class를 아래처럼 변경 가능
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # Person()
        super().__init__(name, age, number, email) 
        #person에 생성자함수를 실행한 것과 같은 효과(중복해서 적을 필요없음)
        self.student_id = student_id
```

### 3.11 메서드 오버라이딩

- Method Overriding(메서드 재정의): 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것
- 상속 받은 클래스에서 같은 이름의 메서드로 덮어씀

### 3.12 다중 상속

- 두개 이상의 클래스를 상속받는 경우

```python
class Person:
    def __init__(self, name): #firstchild의 클래스에 생성자함수는가 없어서 상위 클래스에 있는 생성자함수를 따르는데 name을 지정해줘야됨
        self.name = name
    
    
    def breath(self):
        return '날숨'
    
    
    def greeting(self):
        return f'hi, {self.name}'
```

```python
class FirstChild(Dad, Mom):  # 상속의 순서가 중요합니다.(왼쪽에서 오른쪽). gene은 Dad의 gene값을 가져오게 됩니다.
    def swim(self):  # Mom의 swim 메서드를 overriding 합니다.
        return '챱챱'
    
    
    def cry(self):  # Child 만이 가지는 인스턴스 메서드 입니다.
        return '응애'
```

