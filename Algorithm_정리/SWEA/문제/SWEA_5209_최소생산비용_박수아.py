'''
한행에 한개를 골라서 최소 생산비용을 골라라
순열로 각 열의 행을 뽑고, 그 값들 중 최솟값을 구하라
'''
import sys
sys.stdin = open('input.txt','r')

def perm(idx,total):
    global MIN
    if total >= MIN:
        return

    if idx == N:
        if MIN > total:
            MIN = total
        return

    for i in range(N):
        if not sel[i]:
            sel[i] = 1
            perm(idx+1,total+factory[idx][i])
            sel[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    factory = [list(map(int,input().split())) for _ in range(N)]
    MIN = 987654321
    sel = [0]*N
    perm(0,0)
    print('#{} {}'.format(tc,MIN))