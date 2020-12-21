'''
NxN배열에 숫자가 들어있음
한줄에 하나씩 N개의 숫자를 골라 합이 최소가 되게하려함
한줄에 하나, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없음.
'''
import sys
sys.stdin = open('input.txt','r')

def perm(i,sum):
    global MIN
    # sum이 MIN보다 크거나 같으면 종료
    if sum >= MIN:
        return
    #idx가 N과 같아지면
    if i == N:
        #저장된 MIN과 sum을 비교해서 MIN보다 작으면 갱신함
        if MIN > sum:
            MIN = sum
        return
    
    for k in range(N):
        #방문표시 했다면 지나가라
        if visited[k]:
            continue
        #방문을 했다고 표시
        visited[k] = True
        #다음 idx로 함수 호출, 그 값을 더해준것을 같이 보냄
        perm(i+1,sum+board[i][k])
        #다시 방문 표시 원상 복구
        visited[k] = False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for i in range(N)]
    visited = [False for i in range(N)]
    MIN = 9999999
    select = [-1 for i in range(N)]
    perm(0,0)
    print('#{} {}'.format(tc,MIN))

#선생님 코드
#순열을 하려면 열값을 [0,1,2,....N-1]까지 각 idx에 있는 값을 행의 같은 idx에 저장!
#이렇게 하면 7개에서 timeerror!
def perm(k):
    if k == N:
        S = 0
        for r,c in enumerate(cols):
            S += arr[r][c]
        global ans;ans = min(ans,S)
    else:
        for i in range(k,N):
        #k idx의 위치를 기준으로!
		    cols[k], cols[i] = cols[i], cols[k]
            perm(k+1) #다음 idx로 넘어감
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(int(int(input()))+1):
    N = int(input())
    arr = [list(map(int,input().split())) for_ in range(N)]
    cols = [i for i in range(N)]
    ans = 0xffffff
    perm(0)
    
#가지치기 -> 이렇게 하면 9개에서 timeerror
def perm(k,cur_sum): #cur_sum : 0~k-1행에 선택한 값들의 합
    global ans
    if k == N:
        ans = min(ans,cur_sum)

    else:
        for i in range(k,N):
        #k idx의 위치를 기준으로!
		    cols[k], cols[i] = cols[i], cols[k]
        #K행에 선택한 열값은 cols의 [k]idx에 있다!
            perm(k+1,cur_sum + arr[k][cols[k]]) #다음 idx로 넘어감
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(int(int(input()))+1):
    N = int(input())
    arr = [list(map(int,input().split())) for_ in range(N)]
    cols = [i for i in range(N)]
    ans = 0xffffff
    perm(0,0)

#가지치기는 함수 호출 전 어디서든 적어도 됨!, 그 이전의 자기를 호출한 함수로 돌아감!
#지금까지 발견한 가장 좋은 해를 저장!
#탐색을 하다가 지금까지 가장 좋은 해와 비교했더니 이미 크면 더 안가봐도 되므로 바로 끊음!
#아직 확인안해본 곳을 봐라!
def perm(k,cur_sum): #cur_sum : 0~k-1행에 선택한 값들의 합
    global ans
    #가지치기
    if ans <= cur_sum:
        return #더이상 보지않고, 안해본 다른 선택지를 보러감

    if k == N:
        ans = min(ans,cur_sum)

    else:
        for i in range(k,N):
        #k idx의 위치를 기준으로!
		    cols[k], cols[i] = cols[i], cols[k]
        #K행에 선택한 열값은 cols의 [k]idx에 있다!
            perm(k+1,cur_sum + arr[k][cols[k]]) #다음 idx로 넘어감
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(int(int(input()))+1):
    N = int(input())
    arr = [list(map(int,input().split())) for_ in range(N)]
    cols = [i for i in range(N)]
    ans = 0xffffff
    perm(0,0)
