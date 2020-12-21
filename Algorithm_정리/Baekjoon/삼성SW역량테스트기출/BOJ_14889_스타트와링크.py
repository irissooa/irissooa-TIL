'''
14:11
조합 차 최소구하기
'''
import sys
input = sys.stdin.readline

def power(sel,ops):
    sans = 0
    lans = 0
    # print(sel,ops)
    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                # print(sans,lans)
                sans += arr[sel[i]][sel[j]]
                lans += arr[ops[i]][ops[j]]
    return abs(sans-lans)


def comb(idx,sidx):
    global MIN
    if sidx == N//2:
        # print(steam)
        ops = []
        for i in range(N):
            if i not in steam:
                ops.append(i)
        ans = power(steam,ops)
        # print(ans)
        if ans < MIN:
            MIN = ans
        return
    if idx == N:
        return
    steam[sidx] = idx
    comb(idx+1,sidx+1)
    comb(idx+1,sidx)


# def comb2(idx):
#     if idx == N:
#         if sum(sel) != N//2:
#             return
#         print(sel)
#         return
#
#     sel[idx] = i
#     comb2(idx+1)
#     sel[idx] = 0
#     comb2(idx+1)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
steam = [0]*(N//2)
sel = [0]*N
MIN = 987654321
comb(0,0)
# comb2(0)

print(MIN)
