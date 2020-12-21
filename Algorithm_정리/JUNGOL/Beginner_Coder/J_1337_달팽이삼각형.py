'''
n높이
숫자 0부터 9까지(반복) 삼각형으로 출력
델타이동 [우하대,좌,상]
범위를 벗어나지 않고 숫자가 없으면 적어주기
범위 -> n범위밖 + j는 i까지만 갈수있다
'''
n = int(input())
arr = [['' for j in range(n)] for i in range(n)]
di = [1,0,-1]#우하대, 좌,상
dj = [1,-1,0]
num = 0
cnt = 0
for i in range(1,n+1):
    cnt += i
i,j,d=0,0,0
arr[i][j] = num
# print(cnt)
num+=1
while cnt >1:
    ni = i + di[d]
    nj = j + dj[d]
    if 0 <= ni < n and 0 <= nj <= i+1 and arr[ni][nj] == '':
        # print(i,j,ni,nj)
        i,j = ni, nj
        arr[ni][nj] = num
        num += 1
        cnt -= 1
        if num > 9:
            num = 0
    else:
        d = (d+1)%3
for i in range(n):
    for j in range(i+1):
        print(arr[i][j],end = ' ')
    print()