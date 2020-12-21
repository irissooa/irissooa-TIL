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
sys.stdin= open('input.txt','r')
sys.setrecursionlimit(10**8)
from collections import deque
input = sys.stdin.readline
di = [-1,-1,0,1,1,1,0,-1] #상(0),우상(1),우(2),우하(3),하(4),좌하(5),좌(6),좌상(7)
dj = [0,1,1,1,0,-1,-1,-1]
#공위치시키기
def position(q):
    global cnt
    cnt += 1
    # print(cnt)
    while q:
        pi,pj,pd,ps,pm = q.popleft()
        # print('-현위치-i,j,pd,ps,pm-')
        # print(pi,pj,pd,ps,pm)
        ni = (pi + di[pd] * ps) % N
        nj = (pj + dj[pd] * ps) % N
        # print('-이동후-ni,nj,pd,ps,pm-')
        # print(ni,nj,pd,ps,pm)
        arr[ni][nj].append([pd,ps,pm])
    # for x in arr:
    #     print(x)
    move(arr)

#공움직이기
def move(temp):
    global cnt,ans
    next = deque()
    # print('움직여라')
    # for x in temp:
    #     print(x)
    for i in range(N):
        for j in range(N):
            if not temp[i][j]:
                continue
            #공이 두개이상 만났을떼 질량, 속력,방향 바꾸고 next에 담아주기
            ''''
            4-1. 질량은 [(합쳐진 파이어볼 질량의 합)/5]
            4-2 속력은 [(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)]
            4-3 합쳐지는 파이어볼의 방향이 모두 홀수, 모두 짝수, 방향은 0,2,4,6이 됨,
            그렇지 않으면 1,3,5,7이 됨
            '''
            if len(temp[i][j])>=2:
                # print(i,j,temp[i][j])
                M,S,flag,D=0,0,0,[]
                odd=0
                for x in temp[i][j]:
                    pd,ps,pm = x
                    M += pm
                    S += ps
                    if pd % 2:
                        odd += 1
                    # if flag == 3:
                    #     continue
                    # #방향이홀수
                    # if pd % 2 and flag !=2:
                    #     D = [0,2,4,6]
                    #     flag = 1
                    # #방향이 짝수
                    # elif not pd % 2 and flag !=1:
                    #     D = [0,2,4,6]
                    #     flag =2
                    # #홀수 짝수가 같이 있음
                    # else:
                    #     flag = 3
                    #     D = [1,3,5,7]
                #질량
                M = M //5
                #M이 0이 되면 소멸
                if not M:
                    continue
                #속력
                S = S// len(temp[i][j])
                #4방향으로 보내줌
                if odd == len(temp[i][j]) or odd ==0:
                    D = [0,2,4,6]
                else:
                    D = [1,3,5,7]
                for d in D:
                    # print('변하고, 이동할좌표 i,j,d,S,M')
                    # print(i,j,d,S,M)
                    next.append([i,j,d,S,M])
            #공이 한개만 있을때 한번 더 그 방향과 속력,질량을 갖고 보내기
            elif temp[i][j]:
                # print(temp[i][j])
                for x in temp[i][j]:
                    pd,ps,pm = x
                    # print('그냥 이동할좌표 i,j,d,S,M')
                    # print(i,j,pd,ps,pm)
                    next.append([i,j,pd,ps,pm])
    for i in range(N):
        for j in range(N):
            temp[i][j] = []
    # print('이동할 좌표')
    # for x in next:
    #     print(x)
    if cnt ==K:
        if not next:
            return
        for x in next:
            # print(x)
            ans += x[-1]
            # print(ans)
        return
    else:
        position(next)


N,M,K = map(int,input().split())
arr = [[[] for j in range(N)] for i in range(N)]
#r-1,c-1,m,s,d
cnt = 0
ans = 0
fireball= deque()
for i in range(M):
    r,c,m,s,d = map(int,input().split())
    fireball.append([r-1,c-1,d,s,m])
position(fireball)
# for x in arr:
#     print(x)
print(ans)