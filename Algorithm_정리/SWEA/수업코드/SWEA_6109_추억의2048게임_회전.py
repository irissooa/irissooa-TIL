# 위쪽으로 밀기
def push():
    for i in range(N):
        stack = []
        for j in range(N - 1, -1, -1):
            # 값이 있다면 스택에 담기
            if tile[j][i]:
                stack.append(tile[j][i])
                tile[j][i] = 0

        idx = 0
        while stack:
            if len(stack) > 1:
                # 두개의 값을 꺼내어
                A, B = stack.pop(), stack.pop()
                # 같다면 더하여 기록
                if A == B:
                    tile[idx][i] = A + B
                # 다르다면 A만 기록, B는 다시 넣기
                else:
                    tile[idx][i] = A
                    stack.append(B)
                # 위의 작업이 끝나면 무조건 idx 증가
                idx += 1
            # 한개남았을땐 바로 꺼내어 넣기
            else:
                tile[idx][i] = stack.pop()


# 시계방향으로 90도 회전
def rotation(arr):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[N - 1 - j][i]
    return tmp


for tc in range(1, int(input()) + 1):
    N, S = input().split()  # 한변의길이, 방향명령
    N = int(N)  # 정수화
    # 게임판 입력
    tile = [list(map(int, input().split())) for _ in range(N)]

    # 그냥 밀기
    if S == 'up':
        push()
    # 회전 밀기 회전 회전 회전
    elif S == 'left':
        tile = rotation(tile)
        push()
        tile = rotation(tile)
        tile = rotation(tile)
        tile = rotation(tile)
    # 회전 회전 밀기 회전 회전
    elif S == 'down':
        tile = rotation(tile)
        tile = rotation(tile)
        push()
        tile = rotation(tile)
        tile = rotation(tile)
    # 회전 회전 회전 밀기 회전
    else:  # right
        tile = rotation(tile)
        tile = rotation(tile)
        tile = rotation(tile)
        push()
        tile = rotation(tile)

    # 출력
    print("#{}".format(tc))
    # for i in range(N):
    #     for j in range(N):
    #         print(tile[i][j], end=" ")
    #     print()

    for i in range(N):
        print(*tile[i])
