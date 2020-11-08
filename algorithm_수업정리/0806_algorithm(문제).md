# Algorithm

## 부분집합 합(SWEA_4837)

- 처음에는 부분집합 리스트를 따로 만들어서 그 부분집합의  len이 N개 인 것을 골라서 했지만 굳이 그렇게 안해도 SUM과 cnt를 이용하여 더 단순하게 코딩을 만드는 법이 있었다.

```python
#1~12 부분집합 원소
#집합 A의 부분집합 중 N개의 원소를 갖고있음
#원소의 합이 K인 부분집합개수

#집합 A에서 tc를 돌면서
#비트 연산자를 이용 부분집합을 만들고
#그 부분집합의 원소를 하나씩 더하면서 cnt를 하고
#합이 K이고 cnt가 N개인 것의 수를 세어라


T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(A) # 원소의 개수
for tc in range(1,T+1):
    N, K = map(int,input().split())
    res = 0
    for i in range(1<<n): #부분집합의 개수 0에서 2^n전까지 움직임
        SUM = 0# 부분집합 합
        cnt = 0
        for j in range(n): #원소 수만큼 비트를 비교함
            if i & (1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
                SUM += A[j]
                cnt += 1
        if SUM == K and cnt == N:
            res += 1
    print(f'#{tc} {res}')
```

#### **속도가 더빨라지는 방법

- 부분집합 모두를 한 list에 넣고 testcase를 그 밑에 돌리면서 거기서 len으로 개수를 센뒤 구하고자하는 것을 구함

```python
#하영이가 가르쳐줌
# 부분집합 모두를 한 list에 넣고
# testcase를 그 밑에 돌리면서 거기서 len으로 개수를 센뒤 구하고자하는 것을 구함

T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(A) # 원소의 개수
sub = []#담은 부분집합들을 넣을 리스트
for i in range(1 << n): # 부분집합의 개수 0에서 2^n전까지 움직임
    bin =[]#부분집합 한개를 담음
    for j in range(n):  # 원소 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            bin.append(A[j])
    if bin:#bin에 원소가 들어있다면, True
        sub.append(bin)


for tc in range(1,T+1):
    N, K = map(int,input().split())
    cnt = 0
    for s in sub: #sub안의 부분집합들 각각을 빼냄
        if len(s) == N:
            if sum(s) == K:
                cnt += 1
    print(f'#{tc} {cnt}')
```



## 이진탐색(SWEA_4839)

- 이진탐색을 함수로 만들었다, 처음에는 key값보다 크거나 작을때 end값과 start값을 middle-1,middle+1로 줘서 오류가 났다. 아마 값을 1크게 하더라도 나중에 middle을 구하는 과정 중 오류가 나기 때문인 것같다.

```python
#이진탐색을 이용
#전체 쪽수와 A와 B가 찾아야될 숫자를 입력받는다
#A의 이진탐색과 B의 이진탐색 횟수를 비교해서 적은 사람이 이긴다, 비기면 0

def bin_search(P,key):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end) // 2

        #key 값과 같은 경우
        if middle == key:
            return cnt
        #key값보다 큰 경우
        elif middle > key:
            end = middle
        #key값보다 작은 경우
        else:
            start = middle


T = int(input())
for tc in range(1,T+1):
    P, Pa, Pb = map(int,input().split())

    A = bin_search(P,Pa)
    B = bin_search(P,Pb)

    #A의 cnt가 B보다 클때
    if A > B:
        print(f'#{tc} B')
    elif A == B:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A')
```



## 특별한 정렬(SWEA_4843)

- idx를 뽑을때 idx는 홀수일때 짝수일때 모두 aj의 오름차순 내림차순 한 것들의 같은idx를 뽑아야되기 때문에 `i//2`를 해줌

```python
#arr.sort():오름차순 정렬
#arr.sort(reverse = True):내림차순 정렬

#N개의 정수가 주어짐
#제일 앞 가장 큰 수 , 가장 작은수, 2번째 큰수 반복 정렬..
#idx가 짝수이면 내림차순정렬한 aj의 idx를 뽑고, 홀수이면 오름차순정렬한 aj의 idx를 뽑는다.
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    aj = list(map(int,input().split()))
    lis = []
    aj_s = sorted(aj) #오름차순
    aj_b = sorted(aj,reverse = True) #내림차순
    # print(aj_s)
    # print(aj_b)
    for i in range(10): #idx개수만큼 돌거야
        if i % 2 :  #홀수
            lis.append(aj_s[i//2])

        else: #짝수
            lis.append(aj_b[i//2])
    word = ''
    for s in lis:#리스트에서 str로 빼서 나열해줌
        word += ' ' + str(s) #공백을 앞쪽에 넣어서 간격을 띄어줌

    print(f'#{tc}{word}')
```



## 색칠하기(SWEA_4836)

```python
모두 0을 가진 10*10배열이 주어짐
#N개의 영역이 주어지고
#다음줄에 왼쪽 위 모서리 인덱스 r1,c1, 오른쪽 아래 모서리 r2,c2와 색상 정보 color가 나옴
#가로(row) : |r1-r2|,세로(col) : |c1-c2| =>range(c1,c2+1) for문 밑에 range(r1,r2+1) for문으로 사각형을 만들며 수를 넣음
#color = 1(빨강) color = 2(파랑)
#보라색 3이 된것의 개수를 구하라

#1을 가진 영역을 0->+1로 수를 바꿔줌
#2를 가진 영역을 0->+2로 수를 바꿔줌
# 이중 3의 값을 가진 것의 개수를 구함

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    temp = [[0 for col in range(10)] for row in range(10)] # 10*10 2차원배열 0으로 채우기

    N = int(input()) #N개 영역
    puple = 0
    for n in range(N):
        r1,c1,r2,c2,color = map(int,input().split())
        for col in range(c1,c2+1): #세로만큼 가로를 출력해줄거야
            for row in range(r1,r2+1): #세로1당 출력할 가로1
                temp[row][col] += color #열이 같을때 해당하는 컬러만큼을 temp위치에 더함
    for cnt in temp: #temp에 적힌 숫자가 3인것 개수세기
        for i in cnt:#temp안의 list안의 수를 봐야됨
            if i == 3:
                puple += 1
    print(f'#{tc} {puple}')
```



## 파리퇴치(SWEA_2001)

```python
#N*N 2차 배열을 만든다
#그 안의 숫자는 파리의 개수
#M*M 배열은 for문으로 N*N 안을 돌면서 그안에 들어있는 값들의 합을 구함
#M배열의 총 합이 가장 큰 값 구하라
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flies =[]
    #N*N배열에 값을 넣어 만듦
    for n in range(N): #N번 반복할거야
        fly = list(map(int,input().split()))
        flies.append(fly)

    #M*M배열을 구하기
    #시작점을 for문으로 만든다
    #주의! idx값(N)d을 넘어가지 않게 만듦
    MAX = 0
    #시작점(j이 가로, i가 세로) ****제발 적을때 세로부터!
    for i in range(N-M+1): #N-M한 것을 포함해야되니까 +1
        for j in range(N-M+1):
            SUM = 0 #M안의 합
            # N안에 반복될 M값들
            for m in range(i,i+M):
                for n in range(j,j+M):
                    SUM += flies[m][n]
            if MAX < SUM:
                MAX = SUM
    print(f'#{tc} {MAX}')
```

- 함수로 푼 다른 코드

```python
#병훈
def M(arr,n,m):
    MAX = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            flies = 0
            for k in range(m):
                flies += sum(arr[i+k][j:j+m]) ##이코드 대박...이렇게 할 수 있구낭...
            if MAX < flies:
                MAX = flies
    return MAX
for t in range(1,input()+1):
    n,m = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    print(f'#{t} {M(arr,n,m)}')
```





## 패턴 마디의 길이(SWEA_2007)

- 다들 천재...생각은 했지만 코드가 잘 안나와서 참고를 했당....ㅠㅠㅠㅠㅠ

```python
#반복되는 단어의 문자열을 받는다
#1)병훈
#문자열의 문자들을 for문으로 돌아본다
#문자를 하나씩 보면서  다음에 오는 그 길이만큼의 문자가 연결되는지 본다!
#만약에 같은게 나오면 그 길이를 출력하고, 다르다면 하나씩 추가를 해가며 같은지 비교한다.
for t in range(1,int(input())+1): #테스트케이스
     words = input()
     for pattern in range(1,11): #마디의 길이는 최대 10
        # 마디의 길이가 처음부터 i까지 했을 때랑 i부터 i만큼 잘랐을 떼 그 값이 같다면 
        if words[:pattern]==words[pattern:pattern*2]: #단어를 처음부터 마디길이까지 본것 == 다음 마디의 단어가 같을때 마디길이를 출력해라
             print(f'#{t} {pattern}')
             break
#2)하영
#첫단어를 보고 문자열에서 첫단어와 같은 단어가 나오는 곳까지 자름
#그 사이 단어가 바로 뒤의 문자열에서 다시 나오는지 확인
#나온다면 그 단어의 길이를 구하고
#아니라면 그 다음으로 오는 첫단어와 같은 단어까지 자름, 그리고 확인
 T = int(input())
 for i in range(1, T + 1):
     res = 0
     string = input()
     start = string[0]
     for j in range(1, 21): #왜1~20까지일까??
         if start == string[j]: #처음과 같은 단어가 뒤에 나오는지 찾고
             length = j #같다면 마디길이=j이고
             if string[: j] == string[j: j + length]:#만약 처음부터j까지의 단어가 j부터 마디길이까지가 같다면 그 길이를 출력해라
                 res = length
                 break
     print(f'#{i} {res}')
```





## 파스칼삼각형(SWEA_2005)

```python
#파스칼삼각형은 조합으로 푼다(이현우's 아이디어)
#펙토리얼 함수를 재귀로 만든다
#nCr = n!/r!*(n-r)!
#N번만큼 for문돌리면서 그 밑의 for문도 n번만큼 돌린다

import sys
sys.stdin = open("input.txt", "r")


#팩토리얼 재귀함수 만들기
def fact(n):
    if n <= 1: #n이 1이하이면 1을 return함
        return 1
    else:
        return n*fact(n-1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            result = fact(i)/(fact(j)*fact(i-j))
            print(f'{int(result)}',end = ' ') #같은 i의 j들은 서로 띄어쓰고
        print() #i가 달라지면 줄바꿈
    # print()#각 테스트케이스들 끼리 줄바꿈
```



## 초심자의 회문 검사(SWEA_1989)

- 이건 다행히 한번에 잘 풀었다😂

```python
#단어를 앞에서 봤을 때랑 뒤부터 봤을때 같다면
#회문 1 출력, 아니라면 0 출력
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    word = input()
    if word[:] == word[::-1]: #word를 그냥 본것과 거꾸로 본 것이 같다면
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
```

