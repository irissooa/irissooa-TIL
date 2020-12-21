'''
비트마스크, 메모이제이션 이용해서 풀기!
시작값은 0~N-1까지로 정해주기

'''

import sys
sys.stdin = open('input.txt','r')


def maxPer(now,before):
    #방문한적이 있음,
    if dp[now][before] != -1:
        return dp[now][before]
    #모두 방문한 경우 값 출력, dp가 1 <<N 개의 list가 있으니 idx는 -1
    # if before == (1<<N)-1:
    #     return works[now][0] if works[now][0] > 0 else 0

    ans = 1
    for i in range(N):
        if not (before >> i)%2 and works[now][i]:
            #i부터 0까지 일확률 // before|(1<<i) = before + (1<<i)
            tmp = maxPer(i,before|(1<<i))
            ans = max(ans,tmp * works[now][i])

    #메모이제이션, 중복되는 값들의 합을 저장
    dp[now][before] = ans
    return ans


def perm(idx,check):
    global MAX
    if idx == N:
        # print(sel)
        ans = 1
        for i in range(N):
            ans *=works[i][sel[i]]
        if ans>MAX:
            MAX = ans

        return
    for i in range(N):
        if (check & (1<<i))!= 0:
            continue
        sel[idx] = i
        perm(idx+1,check|(1<<i))


def find_path(last,visited):
    if visited == (1<<N)-1:
        return

    if dp[last][visited] is not None:
        return dp[last][visited]

    tmp = INF
    for col in range(N):
        if visited & (1<<col) == 0 and works[last][col] != 0:
            tmp = max(tmp,find_path(col,visited|(1<<col)) + works[last][col])
    dp[last][visited] = tmp
    return tmp



T = int(input())
for tc in range(1,2):
    N = int(input())
    works = [list(map(int,input().split())) for _ in range(N)]
    sel = [0]*N
    # MAX =0
    INF = -sys.maxsize
    dp = [[None]*(1<<N) for _ in range(N)]
    print(find_path(0,1<<0))
    # perm(0,0)
    # print(MAX)
    # print(dp)


    # print(maxPer(0,0))
    # print(dp)