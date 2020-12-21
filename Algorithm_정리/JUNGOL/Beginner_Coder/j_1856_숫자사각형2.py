import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = 1
for i in range(n):
    if i%2:
        for j in range(m-1,-1,-1):
            print(num+j,end=' ')
            # num += 1
        num = num+m
    else:
        for j in range(m):
            print(num,end = ' ')
            num += 1
    print()