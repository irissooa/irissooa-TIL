'''
20/10/23/22:15
1. x % 3 == 0; x//3
2. x % 2 ==0; x//2
3. x-1
이 3가지 방법을 통해 1을 만드는 최소 연산 수?
BFS로 풀기!
방문배열 이용해서 cnt를 방문배열에 넣어줌!
그리고 최솟값 구하기
'''
import sys
sys.stdin = open('input.txt','r')

# MIN = 987654321
# q = []
# def BFS(num,cnt):
#     global MiN
#     q.append((num,cnt))
#     while q:
#         n,c = q.pop()
#         if c > MIN:
#             return
#         if n == 1:
#             if MIN > c:
#                 MIN = c
#             return
#
#         if visited[n]!=0:
#             if n % 3 == 0:
#                 c += 1
#                 BFS(n//3,c)
#             if n % 2 == 0:
#                 c += 1
#                 BFS(n//2,c)

# visited = [0 for _ in range(N+1)]


N = int(input())
# 점화식
'''
N이라는 수는 N//3을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
N이라는 수는 N//2을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
N이라는 수는 N-1을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
따라서 !!! 점화식 : dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )
'''
dp = [0 for _ in range(N+1)]
for i in range(2,N+1):
    dp[i] = dp[i-1]+1
    if i %2 ==0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2]+1
    if i %3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3] +1
print(dp[N])