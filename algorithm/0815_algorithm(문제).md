# SWEA

## 1945. 간단한 소인수분해

```python
# 숫자 N을 입력받고 소수인 2,3,5,7,11 중 작은 소인수부터 차례로나누며 몫이 소수가 되면 멈춤
#나눈 소수들과 마지막 몫을 곱으로 나타냄
# 그소수들의 지수들을 출력하라

#숫자 N을 입력받고  소수 2,3,5,7,11을 리스트로 만듦
#숫자N을 리스트중 작은 소수들 순으로 나눔
#나누어떨어지지 않을 때까지 나눈 것의 수를 셈
#나누어떨어지지 않는다면 다음 수로 나눔 그렇게 개수를 세서 출력!!

import sys
sys.stdin = open("input.txt", "r")

numbers = [2,3,5,7,11]
for tc in range(1,int(input())+1):
    N = int(input())
    p_num = []
    for number in numbers:
        cnt = 0
        while True:
            if N % number == 0:
                N //= number
                cnt += 1
            else:
                break
        p_num.append(cnt)
    p_num = ' '.join(map(str,p_num))
    print(f'#{tc} {p_num}')
```



## 1940. 가랏! RC카!

```python
# RC카가 현재속도를 유지할지(0) 가속(1)을 하는지 감속(2)을 하는지와 가속도의 값을 추가로 입력받는다
#초기속도인 0m/s에 더하거나 뻄
#거리 = 속도*시간
#N초를 입력받고 매초마다 한줄씩 속도를 어떻게 할지와 가속도가 주어짐
#0부터 시작해서 가속을 한다면 가속도값을 더해주고, 감속을한다면 빼주되 0보다 내려가면 0이다, 유지한다면 그대로 유지시켜라
#시간은 모두 1초씩 곱하고 거리를 계산해서 계속 더해줘라
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    RC_v = 0
    s = 0 #거리 초기값
    for n in range(int(input())):
        command_list= list(map(int,input().split()))
        if command_list[0] == 1:
            RC_v += command_list[1] #가속도 값을 더함
        elif command_list[0] == 2:
            RC_v -= command_list[1] #감속하니까 가속도값을 뺌
            if RC_v <= 0:
                RC_v = 0 #0보다 속도가 작아지면 0으로 함
        s += 1 * RC_v #거리 = 시간(1초) * 속도
    print(f'#{tc} {s}')
```



## 1288. 새로운 불면증 치료법

```python
#N을 입력받고 양세기를 N배수번 하는데 N배수의 자릿수를 한 set()에 넣고 그 set()이 0부터 9까지 들어가면 양세기를 멈추고 gop을 출력
#빈 set()을 만듦
#set()이 0,1,2,3,4,5,6,7,8,9가 되면 멈추는 while문을 만듦
#N배수의 각 자릿수를 set에 넣음
#다 넣으면 1씩 더해서 *1 *2 *3 ..을 해서 set에 0~9가 다 들어갈때까지 반복함

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    num_set = set()
    N = int(input())
    k = 0 #k배
    gop = 0
    sort_set = []
    while True:
        if sort_set == [0,1,2,3,4,5,6,7,8,9]:
            break
        else:
            k += 1
            gop = N * k
            for n in str(gop): #N을 문자로 받고 각 숫자들을 set에 넣는다
                num_set.add(int(n))
            sort_set = sorted(num_set)
    print(f'#{tc} {gop}')
```

- 다른 코드

```python
#의수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # str로 바로 받을까 생각했는데 숫자의 연산이 이루어져야 하기 때문에 우선 숫자로 받는다.
     
    index = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} # 비교를 하기 위해 인덱스를 설정!
    temp = [] # 빈 리스트 초기화
    step = 0 # 단계 초기화
     
    while True: 
        step += 1 # 몇단계 까지 갈까
        num = N * step # num = 입력값 * 단계, 여기서 숫자의 연산이 이루어져야 하기 때문에 처음에 N을 인트로 받은것
         
        num_str = str(num) # set이랑 비교하기 위해서는 int를  str로 바꿔줘야한다
        temp.extend(num_str) # temp에 계속 추가하자 
        
        res = set(temp) # 중복제거하기위해 set을 사용  
        if res == index: # 중복제거한 결과와 인덱스 비교해서 같으면 와일문 탈출
            break
    print(f'#{tc} {num}')
```

- 다른 코드

```python
#병훈
for t in range(1,int(input())+1):
    N = int(input())
    zero_to_nine = [False]*10
    count = 1
 
    while sum(zero_to_nine) != 10:
        N_sheep = N * count
        str_N_sheep = str(N_sheep)
 
        for n in str_N_sheep:
            zero_to_nine[int(n)]=True
 
        count+=1
 
    print(f'#{t} {N_sheep}')
```



## 1284. 수도 요금 경쟁

```python
# A,B 두 수도 회사 중 수도요금 적게 부담해도 되는 회사를 고르자
# A사는 1L당 P원
#B사는 R리터까지는 Q원, 이후부터는 1L당 S원
#한달간 사용하는 수도의 양이 WL
#P,Q,R,S,W를 입력받는다
#A는 W*P원
#B는 W가 R이하면 Q원 이상이면 (W-R)*S를 해줌

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    P,Q,R,S,W = map(int,input().split())
    A = P*W
    money = 0
    if W <= R :
        B = Q
    else:
        B = Q + (W-R)*S
    if A > B:
        money = B
    else:
        money = A
    print(f'#{tc} {money}')
```



## 1285. 아름이의 돌던지기

```python
#+-100,000에서 최대한 0에 가까운 위치로 돌을 던지려고 함
#N명의 사람들이 돌은던질때 가장 0에 가까운 돌이 떨어진 위치와 0사이의 거리 차이와 몇명이 그렇게 돌을 던졌는가?
# N개의 돌을 입력받음
#절댓값이 0과 가까운 것을 고르고 그것의 개수를 셈
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N = int(input())
    rock = []
    rock_nums = list(map(int,input().split()))
    for n in rock_nums:
        n = abs(n)
        rock.append(n) #입력받은 것의 절댓값을 리스트에 넣음
    best = rock[0] #가장 가까이 던진 돌의 최솟값

    cnt = 0 # 개수 초기값
    for r in rock:
        if r < best:
            best = r #최소값보다 수가 작으면 갱신하고 개수를 리셋
            cnt = 1
        elif r == best:
            cnt += 1 #같다면 개수를 셈
    print(f'#{tc} {best} {cnt}')
```

- 다른 코드

```python
#의수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    stone_throw = list(map(int, input().split())) # 입력데이터를 받자 받자
    min_stone = abs(stone_throw[0]) # 첫번째 입력데이터의 절댓값을 변수에 저장
    cnt = 0 # 최소데이터가 몇번 나오는지 카운트 하기 위해 존재
    for stone in stone_throw: # 리스트를 하나씩 까보자
        if min_stone > abs(stone): # 꺼낸 데이터의 절댓값이 최솟값보다 작으면
            cnt = 1 # 카운트 1로 초기화
            min_stone = abs(stone) # 최솟값에 꺼낸 데이터의 절댓값 저장
        elif min_stone == abs(stone): # 최솟값 데이터와 꺼낸 데이터의 값이 같다면
            cnt += 1 # 카운트 +1 
    print(f'#{tc} {min_stone} {cnt}')
```

