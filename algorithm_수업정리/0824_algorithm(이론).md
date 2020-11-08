# Algorithm

## 문자열

> - 문자열
> - 패턴 매칭
> - 문자열 암호화
> - 문자열 압축
> - 실습 1,2

- 컴퓨터에서의 (영)문자표현

  - 영어가 대소문자 합쳐서 52이므로 6(64가지)비트면 모두 표현 가능, 이를 코드체계라고 함
  - 네트워크가 발전하면서 서로간 정보를 주고받을 때 정보를 달리 해석한다는 문제 생김
  - 혼동을 피하기 위한 표준안, **ASCII**라는 문자 인코딩 표준이 제정됨
  - **7bit**(0~127)인코딩으로 128문자를 표현, 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어짐
  - \0 null문자
  - byte는 영문자 한자를 나타내는 단위 100byte=영문자 100자
  - parity bit : 에러체크 가능

  ![image-20200824102829944](0824_algorithm(이론).assets/image-20200824102829944.png)

- 확장 아스키 : 표준문자 이외, 악센트문자, 도형문자, 특수문자, 특수 기호 등 부가적인 문자 128개 추가할 수 있게 하는 부호
- 요즘 별로 안씀
- 확장아스키는 1B내의 8bit를 모두 사용함으로써 추가적인 문자 표현 가능
- 표준 아스키와 같이 서로 다른 프로그램이나 컴퓨터 사이에 교환되지 못함, 컴퓨터나 프린터가 그것을 해독할수 없어서 안 씀
- 오늘날 대부분의 컴퓨터는 ASCII형식 사용
- 다국어 처리를 위한 표준은 **유니코드**
- 유니코드도 다시 character set으로 분류됨
- 저장하는 변수의 크기를 정의, but 바이트 순서에 대해서 표준화하지 못함
- 파일 인식 시 이 파일이 UCS-2, UCS-4인지 인식하고 각 경우를 구분해서 모두 다르게 구현해야 하는 문제 발생
- 유니코드의 적당한 외부인코딩이 필요함(이런게 있다..정도...ㅎ)
- 파이썬 UTF-8, 자바 UTF-16

![image-20200824104912527](0824_algorithm(이론).assets/image-20200824104912527.png)

- 파이썬에서의 문자열 처리
  - char타입 없음
  - 텍스트 데이터의 취급방법이 통일됨
  - 문자열 기호(`',",''',"""`)
  - 연결(+) : 문자열 이어붙여줌
  - 반복(*) :  수만큼 문자열이 반복
  - 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
  - `replace(), split(), isalpha(), find()` 사용 가능
  - 튜플과 같이 요소값을 변경할 수 없음(**immutable**)
- C는 아스키코드로 저장
- java는 유니코드(UTF16,2byte)로 저장
- 파이썬은 유니코드(UTF8)로 저장

### 문자열 뒤집기

- 자기 문자열에서 뒤집는 방법이 있고, 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있음
- 자기 문자열을 이용할 경우 swap을 위한 임시변수가 필요, 반복 수행을 문자열 길이의 반만을 수행해야 함
- str은 immutable이기때문에 
  1.  str->list
  2. swap 
  3. list->str로 변환해야됨

```python
#회문, 반만(전체 len의 1/2) 비교
def str_rev(str): #매개변수 str과 아래의 지역변수 str은 다른 것
#str->list
	arr = list(str)
#swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
#list->str
	str = "".join(arr)
    return str
 #  ___________
str = 'algorithm'
str1 = str_rev(str)
print(str1)

#반복문
str1 = 'algorithm'
for i in range(len(str1)-1,-1,-1):
    print(str[i],end='')

#slicing 사용
s = 'algorithm'
s = s[::-1]
print(S)

#reversed내장함수
str3 = reversed(str)
print(''.joint(str3))
```

### `atoi` Vs `itoa`

- atoi

```python
str,int사용하지 않고!
#내장함수 사용안하고
#문자열을 int형으로 전환

#1.
def atoi(line):
    num = 0
    for i in range(len(line)):
        #아스키코드로 만든 문자를 10곱해서 1의자리에 다음 숫자를 넣어야되기 때문
        num *=10
        #문자를 아스키코드로 숫자로 만들건데 아스키코드를 보면 문자가 숫자 뒤에 있기 떄문에
        #0의 아스키코드번호를 빼주면 전환가능.....
        num +=ord(line([i]))-ord('0')
    return num
		

num = atoi('1234')
print(type(num),num)

#2.
def atoi(str):
    value = 0
    #2-1방법
    for i in range(len(str)):
        c = str[i]
        #0~9
        #if c>= '0' and c<='9':
        if '0' <= c <= '9': #파이썬이라 이렇게 적는거 가능
            digit = ord(c)- ord('0')
        else:
            break
        #이부분 중요
        value = vlaue *10 +digit
    return value
	#2-2방법
    #숫자로된 문자열 들어온다고 확신하면
    #if필요없고 그냥 value = value *10 +ord(c)- ord('0')이렇게 적으면 끝
    for i in range(len(str)):
        c = str[i]
    	value = value *10 + c
        
        ###숫자로된 문자열이라 치면 .....이거만적으면되나?위에껀 뭐야
        value = value *10 + ord(c)-ord('0') 
    return value
num = atoi('1234')
print(type(num),num)
```

- itoa
- str()함수를 사용하지 않고, 구현
  - 양의 정수를 입력 받아 문자열로 변환하는 함수
  - 입력값 : 변환할 정수 값, 변환된 문자열을 저장할 문자배열
  - 반환값 : 없음
  - 음수를 변환할 떄는 어떤 고려사항이 필요한가?
    - if를 이용해 `-`기호를 붙여라

```python
#1.
#int형을 문자열로 전환
def itoa(num):
    line = ''
    tmp = num
    while tmp >0:
        number = tmp % 10
        #0을 아스키코드값으로 바꾼 것을 더하면 지금 숫자의 아스키코드값을 알 수 있음
        #다음값을 이전 문자 앞에 더해줘도 되고, 다 만든 뒤 아까 배운 문자 뒤집기해도딤
        line = chr(number+ord('0')) + line
        tmp //= 10
    return line
line = itoa(1234)
print(type(line),line)


#2.
def itoa(num):
    x = num #몫
    y = 0 #나머지가 들어갈 변수
    arr = []
    #2-1방법
    while x: #x가 0이 아닌동안 반복문 돌림
        y = x % 10
        x = x//10 # x//=10
        arr.append(chr(y+ord('0'))) #나머지를 문자열로 넣기
    arr.reverse() #뒤집음
    str = ''.join(arr) #뒤집은걸 문자열로 바꿈
    return str
	
    #2-2방법
    while x: #x가 0이 아닌동안 반복문 돌림
        y = x % 10
        x = x//10 # x//=10
        arr.append(y)
    arr.reverse() #뒤집음
    return arr

x = 123
print(x,type(x))
str = itoa(x)
print(str,type(str))
```

- `atoi`, `itoa`를 같이 쓰는 문제들이 종종 나올때 함수를 만들어 놓고 쓰면 됨.....



### 문자열 비교

- `c strcmp()`함수를 제공함
- Java에서는 `equlas()`메소드를 제공
  - 문자열 비교에서는 `==`연산은 메모리 참조가 같은지를 묻는 것
- Python `==`연산자와 `is`연산자를 제공
  - `==`연산자는 내부적으로 특수 메서드 `__eq__()`를 호출

```python
# `==`를 사용하면 됨, 이런식으로 돌아간다는 것 알기.
def strcmp(s1,s2): 
    if len(s1) != len(s2):
        return False
    else:
        i = 0 #초기값(초기식)
        while i < len(s1) and i < len(s2): #조건식
            if s1[i] != s2[i]:
                return False
            i += 1 #증감식
    return True

a = 'abc'
b = 'abc'
print(strcmp(a,b)) #True, False 받을예정
```

- `eval(), repr()` ??알아야되는거..겠죵..



## 패턴 매칭

- **고지식한 패턴 검색 알고리즘**(구현 알기)
- 카빈-라빈 알고리즘(책에 없음)
- KMP 알고리즘(개념정도)
- 보이어-무어 알고리즘(개념정도)

### 고지식한 알고리즘(Brute Force)

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작

![image-20200824151926896](0824_algorithm(이론).assets/image-20200824151926896.png)

![image-20200824152024639](0824_algorithm(이론).assets/image-20200824152024639.png)

- 파이썬 코드로 구현
- while문

```python
p = 'is' #찾을패턴
t = 'This is a book~!' #전체 텍스트
M = len(p) #찾을 패턴의 길이
N = len(t) #전체 텍스트의 길이

def BruteForce(p,t):
    i = 0 #t의 인덱스
    j = 0 #p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]: #패턴이 다르면
            i = i-j #i를 shift이동
            j = -1 #j를 초기화
        i = i+1
        j = j+1
    if j==M : return i-M #검색성공
    else: return -1 #검색실패
print(BruteForce(text,pattern))
# find쓰면 한방에 끝남
print(text.find(pattern))
```

- 2중 for문

```python
str1 = 'A pattern matching algorithm'
str2 = 'rithm'

def BruteForce(str1,str2):
    A = len(str1)
    B = len(str2)

    for i in range(A-B+1): #A안에 B찾기(index설정)
        cnt = 0
        for j in range(B): #문자가 같은지 비교
            if str1[i+j] == str2[j]:
                cnt += 1
            else:
                break
        if cnt == B: #str2의 len과 일치하기 때문에 같은패턴 찾음
            print('여기부터 일치',i)
            return i
    return -1 #발견하지 못한다면 검색실패로 -1반환
tmp = BruteForce(str1,str2)
print(tmp)
```

- 시간복잡도

  - 최악의 경우 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(M*N)이 됨
  - 예에서는 최악의 경우 약 (10,000*80)번 비교가 일어남

  

### KMP 알고리즘(개념..정도만!)

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행

- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함

  - next[M] : 불일치가 발생했을 경우 이동할 다음 위치

- 시간복잡도 : O(M+N)

- 아이디어 설명

  - 텍스트에서 abcdabc까지는 매치되고, e에서 실패한 상황 패턴의 맨 앞의 abc와 실패 직전의 abc는 동일함을 이용할 수 있음
  - 실패한 텍스트 문자와 P[4]를 비교함

  ![image-20200824153121950](0824_algorithm(이론).assets/image-20200824153121950.png)
  - 매칭이 실패했을 때 돌아갈 곳을 계산함

  ![image-20200824153208141](0824_algorithm(이론).assets/image-20200824153208141.png)

  - abcdabcef위 숫자는 틀렸을 때 돌아갈 숫자 e에서 틀렸으니 3번으로 돌아가라!!
  - **전처리**란??
    - 전처리는 실제 패턴 매칭을 하기전에 어떤 정보를 계산해두는걸 말함
    - 실제 패턴매칭을 할 때 사용할 정보
    - 보통 KMP나 보이어무어 알고리즘들은 각각의 전처리방법이 존재
    - 전처리한 정보는 단순한 패턴매칭보다 효율적으로 하기 위해 필요한 정보
  - 고지식한 알고리즘은 실패하면 다시 처음부터 하지만 KMP알고리즘은 처음부터 시작하지 않음!!

  

### 보이어-무어 알고리즘(개념..정도만!!)

- 전체적인 흐름은 왼쪽에서 오른쪽이 맞지만 비교할 때, 오른쪽에서 왼쪽으로 비교!!
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 패턴에 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이 만큼이 됨

![image-20200824153909691](0824_algorithm(이론).assets/image-20200824153909691.png)

- 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재할 경우 위치를 맞추고 다시 검사해봄
- 만약 똑같은게 두개 있다면 뒤에 있는 문자로 맞춰줘서 다시 검사(최소한으로 띄우고 다시검사)

![image-20200824153954013](0824_algorithm(이론).assets/image-20200824153954013.png)

- 초록색 글자가 패턴안에 없으면 그 글자 수만큼 띄움, 계속 반복

![image-20200824154157157](0824_algorithm(이론).assets/image-20200824154157157.png)

- rithm 문자열의 skip 배열(숫자만큼 띄움)

|  m   |  h   |  t   |  i   |  r   | 다른 모든 문자 |
| :--: | :--: | :--: | :--: | :--: | :------------: |
|  5   |  1   |  2   |  3   |  4   |       5        |



### 문자열 매칭 알고리즘 비교

- 찾고자 하는 문자열 패턴의 길이m, 총 문자열 길이n
- 고지식한 패턴 검색 알고리즘 : 수행시간 `O(mn)`
- 카프-라빈 알고리즘 : 수행시간 `O(n)`
- KMP 알고리즘 : 수행시간 `O(n)`
- 보이어-알고리즘
  - 앞의 두 매칭 알고리즘들의 공통점 텍스트 문자열의 문자를 적어도 한번씩 훑는다, 최선의 경우에도 `오메가(n)`->#이거뭐야???
  - 보이어-무어 알고리즘은 **텍스트 문자를 다 보지 않아도 됨**
  - 발상의 전환 : 패턴의 오른쪽부터 비교
  - 최악의 경우 수행시간 :`O(mn)`
  - 입력에 따라 다르지만  일반적으로 `O(n)`보다 시간이 덜듬



### (참고)문자열 암호화..별로 안중요하다고 하셨당...!

- 시저 암호
- bit열의 암호화
  - 배타적 논리합 연산 사용
  - `XOR` : exclusive-or
  - 다르면 `1`, 같으면 `0`을 반환