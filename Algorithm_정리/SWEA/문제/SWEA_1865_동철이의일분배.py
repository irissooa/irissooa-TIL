import sys
sys.stdin = open('input.txt','r')
def perm(idx,percent):
    global MAX
    if percent <= MAX:
        return
    if idx == N:
        # print(sel,percent)
        if MAX < percent:
            MAX = percent
        return
    for i in range(N):
        if not sel[i]:
            sel[i] = 1
            perm(idx+1,percent*works[idx][i])
            sel[i] = 0

def perm_bit(idx,check,percent):
    global MAX
    if percent <= MAX:
        return

    if idx == N:
        if percent > MAX:
            MAX = percent

        return
    for i in range(N):
        if (check & (1<<i))!= 0:
            continue
        sel[idx] = True
        perm_bit(idx+1,check|(1<<i),percent*works[idx][i])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    works = [list(map(lambda x:int(x)/100,input().split())) for _ in range(N)]
    sel = [0]*N
    MAX = -1
    # perm(0,1)
    perm_bit(0,0,1)
    result = MAX*100
    print('#{}'.format(tc),end=' ')
    print('{0:0.6f}'.format(result))