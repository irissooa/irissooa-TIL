'''
2020-12-03 11:05-11:13
맛에대한 점수 조합중 칼로리를 넘지 않는 가장 높은 점수 구하기
조합 함수 짜고 점수를 제한으로 걸자
'''
import sys
sys.stdin = open('input.txt','r')

def comb(idx,total):
    global MAX
    if total > L:
        return
    if idx == N:
        if sum(sel) > MAX:
            MAX = sum(sel)
        return
    sel[idx] = taste[idx][0]
    comb(idx+1,total+taste[idx][1])
    sel[idx] = 0
    comb(idx+1, total)

T = int(input())
for tc in range(1,T+1):
    #재료수, 제한칼로리
    N,L = map(int,input().split())
    # 재료에 대한 맛에 대한 점수와 칼로리
    taste = [list(map(int,input().split())) for _ in range(N)]
    sel = [0]*N
    MAX = 0
    comb(0,0)
    print("#{} {}".format(tc,MAX))