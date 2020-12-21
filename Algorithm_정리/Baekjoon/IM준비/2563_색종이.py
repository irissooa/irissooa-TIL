'''
가로, 세로 100 정사각형
크기가 각 10
검은 영역 넓이를 구하는 프로그램
'''
N = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
for i in range(N):
    #x는 열, y는 행
    y,x = map(int,input().split())
    for i in range(10):
        for j in range(10):
            arr[y+i][x+j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1


print(cnt)