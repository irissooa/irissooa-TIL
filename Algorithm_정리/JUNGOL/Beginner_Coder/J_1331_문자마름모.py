'''
20-12-11 11:29-13:45
마름모 한번의 길이ㅣ N
1) 첫번쨰 행의 중앙부터 출발하여 시계반대 방향으로 A부터 채워나감,Z다음은 A
2) 바깥 부분이 다 채워지면 두번째 행 중앙부터 다시 같은 작업 반복
3) 같은 방법으로 마름모 다 채워지도록 출력

1.첫시작 chr(65)부터 좌하대->우하대->우상대->좌상대 순서로 채워나감!
1) squ = 1
n만큼 문자입력, d= 0
2)squ = 2
n-1만큼 문자입력 , d = 1
3) squ = 3
n-1만큼 문자입력, d=2
4) squ = 4
n-2만큼 문자입력, d=3
5)squ가 4인데 cnt가 0이되면 i는 그대로, j-1로 옮김, squ = 1로 초기화하고, n-=1로 함
6)반복
2. 범위를 벗어나지 않게, 배열에 들어있지 않은 것, n*n개수만큼 반복
3. Z가 끝나면(91이되면 65로 초기화)
'''
n = int(input())
N = n
arr = [['' for j in range(n*2-1)] for i in range(n*2-1)]
di = [1,1,-1,-1] #좌하대,우하대,우상대,좌상대
dj = [-1,1,1,-1]
num = 65
cnt = n
i,j,d =0,n-1,0
squ = 1
arr[i][j] = chr(num)
num += 1
cnt-=1
while n >=1:
    if squ == 1 and cnt ==0:
        d=1
        squ += 1
        cnt = n-1
    if squ == 2 and cnt ==0:
        d= 2
        squ += 1
        cnt = n-1
    if squ == 3 and cnt ==0:
        d= 3
        squ += 1
        cnt = n-2
    if squ == 4 and cnt ==0:
        d= 0
        n-=1
        squ  = 1
        cnt = n
        i,j = i-1,j
    ni = i+di[d]
    nj = j+dj[d]
    arr[ni][nj] = chr(num)
    # print(ni,nj,cnt,arr[ni][nj],squ,n)
    num += 1
    cnt-=1
    i,j = ni,nj
    if n== 1:
        break
    if num > 90:
        num = 65
idx=2*N-2
for x in range((2*N)-1):
    print(' '*idx,end='')
    for y in range(2*N-1):
        if arr[x][y]:
            print(arr[x][y],end=' ')
    print()
    if x <N-1:
        idx -=2
    else:
        idx+=2
