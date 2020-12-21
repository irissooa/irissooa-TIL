'''
러시아 국기 만들기
N행 M열 배열 주어짐
위에서 부터 최소 한줄 흰 , 파, 빨강 색을 만들어야 됨
새로 칠 해야 하는 칸긔 개수 최소값을 구하라
최소 1줄씩은 색이 있어야됨(첫줄, 마지막줄은 흰, 빨로 고정)
하영's hint
for문으로 보는데 W는 0,N-2까지, B는 w+1,N-1까지, R는 b+1,N까지!
열을 다 둘러봤을 때 다음 코드를 적으며 cnt를 세고! 다 더한 뒤 MIN값을 갱신!
'''
import sys
sys.stdin =open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    color = [list(input()) for _ in range(N)]
    cnt = 0#색을 바꾼 횟수를 담을 변수
    MIN = 987654321
    #하영's hint
    #for문으로 보는데 W는 0,N-2까지, B는 w+1,N-1까지, R는 b+1,N까지!
    #열을 다 둘러봤을 때 다음 코드를 적으며 cnt를 세고! 다 더한 뒤 MIN값을 갱신!
    w_cnt = 0 #하양
    for w in range(0,N-2):
        for j in range(M):
            if color[w][j] != 'W':
                w_cnt += 1
        b_cnt = 0 #파랑
        for b in range(w+1,N-1):
            for j in range(M):
                if color[b][j] != 'B':
                    b_cnt += 1
            r_cnt = 0 #빨강
            for r in range(b+1,N):
                for j in range(M):
                    if color[r][j] != 'R':
                        r_cnt += 1
            #여기서 cnt = 모든 색의 cnt를 더한 것!
            cnt = w_cnt + b_cnt + r_cnt
            if MIN > cnt:
                MIN = cnt
    print('#{} {}'.format(tc,MIN))

#선생님 풀이
T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    #각 행의 색 카운팅
    w = [0] * N
    b = [0] * N
    r = [0] * N

    for i in range(N):
        color = input()
        w[i] = color.count("W")
        b[i] = color.count("B")
        r[i] = M - w[i] - b[i] #M개에서 w의 개수, b의 개수를 뺀 값이 r의 개수
    #누적합을 구해서 나중에 한번에 계산하기 위해..
    for i in range(1,N):
        w[i] += w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1]


    ans = N*M
    #흰색의 경계를 정함.마지막에 파랑 빨강을 보장해야됨
    for i in range(N-2):
        #파란색의 경계를 정함
        for j in range(i+1,N-1):
            #흰색칠하기
            #i까지의 저체 개수를 구한 뒤 지금까지 칠해져 있는 화이트 개수를 빼기
            cnt = M *(i+1) -w[i]
            #파란색칠하기
            #j-1를 해서 유의미한 전체의 개수를 뽑고, b[j]-b[i]를 하여 해당 범위의 전체 파랑 개수를 뽑아내기
            cnt += M * (i+1) - (b[j] -b[i])
            #빨간색 칠하기
            #위와 마찬가지...ㅎ
            cnt += M * (N-1 -j)-(r[N-1]-r[j])
            ans = min(ans,cnt)
    print('#{} {}'.format(tc,ans))


#러시아 국기 조합으로 풀기
def combination(sel,idx,cnt):
    global ans
    if cnt == 2:
        print(sel)
        #각각의 1이 경계를 의미
        w = -1
        b = -1
        for i in range(N):
            if sel[i] == 1:
                if w == -1:
                    a = i
                else:
                    b = i
        count = 0
        #흰색 영역 칠하기
        for W in range(0,w+1):
            for k in range(M):
                if flag[W][k] != 'W':
                    count += 1
        for B in range(w+1,b+1):
            for k in range(M):
                if flag[B][k] != 'B':
                    count += 1
        for R in range(b+1,N):
            for k in range(M):
                if flag[R][k] != 'R':
                    count += 1
        return

    if idx >= N-1:
        return
    #경계 뽑고
    sel[sidx] = 1
    combination(sel,idx+1,cnt+1)
    #경계다시 원상복구
    sel[sidx] = 0
    combination(sel,idx+1,cnt)


T = int(input())
for tc in range(1,T+1):
    N,M =(int,input().split())
    #스트링도 idx가 있기 때문에 list로 안 바꿈
    flag = [input() for _ in range(N)]

    ans = M*N

    combination([0]*N,0,0)




#의수
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    temp = []

    # 각행의 색깔의 갯수를 카운트 하여 temp에 리스트 형태로 저장된다
    for i in range(N):
        w = arr[i].count('W')
        b = arr[i].count('B')
        r = arr[i].count('R')
        temp.append([w, b, r])

    # 가장 최소이동의 경우의 수를 맞춰야 하기 때문에 누적합을 이용한다
    # 원래의 상태
    # temp = [[3, 0, 2], [2, 2, 1], [3, 0, 2], [2, 1, 2]]
    # 아래 포문 후 상태
    # temp = [[3, 0, 2], [5, 2, 3], [8, 2, 5], [10, 3, 7]]
    # 즉, 맨 아래 행렬의 값인 [10, 3, 7] 이 의미하는 바는 국기에서 각각의 색이 가지고 있는 수의 합이다.
    # white = 10, blue = 3, red = 7 총 N * M = 20
    for i in range(1, N):
        temp[i][0] += temp[i - 1][0]
        temp[i][1] += temp[i - 1][1]
        temp[i][2] += temp[i - 1][2]

    # 첫번째 i, range 범위는 맨 윗쪽의 white의 색이기 때문에 아래 최소 2가지 색이 남을 수 있으니 N-2한다
    # 두번째 j, range 범위는 가운데 파랑색을 돌리는 것이라 최소 i(white)의 갯수+1 부터 최대 마지막 red 한줄을 남겨야 해서 N-1
    # 반복문을 돌리며 최소로 소모되는 이동을 구해야 하니 모든 경우의 수 탐색
    # res에 값에는 움직이지 안아도 될 ww, bb, rr의 갯수의 합의 최댓값이 저장된다
    # 출력할때 N * M - res 하면 이동해야 할 최솟값이 나온다!
    res = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # 0 은 white, 1은 blue, 2는 red
            # temp엔 누적합이 저장되어 있다
            # 첫번째 ww는 그냥 그대로의 값을 받는다
            ww = temp[i][0]
            # bb는 j까지 누적된 합에서 i까지 누적된 합을 빼면 안움직여도 되는 갯수가 나온다
            bb = temp[j][1] - temp[i][1]
            # rr는 맨 마지막줄에 적혀있는 누적합에서 red의 j 값까지의 누적합을 배면 red에서 움직이지 않아야 하는 갯수가 나온다.
            rr = temp[N - 1][2] - temp[j][2]
            # 최댓값 res 저장 (전체에서 빼면 움직여야할 최솟값이 나오므로!)
            if res < ww + bb + rr:
                res = ww + bb + rr
    print('#{} {}'.format(tc, M * N - res))

#현우
# 가운데 애들은 일단 시작은 흰색 아니면 파란색.
# 근데 가운데 중 최소 한 줄은 파란색이어야 함.
# 파란색으로 칠했으면, 그담 부터는 파랑 아니면 빨강
# 빨강으로 칠했으면, 그담 부터는 무조건 빨강
# 따라서 파란색,빨간색 칠했음을 나타내는 표시가 있어야함
# 걔네를 DFS에 인자로 줌

# 해당 줄에서 그 색이 아닌애들 세는거
def count_not_color(i, color):
    not_color = 0
    for j in range(M):
        if board[i][j] != color:
            not_color += 1
    return not_color


def DFS(i, painted_blue, painted_red, cnt):
    if i == N - 1:
        # print(cnt,row_color)
        # 파란색 칠해져 있을 때만 답임
        if painted_blue:
            global ans
            if cnt < ans:
                ans = cnt
        return
    # i번째 줄을 칠한다.
    # 파랑 색 안칠했으면, 흰색,파랑색 칠 가능
    if not painted_blue:
        # 흰색 으로 칠함.
        not_white = count_not_color(i, 'W')
        # 다음 줄 칠하러 감
        row_color[i] = 'W'
        DFS(i + 1, False, False, cnt + not_white)
        # 파랑색으로 칠함
        row_color[i] = 'B'
        not_blue = count_not_color(i, 'B')

        DFS(i + 1, True, False, cnt + not_blue)
    # 파랑색 칠 했을 때
    else:
        # 빨강을 이미 칠한 경우 빨강만 칠 가능
        if painted_red:
            not_red = count_not_color(i, 'R')
            row_color[i] = 'R'
            DFS(i + 1, True, True, cnt + not_red)
        # 빨강을 안 칠한 경우 파랑,빨강 가능
        else:
            not_blue = count_not_color(i, 'B')
            row_color[i] = 'B'
            DFS(i + 1, True, False, cnt + not_blue)
            row_color[i] = 'R'
            not_red = count_not_color(i, 'R')
            DFS(i + 1, True, True, cnt + not_red)


T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    ans = 987654321
    board = []
    for _ in range(N):
        board.append(list(input()))
    cnt = 0
    row_color = ['' for i in range(N)]
    row_color[0], row_color[N - 1] = 'W', 'R'
    # 첫 한 줄은 무조건 흰색
    # 마지막 한 줄은 무조건 빨간색
    # 아닌 애들 cnt에 추가
    for j in range(M):
        if board[0][j] != 'W':
            cnt += 1
        if board[N - 1][j] != 'R':
            cnt += 1
    # print(cnt)
    DFS(1, False, False, cnt)
    print('#{} {}'.format(tc, ans))

#병훈
# W의 행 : w는  1부터 N-3까지 --> 바꿔야될 것의 합은 W[w]
# B의 행 : b는 w+1부터 N-2까지 --> 바꿔야될 것의 합은 B[b]-B[w]
# R의 행 : r는 b+1부터 N-1까지 --> 바꿔야될 것의 합은 R[M-1]-R[b]

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    B = [M] * N;
    R = [M] * N;
    W = [M] * N
    for i in range(N):
        line = input()
        for color in line:
            if color == 'W':
                W[i] -= 1
            elif color == 'B':
                B[i] -= 1
            else:
                R[i] -= 1
        if i != 0:
            W[i] += W[i - 1]
            B[i] += B[i - 1]
            R[i] += R[i - 1]
    MIN = M * N
    for w in range(N - 2):
        for b in range(w + 1, N - 1):
            change = W[w] + B[b] - B[w] + R[N - 1] - R[b]
            if change < MIN:
                MIN = change
    print("#{} {}".format(t, MIN))

