# Algorithm

> - 스택
> - **재귀호출**
> - Memorization
> - DP(동적프로그래밍)
> - **DFS**

![image-20200826125001437](0826_algorithm(이론).assets/image-20200826125001437.png)

1. CODE 

- 프로그램의 소스코드가 저장된다. 

2.  

   1) DATA

   - 전역변수(global), 정적변수(static), 배열(array), 구조체(structure) 등이 저장됨
   - 초기화 된 데이터는 data 영역에 저장

   2) BSS

   - 초기화 되지 않은 데이터는 BSS (Block Stated Symbol) 영역에 저장

3. HEAP 

- 크기가 가변
-  프로그래머의 필요에 따라 할당하여 사용
- 위에서 부터 채워져 내려옴.

4. STACK

- 크기가 가변
- 지역변수가 저장
- 스택에는 여러개의 스택 프레임이 존재
- 데이터 용량의 불확실성을 가지므로 밑에서부터 채워 올림
- 커널영역을 침범하지 않게 하기위해 밑에서부터 채워 올림
- HEAP과 STACK이 서로 반대로 채워 나가기 떄문에 서로의 영역을 침범할 수 있음. (이를 악용해 공격도 가능하다)

출처: https://phaphaya.tistory.com/24 [pAPaYA]



## 스택

- 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형구조를 가짐
  - 선형구조 : 자료간의 관계가 1대1의 관계를 가짐
  - 비선형구조 : 자료 간의 관계가 1대 N의 관계를 가짐(ex.트리)
  - Graph : 모든 방법을 순회, N대 N의 관계를 가짐
- 스택에 자료를 삽입하거나 꺼낼 수 있음
- `후입선출(Last-In-First-Out)`마지막에 삽입한 자료를 가장 먼저 꺼냄
  - ex. 1,2,3 순으로 자료 삽입후 역순 3,2,1으로 꺼냄
  - **Stack과 Queue의 차이** : Queue = First-In-First-Out 선입선출 방식
- 2차원배열 + for문 많은 연습 필요........ㅎ 코딩을 많이 해봐야된다....!

### 스택의 구현

- 자료구조 : 자료를 선형으로 저장할 저장소
  - C언어에서는 배열을 사용할 수 있음
  - 저장소 자체를 스택이라 부름
  - 스택에서 마지막 삽입된 원소의 위치를 `top`이라 부름
- 연산
  - 삽입(`push`) : 저장소에 자료를 저장
  - 삭제(`pop`): 저장소에서 자료를 꺼냄, 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄
  - `isEmpty`: 스택이 공백인지 아닌지 확인, `pop`을 할 때 항상 봐야됨!, 주의해라!
  - `peek` : 스택의 `top`에 있는 `item`(원소)을 반환
- 빈 스택에 있는 원소 A,B,C를 차례로 삽입 후 한번 삭제하는 연산과정

![image-20200826100127729](0826_algorithm(이론).assets/image-20200826100127729.png)

- `push` : top을 먼저 증가(+1)시켜줌, 배열에 그자리에 값을 넣어줌
- `pop` : 맨 꼭대기에 있는 top을 먼저 빼내고 top를 하나 줄임(-1)



- 오류 왜 남? python은 기본적으로 stack이나 top이 전역변수 => `global top`적어줘야됨!!
  - `top` :  값 형 (read만 됨) -> 수정하게 하고싶으면 `global`을 꼭 써줘야 됨
  - `stack` : 참조형(read, write 다 됨)

```python
# C style
def push(item):
    #global top
    if top>100 -1:
        return
    else:
        top += 1
        stack[top] = item


def pop(): #isEmpty 인지 항상 확인해야됨!
    #global top
    if top== -1:
        print('Stck is Empty!!')
        return
    else:
        result = stack[top]
        top -= 1
        return result


stack = [0] * 100 #고정(꽉차지 않고 넉넉하게 만들어야됨)
top = -1
push(1)
push(2)
push(3)
print(pop()) #3
print(pop()) #2
print(pop()) #1

# UnboundLocalError: local variable 'top' referenced before assignment
```

- 파이썬 `push`

```python
#스택의 push 알고리즘
#Append 메소드를 통해 리스트의 마지막에 데이터 삽입
def push(item):
    s. append(item)
```

- `pop` : 가장 뒤에있는것 꺼냄`(-1)` , `()`이렇게 내도 마지막꺼 꺼냄

```python
#스택의 pop알고리즘
def pop():
    if len(S) == 0:
        #uderflow
        return
    else:
        return s.pop(-1)
```

```python
# Python style
stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0: #항상 스택이 비어있는지 확인! 이게 isEmpty임
        print('Stack is empty!!')
    else:
        return stack.pop()

push(1)
push(2)
push(3)
print(pop()) #3
print(pop()) #2
print(pop()) #1
print(pop()) #Stack is empty!!
```

- 아래처럼 함수 안 만들어도 됨

```python
stack = []

stack.append(1) #push
stack.append(2)
stack.append(3)

if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())
if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())
if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())
if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())
    
'''
3
2
1
'''
```

### 스택 구현 고려사항

> BUT 이건 다른 언어 내용! 파이썬은 관계 없음!

- 1차원 배열을 사용하여 구현할 경우 구현이 용이
- 스택의 크기를 변경하기 어렵다
  - 다른 언어에서는 `isFull`인지 확인해야됨, 스택 크기가 정해져 있기 때문
- 저장소를 동적으로 할당하여 스택을 구현하면 단점을 보완할 수 있다
  - 동적 연결리스트를 이용하여 구현하는 방법을 의미함
  - 구현이 복잡하지만 메모리를 효율적으로 사용한다는 장점을 가짐



#### 스택응용 : 괄호 검사(SWEA_1218풀어보기..!)

- 괄호의 종류 : 대괄호, 중괄호, 소괄호가 있음
- 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야함
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야함
- 괄호 사이에는 포함 관계만 존재함
- ex. 잘못된 괄호사용 `(a(b)), (a(b)c), a{b(c[d]e)f}`
- 같은 괄호, 왼쪽 괄호를 만나면 push, 오른쪽 괄호를 만나면 pop

![image-20200826104217750](0826_algorithm(이론).assets/image-20200826104217750.png)

- 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 `push`하고,
- 오른쪽 괄호를 만나면 `pop` 후 오른쪽 괄호와 짝이 맞는지 확인
- pop하려고 하는데 스택이 비어있다면 개수가 맞지 않음!
- 괄호의 짝이 맞지 않으면 짝이 맞지 않은것
- 마지막 괄호까지도 조사 한 후 에도 스택에 괄호가 남아있으면 개수가 안맞는 것!

```python
def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(': #왼쪽괄호면 push
            stack.append(arr[i])
        elif arr[i] == ')': #오른쪽괄호면 pop, 비교해야됨(두개밖에없으니 안 해도됨)
            #stack이 비었는지 확인
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack :return False #다 끝났는데 비어있지 않으면 false
    else: return True


stack = []
arr1 = '()()((()))'
arr2 = '((()((((()()((()())((())))))'
print(check(arr1))
print(check(arr2))
'''
True
False
'''
```

- 괄호가 대괄호, 중괄호, 소괄호 모두 있을 경우
  - 인자로 넘어온 괄호들을 순회하면서 검사
  - 여는 괄호라면 무조건 push
  - 닫는 괄호라면 스택에 top위치와 비교하여 짝이면 pop
  - 짝이 아니라면 False
  - 끝까지 순회했을 떄 스택의 길이가 0이 아니라면 False

```python
def check2(arr):
    
    stack = []

    for i in range(len(arr)):
        if arr[i] == '[' or arr[i] == '{' or arr[i] == '(': #왼쪽괄호면 push
            stack.append(arr[i])
        elif arr[i] == ']' or arr[i] == '}' or arr[i] == ')': #오른쪽괄호면 pop, 비교
            #stack이 비었는지 확인
            if len(stack) == 0:
                return False
            else:
                top = stack.pop() #top에 추출한 닫는괄호를 저장 후 짝이 맞는지 확인
            if arr[i] == ')' and top == '(':
                continue
            elif arr[i] == '}' and top == '{':
                continue
            elif arr[i] == ']' and top == '[':
                continue
            return False
    if len(stack) > 0: #남아있는 stack이 있다면, 짝이 맞지 않는 것!
        return False
    return True
arr3 = '{()}{[]}'
arr4 = '([)](())'
arr5 = '(][())'
print(check2(arr3))
print(check2(arr4))
print(check2(arr5))
'''
True
False
False
'''
```



#### 스택응용 : Function call

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
- 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 `후입선출 구조`
- 함수의 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입
- 함수의 실행이 끝나면 스택의 top원소를 삭제하면서 프레임이 저장되어 있던 복귀주소를 확인하고 복귀
- 함수호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백스택이 됨

![image-20200826105553109](0826_algorithm(이론).assets/image-20200826105553109.png)

- 시스템스택 예시

1. main()함수 실행 시작
2. F_1() 함수 호출
3. 호출된 함수 F_1() 실행
4. F_2() 함수 호출
5. 호출된 함수 F_2() 함수 실행
6. F_2() 함수 실행 종료, F_1() 함수로 복귀
7. F_1() 함수로 복귀하여 F_1() 함수의 나머지 부분 실행
8. main()함수 실행 완료(전체 프로그램 실행 완료) -> 스택 프레임도 삭제

출처: https://throwexception.tistory.com/294?category=870842 [집밖은 위험해 OTL]

```python
def func2():
    print('함수 2 시작')
    print('함수 2 종료')
def func1():
    print('함수 1 시작')
    func2()
    print('함수1 종료')

print('메인시작')
func1()
print('메인끝')

'''
메인시작
함수 1 시작
함수 2 시작
함수 2 종료
함수1 종료
메인끝
'''
```



##### 재귀호출 : 팩토리얼

- 자기 자신을 호출하여 순환 수행
- 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성

![image-20200826110007812](0826_algorithm(이론).assets/image-20200826110007812.png)

```python
def fact(n): # f(n) = n * f(n-1)
    if n == 1: #basic
        return 1
    else: #inductive(유도)
        return n * fact(n-1)

print(fact(4))
```

- 위 코드 디버깅을 해보자
- 파이참에서 왼쪽하단의 `Frame`이 stack이다

![image-20200826134113643](0826_algorithm(이론).assets/image-20200826134113643.png)



##### 재귀호출 : 피보나치

- 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열
  - F0 = 0, F1 = 1
  - Fi = F(i-1) + F(i-2) for i >=2
- 구현

```python
def fibo(n):
    if n < 2: #basic 기본파트
        return n
    else: #inductive 유도파트
        return fibo(n-1) + fibo(n-2)
    
print(fibo(8))
```

- **문제점이 있다**
- 엄청난 `중복 호출`이 존재한다는 것!!
- 컴퓨터가 힘들어함......수많은 overflow가 존재해서 시간이 많이 걸림....
- 재귀가 어떻게 돌아가는지 그릴 수 있어야 됨 : 상태 공간 트리 or Call Tree라고 함
- 재귀식은 디버깅하기 힘들어짐!! 아래와 같이 복잡하기 때문. 만든 자신을 믿어랏.....ㅎ!

![image-20200826111400323](0826_algorithm(이론).assets/image-20200826111400323.png)



**Memoization**(메모이제이션, '리'아님)

- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 동적 계획법의 핵심
- '메모리에 넣기' 라는 의미
- 위의 피보나치 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면, 실행시간을 `O(n)`으로 줄일 수 있음

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화 함
# memo[0]을 0으로 memo[1]는 1로 초기화 함

def fibo2(n):
    # global memo 안적어도 됨!!
    if n >= 2 and len(memo) <= n: 
        memo.append(fibo2(n-1)+fibo2(n-2))
    return memo[n]

memo = [0,1] #참조형, read, write 다 됨
#참고) ans = 0 값 형은 read밖에 안됨, global 써야됨
print(fibo2(7))
'''
memo: <class 'list'>: [0,1,1,2,3,,,,]
'''
```

- global memo : 꼭써야되나요? 
  - 안써도됨!! 
  - why? memo가 전역변수인데 참조형이다
- len(memo)는 list가 구해졌나 아닌가를 확인하는 것, 계산되어 있으니 확인 안해도  된다는 것을 알려줌
- 최초에 호출이 될 때 값을 구하고 이후부턴 memo에 저장된 값을 가져오면서 실행시간을 `O(2^n)->O(n)`으로 줄일 수 있음
- 1000번 돌리면 `RecursionError: maximum recursion depth exceeded in comparison` 너무 많이 돌렸다고함... 더 좋은 방법이 뭐가 있을까? `DP`

```python
N = int(input())
#내가 구하고 싶은 N까지 메모를 선언
memo = [-1] * (N+1)
#초기 2개의 값은 미리 초기화
memo[0] = 0
memo[1] = 1

def fibo(N):
    #-1이라는 말은 아직 값이 구해지지 않음이란 뜻,fibo를 구해서 저장시킴
    if memo[N] == -1:
        memo[N] = fibo(N-1) + fibo(N-2)
    #위에걸리지 않으면 구한 값을 바로 리턴
    return memo[N]

print(fibo(N))
```



##### global

```python
def func():
    #값형은 global ans를 적지 않으면 그대로 print(ans)하면 0이 출력됨
    #global ans를 적으면 1이 출력됨
    ans = 1
    # global memo는 참조형이기 때문에 global 적지 않아도 수정가능하지만
    #memo = [1,2,3,4,5] 이렇게 할당을 해버리면 출력을 해도 [1,2,3,4]가 나옴, 이건 global memo를 적어줘야됨
    memo[2] = 10 #이런식으로 적혀있다면 global memo를 적지않아도 수정가능.
ans = 0
memo=[1,2,3,4]
func()

print(ans)
```





## DP(Dynamic Programming)

> DP 대신 백트래킹[완전검색(재귀) + 가지치기]으로도 풀 수 있음
>
> DP의 핵심 기술  :  위에 적힌, **memoization(메모이제이션)**

- 동적계획 알고리즘
- 최적화 문제(결정문제)를 해결하는 알고리즘
- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

### 피보나치 수 DP적용

- 부분문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어짐

1. 문제를 부분 문제로 분할
   - Fibonacci(n)함수는 Fibonacci(n-1)과 Fibonacci(n-2)의 합
   - Fibonacci(n-1)은 Fibonacci(n-2)와 Fibonacci(n-3)의 합....등등
   - Fibonacci(n)은 Fibonacci(n-1),Fibonacci(n-2),,,,Fibonacci(0)의 부분집합으로 나뉨
2. 부분 문제로 나누는 일이 끝나면 가장 작은 부분 문제부터 해를 구함
3. 결과를 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구함

![image-20200826144009042](0826_algorithm(이론).assets/image-20200826144009042.png)

```python
#1.함수 만듦
def fibo3(n):
    f = [0,1] #memo 테이블
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
print(fibo3(7))

#2. 함수 만들지 않고,
f = [0,1]
for i in range(2, 7+1):
    f.append(f[i-1]+f[i-2])
print(f[7])
```

- DP는 1000번(f[1000]) 나옴
- DP의 구현방식
  - recursive(재귀) 방식 :`fibo2()`->메모이제이션에 적혀져 있음
  - iterative 방식:` fibo3()` -> 바로 위 코드
- memorization을 재귀적 구조에서 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능면에서 보다 효율적
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문



## 비선형구조

- **비선형구조**인 그래프 구조, 트리(그래프안에 트리 포함)는 그래프로 `표현(메모리저장)`된 모든 자료를 `빠짐없이 검색(순회)`하는 것이 중요
- 표현
  - 인접행렬
  - 인접리스트
  - 간선배열
- 순회
  - **DFS**(Depth First Search) : 깊이 우선 탐색(**제일중요!!**)
    - 정점의 자식들을 먼저 탐색하는 방식
    - ex. 피보나치(call tree)
    - 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순회함
    - ex. 아래 그림 A - B - D - E - F - C - G - H - I - J
  - **BFS**(Breadth First Search) : 너비 우선 탐색
    - 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식
    - 한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 순회함
    - ex. 아래 그림 A - B - C - D - G - H - I - E - F - J

![image-20200826152039396](0826_algorithm(이론).assets/image-20200826152039396.png)

- 방법
  1. 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색 
  2. 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아옴
  3. 다른 방향의 정점으로 탐색을 계속 반복하여
  4. 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 `후입선출`구조의 스택(stack) 사용

#### **DFS 알고리즘** (꼭!!!!알기!!!제일중요함!!!!!)

> 반복(stack) VS 재귀 뭐가 더 빠를까? 반복!!
>
> 속도는 stack이 빠르지만, 보통 재귀를 많이 이용, 코드가 더 간단하기 때문

##### DFS란?

- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
- 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 이곳으로부터 다른 방향으로 다시 탐색을 진행하는 방법과 유사하다.
- 즉, 넓게(wide) 탐색하기 전에 깊게(deep) 탐색하는 것이다.
- 사용하는 경우: 모든 노드를 방문 하고자 하는 경우에 이 방법을 선택한다.
- 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 좀 더 간단하다.

- 단순 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느리다.

[출처](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)

##### DFS 특징

- 자기 자신을 호출하는 순환 알고리즘의 형태 를 가지고 있다.
- 전위 순회(Pre-Order Traversals)를 포함한 다른 형태의 트리 순회는 모두 DFS의 한 종류이다.
- 이 알고리즘을 구현할 때 가장 큰 차이점은, 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사 해야 한다는 것이다.
- 이를 검사하지 않을 경우 무한루프에 빠질 위험이 있다.

[출처](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)

##### DFS 과정

1. 시작 정점 `v`를 결정하여 방문

2. 정점 `v`에 인접한 정점 중

   1) 방문하지 않은 정점 `w`가 있으면, 정점 `v`를 스택에 `push`하고 정점 `w`를 방문

   2) 그리고 `w`를 `v`로 하여 다시 `2.`을 반복

   3) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 스택을 `pop`하여 받은 가장 마지막 정점을 `v`로 하여 다시 `2.`반복

3. 스택이 공백이 될 때까지 `2.`를 반복.

###### DFS 동작

![image-20200826154350842](0826_algorithm(이론).assets/image-20200826154350842.png)

[출처](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)

0. 초기상태 : 배열 visited를 False로 초기화하고, 공백 스택을 생성

1. 정점 A를 시작으로 깊이 우선 탐색을 시작

![image-20200826153320982](0826_algorithm(이론).assets/image-20200826153320982.png)

2. 정점 A에 방문하지 않은 정점 B, C가 있으므로 A를 스텍에 push 하고, 인접정점 B와 C중에서 오름차순에 따라 B를 선택하여 탐색을 계속함

![image-20200826153343502](0826_algorithm(이론).assets/image-20200826153343502.png)

3. 정점 B에 방문하지 않은 정점 D, E가 있으므로 B를 스택에 push 하고, 인접 정점 D와 E중에서 오름차순에 따라 D를 선택하여 탐색을 계속함

![image-20200826153407605](0826_algorithm(이론).assets/image-20200826153407605.png)

4. 정점 D에 방문하지 않은 정점 F가 있으므로 D를 스택에 push하고, 인접정점 F를 선택하여 탐색을 계속함

![image-20200826153428890](0826_algorithm(이론).assets/image-20200826153428890.png)

5. 정점 G와 방문하지 않은 정점 E,F가 있으므로 G를 스택에 push하고, 인접 정점 E와 F중에서 오름차순에 따라 E를 선택하여 탐색을 계속함

![image-20200826153450807](0826_algorithm(이론).assets/image-20200826153450807.png)

6. 정점 E에 방문하지 않은 정점 C가 있으므로 E를 스택에 push하고, 인접정점 C를 선택하여 탐색을 계속함

![image-20200826153301511](0826_algorithm(이론).assets/image-20200826153301511.png)

7. 정점 C에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 E에 대해서 방문하지 않은 인접정점이 있는지 확인

![image-20200826153238625](0826_algorithm(이론).assets/image-20200826153238625.png)

8. 정점 E는 방문하지 않은 인접정점이 없으므로, 다시 스택을 pop하여 받은 정점 F에 대해서 방문하지 않은 인접정점이 있는지 확인

![image-20200826153552609](0826_algorithm(이론).assets/image-20200826153552609.png)

9. 정점 F에 방문하지 않은 정점 G가 있으므로 F를 스택에 push 하고, 인접정점 G를 선택하여 탐색을 계속함

![image-20200826153643567](0826_algorithm(이론).assets/image-20200826153643567.png)

10. 정점 G에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 F에 대해서 방문하지 않은 인접정점이 있는지 확인 

![image-20200826153739847](0826_algorithm(이론).assets/image-20200826153739847.png)

11. 정점 F에서 방문하지 않은 인접정점이 없으므로, 다시 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 D에 대해서 방문하지 않은 인접정점이 있는지 확인

![image-20200826153838481](0826_algorithm(이론).assets/image-20200826153838481.png)

12. 정점 D에서 방문하지 않은 인접정점이 없으므로, 다시 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 B에 대해서 방문하지 않은 인접정점이 있는지 확인

![image-20200826153925775](0826_algorithm(이론).assets/image-20200826153925775.png)

13. 정점 B에서 방문하지 않은 인접정점이 없으므로, 다시 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 A에 대해서 방문하지 않은 인접정점이 있는지 확인

![image-20200826154017113](0826_algorithm(이론).assets/image-20200826154017113.png)

14. 현재 정점A에서 방문하지 않은 인접 정점이 없으므로 마지막 정점으로 돌아가기 위해 스택을 pop하는데, 스택이 공백이므로 깊이 우선 탐색을 종료함

![image-20200826154124227](0826_algorithm(이론).assets/image-20200826154124227.png)

##### DFS 시간복잡도

- DFS는 그래프(정점의 수: N, 간선의 수: E)의 모든 간선을 조회한다.
- 인접 리스트로 표현된 그래프: O(N+E)
- 인접 행렬로 표현된 그래프: O(N^2)
- 즉, 그래프 내에 적은 숫자의 간선만을 가지는 희소 그래프(Sparse Graph) 의 경우 인접 행렬보다 인접 리스트를 사용하는 것이 유리하다.

[출처](https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html)

##### DFS 구현

> 1. 순환 호출 이용(재귀)
> 2. 명시적인 스택 사용(반복)
>    - 명시적인 스택을 사용하여 방문한 정점들을 스택에 저장하였다가 다시 꺼내어 작업한다.

###### DFS알고리즘-재귀 수도코드(의사코드)

```sh
DFS_recursive(G,v)
	visited[v] <-True // v 방문 설정
	FOR each all w in adjacency(G,v)
		IF visted[w] != True
			DFS_Recursive(G,w)
```

- G시작 v 시작 정점
- 방문했다
- 모든 정점을 찾아서
- 방문 하지않았다면 
- 재귀호출



- DFS알고리즘-반복 구현

```python
'''
입력값
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    #방문체크
    visited[v] = 1 #True란 뜻
    print(v,end = ' ') #출력
    #v의 인접한 정점 중에서 방문안한 정점을 재귀호출
    #인접행렬의 해당하는 v행을 돌려야됨
    for w in range(1,N+1): #정점의 개수만큼 돌릴거야(0번안씀)
   		#G가 v(시작정점) w(뺑뺑이돔) 이게 1(인접하여있고) 
        #그 인접한정점이 0(방문안했으면) dfs를 w를 가지고 돌려라
        if G[v][w] == 1 and visited[w]==0:
            dfs(w)

# 정점, 간선
N, E = map(int,input().split())
#간선들..
temp = list(map(int,input().split()))
#인접행렬
G = [[0] * (N+1) for _ in range(N+1)]
#방문체크
visited = [0] * (N+1)
#간선들을 인접행렬에 저장
for i in range(E): #8쌍(Edge만큼)을 받아올거야
    s,e = temp[2*i], temp[2*i+1] #start,end
    #인접행렬 이어져 있다고 표시하기 위해
    #s->e 가 1이고, e->s 도 1이라고 표시함
    G[s][e] = 1 
    G[e][s] = 1

dfs(1)

'''
1 2 4 6 5 7 3 
'''
```

- 선생님 코드

```python
'''
input
7 8 
1 2 #여기부터는 연결되어 있는 두 정점
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

def DFS(v):
    print(v, end = ' ')
    visited[v] = 1 #방문을 했기 때문에 바꿔줌
    for i in range(1, V+1): #global이 아니라도 V를 쓸수 있는건 수정이 아니라 읽어올거기 때문
        #현재 내 정점 v와 연결되어 있는지 확인
        if arr[v][i] == 1 and visited[i] == 0: #1 : 연결이 되어있다면, 0: 방문하지 않았다면
            DFS(i) #DFS(i)를 출력


# input
# 정점수(꼭지점), 간선수(연결된 선들)
V, E = map(int, input().split())
#인접행렬 초기값을 만듦
#한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해
#0번 idx따위 버려버리기
arr = [[0]*(V+1) for _ in range(V+1)] #V+1을 하는 이유는? V까지의 idx를 쓰기위해

for i in range(E):
    st, ed = map(int, input().split())
    #그래프가 방향이 없기 때문에 서로 이어져 있다고 표시해줌
    #방향이 정해져있는건 arr[st][ed] = 1만 해도됨
    #무향그래프이기 떄문에 서로 연결되어있음을 표시
    arr[st][ed] = arr[ed][st] = 1

#방문 배열 선언
visited = [0] * (V+1)

DFS(1) #1번부터 출발할거야
```

>이건 그냥 참고...다른얘기
>
>arr = [[0] * (v+1)] * (v+1) 이런식으로 2차원 행렬 만들면 다른 결과가 나옴, WHY??
>
>- 그렇게 하면  얕은 복사이기 때문에 내부 행렬이 주소가 복사되서 처음 arr[0]에 리스트가 나머지 리스트랑 똑같아짐
>-  같은 리스트만 남음
>- for문으로 내부에서 돌려줘 그래야 안전



###### DFS알고리즘-반복 수도코드(의사코드)

> DFS stack 버전..
>
> 보통 시스템이 스택을 해주기 떄문에 잘 안씀, 재귀가 훨씬훨씬많음!!!
>
> 이건 시스템스택이아니라 그냥 스택!
>
> 재귀를 사용하는 방법과 답이 다름

```sh
STACK s
visited[]
DFS(v)
	push(s,v)
	WHILE NOT isEmpty(s)
		v <- pop(s)
		IF NOT visited[v]
			FOR each w in adjacency(v)
				IF NOT visited[w]
					push(s,w)
```

- 방문배열을 스택에 넣음
- 스택이 빌때까지 반복문을 계속 돌면서
- 현재 스택에서 하나씩 뺴옴 그 점이 방문을 하지 않은 점이라면
- 방문을 하고
- 그 인접한 모든 정점들을 스택에 집어넣음t

- stack버전 코드 구현

```python
#DFS 스택 이용한 버전
#input
'''
7 8
1 2 
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
# 정점수(꼭지점), 간선수(연결된 선들)
V, E = map(int, input().split())
#인접행렬 초기값을 만듦
#한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해
#0번 idx따위 버려버리기
arr = [[0]*(V+1) for _ in range(V+1)] #V+1을 하는 이유는? V까지의 idx를 쓰기위해

for i in range(E):
    st, ed = map(int, input().split())
    #그래프가 방향이 없기 때문에 서로 이어져 있다고 표시해줌
    #방향이 정해져있는건 arr[st][ed] = 1만 해도됨
    #무향그래프이기 떄문에 서로 연결되어있음을 표시
    arr[st][ed] = arr[ed][st] = 1

#방문배열
visited = []
#스택
stack = []
#시작정점을 담는다
stack.append(1)

#stack이 빌때까지 무한히 반복
while len(stack)>0:
    #정점을 하나 꺼냄
    v = stack.pop() #-1을 쓰지않아도 자동으로 들어감()
    #해당 정점이 방문한 정점이 아니라면
    if v not in visited: #visited 안에 v가 안들어있다면
        print(v, end = ' ') #경로를 보기위한 출력(그리 중요치않음)
        #정점을 방문체크
        visited.append(v)
        #현재 내 정점에서 연결돼있는 모든 정점을 탐색하기 위한 반복문
        for i in range(1,V+1):
            # 현재정점과 연결되어 있으면서 방문하지 않은 정점i가 있다면
            if arr[v][i] == 1 and i not in visited:
                #모두 다 스택에 push
                stack.append(i) #스택에 담겠다
                
'''
1 3 7 6 5 2 4 
'''
```



## DFS를 왜 쓰느냐?

- 미로가 있다고 생각을 해보자
- 모든 칸을 다 탐색하고 싶다(내가 갈수 있는 곳은 무조건 다 갈수 없을 떄 까지 가본다 `깊이 우선탐색`)
- DFS와 델타 이동이 주로 많이 사용됨
- 재귀호출 반복문이 0~3으로 for문돌거야(4방향)
- 시스템 스택에 경로가 저장됨 



## Ladder!!

> 현우오빠가 가르쳐줌...천사선생님👼
>
> - 100x100크기의 2차원배열을 받는다
> - '0'으로 채워져있고 연속된 사다리는 '1', 도착지점은 '2'로 표현됨
>
> - 출발점 x=0~x=9가 있는데 세로 방향의 두 막대 사이에 임의의 막대들이 랜덤 간격으로 추가됨
> - 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향을 전환함
> - 방향 전환 후 다시 아래 방향으로만 이동, 바닥에 도착하면 멈춤
> - dfs로 풀어야되는문제.........
> - 2차원배열을 입력받는다
> - 첫줄에서 1인 값 찾기 -> list에 담아두기,아닐때 그다음값으로 바로 넘어감
> - 양 옆중 1이 나올때까지 밑으로 내려감 -> 복잡한거 함수로 만들면 편함
> - 옆에 1이 나왔다면 방향전환
> - 방향전환 후 다시 옆에 1이 나올때까지 내려감
> - 만약 2가 없다면 다시 첫줄에 방문하지 않은 1로 들어감
> - 반복...............................?

```python
import sys
sys.stdin = open('input.txt','r')
#위에 계속 써먹을 것들을 올리고
#그밑에 함수를 만들어야 함수에서도 적용이 됨!

#방향..델타...
di = [0,0,1,-1] #오른쪽, 왼쪽, 아래, 위 #여기서 위는 필요없음
dj = [1,-1,0,0]
ladder = [] #함수에서 사용될 ladder선언
#ni는 다음 위치, ni=i+di[방향] 그러면 옮겨짐!, nj도 마찬가지

def check(i,j,dir): #x,y,방향 인자로 받음
    #종료조건!!!!(중요)
    if ladder[i][j] == 2:
        return True #종료이면 True...본문에서 조건식으로 시작지점 나오게함

    #종료조건 1개더인데 끝일때!!! 2가아니면 False를 반환
    elif i == 99:
        return False

    else:
        #방향을 설정해줄거야
        #초반 방향은 무조건 아래부터 시작!!
        #오른쪽, 왼쪽으로 갈때 그 방향을 우선시해줌! 아래로 내려갈땐 옆을 봐줌...ㅠㅠ
        #dir은 방향의 idx임, idx가 0이면 오른쪽, 1이면 왼쪽, 2면 아래
        #di[dir]
        if (dir == 0) or (dir == 1): #오른쪽이나 왼쪽을 볼때 해당 방향을 우선시해줄거야
            #다음 위치를 변수로 만들건데 현위치(i)에 방향을 더함..ㅎ
            ni, nj = i + di[dir], j + dj[dir]
            #그 다음 위치가 out of idx가 됐는지 아닌지 체크해줘야됨, 그리고 옆이 1일때!!!!
 
#재귀로 만든다..
 #다음 위치의 좌표도 옆에 1이 있는지 확인,check(li,lj,dir)

            if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0: #ladder[ni][nj] == 1해도 돌아가지만, 사실!=0해줘야됨
                return check(ni,nj,dir)
            else: #못갔어, 그러면 아래로(dir=2) 내려감!!!!
                return check(i+1,j,2)

        else:#애초에 아래로 내려가는 중...dir=2
            #양옆을 우선 확인!!! 배열밖인지 ,1인지 확인한뒤, 1이면 방향전환 아니면 내려감!!!!
            #오른쪽(0) 왼쪽(1)이기 때문에 for문을 돌릴거야!
            for d in range(2): #d가 dir
                ni,nj = i + di[d], j + dj[d]
                if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0: #ladder[ni][nj] == 1해도 돌아가지만, 사실!=0해줘야됨
                    return check(ni,nj,d)
                #만약 if가 false면 그냥 다음으로 넘어감!
            #for문이 끝났는데, return이 안됐다는건 idx가 밖이거나 양옆이 1이 아니라는것! 그럼 내려가....!
            return check(i+1,j,2) #아래로 내려가!!!!!!!
        





for tc in range(1,11):
    T = int(input())
    #1 이차원배열 받기
    ladder = [list(map(int,input().split())) for _ in range(100)]
    #2 출발점들을 start 리스트에 넣기! 열이기 떄문에 j...
    start = []
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    #3 출발점을 하나씩 빼올거야! s가 j임
    for s in start:
        #기본방향은 밑으로 내려갈거고, 출발점은 행이 0이고, 열이 s임
        #check의 return 값이 True니까...if로...해줌....답을 찾았으니 그 출발점인 s를 출력하게 해라!
        if check(0,s,2):
            print('#{} {}'.format(tc,s))
            break #답을 찾았기 떄문에 나가줌!!!!

```

- 

```sh
ladder[ni][nj] != 0이렇게 써야되는 이유는 만약에 2를만나면 False가 됨, 그러면 갈수 없음..
근데 여기선 양옆만 보기 떄문에 ladder[ni][nj] ==1 이라고 적어도 답은 구해졌음..
```



- 방문배열로 풀어보자!!!

```python
#이제 방문배열로 해볼거야!!!!!!!
#100x100인 False 2차배열을 만든다
#방문하면 True로 바꿔줌(이걸 함수로 만들거야!)

di = [0,0,1] #오른쪽, 왼쪽, 아래
dj = [1,-1,0]
ladder,visited = [],[]

def check_v(i,j):
    #방향을 for문으로 오,왼,아래순서로 둘러볼거야
    #idx 안벗어나는지, 1인지, 방문하지 않았으면(False) 그 방향으로 갈거야!!!

    #방문한 곳을 다 True로 체크 먼저 해줘야됨!!! 이미 들어가 있으니까
    visited[i][j] = True
    # print(i,j)
    #종료조건!!!
    if ladder[i][j] == 2:
        return True
    elif i == 99: #끝까지 왔는데 못찾음
        # print('{} 에 도착'.format(i))
        return False
    else:
        #방향을 정함
        for d in range(3): #만약에 len(di)를 쓰면 계속 함수를 호출하니까 그냥 변수에 할당에서 지정해주던지, 3을 쓰던지 하자!!
            ni, nj = i + di[d], j+dj[d]
            if ni >=0 and ni<100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0 and visited[ni][nj] == False: #방문하지 않았으면!
                return check_v(ni,nj)



for tc in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # print(ladder)
    #방문배열도 선언해줌 j가 열
    visited = [[False for j in range(100)] for i in range(100)]
    # print(visited)
    #1인지, False인지, idx밖인지 체크
    #아니라면 그 방향으로 가면됨
    #오, 왼, 아래 순서로 돌면서 체크...! -> 함수로 만들거ㅑㅇ
    start = []
    #스타트지점들을 list에 넣음
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    # print(start)
    for s in start:
        #start 도는데 만약 못찾았어! 그러면 visited를 초기화 해줘야됨!!!!
        # if s != 67:
        #     continue
        visited = [[False for j in range(100)] for i in range(100)]
        # print('{} 에서 출발'.format(s))
        if check_v(0,s): #시작점이 true면 찾은거!
            print('#{} {}'.format(tc,s))
            break #찾았으니 끝!!
        # print(visited[99][57],)
    # else:
    #     print('못찾음')
```



- 
- 다른사람 코드

```python
#병훈
#2에서 시작해서 위로 올라간다
#move_up 중에는 좌우만 살핀다.
#좌우를 살피다 1이 나오면 move_side로 바뀐다.
#move_side 중에는 위만 살핀다
#위 칸에 1이 나오면 다시 move_up로 바뀐다.
#위에 0이 나오면 종료한다
def search_ladder(row,col):
    move_up = True
    move_side = False
    move = 0 #왼쪽 진행 중인지 오른쪽 진행 중인지
    while ladder[row][col] != 0:
        # print(row,col)
        if move_up:
            if ladder[row-1][col]==0:
                return col-1
 
            elif ladder[row][col+1] == 1: #오른쪽이 1이면 오른쪽으로 진행
                move_side = True
                move_up = False
                move = 1
                col+=1
            elif ladder[row][col-1] == 1: #왼쪽이 1이면 왼쪾으로 진행
                move_side = True
                move_up = False
                move = -1
                col-=1
            else:
                row-=1
 
 
        if move_side:
            if ladder[row-1][col]==1:
                move_up=True
                move_side=False
                row-=1
            elif move==1:
                col+=1
            elif move==-1:
                col-=1
 
for t in range(1,11):
    tc = int(input())
    ladder = [0]*101
    ladder[0] = [0]*102
    for i in range(1,101):
        ladder[i] = [0]+list(map(int,input().split()))+[0]
    for i in range(1,101):
        if ladder[-1][i]==2:
            end_idx = i
            break
 
    print('#{} {}'.format(tc,search_ladder(100,end_idx)))
```

- 

```python
#의수
def find_ladder(x, y):
    while x != 0: # 맨 윗줄의 띄 까지 오면 와일문 탈출
        # 좌우가 0이면 위쪽 행으로올라가자
        if arr[x][y-1] == 0 and arr[x][y+1] == 0:
            x -= 1
 
        # 오른쪽에 사다리 등장
        elif arr[x][y+1] == 1:
            while arr[x][y+1]: # 오른쪽 벽에 막힐떄까지 오른쪽으로 가자
                arr[x][y] = 0 # 현위치를 0으로 만들고 이동하자
                y += 1 # 한칸 옆으로 고고
 
        # 왼쪽에 사다리 등장
        elif arr[x][y-1] == 1:
            while arr[x][y-1]: # 왼쪽 벽에 막힐떄까지 왼쪽으로 가자
                arr[x][y] = 0 # 현위치를 0으로 만들고 이동하자
                y -= 1  #한칸 옆으로 고고
    return y
 
T = 10
for tc in range(1, T+1):
    test_case = input()
    # 띄 0 두르고 안에 입력받기
    N = 100
    arr = [0] * (N + 1) # 배열의 행 101개 만들기 (0으로 배열의 띄 만들기, 맨 마지막줄은 안해서 101개)
    arr[0] = [0] * (N + 2) # 배열의 1번째 행 102개 만들기(맨 윗줄 띄)
    for i in range(N):
        arr[i + 1] = [0] + list(map(int, input().split())) + [0] # 입력받으며 양 옆의 띄 생성
 
    # 도착지점부터 찾으면 개꿀인걸? 꺼꾸로 가자
    for i in range(1, 101):
        if arr[-1][i] == 2: # 도착점을 찾으면
            end = i # 인덱스값 저장
            break # 시간단축을 하자
 
    # 도착지점의 바로 한칸 위 지점부터 시작, 띄로 인한 인덱스 밀림 방지를 위해 -1 한다
    result = find_ladder(99, end) - 1
    print('#{} {}'.format(test_case, result))
```

