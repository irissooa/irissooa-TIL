'''
20-12-21 12:50-13:17
N개 정수 배열, 가능한 연속 부분합 찾기
연속된 숫자들을 선택해서 합했을떄, 가장 큰 연속 부분합 출력
'''
N = int(input())
arr =list(map(int,input().split()))
dp = [0]*N
dp[0] = arr[0]
for i in range(N-1):
    if arr[i+1] > arr[i+1] + dp[i]:
        dp[i+1] = arr[i+1]
    else:
        dp[i+1] = arr[i+1] + dp[i]
print(max(dp))