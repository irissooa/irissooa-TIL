'''
가로 세로 크기 100 정사각형
색종이가 붙은 검은 영역 넓이 구하기
색종이를 좌표에 올려 1로 바꿈
1인것 개수 세기
'''
N = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
for n in range(N):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            ans+=1

print(ans)