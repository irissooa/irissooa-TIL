'''
종류1
n//2+1까지 '*'*cnt(+1)늘어나다가 지나면 줄어듦
종류2
n//2만큼 공백으로 시작해서 '*'*cnt(+1)늘어나다가 공백이 0이되면 출력하고 다시 공백 늘어남
종류3
'*'*n만큼 출력된뒤 공백이 1씩늘어나고 별은2씩 줄다가 1이되면 다시 공백줄어듦(공백이n//2)
종류4
'*'*(n//2+1)만큼 출력되고(-1) 공백이 1씩 늘어나다가 cnt가 n//2+1이되면 공백 유지 별개수는 +1
n,m범위 벗어나면 input error
'''
n,m = map(int,input().split())
if not n%2 or n < 0 or n >100 or m < 1 or m > 4:
    print('INPUT ERROR!')
else:
    if m == 1:
        cnt= 1
        idx = 0
        while idx < n:
            print('*'*cnt)
            if idx < n//2:
                cnt+=1
            else:
                cnt -= 1
            idx+=1
    elif m == 2:
        cnt= 1
        idx = 0
        blank = n//2
        while idx < n:
            print(' '*blank+'*'*cnt)
            if idx < n//2:
                cnt+=1
                blank-=1
            else:
                cnt -= 1
                blank+=1
            idx+=1
    elif m == 3:
        cnt= n
        idx = 0
        blank = 0
        while idx < n:
            print(' '*blank+'*'*cnt)
            if idx < n//2:
                cnt-=2
                blank+=1
            else:
                cnt += 2
                blank-=1
            idx+=1
    else:
        cnt= n//2+1
        idx = 0
        blank = 0
        while idx < n:
            print(' '*blank+'*'*cnt)
            if idx < n//2:
                cnt-=1
                blank+=1
            else:
                cnt += 1
            idx+=1


