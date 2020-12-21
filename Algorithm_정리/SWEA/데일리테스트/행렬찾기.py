#가로, 세로 시작점을 기준으로 수를 늘려가는데 0을만나면 하나의 행렬 끝
#맨앞에 사각형의 개수 출력 뒤는 행과 열을 곱한 값으로 크가가 작은 순서대로 출력(오름차순)
#2중 for를 도는데 시작지점을 기준으로 

import sys
sys.stdin = open("input.txt", "r")

#선생님풀이
def search_size(r,c):
    r_cnt = 0
    c_cnt = 0
    #띠를 둘러줬기 떄문에 따로 범위를 주지않아도 검사가능, idx에러안남
    
    for i in range(r,N+2):
        if arr[i][c] == 0
            break
        r_cnt += 1
    for j in rangE(c,N+2):
        if arr[r][j] == 0:
            break
        c_cnt += 1
    ans.append([r_cnt,c_cnt])
    init(t,c,r_cnt,c_cnt)
#구한 행렬을 0으로 초기화 시키는 것
def init(r,c,r_cnt,c_cnt):
    for i in range(r,r+r_cnt):
        for j in range(c,c+c_cnt):
            arr[i][j] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #0이면 멈춰야되니까 전체 띠를 두름
    # 제일 위와 제일 밑에 띠를 두른것처럼 0으로 만들어줌
    # 전체적인 띠를 두르는 작업
    arr = [0] * (N+2)
    arr[0] = arr[N+1] = [0] * (N+2)
    for i in range(N):
        #왼쪽 오른쪽에도 띠를 만들어줌
        arr[i+1] = [0]+list(map(int,input().split()))+[0]
    ans = []
    for i in range(1,N+2):
        for j in range(1,N+2):
            if arr[i][j] !=0:
                search_size(i,j)
    #정렬, 행렬크기 기준, 같다면 행크기 기준
    ans = sorted(ans, key=lambda x:((x[0]*x[1]),x[0]))
    print('#{} {}'.format(tc,len(ans)), end = ' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0],ans[i][1]),end= ' ')
    print()








#다른 사람 코드 참조..........ㅠㅠ다시 풀겠습니당....
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dic = {} #가로가 key, 세로가 value
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] > 0:
                cnt += 1
            elif arr[i][j] == 0 and cnt != 0:
                dic[cnt] = dic.get(cnt,0)+1
                cnt = 0
        if cnt > 0:
            dic[cnt] = dic.get(cnt,0)+1
    size = []
    for row, col in dic.items(): #가로 키 세로 값
        size.append((col*row,col,row))
    size.sort()
    print(f'#{tc} {len(size)}',end ='')
    for i in range(len(size)):
        print(size[i][1],size[i][2], end='')
    print()


T = int(input())  # 테스트케이스 T
for t in range(1, T + 1):
    n = int(input())  # nxn크기
    dic = {}  # 최종목표 {키key=가로길이 : 값value=세로길이}
    # 주의 : 모든 사각형의 가로의 값이 다르기 때문에(중복없음) 이를 키값으로 사용가능

    arr = [list(map(int, input().split())) for _ in range(n)]
    # 2차원배열을 한 행 씩 훑으며 1~9의 숫자가 있는지 찾기
    for y in range(n):
        cnt = 0  # cnt = 가로길이(cnt증가)
        for x in range(n):
            # ((1))행x가 증가하다가, 0 초과(1~9)값이 존재 할 때 수세기
            if arr[y][x] > 0:
                cnt += 1  # (가로길이 카운팅)
            # ((2))행x가 증가하다가, 0을 만났는데 and
            # 그런데 이전에 가로길이가 존재했다. dic에 키로 넣어주며
            # 새로 들어온 키면 값을 1, 이전에 있던 키면 1 증가(세로길이 카운팅)
            elif arr[y][x] == 0 and cnt != 0:
                dic[cnt] = dic.get(cnt, 0) + 1
                cnt = 0  # 초기화
            # ((3))행x가 증가하다가, 0을 만나면 cnt 하지 않는다.
            # arr[y][x] == 0 and cnt == 0 이면 어차피 초기화 상태라서 필요없는 코드
            # else:
            #     cnt = 0
        # ((4))행을 다 돌았는데, 0을 못만나고 벽인 경우
        # 벽까지해서 카운팅된 가로길이가 있으면 키값으로 넣어줌.
        if cnt > 0:
            dic[cnt] = dic.get(cnt, 0) + 1

    matrix = []  # [(넓이, 세로, 가로) 순으로 저장]
    for garo, sero in dic.items():
        matrix.append((sero * garo, sero, garo))
    # 넓이를 기준으로 먼저 sort (넓이가 같다면 자동으로 세로 순으로 정렬)
    matrix.sort()

    print('#{} {}'.format(t, len(matrix)), end=' ')  # matrix 개수, 즉 화학물질 개수를 print
    for i in range(len(matrix)):
        print(matrix[i][1], matrix[i][2], end=' ')  # 세로, 가로 순으로 print
    print()

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    size_list = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] != 0: #값이 0이 아닐때
                x = y = 0 #행열초기값 영
                while arr[x+i][j] != 0:#x가 계속 0 부터 시작하면 안되니 +i
                    x+=1 #가로의 길이를 알 수 있다

                while arr[i][y+j] != 0: #y가 계속 0부터 시작하면 안되니까 +j
                    y+=1 #세로의 길이를 알 수 있다

                #x,y sixe값을 빈 리스트에 담음
                # 그 곱이 작은것부터 써줌
                size = []
                size.append([x*y,x,y]) #순서를 정해줄 xy곱과, x와 y를 size list에 담음
                cnt += 1

    print(f'#{tc} {cnt} {size}')

#의수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(N)]
    dic_res = {}
    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[x][y]:
                cnt += 1
            elif arr[x][y] == 0 and cnt != 0:
                dic_res[cnt] = dic_res.get(cnt, 0) + 1
                cnt = 0
        if cnt:
            dic_res[cnt] = dic_res.get(cnt, 0) + 1

    res_arr = []
    for x, y in dic_res.items():
        res_arr.append((x * y, y, x))
    res_arr.sort()
    print(f'#{tc} {len(res_arr)}', end=' ')
    for i in range(len(res_arr)):
        print(f'{res_arr[i][1]} {res_arr[i][2]}', end=' ')
    print()

#병훈
def arr_num_to_zero(arr, i, j):
    size_of_col = 1
    size_of_row = 1

    while True:
        if arr[i + size_of_row][j]:
            size_of_row += 1
        else:
            break
    while True:
        if arr[i][j + size_of_col]:
            size_of_col += 1
        else:
            break
    for row in range(size_of_row):
        for col in range(size_of_col):
            arr[i + row][j + col] = 0

    return [size_of_row, size_of_col]


for t in range(1, int(input()) + 1):
    n = int(input())
    array_size = []
    arr = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        arr[i][1:n + 1] = list(map(int, input().split()))

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]:
                array_size.append(arr_num_to_zero(arr, i, j))

    array_size.sort(key=lambda x: (x[0] * x[1], x[0]))
    result = ''
    for size in array_size:
        result += str(size[0]) + ' ' + str(size[1]) + ' '
    print(f'#{t} {len(array_size)} {result}')