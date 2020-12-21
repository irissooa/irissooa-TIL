'''
2020-12-09 19:55-(20:08밥-20:35컴백)-
출발 상근이네 -> 맥주한박스들고 출발(20개) 50미터에 한병씩 마심
맥주를 더 구매해야할 수 도 있음
편의점을 들렸을때 빈병은 버리고 새 맥주 병 살 수 있다(20개까지)
상근이와 친구들 행복하게 페스티벌 도착해야됨

송도는 직사각형 모양으로 생긴 도시
두 좌표 사이의 거리는 (x좌표 차이 + y좌표의 차)
행복하게 갈수있으면 happy, 아니면 sad출력

너무 오래 걸렸다...ㅠ
어려운 문제는 아닌데 설계를 잘못함
1. start는 home!
2. festival의 위치도 기록한 뒤, 편의점과 festival을 같은 infolist에 묶어서 home과의 거리가 짧은 순으로 정렬!
# 여기서 2번이 문제였다...home과의 거리란,,, festival과 반대로 멀어질수도있다는걸 생각못함ㅠㅠ->플로이드 와샬..알고리즘..공부하자ㅠ
3. info를 돌면서 festival에 도착하면 happy아니면 sad(거리비교 beer-dist/50>=0)

# 다시생각
집 -편의점 - Festival
이렇게 위치해있고 집-편의점 : a // 편의점 -Festival :b // 집-festival :c라면
a랑 b는 c보다 작아야된다! 그래야 집- 편의점-축제 순서가 됨!
c가 바로갈수있는 거리가 아니고 a는 갈수있다면 a,b가 c보다 작다면 편의점으로 내 위치 갱신
아니라면 다음 편의점과 반복
이렇게...해서 찾아보자....!

#사람들코드보고 다시 생각
1. 집, 편의점, festival list에 각각 좌표 담는다
2. 첫시작은 집, bfs를 돌리는데 현재지점과 축제와의 거리가 1000이하인지 계속 확인
3. 아니라면 편의점list에서 현재지점과 거리가 1000이하이고 방문하지 않은 점 확인하고 다음좌표로 갈 리스트로 담아줌
4. 다보면 그 편의점 리스트들을 q에 담아주고 반복
5. 축제에 도착하면 flag줌
'''
import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

def BFS(start):
    global flag
    visited = set()
    q = deque()
    q.append(start)
    ex,ey = festival
    while q:
        px,py = q.popleft()
        if abs(px-ex) + abs(py-ey) <= 1000:
            flag = True
            return
        next_store = []
        for idx in range(N):
            nx,ny = store[idx]
            if abs(px-nx) + abs(py-ny) <= 1000 and (idx not in visited):
                visited.add(idx)
                next_store.append([nx,ny])
        q.extend(next_store)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    home = list(map(int,input().split()))
    store = [list(map(int,input().split())) for _ in range(N)]
    festival = list(map(int,input().split()))
    flag = False
    BFS(home)
    if flag:
        print('happy')
    else:
        print('sad')










'''
틀린코드,,,,,
T = int(input())
for tc in range(1,T+1):
    # 편의점 개수
    n = int(input())
    # 상근이네 집, 편의점,락페스티벌 좌표x,y
    home = list(map(int,input().split()))
    info = [list(map(int,input().split())) for _ in range(n)]
    festival = list(map(int,input().split()))
    # 거리순으로 일단 정렬은 했는데 만약에 c보다 b가 크다면 지나가게하자
    info.sort(key = lambda x:(abs(x[0]-home[0])+abs(x[1]-home[1])))
    # print(info)
    # print(festival)
    beer = 20
    sx,sy = home
    ex,ey = festival
    flag = False
    c = abs(sx-ex) + abs(sy-ey)
    if beer - c/50 >= 0:
        print('happy')
        flag = True
        continue
    for i in info:
        nx,ny = i
        a = abs(sx-nx) + abs(sy-ny)
        b = abs(nx-ex) + abs(ny-ey)
        c = abs(sx-ex) + abs(sy-ey)
        # 갈수 있다면
        if c <= 1000:
            print('happy')
            flag = True
            break
        # 편의점이 출발점과 끝점 사이에 있다면 시작점 갱신
        if a <= 1000 and a < c and b < c:
            sx,sy = nx,ny
        if a<=1000 and b <= 1000:
            print('happy')
            flag = True
            break
    if flag:
        continue
    if c <=1000 or b <=1000:
        print('happy')
    else:
        print('sad')
'''