#N*N을 2차배열로 만든다
#가로의 길이가 k만큼인 것이 몇개인지 구하라
#2차배열을 받고
#가로를 보는데 만약 1이 나왔을 때 그담이 0이면 그사이 수를 세어본다
#그렇게 나온 합들이 K인지 확인, K라면 result += 1을 해라
#세로도 마찬가지로 진행한다

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    arr = []

    result = 0
    for _ in range(N):
        temp = list(map(int,input().split()))
        arr.append(temp)

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if cnt == K:
                    result += 1
            else:  # 값이 0일때
                cnt = 0
            if cnt > K: #cnt가 K가 넘으면
                result -= 1 #위에서 더해졌던걸 하나 빼주고 cnt를 리셋시켜라
                cnt = 0 #그 뒤에 맞는 단어가 있을 수 있음

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == K:
                    result += 1
            else:  # 값이 0일때
                cnt = 0
            if cnt > K: #cnt가 K가 넘으면
                result -= 1 #위에서 더해졌던걸 하나 빼주고 cnt를 리셋시켜라
                cnt = 0


    print(f'#{tc} {result}')

#병훈
# find_row 함수는 행에서 단어가 들어갈 수 있는곳 찾기
# N*N 행렬
# index 0인  열에서는 1이 K개 나오고 0이 K+1 번째  나와야한다
# index 마지막 열에서는 1이 K개 나오고 N-1-K 번째 열이 0
# 나머지는 0 1 1 1 1 ...(K개) 0
# find_col 함수는 입력된 행렬을 90도 시계방향 회전 후 find_row 함수 호출
def find_row(arr, K):
    count = 0
    for i in range(N):
        if sum(arr[i][0:K]) == K and arr[i][K] == 0:
            count += 1
        if sum(arr[i][N - K:N]) == K and arr[i][N - K - 1] == 0:
            count += 1
        for j in range(1, N - K):
            if sum(arr[i][j:j + K]) == K and arr[i][j - 1] == 0 and arr[i][j + K] == 0:
                count += 1
    return count


def find_col(arr, K):
    rot_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot_arr[i][j] = arr[N - 1 - j][i]
    return find_row(rot_arr, K)


for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {find_row(arr, K) + find_col(arr, K)}')

#의수
def ro90(li):
    tmp = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            tmp[y][N - x - 1] = li[x][y]
    return tmp


def discrim(lists):
    for x in range(N):
        global res
        cnt = 0
        for y in range(N):
            if lists[x][y]:
                cnt += 1
                if y == N - 1 and cnt == target:
                    res += 1
                    cnt = 0
            else:
                if cnt == target:
                    res += 1
                cnt = 0
    return res


for tc in range(1, int(input()) + 1):
    N, target = map(int, input().split())
    puz = [[int(x) for x in input().split()] for _ in range(N)]
    res = 0
    a = discrim(puz)
    res = 0
    b = discrim(ro90(puz))
    print(f'#{tc} {a + b}')