'''
2020-12-03 19:20
최종적으로 2048을 만들어내는것이 목표
한번 타일을 밀때 상하좌우로 정해서 밀어야됨
방향을 정하면 모든 타일이 그 방향으로 밀림
밀리는 방향이 같고 겹칠때 두 타일에 적힌 숫자가 같다면 합쳐져 그 숫자 합의 타일이 새로됨(2개만)
만약 같은 숫자가 적힌 타일이 3개 이상일 경우 빨리 벽에 닿게 될 타일을 먼저 민다고 생각하자
격자에서 어떻게 타일을 이동시킬지 방향이 주어질때
타일을 모두 이동시키고 나면 격자가 어떻게 바뀌는지 출력

S를 입력받고 up,down,left, right에 따라 타일 이동 방향을 정함
방향에 따라 값이 있으면 순서대로 q에 담고, pop해서 보면서 같으면 더해서 담아주고
다르면 그냥 담아줌
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque
di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def move(S):
    if S == 'up':
        for i in range(N):
            q = deque()
            for j in range(N):
                if arr[j][i]:
                    q.append(arr[j][i])
            idx = 0
            while q:
                if len(q)>1:
                    a,b = q.popleft(),q.popleft()
                    if a == b:
                        temp[idx][i] = a+b
                    else:
                        temp[idx][i] = a
                        # 제일앞에 다시 넣어줌->다음수와비교해야되니까
                        q.appendleft(b)
                    idx +=1
                else:
                    c=q.popleft()
                    temp[idx][i] = c

    if S == 'down':
        for i in range(N):
            q = deque()
            for j in range(N-1,-1,-1):
                if arr[j][i]:
                    q.append(arr[j][i])
            idx = N-1
            while q:
                if len(q)>1:
                    a,b = q.popleft(),q.popleft()
                    if a == b:
                        temp[idx][i] = a+b
                    else:
                        temp[idx][i] = a
                        q.appendleft(b)
                    idx -=1
                else:
                    c=q.popleft()
                    temp[idx][i] = c

    if S == 'left':
        for i in range(N):
            q = deque()
            for j in range(N):
                if arr[i][j]:
                    q.append(arr[i][j])
            idx = 0
            while q:
                if len(q)>1:
                    a,b = q.popleft(),q.popleft()
                    if a == b:
                        temp[i][idx] = a+b
                    else:
                        temp[i][idx] = a
                        q.appendleft(b)
                    idx +=1
                else:
                    c=q.popleft()
                    temp[i][idx] = c

    if S == 'right':
        for i in range(N):
            q = deque()
            for j in range(N-1,-1,-1):
                if arr[i][j]:
                    q.append(arr[i][j])
            idx = N-1
            while q:
                if len(q)>1:
                    a,b = q.popleft(),q.popleft()
                    if a == b:
                        temp[i][idx] = a+b
                    else:
                        temp[i][idx] = a
                        q.appendleft(b)
                    idx -=1
                else:
                    c=q.popleft()
                    temp[i][idx] = c

T = int(input())
for tc in range(1,T+1):
    N,S = list(input().split())
    N = int(N)
    arr = [list(map(int,input().split())) for _ in range(N)]
    temp = [[0 for j in range(N)] for i in range(N)]

    move(S)
    print('#{}'.format(tc))
    for x in temp:
        print(*x)