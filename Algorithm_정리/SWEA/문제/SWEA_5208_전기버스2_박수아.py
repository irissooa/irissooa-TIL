'''
출발지에서의 배터리 장착은 교환횟수에서 제외
앞에서부터 보면서 bfs돌림?
battery에서 해당 idx에 idx값만큼 갈수 있는 곳을 인접리스트에 담음
그리고 bfs돌리며 dist최솟값....ㅎ
'''
import sys
sys.stdin = open('input.txt','r')

# def BFS(node):
#     q = [node]
#
#     while q:
#         p = q.pop(0)
#         for i in linked[p]:
#             if i == N:
#                 return
#             if dist[i]:
#                 continue
#             dist[i] = dist[p] +1
#             q.append(i)
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     #정류장 수 N,N-1개의 정류장 별 배터리 용량
#     info = list(map(int,input().split()))
#     N = info[0]
#     #종점은 배터리가 없음
#     battery = info[1:]+[0]
#     # print('b',battery)
#     linked = [[] for _ in range(N)]
#     for i in range(N):
#         linked[i].extend(list(x for x in range(i+1,i+battery[i]+1)))
#     # print(linked)
#     dist = [0 for _ in range(N)]
#     BFS(0)
#     print('#{} {}'.format(tc,dist[N-1]-1))

def dfs(L,cnt):
    global MIN
    # if total+(sum(capacity)-tsum) < busstop:
    #     return
    # print(L,cnt)
    if MIN<cnt:
        return
    if L>=len(capacity):
        if MIN>cnt:
            MIN=cnt
            # print('MIN',MIN)
    else:
        for x in range(L+1,L+capacity[L]+1)[::-1]:
            if x>len(capacity):
                continue
            dfs(x,cnt+1)


for tc in range(1,int(input())+1):
    temp=list(map(int,input().split()))
    busstop=temp[0]
    capacity=temp[1:]
    # print(capacity)
    MIN=987654321
    dfs(0,0)
    print('#{} {}'.format(tc,MIN-1))