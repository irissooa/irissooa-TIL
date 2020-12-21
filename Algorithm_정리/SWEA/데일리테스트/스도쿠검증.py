# 9*9 스도쿠 2차배열을 입력받아 완성시킨다
# 이때 같은 줄 세로 i가 1~9가 한번씩 다 들어가있는지 확인하는데=> 중복을 제거하는 set을 이용!
# 가로 j도 1~9까지 한번씩 다들어있는지 확인 => set의 len이 9인지 확인
# 이때 더 소규모로 3*3도 1~9가 한번씩 들어가 있는지 확인해야됨 => set의 len이 9인지 확인
# 3*3이 9*9에 위치할 초기값들을 설정하고, 그 안의 수들이 1~9까지 하나씩만 있는지 확인 =>arr[i][j]가 len ==9인지 확인

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]  # 가로입력되는 값을 세로9만큼 반복
    # 세로에 1~9까지 들어있는지 확인하는데 가로도 1~9까지 들어있는지 확인
    # 수를 담을 set을 만든다
    result = 1
    for x in range(9):
        row = set()  # 가로
        col = set()  # 세로
        for y in range(9):
            row.add(arr[x][y])  # 행
            col.add(arr[y][x])  # 열
        if len(row) != 9:
            result = 0
            break  # 스도쿠가 아니니까 끝
        if len(col) != 9:
            result = 0
            break

    trg = 0
    for x in range(0, 9, 3):  # 3*3의 세로 값은 3씩 더해짐
        for y in range(0, 9, 3):
            rec = set()
            for i in range(3):
                for j in range(3):
                    rec.add(arr[x + i][y + j])
            if len(rec) != 9:
                result = 0
                trg = 1  # 하나라도 trg 1이면 빠져나가도록
                break  # 이미 스도쿠가 없으니까 끝
        if trg:  # tru값이 1이냐 1이면 빠져나와라 #이미 그전에 스도쿠가 아니라면 빠져나와라
            break

    print(f'#{tc} {result}')


#병훈
def get_square(arr, i, j):
    square = []
    for i in range(3):
        square.extend(arr[i][j:j + 3])
    return square


def get_col(arr, i):
    col = []
    for j in range(9):
        col.append(arr[j][i])
    return col


for t in range(1, int(input()) + 1):
    arr = []
    sudoku = True
    result = 1
    for i in range(9):
        arr.append(list(map(int, input().split())))
    for i in range(9):
        if (len(set(arr[i])) + len(set(get_col(arr, i)))) < 18:
            sudoku = False
            result = 0

    if sudoku:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                square = get_square(arr, i, j)
                if len(set(square)) < 9:
                    sudoku = False
                    result = 0

    print(f'#{t} {result}')

#선생님풀이
def check():
    for i in range(9):
        row = [0] * 10 
        col = [0] * 10
        for j in range(9):
            #행우선검사
            num1 = sudoku[i][j]
            #열우선검사
            num2 = sudoku[j][i]
            #이미 사용한 숫자라면 유효한 스도쿠가 아니라서 0을 리턴
            if row[num1]:#0, False, [],None,,,등이 아니라 값이 있다면 True
                return 0
            if col[num2]:
                return 0
            #위에 걸리지 않았다면 사용했음을 표시
            row[num1] = col[num2] = 1

            #0~8까지 사용이 가능하므로 0,3,6일때 걸리게됨
            if i % 3 == 0 and j % 3 == 0: #0,3,6이 걸림
                square = [0]*10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    #위에서 리턴되지 않았다면 유효한 스도쿠
    return 1


T = int(input())
for tc in range(1,T+1):
    sudoku = [list(map(int,input(.split()))) for _ in range(9)] #2차원배열 입력받음
    if check(): #check()==1이라면
        print('#{} 1'.format(tc))
    else:
        print('#{} 1'.format(tc))