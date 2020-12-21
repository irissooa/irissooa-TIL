'''
V개의 노드 개수
방향성 없는 E개 간선
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는가
S와 G가 서로 연결되어 있지 않다면 0 출력
BFS이용, 방문하면 +1을 하여 최단 거리를 기록함
인접리스트도 이용함
'''
import sys
sys.stdin =open('input.txt','r')

def BFS(s):
    q = []
    #시작점을 넣는다
    q.append(s)
    visited[s] = 1

    while q:# q가 있다면
        #queue는 선입선출, 제일 앞 정점을 뽑음
        p = q.pop(0)

        #해당 정점의 인접리스트를 볼거야
        for i in adj_list[p]:
            #그 정점을 방문하지 않았다면
            if not visited[i]:
                #queue에 append를 하고 방문표시
                q.append(i)
                visited[i] = visited[p] + 1 #다음 방문표시를 해주는데, 현 방문표시에+1로 거리를 표현함
            #종료조건(도착한다면)
            if p == G:
                return visited[G]-1
    #도착하지 못한다면
    return 0



T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    #인접 리스트
    adj_list = [[] for _ in range(V+1)]
    #간선수만큼 시작점, 끝점 이어진 것 표시
    for i in range(E):
        st,ed = map(int,input().split())
        #시작점(idx)의 list에 ed를 넣음
        adj_list[st].append(ed)
        #끝점(idx)의 list에 st를 넣음
        adj_list[ed].append(st)
    S, G = map(int,input().split())
    visited = [0] * (V+1) #정점+1개의 방문배열 만듦,0idx는 사용안함
    # BFS(S)

    print('#{} {}'.format(tc,BFS(S)))


#선생님풀이
for tc in range(1,int(input())+1):
    V,E = map(int,input().split())
    #인접행렬
    G = [[0] * (V+1) for _ in range(V+1)]
    #인접리스트
    G = [[] * (V+1) for _ in range(V+1)]



    for _ in range(E):
        u,v = map(int,input().split())
        #방향이 없기 때문
        G[u][v] = G[v][u] = 1
        G[u].append(v)
        G[v].append(u)


    s,e = map(int,input().split()) #출발 도착
    
    visit = [0] * (V+1) #정점의 개수만큼 ㄷ만듦
    Q = [s] #출발점을 미리 넣어둠
    visit[s] = 1 #출발점의 방문표시 0으로 해야되지만 방문표시랑 같이 사용하기 위해 1이라고 함, 큐에 삽입
    
    while Q: #빈큐가 아닐동안 반복
        v = Q.pop(0) #큐에서 뺌
        # #여기다가 종료조건을 줘도됨
        # if v == e:
        #     break
        #v의 방문하지 않은 인접정점을 찾는다
        #연결된 모든 정점들 확인함
        for w in range(1,V+1):
            if G[v][w] and not visit[w]: #G[v][w] == 1 and visit[w]==0:이란 말
                visit[w] = visit[v] + 1 #거리계산
                # if w == e:# 도착점에 도착했네?
                #     Q.clear() #큐를 비우고(break해도 while에서 못나가서) 빠짐
                #     break
                Q.append(w)
        #인접리스트
        for w in G[v]:
            if visit[w] ==0:
                visit[w] = visit[v]+1
                Q.append(w)
    print(visit[e]-1)#visit을 방문표시와 거리를 같이 표현했기 떄문에 원래 거리로 했을 시 0부터 시작이니 1을 빼줌