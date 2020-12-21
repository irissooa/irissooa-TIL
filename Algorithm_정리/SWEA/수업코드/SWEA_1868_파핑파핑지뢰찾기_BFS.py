from collections import deque
# 왼상부터 시계방향 모습
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def BFS(r, c):
    #큐를 선언하고 초기값 넣기
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        curr_r, curr_c = queue.popleft()
        #8방향 탐색
        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            #게임 범위를 벗어나지 않으면서 방문하지 않았다면
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True #방문체크
                #지뢰가 없다면 큐에 넣어 연쇄폭발
                if game[nr][nc] == 0: queue.append((nr, nc))

#지뢰가 몇개 있냐가 중요한 것이아니라 8방향에 지뢰가 있냐 없냐가 중요.
def mine_check(r, c):
    cnt = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        #실제 지뢰의 개수를 세기
        if game[nr][nc] == '*': cnt += 1
    return cnt
#####################################
        #지뢰가 있다면 바로 리턴
        # if arr[nr][nc] == '*':
        #     return 1
    # return 0
######################################



for tc in range(1, int(input()) + 1):
    N = int(input()) #한변의 길이
    game = [list(input()) for _ in range(N)] #지뢰판 입력

    # 최소 클릭을 위해 주변에 지뢰가 없는 것들을 먼저 클릭하자.
    zero_list = []
    for i in range(N):
        for j in range(N):
            #지뢰가 아닌 칸이라면
            if game[i][j] == '.':
                #주변 8방향 지뢰 카운트하여 표시 (지뢰 있는지 없는지로만 기입해도 상관 없음)
                game[i][j] = mine_check(i, j)
            #주변에 지뢰가 없다면 리스트에 추가
            if game[i][j] == 0:
                zero_list.append((i, j))

    #중복 방문을 방지하기 위한 방문체크 리스트
    visited = [[False] * N for _ in range(N)]

    ans = 0 #클릭횟수

    for r, c in zero_list:
        #방문하였다면 건너가기
        if visited[r][c]: continue
        ans += 1 #한번 클릭
        BFS(r, c) #터트릴수 있는건 다 터뜨리기

    #지뢰가 아니면서 클릭되지 않은 칸
    for i in range(N):
        for j in range(N):
            #행우선순회로 순회하면서 지나간 칸은 돌아오지 않으므로
            #따로 방문체크를 할 필요 없이 클릭횟수만 증가시킨다.
            if game[i][j] != '*' and not visited[i][j]:
                ans += 1

    print("#{} {}".format(tc, ans))
