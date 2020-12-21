'''
높이 n, 종류m
n100이하 홀수 m은 1~3정수
종류1
i 0,1,2,3,4,5..n
j 0,10,012,3210,01234
i가 홀수일때 j는 역순
j(0,i+1)

종류2
숫자는 idx번호 i
개수는 2*n-1부터 2씩 줄어들고 공백은0부터 1씩 늘어남

종류3
숫자는 1부터 n//2+1까지 각 행이1부터 시작이라고 생각했을때 행만큼 출력 n//2+1부터 줄어듦
'''
n,m = map(int,input().split())
if not n%2 or n<0 or n >100 or m <1 or m>3:
    print('INPUT ERROR!')
else:
    if m==1:
        num = 1
        arr = [['' for j in range(n)] for i in range(n)]
        for i in range(n):
            if i%2:
                for j in range(i+1)[::-1]:
                    arr[i][j] = num
                    num+=1
            else:
                for j in range(i+1):
                    arr[i][j] = num
                    num+=1
        for x in range(n):
            for y in range(x+1):
                print(arr[x][y],end =' ')
            print()
    elif m == 2:
        idx =0
        blank =0
        while idx <n:
            print(' '*blank,end='')
            for i in range(2*(n-idx)-1):
                print(idx,end=' ')
            print()
            idx+=1
            blank+=2
    else:
        for i in range(n):
            if i <= n//2:
                for j in range(1,i+2):
                    print(j,end=' ')
            else:
                for j in range(1,n-i+1):
                    print(j,end=' ')
            print()