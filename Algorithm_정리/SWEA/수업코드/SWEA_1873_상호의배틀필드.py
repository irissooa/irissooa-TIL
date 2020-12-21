import sys

sys.stdin = open("input1873.txt", "r")

tank = ['^', 'v', '<', '>']  # 탱크모습
dir_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#이중 for문 한번에 벗어나기
def search_tank():
    for i in range(H):
        for j in range(W):
            if game[i][j] in tank:
                return i, j, tank.index(game[i][j])

#index 함수, find 함수 : 차이를 알고 사용하기.
#없는 값 찾으려고 하면
#index 함수 : 에러
#find 함수 : -1

for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split()) #높이, 너비
    game = [list(input()) for _ in range(H)]  # 게임 맵입력

    N = int(input()) #명령어 수
    cmd_list = list(input()) #명령어

    #1. 탱크의 위치를 찾기

    #조건을 주어 이중포문 빠져나가기
    # r = c = dir = -1
    # for i in range(H):
    #     for j in range(W):
    #         if game[i][j] in tank:
    #             r = i
    #             c = j
    #             dir = tank.index(game[i][j])
    #             break
    #     if r != -1:
    #         break
    r, c, dir = search_tank()

    # 2. 각각의 상황에 맞게 명령어를 수행한다.
    for cmd in cmd_list:
        # 2-1 포탄발사 : 벽에 부딪히거나 맵밖을 벗어날때까지 포탄 이동 (벽돌벽이면 평지화)
        if cmd == 'S':
            nr = r + dr[dir]
            nc = c + dc[dir]
            # while True:
            #     #맵의 법위를 벗어났다면
            #     if nr <0 or nr >=H or nc<0 or nc>=W: break
            #     if game[nr][nc] == '#': break
            #     if game[nr][nc] == '*':
            #         game[nr][nc] = '.'
            #         break
            #     nr += dr[dir]
            #     nc += dc[dir]

            #범위검사를 while문에 조건으로 넣을 수 있다.
            while 0 <= nr < H and 0 <= nc < W:
                if game[nr][nc] == '#': break
                if game[nr][nc] == '*':
                    game[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]

        # 2-2 방향컨트롤 : 해당 방향으로 돌리고, 전진할수 있으면 전진
        else:
            #새롭게 방향 받아오기
            dir = dir_dict[cmd]
            #전차 돌리기
            game[r][c] = tank[dir]

            #다음칸으로 이동가능하다면 이동
            nr, nc = r+dr[dir], c+dc[dir]
            if 0 <= nr < H and 0 <= nc < W and game[nr][nc] == '.':
                game[nr][nc] = tank[dir] #탱크 옮기기
                game[r][c] = '.' #기존의 자리 평지화
                r, c = nr, nc #전차 좌표 갱신

    # 3. 출력
    print("#{}".format(tc), end=" ")
    # for i in range(H):
    #     print("".join(game[i]))

    #join에 익숙하지 않다면 사용할 수 있는 방법
    for i in range(H):
        for j in range(W):
            print(game[i][j], end="")
        print()
