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