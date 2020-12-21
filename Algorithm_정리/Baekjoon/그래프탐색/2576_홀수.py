'''

'''
import sys
sys.stdin =open('input.txt','r')
MIN = 100
SUM = 0
flag=False
for _ in range(7):
    n = int(input())
    if n % 2:
        SUM += n
        flag = True
        if MIN > n:
            MIN = n
if flag:
    print(SUM)
    print(MIN)
else:
    print(-1)
