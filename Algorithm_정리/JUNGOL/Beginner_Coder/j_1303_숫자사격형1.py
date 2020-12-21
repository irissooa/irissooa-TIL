import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = 1
for i in range(n):
    for j in range(m):
        print(num,end = ' ')
        num += 1
    print()