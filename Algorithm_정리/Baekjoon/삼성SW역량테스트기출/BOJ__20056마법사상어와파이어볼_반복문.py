'''
00:10
NxN 파이어볼 M개 r행 x열 질량 m, 방향 d, 속력 s
8방향 이동 상,우상,우,우하,하,좌하,좌,좌상
1. 모든 파이어볼 자신의 방향 d로 속력 s칸만큼 이동(이동하는 중, 같은칸 여러개의 파이어볼 있을 수 있음)
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있다면,
2. 같은 칸에 있는 파이어볼은 하나로 합쳐짐
3. 파이어볼은 4개의 파이어볼로 나누어짐
4. 나누어진 파이어볼의 질량, 속력, 방향
4-1. 질량은 [(합쳐진 파이어볼 질량의 합)/5]
4-2 속력은 [(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)]
속력 %N번 하면 최소 움직이는횟수가 나오고 만약 범위를 벗어나면 +N(왼쪽방향), -N(오른쪽방향)을 해주면 됨!
4-3 합쳐지는 파이어볼의 방향이 모두 홀수, 모두 짝수, 방향은 0,2,4,6이 됨,
그렇지 않으면 1,3,5,7이 됨
5. 질량이 0인 파이어볼은 소멸
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합!

1. 배열에 놓고 각 방향으로 질량을 가지고, 속력 개수만큼 이동!
ni = r-1 + di[d]
nj = c-1 + dj[d]
2.이동이 끝난뒤 2개이상의 파이어볼이 같은 위치에 있다면 하나로 합쳐지고, 질량, 속력, 방향을 구함
3. 그런뒤에 4방향으로 이동시킴 - 이과정을 K번 반복한 뒤 남아있는 파이어볼 질량의 합! 구하기(질량0-소멸)
'''
import sys
from collections import deque
input = sys.stdin.readline
di = [-1,-1,0,1,1,1,0,-1] #상(0),우상(1),우(2),우하(3),하(4),좌하(5),좌(6),좌상(7)
dj = [0,1,1,1,0,-1,-1,-1]


N,M,K = map(int,input().split())
arr = [[[] for j in range(N)] for i in range(N)]
#r-1,c-1,m,s,d
cnt = 0
ans = 0
for i in range(M):
    r,c,m,s,d = map(int,input().split())
    arr[r-1][c-1].append([m,s,d])

for _ in range(K):
    temp = [[[] for c in range(N)] for r in range(N)]
    #공 움직이기
    for i in range(N):
        for j in range(N):
            #해당 배열에 공이 있으면!
            if arr[i][j]:
                while arr[i][j]:
                    # print(arr[i][j])
                    pm,ps,pd = arr[i][j].pop()
                    ni = (i + di[pd]*ps)%N
                    nj = (j + dj[pd]*ps)%N
                    temp[ni][nj].append([pm,ps,pd])
    #공 합치기
    for i in range(N):
        for j in range(N):
            if temp[i][j]:
                ball_cnt = len(temp[i][j])
                ball_m = 0
                ball_s = 0
                odd = 0
                while temp[i][j]:
                    pm,ps,pd = temp[i][j].pop()
                    if ball_cnt==1:
                        arr[i][j].append([pm,ps,pd])
                        break
                    ball_m += pm
                    ball_s += ps
                    if pd % 2:
                        odd += 1
                ball_m = ball_m // 5
                ball_s = ball_s // ball_cnt
                if odd == ball_cnt or odd == 0:
                    D = [0,2,4,6]
                else:
                    D = [1,3,5,7]
                if ball_cnt >= 2:
                    if ball_m > 0:
                        for d in D:
                            arr[i][j].append([ball_m,ball_s,d])
ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            for x in arr[i][j]:
                ans += x[0]
                # print(x)
print(ans)