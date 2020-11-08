# Algorithm(문제)

## 스도쿠 찾기

```python
def check():
    for i in range(9):
        row = [0] * 10 
        col = [0] * 10
        for j in range(9):
            #행우선검사
            num1 = sudoku[i][j]
            #열우선검사
            num2 = sudoku[j][i]
            #이미 사용한 숫자라면 유효한 스도쿠가 아니라서 0을 리턴
            if row[num1]:#0, False, [],None,,,등이 아니라 값이 있다면 True
                return 0
            if col[num2]:
                return 0
            #위에 걸리지 않았다면 사용했음을 표시
            row[num1] = col[num2] = 1

            #0~8까지 사용이 가능하므로 0,3,6일때 걸리게됨
            if i % 3 == 0 and j % 3 == 0: #0,3,6이 걸림
                square = [0]*10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    #위에서 리턴되지 않았다면 유효한 스도쿠
    return 1


T = int(input())
for tc in range(1,T+1):
    sudoku = [list(map(int,input(.split()))) for _ in range(9)] #2차원배열 입력받음
    if check(): #check()==1이라면
        print('#{} 1'.format(tc))
    else:
        print('#{} 1'.format(tc))
```



## 행렬 찾기

```python
#선생님풀이
def search_size(r,c):
    r_cnt = 0
    c_cnt = 0
    #띠를 둘러줬기 떄문에 따로 범위를 주지않아도 검사가능, idx에러안남
    for i in range(r,N+2):
        if arr[i][c] == 0
            break
        r_cnt += 1
    for j in rangE(c,N+2):
        if arr[r][j] == 0:
            break
        c_cnt += 1
    ans.append([r_cnt,c_cnt])
    init(t,c,r_cnt,c_cnt)

def init(r,c,r_cnt,c_cnt):
    for i in range(r,r+r_cnt):
        for j in range(c,c+c_cnt):
            arr[i][j] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #0이면 멈춰야되니까 전체 띠를 두름
    # 제일 위와 제일 밑에 띠를 두른것처럼 0으로 만들어줌
    arr = [0] * (N+2)
    arr[0] = arr[N+1] = [0] * (N+2)
    for i in range(N):
        #왼쪽 오른쪽에도 띠를 만들어줌
        arr[i+1] = [0]+list(map(int,input().split()))+[0]
    ans = []
    for i in range(1,N+2):
        for j in range(1,N+2):
            if arr[i][j] !=0:
                search_size(i,j)
                
    ans = sorted(ans, key=lambda x:((x[0]*x[1]),x[0]))
    print('#{} {}'.format(tc,len(ans)), end = ' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0],ans[i][1]),end= ' ')
    print()
```



## lambda

- 익명함수

```python
def add(x,y):
    return x+y

print((lambda x, y:x+y)(3,5))
add2 = lambda x,y : x+y

print(add(3,5))
print(add2(5,5))


def f1(x):
    return x[0] #-x[0]하면 내림차순정렬이 됨 값에 -가 붙어서 원래 값이 작던 것이 큰것처럼 되기 때문에 내림차순 정렬이 됨, ex)1,2,3,4->-4,-3,-2,-1
ans = [[2,3],[3,4],[12,4],[4,5],[6,8]]
num = sorted(ans,key=f1)
print(num) #첫번째 인자 기준으로 오름차순 정렬
num = sorted(ans, key=f1, reversed=True) #내림차순으로 정렬
```



## SWEA_4864 문자열 찾기

- `BruteForce`함수 만들어 사용

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





## SWEA_4861 회문찾기

![image-20200825232345003](0825_algorithm(문제).assets/image-20200825232345003.png)

- 회문인지 확인하기 위해서 N만큼 for문을 돌리는데 `N-M+1`은 N안에 회문의 길이인 M이 들어가있는 개수만큼 돌면서 그 idx값을 `if arr[i][j+k] == arr[i][k+M-j-1]` 이렇게 지정해 줄 때 쓰임
- 오래걸렸다..................ㅎ k값을 idx에 적용해주지 않아서...자꾸...3번 값이 none값이 나왔다....` if arr[i][j+k] == arr[i][k+M-j-1]:`

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

- 다른코드

```python
#의수
def discrim(arr):
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            for x in range(M//2):
                if arr[i][j+x] == arr[i][j+M-x-1]:
                    cnt += 1
            if cnt == M//2: 
                return arr[i][j:j+M]
    return 0    

def rotate90(arr): # 배열을 90도 회전시켜주는 함수                
    temp = [[0]*N for _ in range(N)] # arr랑 동일한크기의 임시배열 하나 만들자
    for x in range(N):
        for y in range(N):
            temp[y][N-x-1] = arr[x][y]
    return temp

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[x for x in input()] for _ in range(N)]
    result = discrim(arr)  # 회문이 없으면 0 내놓고 아니면 결과출력
    if result == 0:
        ro90 = rotate90(arr)
        result = discrim(ro90)
    result = ''.join(result) 
    print('#{} {}'.format(tc, result))
```

- 하영

```python
#하영
T = int(input()) # tc개수

def pal_check(line):# 회문 체크 수업시간함수
    for idx in range(len(line) // 2):
        if line[idx] != line[-idx - 1]:
            return False
    return True

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    found = False   # 루프 깨줄 변수
    arr = [list(input()) for _ in range(N)]
    print('#{}'.format(tc), end = " ")
    for i in range(N):
        for j in range(N - M + 1):
            sample = arr[i][j:j + M] # 가로
            sample2 = [a[i] for a in arr[j:j + M]]  # 세로
            if pal_check(sample):  # 가로에서 회문 찾을 경우
                print(''.join(sample)) # 하나로 합쳐주기
                found = True  # 찾았다
                break
            elif pal_check(sample2): # 세로에서 회문 찾을 경우
                found = True  # 찾았다
                print(''.join(sample2))
        if found:   # 회문 1개뿐이므로 찾았으면 루프 깨주기
            break

```

- `zip`함수 사용

```python
#진범님
def c(board,n,m):
    for i in board:
        for j in range(0,n+1-m):
            if i[j:j+m]==i[j:j+m][::-1]:
                return i[j:j+m]

for t in range(int(input())):
    n,m=map(int,input().split())
    board=[input()for _ in range(n)]
    for j in range(n):
        tmp = ''
        for i in range(n):
            tmp += board[i][j]
        board.append(tmp)
    #board+=list(zip(*board)) 세로축을 쪼개서 col을 추가해준다.
    print('#{} {}'.format(t+1,''.join(c(l,n,m))))
```



## 회문2

- 근데 이렇게 90도 돌리는걸 사용하면 메모리 터짐....! 다음부턴 `zip`함수를 이용해보자!!

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



- `zip`함수 이용
- 문자열은 Iterable하면서 immutable, order 하기때문에 파이썬 내에서 튜플과 같다고 생각해도 됨
- ![image-20200825231658047](0825_algorithm(문제).assets/image-20200825231658047.png)

```python
#의수
def discrim(arr, n, m): # 회문인지 판별하는 함수
    for x in range(n): # 2차원 배열로 받아서 각 행을 하나씩 불러온다
        for y in range(n - m + 1): # 각 행에서 n=열의개수, m=회문의길이 즉 n-m+1번 하면 모든 경우의수 돌린다
            if arr[x][y:y + m] == arr[x][y:y + m][::-1]: # [::-1] 스터디때 배운 역슬라이싱 활용, 원본과 역슬라이싱한거 비교
                return m # 만약 회문이면 회문의길이인 m을 리턴
    return 0

for tc in range(10):
    n = 100
    test_case = int(input())
    arr = [[x for x in input()] for _ in range(n)] # 2차원 배열로 다받자

    result = 1 # 결과값은 1로 세팅(문제조건)
    len_pal = 2  # 첫 회문의 길이 세팅

    while len_pal <= 100 and len_pal <= result + 2:
        # while문의 조건 설명
        # len_pal <= 100 회문의길이가 최대 100까지 일 수 있으므로 조건지정
        # len_pal <= result + 2 이 조건을 통해서 실행시간 단축이 가능함 (회문의 속성 이용)
        if discrim(arr, n, len_pal) > result: # 회문의 최대길이를 판별하기 위해 조건문사용
            result = len_pal # 결과값에 최대길이의 회문 저장
        len_pal += 1 # 회문의 길이 +1 하고 while문 돌린다.

    # 가로회문을 확인하기 위한 과정 위와 동일하지만 단지 배열만 zip(*arr)로 회전(?)시켰다
    len_pal = 2
    while len_pal <= 100 and len_pal <= result + 2: # 가로를 찾기위해 한번더한다
        if discrim(list(zip(*arr)), n, len_pal) > result:
            result = len_pal
        len_pal += 1

    print("#{} {}".format(tc+1, result))
```



- 세로를 표현할 떄 `sample2 = [a[i] for a in arr[j:j + M]]`이렇게 표현했다!

```python
#하영
N = 100                     # 행과 열 값

def pal_check(line):        # 회문 판단 함수 (수업시간에 한 것!)
    for idx in range(len(line) // 2):
        if line[idx] != line[-idx - 1]:
            return False
    return True

for tc in range(1, 11):     # 케이스 총 10개
    x = input()             # 날리는 값 (안씀)
    arr = [list(input()) for _ in range(N)]     # 이중배열 받는 line
    maxM = 1 # 가장 긴 회문의 길이를 저장하는 값 (초기값은 1: 'A'하나여도 길이는 1이기 때문)
    M = 2 # 1인 경우는 무조건 있으니까 조사하는 첫 값을 2로 설정
    while M <= 100: # 조사하는 회문의 길이가 100이 넘지 않을 경우 (행, 열 값이 100이므로)
        for i in range(N):  # 인덱싱 (중요!!)
            for j in range(N - M + 1): # 10짜리 열에서 7개짜리 회문 조사하려면 0, 1, 2 idx만 조사 가능
                sample = arr[i][j:j + M] # 가로
                sample2 = [a[i] for a in arr[j:j + M]] # 세로
                if pal_check(sample) or pal_check(sample2): # 가로 세로 중 M길이의 회문이 있을 경우
                    maxM = M # 최대값 교체
                    break  # 찾으면 더 돌릴필요 없으니 break
            if maxM == M:  # 이중포문이라 최대값 확인후 다시 break
                break
        M += 1  # M을 하나 더 늘려서 100까지 돌리는 식 (비 효 율 ㅎ 100에서 줄이는게 더 낫네용)
    print('#{} {}'.format(tc, maxM))
```

- 병훈

```python
def is_palindrome(txt):
    for i in range(len(txt)//2):
        if txt[i]!=txt[len(txt)-1-i]:
            return False
    else:
        return True
 
def get_col(i,j,k):
    #i번째 열의 j행에서  길이 k만큼
    result =''
    for r in range(k):
        result+=txts[j+r][i]
    return result
 
for _ in range(10):
    t = int(input())
    txts  = [input() for _ in range(100)]
    MAX = 0
    for i in range(100):#i번째 행 또는 열
        length = 100
        # 행과 열에서 회문을 찾는다. 길이는 100부터 하나 씩 줄인다
        # i행 혹은 i열에서 회문을 찾는다면 i를 증가시키고 다시 길이를 100으로 만든다.
        while length > MAX:
            for j in range(101-length):
            # i행 j열에서 회문 검사
            # i열 j행에서 회문 검사
                row=txts[i][j:j+length]
                col=get_col(i,j,length)
 
                if is_palindrome(row) or is_palindrome(col):
                    if MAX <len(row):
                        MAX = len(row)
                        length=0
            length-=1
 
    print('#{} {}'.format(t,MAX))
```



