import sys
input = sys.stdin.readline

n,m = map(int,input().split())
if m == 1:
    num = 1
    for i in range(n):
        cnt = 0
        while cnt <n:
            print(num,end =' ')
            cnt+=1
        num+=1
        print()
elif m== 2:
    for i in range(n):
        if i %2:
            num = n
        else:
            num =1
        cnt = 0
        while cnt<n:
            if i%2:
                print(num,end = ' ')
                num-=1
            else:
                print(num,end = ' ')
                num+=1
            cnt +=1
        print()
else:
    num = 1
    for i in range(n):
        cnt = 1
        while cnt <= n:
            print(num*cnt,end = ' ')
            cnt += 1
        num+= 1
        print()