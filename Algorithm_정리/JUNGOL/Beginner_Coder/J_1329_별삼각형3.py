'''
N을 입력받고
별개수cnt 1, idx=0
1. '*'*cnt출력
2. 공백+1 cnt+2 idx+1
3. idx == n//2가 되면 별-2,공백-1
'''
n = int(input())
if not n%2 or n < 0 or n > 100:
    print('INPUT ERROR!')
else:
    cnt = 1
    idx = 0
    blank = 0
    while idx < n:
        print(' '*blank+'*'*cnt)
        idx+=1
        if idx <=n//2:
            cnt +=2
            blank+=1
        else:
            cnt -=2
            blank -=1