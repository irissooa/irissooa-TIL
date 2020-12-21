'''
20-12-13 14:16-14:45(밥-15:50)-18
토네이도가 x->y로 이동할때
y의 모래는 x의 위아래 1%만큼
y의 아래 위 7%만큼, 두칸 아래 위 2%
x->y진행방향 옆 ->a의 아래 위 10%, ->한칸 더 5%
a는 y의 55%모래를 더함
모두 소수점은 버림
범위를 벗어나는 모래의 수를 모두 더함

1. arr[N//2-1][N//2-1]에서 시작
2. 좌, 하, 우, 상 으로 움직임! 칸수 1,1,2,2,3,3,4,4,5,5,6,6 이렇게 움직임
3. 가야될칸만큼 갔을때 flag = true,  flag가 true이고 같은 수의 칸만큼 가면 칸수 다시 리셋한 뒤 가야될칸수  += 1, flag=false로 리셋
4. 이동을 할때 계산할 모래 값을 arr[ni][nj]로 갱신하고 그 그 값의 1%는 arr[pi][pj]의  아래 위에 1%.
arr[ni][nj]아래위 한칸에 7%, 두칸아래위 2%,
arr[ni][nj]의 방향만큼 한칸 더 간 곳에서 55%를 담고, 그 아래 위 10%,
그 한칸 더간 곳의 방향으로 한칸을 더 가서 5%.....
이것을 함수로 만들어서,,
pd가 0왼쪽일때
1% : (ni-1,nj+1),(ni+1,nj+1) // 7% : (ni-1,nj),(ni+1,nj) //2% : (ni-2,nj),(ni+2,nj) // 55% : (ni,nj-1) // 10% : (ni-1,nj-1),(ni+1,nj-1)//5%:(ni,nj-2)
pd가 2오른쪽
1% : (ni-1,nj-1),(ni+1,nj-1) // 7% : (ni-1,nj),(ni+1,nj) //2% : (ni-2,nj),(ni+2,nj) // 55% : (ni,nj+1) // 10% : (ni-1,nj+1),(ni+1,nj+1)//5%:(ni,nj+2)
pd가 3위
1% : (ni+1,nj-1),(ni+1,nj+1) // 7% : (ni,nj-1),(ni,nj+1) //2% : (ni,nj-2),(ni,nj+2) // 55% : (ni-1,nj) // 10% : (ni-1,nj-1),(ni-1,nj+1)//5%:(ni-2,nj)
pd가 1아래
1% : (ni-1,nj-1),(ni-1,nj+1) // 7% : (ni,nj-1),(ni,nj+1) //2% : (ni,nj-2),(ni,nj+2) // 55% : (ni+1,nj) // 10% : (ni+1,nj-1),(ni+1,nj+1)//5%:(ni+2,nj)
범위체크 다해주고 갈수 없다면 나간 모래 += 그 값만큼
bfs로 풀어보쟈...
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque
di = [0,1,0,-1] #좌하우상
dj = [-1,0,1,0]

tornado = [[(-1,1,0.01),(1,1,0.01),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,-1,0.1),(1,-1,0.1),(0,-2,0.05),(0,-1,0)],
    [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.1),(1,1,0.1),(2,0,0.05),(1,0,0)],
    [(-1,-1,0.01),(1,-1,0.01),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,1,0.1),(1,1,0.1),(0,2,0.05),(0,1,0)],
    [(1,-1,0.01),(1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(-1,-1,0.1),(-1,1,0.1),(-2,0,0.05),(-1,0,0)]]

def check(i,j,sand,per,remain):
    global outsand
    if i < 0 or i >= N or j < 0 or j >= N:
        if per == 0:
            outsand += remain
        else:
            outsand += int(sand*per)
        # print('나간거',int(sand*per),outsand)
    else:
        if per == 0:
            arr[i][j] += remain
            # print(remain,'남은거')
        else:
            arr[i][j] += int(sand * per)



def BFS(i,j):
    q = deque()
    q.append((i,j))
    flag = False
    gocnt = 0
    togo = 1
    pd = 0
    while q:
        pi,pj = q.popleft()
        if pi == 0 and pj == 0:
            return
        ni = pi + di[pd]
        nj = pj + dj[pd]
        sand = arr[ni][nj]
        remain = sand
        arr[ni][nj]=0
        q.append((ni,nj))
        gocnt += 1
        if sand:
            for next in tornado[pd]:
                mi,mj,per = next
                check(ni+mi,nj+mj,sand,per,remain)
                remain -= int(sand * per)

        if gocnt == togo:
            #한번 이미 그만 큼 갔으면
            if flag:
                togo += 1
                flag = False
            else:
                flag = True
            gocnt = 0
            pd = (pd+1)%4


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
outsand = 0
BFS(N//2,N//2)
print(outsand)
