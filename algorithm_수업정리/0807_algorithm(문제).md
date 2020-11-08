# Algorithm

## 2차배열 순회

- 사각영역 순회

- 기준점 탐색 

  - 델타 탐색 이용,* bfs(너비우선탐색), *dfs(깊이우선탐색)
  - 시뮬레이션 문제

- 대각, 테두리 탐색

  

## 스도쿠 검증

- 중복을 제거하는 `set()`을 이용해서 문제 풀기

```python
#9*9 스도쿠 2차배열을 입력받아 완성시킨다
#이때 같은 줄 세로 i가 1~9가 한번씩 다 들어가있는지 확인하는데=> 중복을 제거하는 set을 이용!
#가로 j도 1~9까지 한번씩 다들어있는지 확인 => set의 len이 9인지 확인
#이때 더 소규모로 3*3도 1~9가 한번씩 들어가 있는지 확인해야됨 => set의 len이 9인지 확인
#3*3이 9*9에 위치할 초기값들을 설정하고, 그 안의 수들이 1~9까지 하나씩만 있는지 확인 =>arr[i][j]가 len ==9인지 확인

for tc in range(1,int(input())+1):
    arr = [list(map(int,input().split())) for _ in range(9)] #가로입력되는 값을 세로9만큼 반복
    #세로에 1~9까지 들어있는지 확인하는데 가로도 1~9까지 들어있는지 확인
    #수를 담을 set을 만든다
    result = 1
    for x in range(9):
        row = set() #가로
        col = set() #세로
        for y in range(9): 
            row.add(arr[x][y]) #행
            col.add(arr[y][x]) #열
        if len(row) != 9:
            result = 0
            break #스도쿠가 아니니까 끝
        if len(col) != 9:
            result = 0
            break
 
    trg = 0
    for x in range(0,9,3): #3*3의 세로 값은 3씩 더해짐
        for y in range(0,9,3):
            rec = set()
            for i in range(3):
                for j in range(3):
                    rec.add(arr[x+i][y+j])
            if len(rec) != 9:
                result = 0
                trg = 1 #하나라도 trg 1이면 빠져나가도록
                break #이미 스도쿠가 없으니까 끝
        if trg :#trg값이 1이냐 1이면 빠져나와라 #이미 그전에 스도쿠가 아니라면 빠져나와라
            break

    print(f'#{tc} {result}')
```



## 지그재그숫자(SWEA_1986)

- 이거는 생각한대로 나왔당!ㅎㅎ

```python
#1부터 N까지 숫자에서 홀수는더하고 짝수는 뺏을 때 최종 누적된 값 구하기
#1부터N까지 for문을 돌리면서
#한 빈리스트에 수들을 넣는데
#n값이 홀수는 -를 붙이고 전체 합을 구해보자

for tc in range(1,int(input())+1):
    arr = []
    for n in range(1,int(input())+1):
        if n % 2 == 0: #짝수일때 빼자, 앞에 -를 붙이자
           arr.append(-n)
        else:
            arr.append(n)
    print(f'#{tc} {sum(arr)}')
```

- (#의수) 이거도 list말고 sum으로 홀수면 더하고 짝수면 빼는 방식도 가능

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sum1 = 0
    for x in range(1, N+1):
        if x % 2 == 1:
            sum1 += x
        else:
            sum1 -= x
    print(f'#{tc} {sum1}')
```



## 중간 평균값 구하기(SWEA_1984)

- 이거도 생각한대로 나왔당!
- round()로 반올림을 해주고 int로 바꿔줘야 된다

```python
#10개의 수를 입력받아 그 중 최대의 수와 최소의 수를 제외한 나머지 평균값을 출력하는 프로그램
#소수점 첫째지리에서 반올림

for tc in range(1,int(input())+1):
    arr = list(map(int,input().split()))
    MAX = max(arr)
    MIN = min(arr)
    avg = int(round((sum(arr)-MAX-MIN)/(len(arr)-2),0))
    print(f'#{tc} {avg}')
```

- 이렇게도 풀수 있구낭..

```python
#병훈
for t in range(1,int(input())+1):
    num = sorted(list(map(int,input().split())))[1:9] #정렬을 해서 제일 큰값,작은값빼기
    print(f'#{t} {round(sum(num)/len(num))}')
```



## 조교의 성적 매기기(SWEA_1983)

- 이건 조금 걸렸당.. 그래도 혼자서 풀었다:)

```python
import sys
sys.stdin = open("input.txt", "r")
#학점은 상대평가
#총 10개의 평점
#학점: 총범 = 중간고사(35%)+기말(45%) + 과제(20%
#10개의 평점은 총번이 높은순
#각각 평점은 같은 비율로 부여될 수 있음 N명의 학생이 있다면 N/10명의 학생들에게 평점 무여
#학점을 알고 싶은 K번째 학생의 번호가 주어짐, 학점 출력
#N은 항상 10의 배수
#K번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 주어지지 않음

# N명과 K학생 번호를 받음
# 아래의 중간고사, 기말, 과제 점수를 받고 총점을 계산
#총점을 하나의 list에 담음
#그 리스트의 학생수/10한 만큼 각 학점을 부여함
#k번째 학생과 동일한 점수는 없으니, 그 점수를 저장해 놓고
#점수가 높은 순으로 내림차순 해서, 비율만큼 자르고, 학점을 부여함
#k의 점수가 있는 부분의 학점을 출력

for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    arr = []
    for i in range(N):
        mid, final, hw = map(int,input().split())
        total = mid*0.35 + final*0.45 + hw*0.2
        arr.append(total)
    res = arr[K-1] #K번째는 idx값으로는 1빼줘야됨, k번째 점수를 grade에 저장해둠
    arr_b = sorted(arr,reverse = True) #내림차순으로 정렬
    ratio = N//10 #학점을 줄 비율
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0', 'C-','D0']
    for i in range(len(grade)): # grade는 N/10 비율로 나눈 것이기 때문에 그만큼 범위를 나눌거야
        for idx in range(ratio*i,ratio*(i+1)): #ratio에서 ratio만큼 범위까지
            # arr의 ratio범위만큼 grade 설정
            if arr_b[idx] == res: #K번째 값이 들어오면 그 grade를 출력해라
                print(f'#{tc} {grade[i]}')
                break
```



- 병훈 천사님...주석 달아주심...🤣

```python
def get_total_score(scores): #입력받은 점수를 비율에 따라 총점 만들기
    rates = [0.35, 0.45, 0.2]
    score = 0
    for j in range(3):
        score += scores[j] * rates[j]
    return  score
 
 
final_score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for t in range(1,int(input())+1):
 
    N,K = map(int,input().split()) #학생의 수, 출력하고 싶은 학생의 번호
    arr = [] #N 명의 학생들 점수를 총점으로 변환한 점수를 담고 있는 배열
 
    for i in range(N):
        score = get_total_score(list(map(int, input().split())))
        arr.append([score,i])
        # 나중에 K 번째 학생의 점수를 찾기 위해 i를 같이 append한다,
        # enumerate 함수를 써도 된다!
 
    arr.sort(key=lambda x: x[0],reverse=True)
    # 학생들의 총점을 내림차순으로 정렬한다.
    # 이때 arr 배열에는 [[74.6,0],[92.5,1],[88.8,2]...] 이렇게 자료가 있는데
    # 총점을 기준으로 정렬하고 싶기 때문에 sort함수의 key argument를 활용해 기준을 정한다
    # 그 기준은 각각의 요소들 [74.6,0] [92.5,1]...[score,i] 에서 첫 번째 요소인 score가 기준이다
    # key = lambda x : x[0] 를 통해서 score를 기준으로 정렬하도록 만든다.
    # 또한 내림차순으로 정렬하기 때문에 reverse = True
    for i in range(N):
        if arr[i][1] == K-1:
        # 총점을 기준으로 내림차순으로정렬된 arr 안에서 K 번째 학생을 찾는다.
            print(f'#{t} {final_score[ i // (N//10)]}')
            # 그 K 번째 학생의 성적을 입력하기 위해서는
            # 10명의 학생이 있다면 각각 성적 A+, A0, A- ... 은 1명
            # 20명의 학생이 있다면 각각 성적 2명
            # N명의 학생이라면 N//2 명씩이다
 
            # 내림차순으로 정렬되어 있기 때문에 i 는 등수를 의미한다.
            # 10명 중 i 등이면 [A+, A0, A- ..] 의 i 번째 성적을 받는다.
            # 20명 중 i 등이면 [A+, A0, A- ..] 의 i//2 번째 성적을 받는다. (1등도 A+ 2등도 A+)
            #  N명 중 i 등이면 [A+, A0, A- ..] 의 i//(N//10)  번째 성적을 받는다.

```

- 하영👍👍

```python
import math
 
T = int(input())
 
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = []
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):
        m, f, a = map(int, input().split())
        scores.append([i + 1, m * 0.35 + f * 0.45 + a * 0.2])
    scores = sorted(scores, key = lambda x : -x[1])
    for i in range(N):
        if K == scores[i][0]:
            idx = i + 1
            break
    rank = idx * 10 / N
    val = math.ceil(rank)
    print(f'#{tc} {grades[val - 1]}')
```



## 행렬찾기

- 이건 다음에도 다시 풀어보기........ㅠ