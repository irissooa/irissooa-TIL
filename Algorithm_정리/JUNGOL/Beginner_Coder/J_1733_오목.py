'''
20-12-18 10:05-11:25
오목 검정바둑알 1, 흰바둑알 1, 빈자리0, 19줄 19개숫자
가로,세로,대각선, 여섯알 이상 연속적으로 놓인 경우 이긴것아님, 5알이면 이김, 검정흰색 동시에 이기는 경우 엉ㅄ음
검정 이기면1, 흰색 2, 아직 승부가 결정되지 않으면 0
이긴 바둑돌의 가장 왼쪽에 있는 바둑알 출력

1. 0이아닌 수를 만났을때, 가로만 확인, 세로만 확인, 대각선만 확인하는 for문을 만들어 5개면 출력!
각 방문배열을 따로 만듦,
'''
from collections import deque
import sys
sys.stdin = open('input.txt','r')
di = [0,1,1,1] #가로(우),세로(하),대각선(좌하대, 우하대)
dj = [1,0,-1,1]

def check(i,j,color):
    hor.add((i,j))
    ver.add((i,j))
    ldia.add((i,j))
    rdia.add((i,j))
    H,V,R,L = deque(),deque(),deque(),deque()
    H.append((i,j,color))
    V.append((i,j,color))
    R.append((i,j,color))
    L.append((i, j, color))
#     가로
    garo = 1
    ans =[i,j]
    while H:
        pi,pj,pc = H.popleft()
        ni,nj = pi+di[0], pj+dj[0]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in hor:
            break
        garo += 1
        H.append((ni,nj,pc))
        hor.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if garo == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
#     세로
    sero = 1
    ans =[i,j]
    while V:
        pi,pj,pc = V.popleft()
        ni,nj = pi+di[1], pj+dj[1]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in ver:
            break
        sero += 1
        V.append((ni,nj,pc))
        ver.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if sero == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
    # 좌대각선
    ldae = 1
    ans =[i,j]
    while L:
        pi,pj,pc = L.popleft()
        ni,nj = pi+di[2], pj+dj[2]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in ldia:
            break
        ldae += 1
        L.append((ni,nj,pc))
        ldia.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if ldae == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
    # 우대각선
    rdae = 1
    ans =[i,j]
    while R:
        pi,pj,pc = R.popleft()
        ni,nj = pi+di[3], pj+dj[3]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in rdia:
            break
        rdae += 1
        R.append((ni,nj,pc))
        rdia.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if rdae == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
    return False





arr = [list(map(int,input().split())) for _ in range(19)]
flag = False
hor, ver, ldia, rdia = set(), set(), set(), set()
for i in range(19):
    for j in range(19):
        if arr[i][j]:
            if check(i,j,arr[i][j]):
                flag = True
                break
    if flag:
        break
if not flag:
    print(0)
