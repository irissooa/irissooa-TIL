# Algorithm

## 문자열비교

```python
#문자열 비교
#str2안에 str1과 일치하는 부분이 있는지 찾는 프로그램
#두개의 문자열이 주어질 첫 문자열이 두번째에 존재하면 1 존재하지 않으면 0출력

#문자열을 입력받는다
#bruteforce검색방법 이용
#while문 이용
#str1과 str2의 각각의 idx를 넘지 않는 범위에서
#패턴이 다르면 i(str1)를 shift이동
#j를 초기화
#i,j를 1씩 더해주며 비교
#j가 M가지 가게된다면 검색에 성공한것! 1
#아니면 존재하지 않음 0

import sys
sys.stdin = open("input.txt", "r")

def BruteForce(pattern,total):
    i = 0 #str2,t(전체 패턴)의 idx
    j = 0 #str1,p(찾을 패턴)의 idx
    while i < len(total) and j < len(pattern):
        if total[i] != pattern[j]: #패턴이 같지 않다면
            i = i-j # i를 shift이동
            j = -1 #j초기화
        i += 1
        j += 1
    if j == len(pattern):
        return 1 #검색성공
    else:
        return 0 #검색실패

N = int(input())
for tc in range(1,N+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc,BruteForce(str1,str2)))
```

- `for else`
  - for를 진행할 때 break에 걸리지 않는다면 else로 들어감
- 선생님 풀이

```python
#1.
def check(str1,str2):
    #본문에서 패턴길이를 빼고 +1하여 반복
    for i in range(len(str2)-len(str1)+1):
        #패턴의 길이만큼
        for j in range(len(str1)):
            #만약 현재사이클에 다르다면 브레이크
            if str2[i+j] != str1[j]
                break
        #중간에 브레이크 걸리지 않았다면 완벽히 찾은것
        else:
            return 1
    #완벽히 찾지 못했다면 리턴 0
    return 0

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, check(str1,str2)))

    #2. in활용하여 체크
    if str1 in str2:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,0))


    #3. find 활용
    ans = 0
    if str2.find(str1) != -1:
        ans = 1
    print('#{} {}'.format(tc,ans))
```



## 글자수

```python
import sys
sys.stdin = open('input.txt','r')
# str1과 str2가 주어진다
# str1에 포함된 글자 중 str2에서 가장 많이 나오는 문자의 횟수를 출력
# str1의 글자를 dict의 key로 만들고 그 횟수를 value로 str2를 보면서 횟수를 세어라

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    str_dict = {}
    # str1의 문자를 key로 만들고, str2의 그 key값들의 개수를 세어서 value로 넣어라

    for i in str1:
        cnt = 0
        for j in str2:
            if i==j:
                cnt +=1
            str_dict[i] = cnt
    MAX = 0
    for value in str_dict.values():
        if value > MAX:
            MAX = value
    print('#{} {}'.format(tc,MAX))
```

- 선생님 코드

```python
#체크배열, 카운트배열
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    check_arr = [0]*26
    count_arr = [0]*26

    #1. str을 순회하면서 알파벳 체크
    for i in str1:
        check_arr[ord(i)-ord('A')] = 1
    #2. 체크된 알파벳의 카운트 세기
    for i in str2:
        if check_arr[ord(i)-65] == 1:
            count_arr[ord(i)-65] += 1
    print('#{} {}'.format(tc, max(count_arr)))
    
#2방법
    dict = {}
    for i in str1:
        if i not in dict:
            dict[i] = str2.count(i)
    print('#{} {}'.format(tc,max(dict.values())))
```



## 달팽이

```python
cnt=1
arr=[[0]*5 for i in range(5)]

row_start=0
row_end=4
col_start=0
col_end=4

while row_start<=row_end and col_start<=col_end:
    # 왼쪽=> 오른쪽
    for i in range(col_start, col_end+1):
        arr[row_start][i]=cnt
        cnt+=1
    row_start +=1

    # 위=> 아래
    for i in range(row_start, row_end + 1):
        arr[i][col_end] = cnt
        cnt += 1
    col_end -= 1

    # 오른쪽=> 왼쪽
    for i in range(col_end, col_start-1, -1):
        arr[row_end][i]=cnt
        cnt+=1
    row_end -=1

    # 아래=> 위
    for i in range(row_end, row_start - 1, -1):
        arr[i][col_start] = cnt
        cnt += 1
    col_start += 1

print(arr)
```

- 선생님 풀이
- `델타이동` 이용

```python
#선생님 풀이
#우하좌상 방향으로 출력해야됨!
dr = [0,1,0,-1]
dc = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input9)
    #0으로 채워진 N*N배열
    arr = [[0] * N  for _ in range(N)]
    #방향은 idx를 의미함 0:우,1:하, 2:좌,3:상
    dir = 0
    #시작점
    r = 0
    c = 0
    num = 1
    
    while num <= N * N: #num은 N*N만큼만 적을거야..
        arr[r][c] = num #현재 칸에 값을 저장
        num += 1 #다음 숫자 준비
        
        #다음 칸을 결정
        #다음 좌표는 현재좌표 + 방향
        nr = r + dr[dir]
        nc = c + dc[dir]

        #idx가 벗어나는지 체크해야됨, 그리고 방문하지 않은 곳인지 확인
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            #현재좌표 갱신
            r,c = nr,nc
        else:
            #모듈 연산 우(0),하(1),좌(2),상(3) 다음 방향으로 바꿈
            dir = (dir+1) % 4
            r += dr[dir]
            C += dc[dir]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()
```

- 선생님 다른 풀이

```python
#선생님 달팽이 다른 풀이
T = int(input())
for tc in range(1,T+1):
    N = int(input())

    nums = [[0]*N for _ in range(N)]
    K = N #이동거리, 우리가 처음으로 이동할 거리
    d = 1 #방향, 처음에는 열이 증가하기 때문에 1로 둠
    row = 0 #행
    col = -1 #열(초기에는 수평이동이므로 -1로 초기화)
    num = 1 #넣을값

    while True:
        #수평이동
        for c in range(K):
            col += d
            nums[row][col] = num
            num += 1
        #수평이동 끝 이제 수직이동
        K -= 1

        if K == 0:
            break

        #수직이동
        for r in range(K):
            row += d
            num[row][col] = num
            num += 1

        #수직이동이 끝 수평이동
        d *= -1
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()
```



## 델타이동

![image-20200827094544573](0827_algorithm(문제).assets/image-20200827094544573.png)

```python
#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

#한번에 써도 됨
drc = [[-1,0],[1,0],[0,-1],[0,1]]

r = 1
c = 1
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    print(nr,nc)

   
# 8방향 탐색
```



## 회문

```python
#회문
#N을 2차원배열로 NXN을 만듦
#길이가 M인 회문이 가로, 세로 중 1개가 존재함
#가로, 세로를 돌면서 같은 것이 있는지 찾기
#N개 안에 M이 N-M+1개가 나오기 때문에 그만큼 돌려서 볼거야
#행이든 열이든 M//2만큼 돌건데(회문이기때문에 반만돈다)
#arr[i][j]==arr[i][k+M-j-1]이면 cnt를 해줌
#cnt가 M//2와 같아지면 그 단어를 k부터 K+M까지 slicing함

##다른방법(의수), 역슬라이싱으로도 풀 수 있음
# for x in range(n):  # 2차원 배열로 받아서 각 행을 하나씩 불러온다
#     for y in range(n - m + 1):  # 각 행에서 n=열의개수, m=회문의길이 즉 n-m+1번 하면 모든 경우의수 돌린다
#         if arr[x][y:y + m] == arr[x][y:y + m][::-1]:  # [::-1] 스터디때 배운 역슬라이싱 활용, 원본과 역슬라이싱한거 비교
#             return m  # 만약 회문이면 회문의길이인 m을 리턴
# return 0

import sys
sys.stdin=open('input.txt','r')

def row(arr):
    cnt = 0
    STR = ''
    for i in range(N):
        for k in range(N-M+1): #N-M개만큼 N안에 들어갈수 있음
            for j in range(M//2):
                if arr[i][j+k] == arr[i][k+M-j-1]:
                    cnt += 1
                else:
                    cnt = 0

            if cnt == M//2:
                # STR = arr[i][k:k+M]
                for idx in range(k, k+M):
                    STR += arr[i][idx]
                return STR


def col(arr):
    STR = ''
    cnt = 0
    for i in range(N):
        for k in range(N-M+1):
            for j in range(M//2):
                if arr[j+k][i] == arr[k+M-j-1][i]:
                    cnt += 1
                else:
                    cnt = 0
            if cnt == M//2:
                for idx in range(k,k+M):
                    STR += arr[idx][i]
                return STR

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)] #NXN 배열 만듦
    ROW = row(arr)
    COL = col(arr)
    if ROW:
        print('#{} {}'.format(tc,ROW))
    else:
        print('#{} {}'.format(tc,COL))
```



- 선생님 코드

```python
#선생님 코드
def check():
    #전체 크기가 N
    for i in range(N):
        #가로검사
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            if tmp == tmp[::-1]:
                return tmp

        #세로검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == tmp[::-1]:
                return tmp
    return []


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())

    words = [list(input()) for _ in range(N)]
    ans = check()
    print('#{} {}'.format(tc,ans))
```

- 열 슬라이싱! (하영선생님이 가르쳐줌👍)

```python
'''
board
1 2 3 4 
5 6 7 8
9 10 11 12
'''
[b[0:2] for b in board[0:2]]

'''
1. board[0:2] 는 아래와 같이 2행을 모두 뽑는다
1 2 3 4
5 6 7 8
2. 그리고 b[0:2]를 2행 모두 반복해서 적용하여 2열을 뽑는다
1 2
5 6
'''

'''
출력
1 2 
5 6
'''
```

- Zip
  - 같은 열끼리 묶어서 표현을 해줌
  - 열의 갯수가 안맞으면 맞는것 까지만 묶어줌

```python
test1 = [1,2,3,4]
test2 = [5,6,7,8]

test3 = list(zip(test1,test2))

print(test3)
#2차원리스트도 가능
nums = [[1,2,3],[1,2,3]]
#모든 요소를 넣어줘도 좋고
nums2 = list(zip(nums[0],nums[1]))
#unpacking을 하여 한번에 처리도 가능함
nums3 = list(zip(*nums)) # *unpacking연산자
print(nums2)
print(nums3)
tmp = [1,2,3,4]
print(tmp)
print(*tmp)
print(list(zip(tmp)))
# 튜플 요소 하나는 (1,)이렇게 표시
'''
[(1, 5), (2, 6), (3, 7), (4, 8)]
[(1, 1), (2, 2), (3, 3)]
[(1, 1), (2, 2), (3, 3)]
[1, 2, 3, 4]
1 2 3 4
[(1,), (2,), (3,), (4,)]
'''
```



## 회문2

```python
#100X100에 회문이 있는지 확인하고, 회문이 있다면 가징 긴 길이를 출력
#회문인지 판별하는 함수를 만든다
#세로일 때 90도로 돌리는 함수를 만든다
#회문의 길이를 지정하는 함수를 만든다(100에서 작아짐, 진범님 idea)
import sys
sys.stdin = open('input.txt','r')


def palindrome(arr):
    for i in range(100):
        for k in range(100-M+1):
            if arr[i][k:k+M] == arr[i][k:k+M][::-1]: #회문 길이 M만큼 slicing하고 역순이랑 같은지 확인
                return M #같다면 회문의 길이 반환
    return 0 #회문이 아니면 0

def rota90(arr):
    temp = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            temp[j][100-i-1] = arr[i][j]
    return temp

for tc in range(1,11):
    MAX_len = 1 #초기값, 1단어도 회문1
    M = 100 #초기 LEN값, 줄어들예정
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    while M > 0 :#M값은 1~100사이
        if palindrome(arr) or palindrome(rota90(arr)): #가로, 세로 중 값이 true이면 그 값이 최고 회문값
            MAX_len = M
            print('#{} {}'.format(tc,MAX_len))
            break #최고를 찾았으니 멈춤
        else:
            M -= 1 #초기LEN값을 줄여준다
```



- 선생님 코드

```python
#선생님 코드
def check(M):
    for i in range(N):
        for j in range(N-M+1):
            #가로
            tmp = words[i][j:j+M]

            #세로
            tmp2 = zwords[i][j:j+M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0


for tc in range(10):
    tc_num = int(input())
    N = 100
    words = [list(input()) for _ in range(N)]
    zwords = list(zip(*words)) #2중 리스트이니까 언패킹해서 zip으로 묶어줌(열)

    for k in range(100, 0, -1): #최대 회문 길이를 100부터 봄
        ans = check(k)
        if ans != 0:
            break
    print('#{} {}'.format(tc,ans))
```









## SWEA_종이붙이기(점화식)

- 친절한 하영이 설명👍👍

![image-20200827151430526](0827_algorithm(문제).assets/image-20200827151430526.png)

```python
#10X20, 20X20인 직사각형 종이
#교실 바닥에 20XN 크기의 직사각형을 테이프로 표시
#준비한 종이를 빈틈없이 붙이는 방법을 찾아보려함
#10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면
#표시한 영역을 몇 개나 만들어야 되는가
#직사각형 종이가 모자라는 경우는 없다
#첫줄 테스트케이스 개수
#다음 줄 테스트케이스 별로 N주어짐

#N을 입력받는다
#20XN에 10X20과 20X20을 어떻게 집어넣을까....생각해봐ㅏㅏ....
#이거도 방문..배열인가..?
#같은 크기의 False 2차배열을 만들고
#하나씩 채워지면 True..로 바꾸고..
#먼저 큰거 1개 넣고 나머지에 작은거 넣는 방법,

#이건 하영이가 dp로 푸는거랬엉...다시 생각해보자..!

#점화식으로 푼다!
#규칙찾기(하영그림참고)
#N이 10일때 d[10]의 경우의 수 1가지.
#N이 20일때 d[20] 경우의 3가지
#N이 30일때 d[30] 경우의 d[20]의 경우의 수 + d[10]의 경우의 수 + d[10]의 경우의 수
#d[n]점화식 d[n] = d[n-1] + d[n-2]*2
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())//10 #값들이 다 10의 배수기때문에 10의 몫으로 int값 /하면 float
    #그 전값들에 계속 쌓아나가야된다,,,,,,,
    #점화식 값들을 담을 배열을 만듦
    arr = [0 for _ in range(N+1)] #0idx는 안쓰기 때문에 N+1을 해서 1개 더 idx를 줘야 N까지 표현 가능
    arr[1], arr[2] = 1,3 #1과 2의 값, 0은 안씀
    for i in range(3,N+1): #얘도 마찬가지 이유, 그리고 3부터 시작!1과2는 값을 지정
        arr[i] = arr[i-1] + arr[i-2] * 2
        # print(arr[i])
    print('#{} {}'.format(tc,arr[N]))

```

- 선생님 풀이

```python

#선생님 풀이 메모이제이션 사용 재귀+메모이제이션
def f(n): #n : 문제의 크기(식별값)
    #기저 사례
    if n == 1:
        return 1
    if n == 2:
        return 3
    #일반적 사례
    if memo[n]:
        return memo[n]
    memo[n] = f(n-1) + f(n-2) * 2
    return memo[n]

for tc in range(1, int(input())+1):
    N = int(input()) // 10
    memo = [0] * (N+1) #초기값 0 -> 이 문제의 답을 아직 구하지 않음
    print(f(N))
    

#2.반복문+메모이제이션
for tc in range(1, int(input())+1):
    N = int(input()) // 10
    memo = [0] * (N+1) #초기값 0 -> 이 문제의 답을 아직 구하지 않음
    memo[1], memo[2] = 1,3 #기저값

    for i in range(3, N+1): #문제의 크기를 ㄴ타내는값
        memo[i] = memo[i-1] + memo[i-2] * 2

    print(memo[N])

```



## SWEA_4866_괄호검사

```python
#괄호가 짝을 제대로 이루고 있는지 검사
#입력은 한줄의 파이썬 코드일 수 있고, 괄호만 주어질 수 있음
#정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력
#이거도 스택으로
#어제 한거니까 한번 내가 해보자!!!!
#짝을 이뤘는지 봐야되니까 일단 여는 괄호일때 스택에 넣기
#닫는 괄호일때 비교하고 같은 괄호유형이면 pop
#남은 stack이 있다면 짝을 이루지 못했으니 0, 없으면 1
import sys
sys.stdin = open('input.txt','r')
def check(code):
    top =''
    stack = []
    for i in range(len(code)):
        # print(code[i])
        if code[i] == '(' or code[i] == '{':
            stack.append(code[i])
            # print('{}을 추가했습니다'.format(stack))
        elif code[i] == ')' or code[i] == '}':
            #닫는괄호가 나왔는데 만약에 stack이 비었다면 짝이 안맞으니 0반환
            if len(stack) == 0:
                return 0
            #stack에 뭔가가 들어있다면 그건 어떤 형태이든 여는괄호!
            #그중 stack[-1]값을 top에 할당
            else:
                top = stack.pop()
                # print('{}을 제거했습니다'.format(stack))
            #짝이 맞는지 확인!
            if code[i] == ')' and top == '(':
                continue
            elif code[i] == '}' and top == '{':
                continue
            return 0
    #검사 다끝났는데 stack에 뭔가가 남아있다면 그건 짝이 안맞는것
    if len(stack) > 0:
        return 0
    #짝맞춤!
    return 1


T = int(input())
for tc in range(1,T+1):
    code = input()
    print('#{} {}'.format(tc,check(code)))
```

- 선생님 풀이

```python
#선생님풀이
for tc in range(1, int(input())+1):
    arr = input()
    S = [] #스택
    ans = 1
    #한문자씩 읽어서 처리
    for ch in arr:
        #여는 괄호 push
        if ch == '(' or ch == '{':
            S.append(ch)
        #닫는 괄호
        if ch == ')' or ch == '}':
            #빈 스택일 경우
        if len(S) == 0:
            break
        #1.방법
        t = S.pop() #여기서 비교해도됨
        #ch와 S[-1]비교해서 다르다 (짝이 같은지 안같은지 비교)
        if (ch == ')' and t != '(') or (ch == '}' and t != '{'):
            break
        #2.방법
        # if (ch == ')' and S[-1] != '(') or (ch == '}' and S[-1] != '{'):
        #     ans = 0
        #     break
        # t = S.pop() #여기 왔다는건 정상적인 경우
            #같다면 스택에서 제거
        #괄호문자가 아닌 경우

    #빈스택인지 조사 ->남아있다면 잘못된것
    if len(S) == 0:
        ans = 0
    print(ans)
```

- 선생님 풀이 (딕셔너리 이용)

```python
#딕셔너리 만드는 방법
paren = {'(':')','{':'}',')':'(','}':'{'} #딕셔너리 만들어 사용
for tc in range(1, int(input())+1):
    arr = input()
    S = [] #스택
    ans = 1
    #한문자씩 읽어서 처리
    if ch not in paren:continue
    for ch in arr:
        #여는 괄호 push
        if ch == '(' or ch == '{':
            S.append(ch)
        #닫는 괄호
        if ch == ')' or ch == '}':
            #빈 스택일 경우
        if len(S) == 0:
            break
        #1.방법
        t = S.pop() #여기서 비교해도됨
        if paren[ch] != t:
            ans = 0
            break
    #빈스택인지 조사 ->남아있다면 잘못된것
    if len(S) == 0:
        ans = 0
    print(ans)
```





## SWEA_4871_그래프 경로

- DFS(i) 이거 선생님께 여쭤보기!!!

```python
#V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
#특정한 두개의 노드에 경로가 존재하는지 확인하는 프로그램
#경로가 있으면 1 없으면 0 출력
#노드번호는 1번부터 존재, V개의 노드 중 간선으로 연결되지 않은 경우도 있음
#첫줄 테스트케이스
#테스트케이스의 첫줄에 V와 E가 주어짐
#둘째줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어짐
#E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어짐

#DFS, 이건 방향이 있음!
#input받기
#정점수(꼭지점), 간선수(연결된 선들) 주어짐
#인접행렬 초기값을 만듦
#한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해(0번 idx버림, V까지 idx로 쓰기 위해)
#그래프 방향이 있기 때문에 arr[st][ed] = 1만 해줘도 됨
#방문배열을 선언해주고
#방문(함수) , 방문을 했을 떄 1로 바꿔줌
# 현재 내 정점 v와 연결되어 있는지 확인
#연결이 되어있고 : 1, 방문하지 않았다면(0)
#DFS(i)로 반복
#그러다가 i == G(종점)으로 가면 이어진 거니까 1출력

import sys
sys.stdin = open('input.txt','r')

ans = 0 #global 변수 선언
def DFS(v):
    #이번 DFS는 return값이 없음, 그래서 도착지에 도착하면 표시를해줌(global 변수에)
    global ans
    visited[v] = True #방문을 했으니 True
    #종료조건!!, 못찾은건 어차피 ans = 0으로 끝날거니까 따로 조건지정안해도됨
    if v == G:
        ans = 1 #표시를 해준거야 이 함수는 리턴값이 없지만 global변수로 답을 찾았다고 표시를 해줌!(종료는 아님, 그 상위의 DFS 돌아가고있음)
    # 정점만큼 돌면서
    #Linked[v][i] 이게 1(이어져있고) 방문을 안했고(False)
    for i in range(1, V+1): #정점1번부터 볼거야아
        if Linked[v][i] == 1 and visited[i] == False:
            DFS(i) #이거 진심 이해0 -> 뭐냐고,,,,이건 그냥 쓰다보면...이해된대....ㅎ for문 돌듯...걍..재귀야.............




T = int(input())
for tc in range(1,T+1):
    ans = 0 #tc돌때마다 0으로 초기화 해줘야됨!!!
    V, E = map(int,input().split())
    #인접행렬 초기값
    Linked = [[0]*(V+1) for _ in range(V+1)]
    # print(arr)

    #방문배열 선언
    visited = [False for _ in range(V+1)] #배열의 idx를 표시해줘야되는데, 그러면 V까지 꼭 나와야함.
    # 근데 (1,V+1)을 하면 어차피 길이가 (V)와 같음 그래서 (V+1)로 1개 더 추가함
    # print(type(visited))
    # print(visited)

    for i in range(E): #간선수만큼 볼거야..
        st, ed = map(int,input().split()) #start, end
        #유향이기 때문에 st->end = 1만 해주면 됨
        Linked[st][ed] = 1

    S,G = map(int,input().split()) #E개의 줄 이후 출발노드,도착노드 주어짐
    DFS(S) #함수를 선언해줌(출발점), 값이없으니까 변수에 할당을 못함. 그래서 표시한 값을 지정해준거야!
    print('#{} {}'.format(tc,ans))
```

- 선생님 코드

```python

#선생님 풀이
def DFS(v):
    visit[v] = 1
    if v == e: #도착점과 같아
        return 1
    for w in range(1,V+1):
        if G[v][w] == 1 and visit[w] == 0:
            #현재방문한 정점 v라고 생각했을 때 w1,w2,w3,,,등등 갔다가 올건데
            #그중에 만약 1이 나온다면 굳이 반복문 다 돌지 않고 바로 끝내주면됨!!!!
            if DFS(w) == 1:
                return 1
    return 0


for tc in range(1,int(input())+1):
    V,E = mpa(int,input().split())
    #인접행렬, 정점번호 1~V
    G = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E) #간선 정보 읽기
        u,v = map(int,input().split())
        G[u][v] = 1

    s, e = map(int,input().split())
    visit = [0] * (V+1)
    # DFS(s)
    print(DFS(s))
```





## SWEA_4873_반복문지우기

- 리스트 요소 지우기
  1. del 키워드 사용하기
     - del 다음에 지울 값을 입력하면 됨, 만약 지울 값으로 슬라이싱을 전달하면 여러 개의 값을 한번에 삭제할 수 있음
  2. remove함수 사용
     - remove(x) 함수는 리스트에서 값이 x와 같은 첫번째 요소를 제거
  3. pop 함수 사용
     - pop(i) 함수는 리스트에서 주어진 위치(인덱스)에 있는 요소를 삭제하고, 그 요소를 반환
     - 인덱스를 지정하지 않으면 리스트의 맨 마지막 요소를 삭제하고, 그 요소를 돌려줌

```python
#문자열 s에서 반복된 문자들 지움
#지워진 부분은 다시 앞뒤를 연결
#만약 연결했는데 또 반복문자가 생기면 이부분 다시 지움
#반복문자를 지운 후 남은 문자열의 길이 출력
#남은 문자열이 없으면 0 출력

#문자열을 입력받는다
#앞에서부터 두개씩 보면서 반복된 문자가 있는지 찾는다
#반복된다면 그 두 문자를 지우고 이어 붙인다
#이어붙인 뒤 다시 두개씩 보면서 찾는다
#이 과정 반복 함수로 만들어야 되지 않을까?
#끝난 뒤 최종 문자열 길이

#근데 반복된애를 지우면..idx가 그만큼 줄어듬...이걸 어떻게 고치지?!
#재귀..? 문자도 재귀가 되나.............아냐 하영이가 스택이래
#스택으로 풀어보쟈
#어제 본거 참고함...ㅠ나중엔 혼자 풀수 있길........ㅠㅠㅠ
#check 함수를 만들건데
#만약 STR을 둘러보면서 문자를 담고 다음에 들어오는 문자랑 같은지 확인하고
#같다면 pop, 반복..
import sys
sys.stdin = open('input.txt','r')
STR = []
# def check(STR):
#     S = len(STR)
#     for i in range(S): #STR idx가 나가지 않게 S-1까지 해줌
#         if STR[i] == STR[i+1]:
#             STR[i] = STR.pop(i)
#             print(STR)
#             STR[i+1] = STR.pop(i+1) #지워줌
#             print(STR)
#     else:
#         return S

#넘 오래 못풀어서...결국 구글링...찾아보고..이해함..........후
def check(STR):
    stack = []
    N = len(STR)
    for i in range(N):
        #stack이 비었거나, 스택의 마지막 값이 데이터 내 값과 같지 않은 경우
        #=> stack에 저장(append)
        if not stack or stack[-1] != STR[i]:
            stack.append(STR[i])
        #stack에 값이 있고, 스택의 마지막 값과 데이터 내 값과 같은 경우
        #=> stack에서 제거(pop)
        elif stack and stack[-1] == STR[i]:
            stack.pop()
    return len(stack)

T = int(input())
for tc in range(1,T+1):
    STR = list(input())
    print('#{} {}'.format(tc,check(STR)))
```

- 선생님 풀이
- 스택이용!

```python

#선생님 풀이
for tc in range(1,int(input)+1):
    arr = input()
    S = []

    for ch in arr:
        #빈스택인경우
        if not S:
            S.append(ch)
        #ch와 S[-1] 비교해서 다르면 push
        elif ch != S[-1]:
            S.append(ch)
        # if와 elif하는 일이 같네?
        # if not S or ch != S[-1]: #or은 앞에 것이 True라면 뒤에 안봄, 앞이 False면 뒤엘 봄, 근데 굳이 이런거하다가 실수할 수 있음!
        #     S.append(ch)
        #같으면 ch와 S[-1] 버림
        else:
            S.pop()
    print(len(S))
```



## ladder

- def 에서 ni,nj 범위 정하는 것을 반드시 앞에 둬야 idx에러가 안뜸! idx넘어가면 False라 뒤 조건을 보지 않고 바로 else로 가기때문

```python
#음!ladder풀듯 풀어보자!
#ladder 일단 2차배열을 입력받는다
#ladder 0행-> 첫줄에서 1인 값들을 start list에 넣는다
#그리고 배열을 체크할건데(함수만듦)
#방문배열을 이용할거야!!
#idx가 나가거나 방문한곳이 아닌곳을 볼건데
#양옆 중에 1이 있다면 방향을 전환하고(델타이동을 이용할거야)
#없다면 계속 아래로 내려갈거야
#근데 여기가 아니라면 그냥 다음 start로 넘어가보자!
#이제 만들어보아요~
#근데 문제가 있음!
#종료조건이 틀렸네?
#i가 99일때 이동거리가 가장 짧은 거!!!!!!뽑기!!!!
#거리랑, 시작점을 어딘가에 저장해 둬야됨!(global 사용)

import sys
sys.stdin = open('input.txt','r')

di = [0,0,1] #오,왼,아래
dj = [1,-1,0]

def check(i,j,dist):
    global min_dist, flag #global 사용, 값형(전역변수) 수정 가능해짐

    #방문한 곳은 True로 바꾸기
    visited[i][j] = True
    # print(i,j)
    #종료조건
    #i 마지막 칸에 도달했을 때 도착. min_dist 확인
    if i == 99:
        if min_dist > dist:
            min_dist = dist
            flag = True
            return #값을 리턴해줄 필요없음 왜냐면 flag로 표시해주니까(True이면 START값이 저장됨)
    #범위 체크도 해줄거야
    # D = len(di)
    else:
        for d in range(3):
            #다음 위치 지정
            ni = i + di[d]
            nj = j + dj[d]
            #idx가 벗어나지 않고, 그 값이 0이 아니면 방문하지 않았던 곳으로 갈거야
            # print(ni,nj,visited[ni][nj])
            # print('로 갈라함')
#범위 정하는 것을 반드시 앞에 둬야 idx에러가 안뜸! idx넘어가면 False라 뒤 조건을 보지 않고 바로 else로 가기때문
            # if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0 and visited[ni][nj] == False:
            #     # 양옆중 1이 있는지 확인, 있다면 그 곳으로 방향 전환
            #     return check(ni,nj) #반복

            #현우오빠 방식 조건을 반대로 줘서 하나라도 해당되면 continue를 함
            if ni < 0 or ni >= 100 or nj < 0 or nj >= 100:
                continue #continue를 쓰면 밑에 무시하고 바로 다음 for문으로 감
            if ladder[ni][nj] == 0:
                continue
            if visited[ni][nj] == True:
                continue
            return check(ni,nj,dist+1) #다음으로 넘어갈때 거리1을 더해줌!
            break #이미 찾았으니까 break

for tc in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    #어차피 밑에 리셋시켜놓으니까 여기서 안적어도됨
    # visited = [[False for j in range(100)] for i in range(100)]
    start = [] #start지점들을 넣어줄거야
    min_dist = 9999999999999999 #최소거리 초기값
    START = 0 #시작점
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    #start지점들을 돌면서 체크할거야
    for s in start:
        flag = False #출발점 저장하기 위해 쓰는 표시
        #start마다 방문체크 리셋
        visited = [[False for i in range(100)] for j in range(100)]
        check(0,s,0) #(0,s)는 출발점 돌거야, dist는 아직 안움직였으니 0부터 시작
        if flag: #표시된flag가 True이면
            START = s
    print('#{} {}'.format(tc, START))
```



- 다른 코드

```python
#병훈
#move down 중에는 좌우를 먼저 살피고
#move side 중에는 밑을 먼저 살핀다 만약 밑이 0이라면 move side를 계속한다..
#mode 1은 내려가기  mode 2는 왼쪽으로가기, mode 3은 오른쪽으로 가기
def laddering(row,col,mode):
    move = mode
    cnt = 0
    while ladder[row][col]!=0:
        if move == 1: #내려가는 중 = 좌우 살피기
            if ladder[row+1][col] == 0:
                return cnt
 
            elif ladder[row][col+1] == 1:
                move = 3
                col += 1
 
            elif ladder[row][col-1]==1:
                move = 2
                col -= 1
            else:
                row+=1
 
        elif move == 2: # 왼쪽으로 가는 중 = 밑 살피기
            if ladder[row+1][col]==1:
                move = 1
                row += 1
            else:
                col -= 1
        else:# 오른쪽으로 가는 중 = 밑 살피기
            if ladder[row+1][col]==1:
                move = 1
                row += 1
            else:
                col += 1
        cnt += 1
 
for t in range(1,11):
    tc = int(input())
    ladder = [0]*102
    ladder[0] = [0] * 102
    ladder[-1] = [0] * 102
    result = []
    for i in range(1,101):
        ladder[i] = [0] + list(map(int,input().split())) + [0]
    for col in range(1,101):
        mode = 1
        if ladder[1][col] == 1:
            result.append([col-1,laddering(1,col,mode)])
    result.sort(key=lambda x:(x[1],-x[0]))
    print('#{} {}'.format(t,result[0][0]))
```

```python
#의수
def find_ladder(x, y, cnt, arr):
    # 시작지점 만나면 탈출
    while x > 0: 
        # 좌우 확인하고 둘다 0이면 위로 올라간다
        if arr[x][y+1] == 0 and arr[x][y-1] == 0:
            x -= 1
            cnt += 1
         
        # 오른쪽에 사다리가 있으면
        elif arr[x][y+1] == 1:
            # 벽에 부딫힐 때까지 계속 오른쪽으로 돌진
            while arr[x][y+1]:
                y += 1
                cnt += 1
            # 벽에 부닥치면 위로 한칸 올라가자
            x -= 1
            cnt += 1
             
        # 왼쪽에 사다리가 있는 경우
        elif arr[x][y-1] == 1:
            # 벽에 부딫힐 떄까지 계속 왼쪽으로 돌진
            while arr[x][y-1]:
                y -= 1
                cnt += 1
            # 벽에 부닥치면 위로 한칸 올라가자
            x -= 1
            cnt += 1
    # 다끝나면 시작점과 cnt를 튜플형태로 반환
    return y-1, cnt
 
for tc in range(1, 11):
    test_case = int(input())
     
    # 띄를 둘러보자
    ladder = [0] * 101 # 아래쪽은 띄를 안 두를거라 101개 만든다
    ladder[0] = [0] * 102
    for i in range(1, 101):
        ladder[i] = [0] + list(map(int, input().split())) + [0]
 
    # 끝나는 지점 탐색
    end = []
    for i in range(1, 101):
        if ladder[100][i]:
            end.append(i)
     
    # 모든 경우의 수를 result에 튜플 형태로 저장
    result = []
    for e in end:
        count = 0
        # return 값을 2개주면 튜플형태로 자동으로 반환됨
        temp = find_ladder(100, e, count, ladder) 
        result.append(temp)
     
    # 우선 cnt로 정렬하고, 동일한 것이 있을 때는 시작번호가 큰것 순서로 저장
    result.sort(key=lambda x: (x[1], -x[0])) 
    print('#{} {}'.format(tc, result[0][0]))
```



- 선생님 풀이
- 방향 정보- 한칸씩 이동
- 현재 위치에서 이동할 다음 위치를 계산
  - 진행 중 방향 정보(위, 좌, 우)필요
  - 교차점을 만나면 좌, 우, 위로 이동하는 방향 결정

1. 위
   - 오른쪽에 길이 있으면 이동, 방향 설정
   - 왼쪽에 길을 있으면 이동, 방향 설정
   - 위로 이동
2. 왼쪽
   - 왼쪽에 길이 있으면 이동
   - 위로 이동, 방향 설정
3. 오른쪽
   - 오른쪽에 길이 있으면 이동, 방향 설정
   - 위로 이동 방향 설정

```sh
사다리 정보 = arr[][]
현재 위치(x,y) = (행, 열)
방향정보 = dir (0:상, 1:좌, 2:우)
Check(x,y)
- x,y 의 경계조사
- arr[x][y]가 1인가?

[조건식]
dir == 0 and check(x,y-1) 좌
dir == 1 and check(x,y-1) 좌

dir == 0 and check(x,y+1) 우
dir == 2 and check(x,y+1) 우

dir == 0 and check(x-1,y) 상
dir == 1 and check(x-1,y) 상
dir == 2 and check(x-1,y-1) 상

[조건식]
dir == 0 or 1 and check(x,y-1)  좌
dir == 0 or 2 and check(x,y+1) 우
그외
```

- 왼쪽이나 오른쪽 길이 없으면
  - 위로 이동

- 오른쪽 길이 나오면(계속 가던길을 가게함)
  - 오른쪽 길이 없을 때까지 계속 이동한 후 위로 한 칸이동
- 왼쪽길이 나오면(계속 가던길을 가게함)
  - 왼쪽으로 없을 떄까지 계속 이동한 후 위로 한 칸 이동

- 이렇게 상황 판단하기 싫어요!!!!

```python
def check(x,y):
    #범위를 벗어나는지
    if x < 0 or x >= 100 or y < 0 or y >= 100:
        return  False
    #길인지아닌지 보고
    if arr[x][y] ==0:
        return False
    #맞다면 true
    return True

 for tc in range(1,11):
     case_num = input()
     arr = [list(map(int,input().split())) for _ in range(100)]

     #도착점을 찾는다
     x = y = 0
     for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break
    dir = 0 #방향정보 저장 0:위, 1:좌, 2:우

    while x: #0이되면 False가 됨, 99부터 올라감
        #가던 방향으로 계속 가고, check가 True일때
        #왼쪽으로 가는 경우
        if dir != 2 and check(x,y-1):
            y -= 1
            dir = 1
        #오른쪽으로 가는 경우
        elif dir != 1 and check(x,y+1):
            y += 1
            dir = 2
        #그외, 위로 가는 경우
        else:
            x -= 1
            dir = 0
    print(y)
```

- 

```python
    #2번 방법 방향정보 필요없고 벽 부딛칠때까지 계속 한쪽으로 직진
    while x:
        if check(x,y-1): #왼쪽으로 가는 경우
            while check(x,y-1):
                y -= 1
            x -= 1
        elif check(x,y+1): #오른쪽으로 가는 경우
            while check(x,y+1):
                y += 1
            x -= 1
        x -= 1
    print(y)

    #3번 사다리를 지움, 그럼 옆에 오른쪽 판단안하고 갔던곳은 벽으로 막히고 한쪽 방향으로 감(이거를 아래 재귀함수로 만듦)
    while x:
        arr[x][y] = 0
        if check(x,y-1): #왼쪽으로 가는 경우
            y -= 1
        elif check(x,y+1): #오른쪽으로 가는 경우
            y += 1
        else:
            x -= 1
    print(y)

    #4번 재귀
    def ladder(x,y):
        if x == 0:
            global ans
            ans = y #시작지점을 저장
        else:
            arr[x][y] = 0
            if check(x, y - 1):  # 왼쪽으로 가는 경우
                ladder(x,y-1)
            elif check(x, y + 1):  # 오른쪽으로 가는 경우
                ladder(x,y+1)
            else:
                ladder(x-1,y)
            arr[x][y] = 1 #지우면서 갔던것들을 원상복구함 
    ans = 0
    ladder(x,y)
    print(ans)


#이거는 반환하는 값이 필요하니까 return 해줌!-> 다시이해필요
def ladder(x,y):
        if x == 0:
            return y #ladder2를 풀때는 return 0하고 아래 return들에 전부 +1해주면 됨
        else:
            arr[x][y] = 0 #길 따라가면서 0으로 지웠다가 아래에서 다시 원상복구 '=2'
            if check(x, y - 1):  # 왼쪽으로 가는 경우
                return ladder(x,y-1)
            elif check(x, y + 1):  # 오른쪽으로 가는 경우
                return ladder(x,y+1)
            else:
                return ladder(x-1,y)
    print(ladder(x,y))
    print(ans)
```



## SWEA_1226_미로찾기

```python
#미로를 짜보쟈(DFS)
#1은 벽이고, 0이 길, 2는 출발점, 3은 도착점
#일단 배열을 입력받는다
#0을따라 계속 감, 가다가 1을 만나면 0인 곳으로 방향 전환(오,왼,아래,위 순서로 볼거야)/일단가는 방향을 우선시해줄거야!
#방문배열을 해서 그전에 갔던 곳은 가지 않게 함,,,근데 이러면 길이 아니라서 돌아갈때 오류가 생기지 않을까? 일단해본다
#다음 위치가 idx에 벗어나지 않는지 확인, 방문하지 않은 곳인지 확인
#종료조건은 3을 만나면 종료!, 아니면 더이상 갈곳이 없을때!
#시작점은 (1,1)이고 도착점(끝점)은(13,13)임 
#도착했다는 것을 저장할 global변수 필요함(ans)


import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #오, 왼, 아, 위
dj = [1,-1,0,0]

def check(i,j):
    global ans
    visited[i][j] = True
    # print(i,j)
    #종료조건
    if maize[i][j] == 3: #3을 만났다는 건 도착했다는 뜻!
        ans = 1 #도착했다는 것 표시
        # print('여기오나')
        return
    else:
        #idx 벗어나면 continue, 방문했던 곳이면 continue, maize[ni][nj]가 0이 아니면 continue,
        for d in range(4): #4방향을 볼거야
            ni = i + di[d]
            nj = j + dj[d]

           
            #maize[ni][nj] == 3을 해주는 건, 만약 3에 도달했을때 위 ans =1을 적용하게 해주기 위해!
            #범위 밖이면 continue(다음 for문으로 넘어감)
            if ni < 0 or ni >= 16 or nj < 0 or nj >= 16:
                continue
             #방문을 했다면 continue
            if visited[ni][nj] == True:
                continue
            #0이 아닌데!(0이어야앞으로감), 근데 3이다? 그럼 ans =1로 표시해주고 끝내야됨
            if maize[ni][nj] != 0:
                if maize[ni][nj] == 3:
                  ans = 1
                  return
                continue
            check(ni,nj)
		#위 조건과 반대로, 해당되면 if문안으로 들어와 다음으로 넘어감
            # if 0 <= ni < 16 and 0 <= nj < 16 and (maize[ni][nj] == 0 or maize[ni][nj] == 3) and visited[ni][
            #     nj] == False:
            #     check(ni, nj)



for tc in range(1,11):
    ans = 0 #초기화(tc돌때마다)
    T = int(input())
    maize = [list(map(int,input())) for _ in range(16)]
    # print(maize)
    # for i in range(16):
    visited = [[False for j in range(16)] for i in range(16)] #방문배열 초기화
    check(1,1)
    if ans == 1:
        print('#{} {}'.format(tc,ans))
        # break
    else: #못찾음
        print('#{} 0'.format(tc))
```

- stack을 이용해서는 어떻게 풀지?

```python
def dfs(graph, start, end):
    """DFS 를 이용하여 미로 찾기 알고리즘을 구현한다. :param graph: 미로 그래프 :param start: 출발 지점(노드) :param end: 도작 지점(노드) :return: 최소 이동 거리 """ 
    stack = [(start, 0)] # idx 0: 노드, idx 1: 이동 거리 
    visit = {start, } # 방문한 노드 저장 공간 
    while stack: 
        node, distance = stack.pop() 
        new_distance = distance + 1 
        for near_node in graph[node]: 
            # 방문한 적 없는 노드인 경우 
            if near_node not in visit: 
                print("{} Node 방문".format(near_node)) 
                # 도착 지점에 도착한 경우 총 이동거리를 반환 
                if near_node == end: 
                    return new_distance 
                visit.add(near_node) # 방문 
                stack.append((near_node, new_distance)) # 이동 거리를 1 증가 시킨다. 
    return -1 # 도착 지점이 막힌 경우(없는 경우)

출처: https://memostack.tistory.com/36 [MemoStack]
```



## 백준 2667_단지번호붙이기 dfs...풀어보기....!