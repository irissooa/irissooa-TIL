def check():
    cnt = 0
    # 가로세로 확인
    for i in range(N):
        cnt_row = 0
        cnt_col = 0
        for j in range(N):
            if bingo[i][j] == 0: cnt_col += 1
            if bingo[j][i] == 0: cnt_row += 1

        if cnt_row == N: cnt += 1
        if cnt_col == N: cnt += 1

    # 대각선, 역대각선 확인
    cnt_l = 0
    cnt_r = 0
    for i in range(N):
        if bingo[i][i] == 0: cnt_l += 1
        if bingo[i][N - 1 - i] == 0: cnt_r += 1

    if cnt_l == N: cnt += 1
    if cnt_r == N: cnt += 1

    if cnt >= 3: return True
    return False


N = 5
bingo = [list(map(int, input().split())) for _ in range(N)]

pos = [0] * 26
#해당 번호 좌표 담기
for i in range(N):
    for j in range(N):
        pos[bingo[i][j]] = (i, j)

call = []

#사회자가 호출하는 번호 한줄로 만들기
for i in range(N):
    call += list(map(int, input().split()))

ans = 0

while not check():
    r, c = pos[call[ans]]
    bingo[r][c] = 0
    ans += 1
print(ans)
