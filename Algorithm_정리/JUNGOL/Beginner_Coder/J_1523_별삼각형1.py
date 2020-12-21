'''
삼각형 높이 n과 종류 m을 입력 받음
종류1
별 한개씩 늘어남
i : 0,1,..,n, j:0,01,012,...,0123..n
while 돌면서 cnt=1부터 n까지 늘리는데 '*'*cnt한뒤 print();cnt+1

종류2
종류1의 반대

종류3
앞에 공백을 N만큼 추가하고 별을 찍는데 내려갈수록 -1
*은cnt가 2씩 증가

n 크기 100이하의 자연수 m 1,2,3

'''
n,m = map(int,input().split())
if n < 1 or n > 100 or m<1 or m>3:
    print('INPUT ERROR!')
else:
    if m == 1:
        cnt = 1
        while cnt <=n:
            print('*'*cnt)
            cnt+=1
    elif m == 2:
        cnt = n
        while cnt>0:
            print('*'*cnt)
            cnt -= 1
    else:
        blank = n-1
        cnt = 1
        while blank >=0:
            print(' '*blank+'*'*cnt)
            cnt += 2
            blank -= 1
