cnt=1
arr=[[0]*5 for i in range(5)]

row_start=0
row_end=4
col_start=0
col_end=4

while row_start<=row_end and col_start<=col_end:
    # 왼쪽=> 오른쪽
    for i in range(col_start, col_end+1):
        arr[row_start][i]=cnt
        cnt+=1
    row_start +=1

    # 위=> 아래
    for i in range(row_start, row_end + 1):
        arr[i][col_end] = cnt
        cnt += 1
    col_end -= 1

    # 오른쪽=> 왼쪽
    for i in range(col_end, col_start-1, -1):
        arr[row_end][i]=cnt
        cnt+=1
    row_end -=1

    # 아래=> 위
    for i in range(row_end, row_start - 1, -1):
        arr[i][col_start] = cnt
        cnt += 1
    col_start += 1

print(arr)

#선생님 풀이
#우하좌상 방향으로 출력해야됨!
dr = [0,1,0,-1]
dc = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input9)
    #0으로 채워진 N*N배열
    arr = [[0] * N  for _ in range(N)]
    #방향은 idx를 의미함 0:우,1:하, 2:좌,3:상
    dir = 0
    #시작점
    r = 0
    c = 0
    num = 1
    
    while num <= N * N:
        arr[r][c] = num #현재 칸에 값을 저장
        num += 1 #다음 숫자 준비
        
        #다음 칸을 결정
        #다음 좌표는 현재좌표 + 방향
        nr = r + dr[dir]
        nc = c + dc[dir]

        #idx가 벗어나는지 체크해야됨, 그리고 방문하지 않은 곳인지 확인
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            #현재좌표 갱신
            r,c = nr,nc
        else:
            #모듈 연산 우(0),하(1),좌(2),상(3) 다음 방향으로 바꿈
            dir = (dir+1) % 4
            r += dr[dir]
            C += dc[dir]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()

#선생님 달팽이 다른 풀이
T = int(input())
for tc in range(1,T+1):
    N = int(input())

    nums = [[0]*N for _ in range(N)]
    K = N #이동거리, 우리가 처음으로 이동할 거리
    d = 1 #방향, 처음에는 열이 증가하기 때무에 1로 둠
    row = 0 #행
    col = -1 #열(초기에는 수평이동이므로 -1로 초기화)
    num = 1 #넣을값

    while True:
        #수평이동
        for c in range(K):
            col += d
            nums[row][col] = num
            num += 1
        #수평이동 끝 이제 수직이동
        K -= 1

        if K == 0:
            break

        #수직이동
        for r in range(K):
            row += d
            num[row][col] = num
            num += 1

        #수직이동이 끝 수평이동
        d *= -1
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()