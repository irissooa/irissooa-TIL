'''
20-12-11 09:58-10:08
정사각형 크기 입력 후 시계방향 돌면서 출력
가장왼쪽 위부터 아래 왼쪽 위 오른쪽 순서
1.n배열을 만들고 0으로 둘러싼다
2.우하좌상으로 델타로 움직임, 배열이 0 이아니면 기록 반복
'''
n = int(input())
num =1
di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
arr = [[0 for j in range(n+2)] for i in range(n+2)]
i,j,d = 1,1,0
arr[i][j] = num
num+=1
cnt = 0
while num<=n*n:
    ni=i+di[d]
    nj = j+dj[d]
    if 1<=ni<=n and 1<=nj<=n and not arr[ni][nj]:
        arr[ni][nj] = num
        i,j = ni,nj
        num+=1
    else:
        d=(d+1)%4
for x in range(1,n+1):
    print(*arr[x][1:n+1])