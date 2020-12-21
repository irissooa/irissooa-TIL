'''
#1. 1로시작하는 순열을 구한뒤!(순열함수로 만들어보자)
#2. for i in range(N-1): arr[i-1][i]의 합을 더한 뒤, 최소값! -> 순환하기 때문에 i-1부터봐도됨
'''
import sys
sys.stdin = open('input.txt','r')

#순열을 비트마스크로 풀어보쟈...
def perm(idx,check):
    global idx_list
    if idx == N:
        #idx담아주기, 그냥 p를 넣으면 얕은복사로 이전에 들어있던 원소들도 모두 바뀌기 때문에 깊은복사인 인덱싱으로 넣어줌
        ans = p[:]
        idx_list.append(ans)
        return
    for i in range(N-1):
        if check & (1<<i) != 0:
            continue
        p[idx] = cost_idx[i]
        perm(idx+1,check|(1<<i))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    costs = []
    for c in range(N):
        costs.append(list(map(int,input().split())))
    cost_idx = [i for i in range(1,N)]
    #제일앞에 0인 순열 구하기(idx)
    p = [0]*N
    idx_list = []
    perm(1,0)
    MIN = 987654321
    # print(idx_list)
    for idx in range(len(idx_list)):
        SUM = 0
        for i in range(N):
            # print(idx_list[idx][i-1],idx_list[idx][i],costs[idx_list[idx][i-1]][idx_list[idx][i]])
            if MIN > SUM:
                SUM += costs[idx_list[idx][i-1]][idx_list[idx][i]]
        if MIN > SUM:
            MIN = SUM
    print('#{} {}'.format(tc,MIN))






