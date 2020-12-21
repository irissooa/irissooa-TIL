from collections import deque


def push():
    # up일때
    if S == 'up':
        #열우선순회
        for i in range(N):
            queue = deque()
            for j in range(N):
                if tile[j][i]:
                    queue.append(tile[j][i])
                    tile[j][i] = 0

            #가장 위부터 채워나가기
            idx = 0
            while queue:
                if len(queue) > 1:
                    A, B = queue.popleft(), queue.popleft()
                    if A == B:
                        tile[idx][i] = A + B
                    else:
                        tile[idx][i] = A
                        queue.appendleft(B)
                    idx += 1
                else:
                    tile[idx][i] = queue.popleft()
    # down일때
    elif S == 'down':
        #열역우선순회
        for i in range(N):
            queue = deque()
            for j in range(N - 1, -1, -1):
                if tile[j][i]:
                    queue.append(tile[j][i])
                    tile[j][i] = 0
            #가장아래부터 채워나가기
            idx = N - 1
            while queue:
                if len(queue) > 1:
                    A, B = queue.popleft(), queue.popleft()
                    if A == B:
                        tile[idx][i] = A + B
                    else:
                        tile[idx][i] = A
                        queue.appendleft(B)
                    idx -= 1
                else:
                    tile[idx][i] = queue.popleft()
    # left일때
    elif S == 'left':
        #행우선순회
        for i in range(N):
            queue = deque()
            for j in range(N):
                if tile[i][j]:
                    queue.append(tile[i][j])
                    tile[i][j] = 0
            #가장 왼쪽부터 채워나가기
            idx = 0
            while queue:
                if len(queue) > 1:
                    A, B = queue.popleft(), queue.popleft()
                    if A == B:
                        tile[i][idx] = A + B
                    else:
                        tile[i][idx] = A
                        queue.appendleft(B)
                    idx += 1
                else:
                    tile[i][idx] = queue.popleft()
    # right일때
    else:
        #행역우선순회
        for i in range(N):
            queue = deque()
            for j in range(N - 1, -1, -1):
                if tile[i][j]:
                    queue.append(tile[i][j])
                    tile[i][j] = 0

            #가장 오른쪽 부터 채워나가기
            idx = N - 1
            while queue:
                if len(queue) > 1:
                    A, B = queue.popleft(), queue.popleft()
                    if A == B:
                        tile[i][idx] = A + B
                    else:
                        tile[i][idx] = A
                        queue.appendleft(B)
                    idx -= 1
                else:
                    tile[i][idx] = queue.popleft()


for tc in range(1, int(input()) + 1):
    N, S = input().split()  # 한변의 길이, 방향명령어
    N = int(N)  # 정수화
    tile = [list(map(int, input().split())) for _ in range(N)]

    push()

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(tile[i][j], end=" ")
        print()
