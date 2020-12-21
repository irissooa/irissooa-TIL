import sys
input = sys.stdin.readline

n = int(input())
num = 1
arr = [[0 for j in range(n)] for i in range(n)]
for j in range(n):
    for i in range(n):
        arr[i][j] = num
        num += 1
for i in range(n):
    for j in range(n):
        print(arr[i][j],end =' ')
    print()