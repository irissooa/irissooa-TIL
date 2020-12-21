'''
2020-12-03 11:15
NxN개의 벌통이 정사각형 모양으로 배치됨
각칸 숫자 꿀의 양
최대한 많은 수익을 내야한다
1. 두명의 일꾼 꿀을 채취할 수 있는 벌통의 수 M 각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택하고, 선택한 벌통에서 꿀 채취 가능
단, 두명의 일꾼이 선택한 벌통 겹칠수없다
2.두 일 꾼 선택한 벌통에서 꿀 채취해 용기에 담음
단, 서로 다른 벌통에서 채취한 꿀이 섞이면 안됨 하나씩!
하나의 벌통에서 꿀을 채취할때 전부 채취해야됨
두 일꾼이 채취할 수 있는 꿀의 양 C
3.채취한 꿀은 시장에서 팔림, 하나의 용기에 있는 꿀의 양이 많을수록 상품가치 높아, 각 용기에 있는 꿀의 양의 제곱만큼 수익 생김
두 일꾼이 꿀을 채취해서 얻을 수 있는 수익의 합이 최대가 되는 경우와 최대수익 출력

1. 두개씩 고를때 방문처리해서 방문한 곳은 못고르게하고 일꾼이 연속된M개를 고름, 각자 sel을 만듦 -> 실패
1. M개 뽑을 수 있는 경우의 수를 모두 뽑고([i,j,honey[i][j]]), 겹치지 않는 것 두개 뽑기
2. 조합함수를 만들어서 그중에 각 합이 C를 넘지 않고 각 값을 제곱해서 더한 값이 최대가 되는 것을 고르기
'''
import sys
sys.stdin=open('input.txt','r')
from collections import deque

# M개를 뽑는 모든 경우의 수 list에 담기
def select(pi,pj,idx):
    global sellist
    for c in range(pj,N):
        sel[idx] = [pi,c,honey[pi][c]]
        # print(sel,idx,honey[pi][c])
        idx += 1
        if idx == M:
            temp = sel[:]
            sellist.append(temp)
            return

def comb(twolist,pidx,total,ans):
    global resultlist
    if total > C:
        return
    if pidx == M:
        if total <= C:
            resultlist.append(ans)
        return
    comb(twolist,pidx+1,total+twolist[pidx][2],ans+(twolist[pidx][2]**2))
    comb(twolist,pidx+1,total,ans)


# 두개를 뽑을건데 i,j가 겹치지 않는것 두개!
def choose(selectlist):
    global MAX,resultlist
    for x in sellist:
        # print('xxxxx',x)
        if len(x) >1:
            for s in x:
                # print('ssss',s,selectlist)
                if s in selectlist:
                    # print('같니',s,selectlist)
                    break
            # 겹치는게 하나도 없으면 추가
            else:
                anslist.append(x)
                result = 0
                comb(anslist[0],0,0,0)
                result += max(resultlist)
                resultlist=deque()
                comb(anslist[1],0,0,0)
                result += max(resultlist)
                # print(resultlist)
                if result > MAX:
                    MAX = result
                    # print('결과야아',result)
                resultlist=deque()
                anslist.pop()
        # 1개만 뽑은 거면
        else:
            if selectlist != x:
                anslist.append(x)
                result = 0
                comb(anslist[0], 0, 0, 0)
                result += max(resultlist)
                resultlist = deque()
                comb(anslist[1], 0, 0, 0)
                result += max(resultlist)
                # print(resultlist)
                if result > MAX:
                    MAX = result
                    # print('결과야아',result)
                resultlist = deque()
                anslist.pop()



T = int(input())
for tc in range(1,T+1):
    # 벌통의 크기, 선택 벌통 개수, 꿀최대양
    N,M,C = map(int,input().split())
    honey = [list(map(int,input().split())) for _ in range(N)]
    # for x in honey:
    #     print(x)
    # print('----')
    sellist = deque()
    MAX = 0
    resultlist = deque()
    visited = [[False for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            sel = [0]*M
            select(i,j,0)
    # print(sellist)
    # 겹치지 않는 두개를 뽑아서 각 C개 뽑은 뒤 수익계산
    for x in sellist:
        anslist = deque()
        anslist.append(x)
        # print('하나들어감',anslist)
        choose(x)

    print('#{} {}'.format(tc,MAX))
