import sys
input = sys.stdin.readline
'''
아스키 A:65~Z:90
'''

n = int(input())
arr= [['' for j in range(n)] for i in range(n)]
num=65
for j in range(n-1,-1,-1):
    for i in range(n-1,-1,-1):
        arr[i][j] = chr(num)
        num += 1
        if num ==91:
            num = 65
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()