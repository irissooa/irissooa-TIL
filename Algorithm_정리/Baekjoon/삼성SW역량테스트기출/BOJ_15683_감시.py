'''
2020-11-30 16:25
CCTV종류
1: 한 방향
2: 서로 반대 두 방향(상하,좌우)
3: 90도 두방향(우하,좌상,우상,좌하)
4: 세방향(한개제외)
5: 네 방향
cctv는 회전가능(대각선만안되면 됨)
벽(6)은 통과할수없지만 cctv는 통과가능
감시할 수 없는 사각지대가 최소인 크기를 구해라
dfs를 돌릴건데
각 cctv좌표가 갈수 있는 범위 까지 cnt를 세고 상하좌우 모두 돌려서 cnt센뒤 list에 담아주고
cctv번호에 따라 개수를 합해서 세어준뒤 제일 많은 cnt를 total에 더함
이걸 반복해서 전체 0의 수에서 빼줌

카메라가 큰번호부터 방문처리를 하는게 좋겠다
딕셔너리? 카메라번호 key : [각 d별 [cnt,방문한좌표]]
근데 딕셔너리로 했을 떄....중복되는 카메라 처리..해야돼서 다시 생각해보자
각 cctv가 갈수 있는 방향으로 모두 구해보자 ->갈수 있는 방향 딕셔너리로 묶어두기
카메라별 각 경우의 수를 다 돌려본뒤 최소를..구해보자
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
camera = {'1':[[0],[1],[2],[3]],'2':[[0,1],[2,3]],'3':[[0,2],[1,3],[0,3],[2,3]],'4':[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],'5':[[0,1,2,3]]}

def search(i,j,dir):
    pi,pj = i,j
    for d in dir:
        ni = pi + di[d]
        nj = pj + dj[d]
        if office[ni][nj] == 6:
            return



def cctv(q):
    while q:
        cameranum,pi,pj = q.pop(0)
        print(cameranum,pi,pj)
        for d in camera[str(cameranum)]:
            search(pi,pj,d)


N,M = map(int,input().split())
# 벽 만듦
office = [[6]+list(map(int,input().split()))+[6] for _ in range(N)]
office.insert(0,[6]*(M+2))
office.insert(N+1,[6]*(M+2))

zero = 0
visited = [[False for j in range(M+2)] for i in range(N+2)]
for x in office:
    print(x)
cctvList = []
for i in range(1,N+1):
    for j in range(1,M+1):
        if office[i][j] == 0:
            zero += 1
        if office[i][j] != 0 and office[i][j] !=6:
            cctvList.append([office[i][j],i,j])
cctvList.sort(key=lambda x:-x[0])
print(cctvList)
cctv(cctvList)
for x in visited:
    print(x)
ans = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if visited[i][j]:
            ans += 1
print(zero-ans)