# 스택 2

> - 계산기
> - **백트래킹**(중요!!) : 완전검색(재귀, DFS) + 가지치기 = >문제 많이 출제!( ex. 부분집합, 순열)
> - 분할정복
> - 실습 1,2

## 계산기

- 문자열로 된 계산식이 주어짐, 스택을 이용해 계산식의 값 계산 가능

- 방법

  ```sh
  중위 표기법(infix notation)
  - 연산자를 피연산자의 가운데 표기하는 방법(A+B)
  후위표기법(postifix notation)
  - 연산자를 피연산자 뒤에 표기하는 방법(AB+)
  ```

  1. 중위 표기법의 수식을 후위 표기법으로 변경(스택 이용)
     1. 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시표현
     2. 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동시킴
     3. 괄호를 제거함

  ```sh
  예 ) A * B - C/D
  1단계 : ((A*B) - (C/D))
  2단계 : ((A B)* (C D)/)-
  3단계 : AB*CD/-
  ```

  2. 후위 표기법의 수식을 스택을 이용해 계산



#### 방법 상세 설명

#### STEP1. 중위 표기법의 수식을 후위 표기법으로 변경(스택 이용)

![image-20200831095702701](0831_algorithm(이론)_스택2.assets/image-20200831095702701.png)

1. 입력받은 중위 표기식에서 토큰을 읽는다(토큰, 요소 하나하나 `6+5`:토큰3개)
2. 토큰이 피연사자이면 토큰을 출력

![image-20200831095732397](0831_algorithm(이론)_스택2.assets/image-20200831095732397.png)

![image-20200831095806626](0831_algorithm(이론)_스택2.assets/image-20200831095806626.png)

![image-20200831095828596](0831_algorithm(이론)_스택2.assets/image-20200831095828596.png)

![image-20200831095856237](0831_algorithm(이론)_스택2.assets/image-20200831095856237.png)

![image-20200831095924202](0831_algorithm(이론)_스택2.assets/image-20200831095924202.png)

![image-20200831095938518](0831_algorithm(이론)_스택2.assets/image-20200831095938518.png)

![image-20200831100002012](0831_algorithm(이론)_스택2.assets/image-20200831100002012.png)

![image-20200831100016698](0831_algorithm(이론)_스택2.assets/image-20200831100016698.png)

![image-20200831100033413](0831_algorithm(이론)_스택2.assets/image-20200831100033413.png)

![image-20200831100101526](0831_algorithm(이론)_스택2.assets/image-20200831100101526.png)

![image-20200831100118213](0831_algorithm(이론)_스택2.assets/image-20200831100118213.png)

3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push함, 만약 top에 연산자가 없으면 push함

![image-20200831100141245](0831_algorithm(이론)_스택2.assets/image-20200831100141245.png)

4. 토큰이 오른쪽 괄호 `)`이면 스택 top에 왼쪽 괄호`(`가 올때까지 스택에 pop연산을 수행, pop한 연산자를 출력, 왼쪽 괄호를 만나면 pop만 하고 출력하지 않음

![image-20200831100203324](0831_algorithm(이론)_스택2.assets/image-20200831100203324.png)

5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복
6. 스택에 남아 있는 연산자를 모두 pop하여 출력
   - 스택 **밖**의 **`왼쪽 괄호`**는 우선 순위가 가장 높으며, 스택 **안**의 **`왼쪽`** 괄호는 우선 순위가 가장 낮음

#### STEP2. 후위 표기법의 수식을 스택을 이용하여 계산

1. 피연산자를 만나면 스택에 push

![image-20200831100605063](0831_algorithm(이론)_스택2.assets/image-20200831100605063.png)

2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산 결과를 다시 스택에 push함
   - 연산 순서 중요함!!! 특히 나누고 뺄때 순서가 중요하다

![image-20200831100624009](0831_algorithm(이론)_스택2.assets/image-20200831100624009.png)

![image-20200831100644135](0831_algorithm(이론)_스택2.assets/image-20200831100644135.png)

![image-20200831100704640](0831_algorithm(이론)_스택2.assets/image-20200831100704640.png)

![image-20200831100716172](0831_algorithm(이론)_스택2.assets/image-20200831100716172.png)

![image-20200831100731398](0831_algorithm(이론)_스택2.assets/image-20200831100731398.png)

3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

![image-20200831100750843](0831_algorithm(이론)_스택2.assets/image-20200831100750843.png)



## 사칙연산 계산기- 후위표기법

> 중위 표기법은 연산자가 피연산자들의 사이에 위치
>
> ex. (A+B) * (C+D)
>
> 후위 표기법은 연산자가 피연산자들 뒤에 위치
>
> ex. AB+CD+*

#### 중위표기식 -> 후위표기식 변환

1. 피연산자는 스택에 넣지 않고 그냥 출력
2. 연산자는 스택이 비었다면 스택에 push
3. 연산자는 스택이 비어있지 않으면 
   1. 스택에 있는 연산자와의 우선순위를 비교해 
   2. 스택에 있는 연산자의 우선순위가 같거나 크다면 
   3. 스택에 있는 연산자를 pop한 후 
   4. 출력하고 
   5. 현재 연산자는 스택에 push
4. 만약 3번에서 우선순위가 현재 연산자가 더 크면 현재 연산자를 push(스택에서 pop하지 않음)
5. 수식이 끝나면 스택이 빌 때까지 pop을 한 후 출력



![image-20200901211250454](0831_algorithm(이론)_스택2(중위후위표기계산기, 백트래킹).assets/image-20200901211250454.png)

1. A는 피연산자이므로 Result에 출력
2. `+`는 연산자, 현재 스택이 비었으므로 `push`함
3. B는 피연산자이므로 출력
4. `*`와 `+`의 우선순위를 비교했을 때, `*`가 더 크므로 스택에 push
5. C는 피연산자이므로 출력
6. 수식이 끝났으므로 스택에 있는 연산자들을 모두 pop하고 출력
7. 식 완성!



#### 괄호가 들어간 수식 -> 후위표기법

1. 괄호가 여는 괄호면 무조건 push
2. 괄호가 닫는 괄호면 stack에서 여는 괄호가 나올 때 까지 pop한 후 출력
3. 여는 괄호가 스택에 push된 후 
   1. 닫는 괄호가 나올 때까지 여는 괄호가 pop이 되면 안됨
   2. 여는 괄호의 우선순위는 제일 작음
4. 괄호는 출력하지 않는다.
5. 나머지는 위와 동일함



![image-20200901212134678](0831_algorithm(이론)_스택2(중위후위표기계산기, 백트래킹).assets/image-20200901212134678.png)

1. 여는 괄호는 무조건 스택에 push
2. A는 피연산자이므로 출력
3. 연산자 우선순위를 비교, 여는 괄호의 우선 순위가 작으므로 +는 push
4. B는 피연산자이므로 출력
5. 닫는 괄호가 나왔음, 여는 괄호가 나올 때 까지 pop을 하고 출력(괄호 제외)
6. 스택이 비었으므로 연산자를 push함

![image-20200901212355694](0831_algorithm(이론)_스택2(중위후위표기계산기, 백트래킹).assets/image-20200901212355694.png)

7. 여는 괄호는 무조건 push
8. C는 피연산자, 출력
9. 연산자 우선순위를 비교, 여는 괄호의 우선순위가 작음, +는 push
10. D는 피연산자, 출력
11. 닫는 괄호가 나왔음, 여는 괄호가 나올 때까지 pop, 출력
12. 수식이 끝남, 스택에 있는 연산자들을 모두 pop하고 출력

[출처](https://jamanbbo.tistory.com/53)

## 백준 후위표기식 문제도 풀어보기!!



## **백트래킹** 중요!!!!!!!!!

- 백트래킹 기법은 해를 찾는 도중에 '막히면' 즉, 해가 아니면, 되돌아가서 다시 해를 찾아 가는 기법
- 최적화 문제와 결정 문제를 해결할 수 있음
- 결정 문제 : 문제의 조건을 맍고하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제
  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합 문제 등
- 모든 후보를 검사하지 않음
- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 가능성이 있으면 유망하다고 함
- 가지치기 : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음

##### 절차

1. 상태 공간 트리의 깊이 우선 검색을 실시
2. 각 노드가 유망한지를 점검
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속함

```python
#일반 백트래킹 알고리즘
def checknode(v): #node
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
       
```

### 백트래킹 : 미로 찾기

- 입구와 출구까지 경로 찾는 문제
- 이동할 수 있는 방향은 4방향으로 제한

![image-20200831102404954](0831_algorithm(이론)_스택2(중위후위표기계산기, 백트래킹).assets/image-20200831102404954.png)

![image-20200831102444776](0831_algorithm(이론)_스택2(중위후위표기계산기, 백트래킹).assets/image-20200831102444776.png)

![image-20200831102459261](0831_algorithm(이론)_스택2(중위후위표기계산기, 백트래킹).assets/image-20200831102459261.png)

![image-20200831102539640](0831_algorithm(이론)_스택2(중위후위표기계산기, 백트래킹).assets/image-20200831102539640.png)

##### 백트래킹과 DFS의 차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(가지치기)
- DFS가 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
- DFS를 가하기에는 경우의 수가 너무나 많음, 즉, N! 가지의 경우의 수를 가진 문제에 대해 DFS를 가하면 당연히 처리 불가능한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수시간을 요하므로 처리 불가능
- 예 ) 어떤 문제...에서 DFS Vs 백트래킹
  - 순수한 깊이 우선 검색 = 155노드
  - 백트래킹 = 27노드



### 부분집합 구하기

> 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 powerset이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n이 나옴

- 재귀 또는 비트연산으로 구하는 방법이 있음
- 백트래킹 이용
- n개의 원소가 들어 있는 집합의 2^n개의 부분집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법 이용
- 배열의 i번째 항목은 i번째 원소가 부분집합의 값인지 아닌지를 나타내는 값

```python
#재귀 호출을 이용한 부분집합 생성 알고리즘
A[] : 해당 원소의 포함여부를 저장(0,1)
def powerset(n,k): #n:원소의 갯수, k:현재depth
    if n == k: #basis part
        print
    else: #inductive part
        A[k] = 1 #k번 요소 포함
        powerset(n,k+1) #다음 요소 포함 여부 결정
        A[k] = 0 #k번 요소 미포함
        powerset(n,k+1) #다음 요소 포함 여부 결정
```

- 다시보기,,,,,,

```python
arr = [1,2,3]
N = len(arr)
A = [0] * N #1,0

def powerset(n,k,cursum):
    if cursum>10:
        return
    if n == k:
        for i in range(n):
            if A[i]:
                print(arr[i],end = ' ')
        print()
    else:
        #k번째 선택
        A[k] = 1
        powerset(n,k+1,cursum+arr[k])
        #k번째 비선택
        A[k] = 0
        powerset(n,k+1,cursum)

powerset(N,0,0)
```

- 선생님 코드
  - `return`의 의미는 나를 불렀던 곳으로 돌아가라! 란 뜻
  - 처음 `sel[idx]=1`이 행을 계속 수행하다가 idx가 N이 됐을 때 N이 됐을때 나를 불렀던 곳으로 돌아감...!
  - 그렇게 계속 sel을 채우고 돌아가고를 반복하다가 `sel[idx]=0`인 것도 다 진행되고 나를 불렀던 곳으로 돌아갈 것도 없어진다면 끝남!

```python
N = 3
arr = [1,2,3]
sel = [0] * N
#부분집합은 각 idx sel(0,1,2,3)를 선택하냐 안하냐 차이
def powerset(idx):
    #도착을 했을 때 지금까지 고른것을 출력
    if idx == N :
        print(sel, ':',end =' ' )
        for i in range(N):
            if sel[i]:
                print(arr[i],end = ' ')
        print()
        return #나를 불렀던 곳으로 돌아가라
    #해당자리를 뽑고가고
    #idx를 선택
    sel[idx] = 1
    #idx를 선택한채로 재귀
    powerset(idx+1) #19번줄
    #해당자리를 안뽑고 가고
    #idx 선택안함
    sel[idx] = 0
    #idx를 선택 안한채로 재귀
    powerset(idx+1) #22번줄 모든 idx가 여기까지 온다면 더이상 돌아갈 곳이 없음! 끝남!
    
powerset(0)
```

- 부분집합의 합 구하기

```python
N = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sel = [0] * N


# 부분집합은 각 idx(0,1,2,3)를 선택하냐 안하냐 차이
def powerset(idx):
    # 도착을 했을 때 지금까지 고른것을 출력
    if idx == N:
        total = 0
        #뽑은 것들의 합을 구함
        for i in range(N):
            if sel[i]:
                total += arr[i]
        #합이 10일 경우만 출력
        if total == 10:
            print(sel)
        return
    # 해당자리를 뽑고가고
    # idx를 선택
    sel[idx] = 1
    # idx를 선택한채로 재귀
    powerset(idx + 1)
    # 해당자리를 안뽑고 가고
    # idx 선택안함
    sel[idx] = 0
    # idx를 선택 안한채로 재귀
    powerset(idx + 1)


powerset(0)

```

- 백트래킹 이용

```python
#백트래킹으로 부분집합의 합 구함

# 부분집합은 각 idx(0,1,2,3)를 선택하냐 안하냐 차이
def powerset(idx,sum_num):
    #지금까지 더한 값들을 들고 다니는데
    if sum_num > 10:
        #이미 벗어나면 더이상 수행할 필요가 없음
        return 
    # 도착을 했을 때 지금까지 고른것을 출력
    if idx == N:
        total = 0
        #뽑은 것들의 합을 구함
        for i in range(N):
            if sel[i]:
                total += arr[i]
        #합이 10일 경우만 출력
        if total == 10:
            print(sel)
        return
    # 해당자리를 뽑고가고
    # idx를 선택
    sel[idx] = 1
    sum_num += arr[idx]
    # idx를 선택한채로 재귀
    powerset(idx + 1,sum_num)
    # 해당자리를 안뽑고 가고
    # idx 선택안함
    sel[idx] = 0
    sum_num -= arr[idx]
    # idx를 선택 안한채로 재귀
    powerset(idx + 1,sum_num)


powerset(0,0)

```





## 재밌는 오셀로 게임

```python
import sys
sys.stdin = open('input.txt','r')
#인풋을 받는다
#입력은 열 행 컬러
#돌을 놓았을 떄 8방향 탐색을 하면서
#나와 같은 컬로 찾는다(이떄 중간에 공백이 있거나, 맵의 범위를 벗어나면 수행x)
#찾은 컬러의 좌표부터 지금 놓은 좌표까지 돌아오면서 색갈을 모조리다 나의 컬러로 바꾼다
#위의 과정을 M번 반복하면 끝

#첫 위치를 배열의 len을 구하고 //2해준 위치,
#
# 8방배열을 할거야
# 오셀로 입력값은

# 8방 우 좌 하 상 오상대 오하대 좌상대 좌하대
di = [0, 0, 1, -1, -1, 1, -1, 1]
dj = [1, -1, 0, 0, 1, 1, -1, -1]


def put(i, j, color):
    arr[i][j] = color  # 놓은 곳의 색깔이 달라짐!
    opp_color = -1 #반대컬러 선언
    if color == 1:
        opp_color = 2
    else:
        opp_color = 1

    # 놓음과 동시에 8방으로 훑어보고 색을 바꿔 줘야됨
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        flag = False  # 중간에 끼인 값들 색을 바꿔줘야된다고 할 표시
        cnt = 0  # 그 중간에 몇개가 껴있는지 세어야됨

        while ni >= 0 and ni < N and nj >= 0 and nj < N:
            #공백일때(0) 빠져나옴
            if arr[ni][nj] == 0:
                break
            if arr[ni][nj] == opp_color:
                cnt += 1
            if arr[ni][nj] == color:
                flag = True #여기까지 색을바꿀거야
                break #같은애 찾았으니 나와랏!
            #그방향으로 계속 감!
            ni += di[d]
            nj += dj[d]
        if flag: #True
            #i,j시작값과 flag가 True인 값 사이의 값을 같은 색으로 바꿀거야!
            for c in range(1,cnt+1): #cnt만큼 돌거야 근데 c는 1부터 해당 cnt까지 돌아야됨!!!!
                #di[d]와 dj[d]가 c만큼 움직였으니까 그거를 원래 좌표에 더한 그 위치를 내 색으로 바꿈!
                arr[i+di[d]*c][j+dj[d]*c] = color




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0 for j in range(N)] for i in range(N)]
    arr[N // 2][N // 2] = 2
    arr[(N // 2) - 1][(N // 2) - 1] = 2
    arr[(N // 2) - 1][N // 2] = 1
    arr[(N // 2)][(N // 2) - 1] = 1
    # print(arr)

    for _ in range(M):
        row, col, color = map(int, input().split())
        #이게 4X4배열일때 입력받은 idx가 1부터 4까지로 해놓음! 그래서 하나씩 빼줘서(컴퓨터배열은 0~3이니까) idx를 맞춰줌!
        put(row-1,col-1,color)
    #흑돌 백돌 개수를 세어야됨!!!
    black ,white = 0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            if arr[i][j] == 2: #0이있을수도 잇으니 else를 하면 안됨!!!!!!
                white += 1
    print('#{} {} {}'.format(tc,black,white))
```



- 선생님 풀이

```python
#선생님 코드
#8방향 델타
#우,우하,하,좌하,좌,좌상,상,우상
dr = [0,1,1,1,0,-1,-1,-1]
dc = [1,1,0,-1,-1,-1,0,1]

def init():
    mid = N//2
    othello[mid][mid] = othello[mid+1][mid+1] = 2 #백돌
    othello[mid+1][mid] = othello[mid][mid+1] = 1 #흑돌

def change(r,c,color):
    #새로운 좌표에 돌을 놓았다
    othello[r][c] = color
    #8방향 탐색
    for i in range(8):
        nr = r
        nc = c
        #해당방향으로 break가 걸리기전까지 무조건 전진
        while True:
            nr += dr[i]
            nc += dc[i]
            #한칸씩 크게 만들었으니 idx가 다름
            #우리는 0idx를 사용하지 않음
            #맵의 범위를 벗어났다면 그만
            if nr <= 0  or nr > N or nc <=0 or nc > N:
                break
            #만약에 중간에 공백이 있다면 의미가 없으니 break
            if othello[nr][nc] == 0:
                break
            #나랑 같은 색을 만나면 색 바꿔주고 그만
            if othello[nr][nc] == color:
                #그 곳에서 원래의 나의 위치까지 오면서 나의색으로 바꿔줌
                while (nr == r and nr == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    othello[nr][nc] =color
                break

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    #0idx는 쓰지 않을거니 N+1로 만들어줌
    othello = [[0]*(N+1) for _ in range(N+1)]

    init()

    for i in range(M):
        c,r,color = map(int,input().split())
        change(r,c,color)
	b_cnt = 0
	w_cnt = 0
    for i in range(N+1):
        b_cnt += othello[i].count(1)
        w_cnt += othello[i].count(2)
    print('#{} {} {}'.format(tc,b_cnt,w_cnt))    
```



## 순열

- 단순하게 순열을 생성하는 방법

```python
arr = [1,2,3]
#1부터 3까지 반복을 돌면서
for a in range(1,4):
    for b in range(1,4):
        #a와 b가 같은것은제외
        if a == b:
            continue
        for c in range(1,4):
            #a,c가 같거나 c,b가 같은건 제외
            if a == c or c == b:
                continue
            print(a,b,c)
```

- 이런 과정을 방문배열을 사용하여 작성함

```python
arr = [1,2,3]
#1부터 3까지 반복을 돌면서
for a in range(1,4):
    for b in range(1,4):
        #a와 b가 같은것은제외
        if a == b:
            continue
        for c in range(1,4):
            #a,c가 같거나 c,b가 같은건 제외
            if a == c or c == b:
                continue
            print(a,b,c)

#순열 방문체크
arr = [1,2,3]
N = 3
sel = [0] * N
visited = [0] *N
def perm(idx): #몇번째 원소인지를 인자로 받음
    if idx == N:
        print(sel)
        return
    for i in range(N):
        #방법1
        # if visited[i]: #True라면
        #     continue
        #방법2
        if not visitied[i]:
            sel[idx] = arr[i]
            #뽑았다고 내려보내고
            visited[i] = 1
            perm(idx+1)
            #다음 꺼도 시도 해봐야되니까 원상복귀 시켜놓음
            visited[i] = 0
    #암묵적으로 반복문이끝났을 때 return함
    #return
perm(0)
```

