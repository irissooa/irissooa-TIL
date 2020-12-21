'''
입출력
'''
import sys
sys.stdin = open('input.txt','r')

N = int(input())
for i in range(1,N+1):
    if i == 1:
        ans= ' '*(N-i)+'*'
    elif i == N:
        ans = '*'*(2*i-1)
    else:
        ans = ' '*(N-i)+'*'+' '*(2*i-3) +'*'
    print(ans)