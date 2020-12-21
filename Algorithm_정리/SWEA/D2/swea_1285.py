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