'''
1. 입력범위 초과시 (1~100,홀수)INPUT ERROR 출력
2. j : (N//2,-1,-1)하는동안 ,i : s=0(i다하면+1) (N//2-s,N//2+s+1)
3. ans = 65로 하고 i넘어가면서 +=1 90 넘어가면 65로 리셋
'''
import sys
input = sys.stdin.readline

n = int(input())
if n < 1 or n > 100 or not n%2:
    print('INPUT ERROR')
else:
    arr = [[' ' for j in range(n)] for i in range(n)]
    ans = 65
    s = 0
    for j in range(n//2,-1,-1):
        for i in range(n//2-s,n//2+s+1):
            arr[i][j] = chr(ans)
            ans+=1
            if ans > 90:
                ans = 65
        s += 1

    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()