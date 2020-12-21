import sys
sys.stdin = open('input.txt','r')
#인풋을 받는다
#입력은 열 행 컬러
#돌을 놓았을 떄 8방향 탐색을 하면서
#나와 같은 컬로 찾는다(이떄 중간에 공백이 있거나, 맵의 범위를 벗어나면 수행x)
#찾은 컬러의 좌표부터 지금 놓은 좌표까지 돌아오면서 색갈을 모조리다 나의 컬러로 바꾼다
#위의 과정을 M번 반복하면 끝

#첫 위치를 배열의 len을 구하고 //2해준 위치,
#
# 8방배열을 할거야
# 오셀로 입력값은

# 8방 우 좌 하 상 오상대 오하대 좌상대 좌하대
di = [0, 0, 1, -1, -1, 1, -1, 1]
dj = [1, -1, 0, 0, 1, 1, -1, -1]


def put(i, j, color):
    arr[i][j] = color  # 놓은 곳의 색깔이 달라짐!
    opp_color = -1 #반대컬러 선언
    if color == 1:
        opp_color = 2
    else:
        opp_color = 1

    # 놓음과 동시에 8방으로 훑어보고 색을 바꿔 줘야됨
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        flag = False  # 중간에 끼인 값들 색을 바꿔줘야된다고 할 표시
        cnt = 0  # 그 중간에 몇개가 껴있는지 세어야됨

        while ni >= 0 and ni < N and nj >= 0 and nj < N:
            #공백일때(0) 빠져나옴
            if arr[ni][nj] == 0:
                break
            if arr[ni][nj] == opp_color:
                cnt += 1
            if arr[ni][nj] == color:
                flag = True #여기까지 색을바꿀거야
                break #같은애 찾았으니 나와랏!
            #그방향으로 계속 감!
            ni += di[d]
            nj += dj[d]
        if flag: #True
            #i,j시작값과 flag가 True인 값 사이의 값을 같은 색으로 바꿀거야!
            for c in range(1,cnt+1): #cnt만큼 돌거야 근데 c는 1부터 해당 cnt까지 돌아야됨!!!!
                #di[d]와 dj[d]가 c만큼 움직였으니까 그거를 원래 좌표에 더한 그 위치를 내 색으로 바꿈!
                arr[i+di[d]*c][j+dj[d]*c] = color




T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0 for j in range(N)] for i in range(N)]
    arr[N // 2][N // 2] = 2
    arr[(N // 2) - 1][(N // 2) - 1] = 2
    arr[(N // 2) - 1][N // 2] = 1
    arr[(N // 2)][(N // 2) - 1] = 1
    # print(arr)

    for _ in range(M):
        row, col, color = map(int, input().split())
        #이게 4X4배열일때 입력받은 idx가 1부터 4까지로 해놓음! 그래서 하나씩 빼줘서(컴퓨터배열은 0~3이니까) idx를 맞춰줌!
        put(row-1,col-1,color)
    #흑돌 백돌 개수를 세어야됨!!!
    black ,white = 0,0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            if arr[i][j] == 2: #0이있을수도 잇으니 else를 하면 안됨!!!!!!
                white += 1
    print('#{} {} {}'.format(tc,black,white))
    
#선생님 코드
#8방향 델타
#우,우하,하,좌하,좌,좌상,상,우상
dr = [0,1,1,1,0,-1,-1,-1]
dc = [1,1,0,-1,-1,-1,0,1]

def init():
    mid = N//2
    othello[mid][mid] = othello[mid+1][mid+1] = 2 #백돌
    othello[mid+1][mid] = othello[mid][mid+1] = 1 #흑돌

def change(r,c,color):
    #새로운 좌표에 돌을 놓았다
    othello[r][c] = color
    #8방향 탐색
    for i in range(8):
        nr = r
        nc = c
        #해당방향으로 break가 걸리기전까지 무조건 전진
        while True:
            nr += dr[i]
            nc += dc[i]
            #한칸씩 크게 만들었으니 idx가 다름
            #우리는 0idx를 사용하지 않음
            #맵의 범위를 벗어났다면 그만
            if nr <= 0  or nr > N or nc <=0 or nc > N:
                break
            #만약에 중간에 공백이 있다면 의미가 없으니 break
            if othello[nr][nc] == 0:
                break
            #나랑 같은 색을 만나면 색 바꿔주고 그만
            if othello[nr][nc] == color:
                #그 곳에서 원래의 나의 위치까지 오면서 나의색으로 바꿔줌
                while (nr == r and nr == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    othello[nr][nc] =color
                break

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    #0idx는 쓰지 않을거니 N+1로 만들어줌
    othello = [[0]*(N+1) for _ in range(N+1)]

    init()

    for i in range(M):
        c,r,color = map(int,input().split())
        change(r,c,color)
    b_cnt = 0
    w_cnt = 0
    for i in range(N+1):
        b_cnt += othello[i].count(1)
        w_cnt += othello[i].count(2)
    print('#{} {} {}'.format(tc,b_cnt,w_cnt))