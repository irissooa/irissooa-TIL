'''
1. 미세먼지확산, 모든 칸 동시에 일어남
인접한 네방향으로 확산되는데 공기청정기가 있거나, 칸이 없으면 그 방향으로 확산 일어나지 않음
확산되는 양은 A[r][c]//5
A[r][c]에 남은 미세먼지의 양은 A[r][c]-A[r][c]//5*확산된방향개수
2. 공기청정기 작동
위쪽 공기청정기의 바람은 반시계방향으로 순환,
아래쪽 공기청정기의 바람은 시계방향으로 순환
바람 불면 미세먼지가 바람의 방향대로 한칸씩 이동
공기청정기에서 부는 바람은 미세먼지 없는 바람, 공기청정기로 들어간 미세먼지는 모두 정화됨
방의 정보가 주어졌을때, T초가 지난 후 남은 미세먼지의 양

1)미세먼지 확산 함수
for돌리다가 먼지가 있는곳 상하좌우 보면서 범위밖이거나 공기청정기가 있는 칸이 아니라면
A[r][c]//5를 추가해주고 cnt를 세어줌, 그런뒤 해당 칸은 A[r][c]//5*cnt만큼 빼줌

2) 공기청정기 함수
공기 청정기가 있는 위에칸은 반시계방향으로 순환하기때문에 처음부터 첫 -1이 있는행까지 반시계로 테두리만 돌림
temp에 해당 크기만큼 배열을 만든 뒤,
반시계방향
2-1.j가 0이고 i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
2-2. i가 마지막이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
2-3. j가 마지막이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
2-4. i가 처음이고,j가 처음이 아니라면 temp[i][j-1]= room[i][j]
시계방향
2-1 j가 0이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
2-2 i가 0이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
2-3 j가 마지막이고, i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
2-4 i가 마지막이고, j가 처음이 아니라면 temp[i][j-1] = room[i][j]

이동한 곳에 공기청정기가 있다면 0이됨
T초간 반복
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def dust(q):
    while q:
        pi,pj,dustnum = q.popleft()
        cnt = 0
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            if room[ni][nj] == -1:
                continue
            if not dustnum//5:
                continue
            room[ni][nj] += (dustnum//5)
            # print(pi,pj,room[pi][pj],'-->',ni,nj,room[ni][nj])
            cnt+=1
        room[pi][pj] = room[pi][pj] - ((dustnum//5)*cnt)
        # print(cnt,room[pi][pj])
        # for x in room:
        #     print(x)


# 반시계
def revcleaner(row):
    temp = [[0 for j in range(C)] for i in range(row+1)]
    # for x in temp:
    #     print(x)
    for i in range(row+1):
        for j in range(C):
            # 공기청정기는 안움직임
            if room[i][j] == -1:
                temp[i][j] = room[i][j]
                continue
            # # 공기청정기에 닿아서 정화될 먼지
            # if i == row-1 and j == 0:
            #     room[i][j] = 0
            # 2-1.j가 0이고 i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
            if (j==0 and i!= row):
                temp[i + 1][j] = room[i][j]
                continue
            # 2-2. i가 마지막이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
            if (i==row and j != C-1):
                temp[i][j + 1] = room[i][j]
                continue
            # 2-3. j가 마지막이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
            if (j == C-1 and i != 0):
                temp[i - 1][j] = room[i][j]
                continue
            # 2-4. i가 처음이고,j가 처음이 아니라면 temp[i][j-1]= room[i][j]
            if (i == 0 and j != 0):
                temp[i][j - 1] = room[i][j]
                continue
            temp[i][j] = room[i][j]
    temp[row][0] = -1
    # for x in temp:
    #     print(x)
    return temp

# 시계
def clockcleaner(row):
    temp = [[0 for j in range(C)] for i in range(row,R)]
    for i in range(row,R):
        for j in range(C):
            # 공기청정기는 안움직임
            if room[i][j] == -1:
                temp[i-row][j] = room[i][j]
                continue
            # # 공기청정기에 닿아서 정화될 먼지
            # if i == row + 1 and j == 0:
            #     room[i][j] = 0
            #2-1 j가 0이고, i가 처음이 아니라면 temp[i-1][j] = room[i][j]
            if (j == 0 and i != row):
                temp[i-1-row][j] = room[i][j]
                continue
            # 2-2 i가 0이고, j가 마지막이 아니라면 temp[i][j+1] = room[i][j]
            if (i==row and j != C-1):
                temp[i-row][j + 1] = room[i][j]
                continue
            # 2-3 j가 마지막이고, i가 마지막이 아니라면 temp[i+1][j] = room[i][j]
            if (j==C-1 and i != R-1):
                temp[i + 1-row][j] = room[i][j]
                continue
            # 2-4 i가 마지막이고, j가 처음이 아니라면 temp[i][j-1] = room[i][j]
            if (i == R-1 and j !=0):
                temp[i-row][j - 1] = room[i][j]
                continue
            temp[i-row][j] = room[i][j]
    temp[0][0] = -1
    # for x in temp:
    #     print(x)
    return temp




R,C,T = map(int,input().split())
# 공기청정기 -1, 나머지는 미세먼지양
room = [list(map(int,input().split())) for _ in range(R)]
# for x in room:
#     print(x)
cleanerRow = 0
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            cleanerRow = i
            break
    if cleanerRow:
        break
# print(cleanerRow)
while T:
    # 1단계 미세먼지 확산
    T-=1
    dustlist = deque()
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j]:
                dustlist.append([i,j,room[i][j]])
    dust(dustlist)
    # print('미세먼지확산')
    # for x in room:
    #     print(x)
    # 2단계 공기청정
    # print('반시계공기청정')
    temp1 = revcleaner(cleanerRow)
    # print('시계공기청정')
    temp2 = clockcleaner(cleanerRow+1)
    room = temp1+temp2
    # print('바뀐room')
    # for x in room:
    #     print(x)
total = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1 and room[i][j]:
            total += room[i][j]

print(total)