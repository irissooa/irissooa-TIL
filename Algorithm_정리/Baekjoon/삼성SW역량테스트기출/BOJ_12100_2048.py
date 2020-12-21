'''
1.상하좌우 4방향을 5번 돈다
+ 2048규칙 ->
상 : 열을 보는데 위에서부터 보는데, 두개씩 비교해서 만약 수가 같으면 더해서 해당 행 배열 제일 앞에 넣어줌, 만약 다르면 앞의 수를 배열에넣고 그다음 수를 꺼내서 비교
하 : 열을보는데 아래서부터 봄
좌 : 행을 보는데 앞에서부터 봄
우 : 행을 보는데 뒤에서부터 봄
이렇게 한번 움직여서 한 배열에 넣은뒤, 재귀로 보냄(arr,cnt,max)이렇게 상하좌우 전부 돌리게 완전탐색
2. 바꾼 배열을 재귀돌림
'''
import sys
sys.stdin = open('input.txt','r')
from collections import deque
input = sys.stdin.readline


def move(arr,cnt):
    global result
    if cnt ==5:
        for i in range(N):
            if result < max(arr[i]):
                result = max(arr[i])
        return
    for d in range(4):
        temp = [[0 for j in range(N)] for i in range(N)]
        # 상
        if d == 0:
            for i in range(N):
                q = deque()
                for j in range(N):
                    if arr[j][i]:
                        q.append(arr[j][i])
                idx = 0
                while q:
                    if len(q) > 1:
                        a, b = q.popleft(), q.popleft()
                        if a == b:
                            temp[idx][i] = a + b
                        else:
                            temp[idx][i] = a
                            # 제일앞에 다시 넣어줌->다음수와비교해야되니까
                            q.appendleft(b)
                        idx += 1
                    else:
                        c = q.popleft()
                        temp[idx][i] = c
            # print('위',cnt,MAX,'---')
            # for x in temp:
            #     print(x)
            move(temp,cnt+1)
        # 아래
        elif d == 1:
            for i in range(N):
                q = deque()
                for j in range(N - 1, -1, -1):
                    if arr[j][i]:
                        q.append(arr[j][i])
                idx = N - 1
                while q:
                    if len(q) > 1:
                        a, b = q.popleft(), q.popleft()
                        if a == b:
                            temp[idx][i] = a + b
                        else:
                            temp[idx][i] = a
                            q.appendleft(b)
                        idx -= 1
                    else:
                        c = q.popleft()
                        temp[idx][i] = c
            # print('아래',cnt, MAX, '---')
            # for x in temp:
            #     print(x)
            move(temp, cnt + 1)
        # 왼쪽
        elif d == 2:
            for i in range(N):
                q = deque()
                for j in range(N):
                    if arr[i][j]:
                        q.append(arr[i][j])
                idx = 0
                while q:
                    if len(q) > 1:
                        a, b = q.popleft(), q.popleft()
                        if a == b:
                            temp[i][idx] = a + b
                        else:
                            temp[i][idx] = a
                            q.appendleft(b)
                        idx += 1
                    else:
                        c = q.popleft()
                        temp[i][idx] = c
            # print('왼',cnt, MAX, '---')
            # for x in temp:
            #     print(x)
            move(temp, cnt + 1)
        # 오른쪽
        else:
            for i in range(N):
                q = deque()
                for j in range(N - 1, -1, -1):
                    if arr[i][j]:
                        q.append(arr[i][j])
                idx = N - 1
                while q:
                    if len(q) > 1:
                        a, b = q.popleft(), q.popleft()
                        if a == b:
                            temp[i][idx] = a + b
                        else:
                            temp[i][idx] = a
                            q.appendleft(b)
                        idx -= 1
                    else:
                        c = q.popleft()
                        temp[i][idx] = c
            # print('오',cnt, MAX, '---')
            # for x in temp:
            #     print(x)
            move(temp, cnt + 1)


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
move(arr,0)
print(result)