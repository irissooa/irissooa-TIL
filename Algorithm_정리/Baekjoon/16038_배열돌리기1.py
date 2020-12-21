'''
배열을 돌릴때 배열의 테두리만 돌리고 N과 M중 작은 값의 2를나눈 몫만큼 돌아가면서 for문의 범위가 줄어든다.
for의 범위를 num(한번돌면 +1해서 돌아가는 배열을 좁힐 변수)~배열의크기-num으로 돌림
그리고 temp라는 배열을 만들어서
제일 처음 열이고 행이 처음부터 마지막-1행은 아래(행+1)로 이동
행이 마지막이고 열이 처음부터 마지막-1열은 오른쪽(열+1)로 이동
열이 마지막이고 행이 처음+1부터 마지막행은 위쪽(행-1)로 이동
행이 처음이고 열이 처음을 제외하고 왼쪽(열-1)으로 이동

이렇게 하면 한번 회전됨!
이거를 함수로 만들어서 회전 수 R번이 주어지면 그만큼 돌게 만들자!
# '''
# import sys
# sys.stdin = open('input.txt','r')
from pprint import pprint
# import copy

def rotate(arr):
    num = 0
    #돌린 arr을 담을 배열
    temp = [[0 for j in range(M)] for i in range(N)]

    while min(N,M)//2 > num:
    # for n in range(min(N,M)//2):
        for i in range(num,N-num):
            # 제일 처음 열이고 행이 처음부터 마지막-1행은 아래(행+1)로 이동
            if i != N-num-1:
                temp[i+1][num] = arr[i][num]
        for j in range(num,N-num):
            # 행이 마지막이고 열이 처음부터 마지막-1열은 오른쪽(열+1)로 이동
            if j !=M-num-1:
                temp[N-num-1][j+1] = arr[N-num-1][j]
        for i in range(num,N-num):
            # 열이 마지막이고 행이 처음+1부터 마지막행은 위쪽(행-1)로 이동
            if i != num:
                temp[i-1][M-num-1] = arr[i][M-num-1]
        for j in range(num,N-num):
            # 행이 처음이고 열이 처음을 제외하고 왼쪽(열-1)으로 이동
            if j != num:
                temp[num][j-1] = arr[num][j]
        #한범위의 테두리를 전부 돌면 num을 +1해서 범위를 좁혀줌
        num += 1
    return temp

#배열의 크기 N,M, 회전수 R
N,M,R = map(int,input().split())

#배열
arr = [list(map(int,input().split())) for _ in range(N)]
# temp = copy.deepcopy(arr)
for r in range(R):
    ans = rotate(arr)
    arr = ans
# print(ans)
for i in range(N):
    for j in range(M):
        print(ans[i][j],end=' ')
    print()

