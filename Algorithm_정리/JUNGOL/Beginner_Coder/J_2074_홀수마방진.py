'''
2020-12-11 15:42-16:03

다음의 순서에 따라 각 위치에 차례대로 값을 넣는다.

1. 첫 번째 숫자인 1을 넣는 위치는 첫 번째 행 가운데이다.

2. 숫자가 N의 배수이면 바로 아래의 행으로 이동하여 다음의 수를 넣고

3. 그렇지 않으면 왼쪽 위로 이동하여 다음의 숫자를 넣는다.
만약 행이 첫 번째를 벗어나면 마지막 행으로 이동하고, 열이 첫 번째를 벗어나면 마지막 열로 이동한다. -> 델타이동

첫숫자를 첫번째 행 가운데 넣는다
num이 N으로 나누어떨어지지 않으면 왼쪽 위로 이동(델타->(i-1)%N,(j-1)%N)
나누어 떨어진다면 아래로 이동((i+1)%4,j)
num += 1 num이 N*N이될때까지 반복
'''

N = int(input())
arr=[[0 for j in range(N)] for i in range(N)]
num = 1
i,j = 0,N//2
arr[i][j] = num
num =1
while num <N*N:
    num += 1
    if num % N !=1:
        ni = (i-1)%N
        nj = (j-1)%N
        # print(ni,nj,num)
    else:
        ni = (i+1)%N
        nj = j
        # print(ni,nj,num,'배수')
    arr[ni][nj] = num
    i,j = ni,nj

for x in arr:
    print(*x)