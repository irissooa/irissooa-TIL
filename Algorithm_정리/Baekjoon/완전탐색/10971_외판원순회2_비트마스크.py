'''
외판원순회2를 비트마스크로 풀어보자!
일단 따라쓰기부터...!!!!ㅠㅠ
'''
import sys
sys.stdin = open('input.txt','r')

#idx들을 인자로 넘겨줌
def find(now,before):
    #순회!! 남아있는 경로를 이미 방문한 적 있음
    if dp[now][before]:
        return dp[now][before]

    #모두 방문한 경우 값 출력,dp가 1<<n개의 list가 있으니 idx는 -1
    if before == (1<<n)-1:
        #만약 값이 0보다 크면 값을 return, 아니라면 갈 수없으니 최댓값을 줘서 min갱신 못하게하자
        return path[now][0] if path[now][0] > 0 else sys.maxsize

    #현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = sys.maxsize
    for i in range(1,n):
        #before>>i는 0이고 path값이 0이아니면
        if not (before >> i)%2 and path[now][i]:
            #i부터 0까지 순회를 만든 최소 비용
            tmp = find(i,before|(1<<i)) #before|(1<<i) == before + (1<<i)
            #(now~i),(i~0)의 합과 현재까지의 최소 비용과 비교
            cost = min(cost,tmp + path[now][i])

    #메모이제이션, 중복되는 값들의 합 저장
    dp[now][before] = cost
    return cost


n = int(input())
path = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#메모이제이션 담을 리스트
dp = [[0]*(1<<n) for _ in range(n)]
print(find(0,1))
