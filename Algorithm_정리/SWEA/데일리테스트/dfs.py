# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
# 
# def dfs(v):
#     #방문체크
#     visited[v] = 1 #True란 뜻
#     print(v,end = ' ') #출력
#     #v의 인접한 정점 중에서 방문안한 정점을 재귀호출
#     #인접행렬의 해당하는 v행을 돌려야됨
#     for w in range(1,N+1): #정점의 개수만큼 돌릴거야(0번안씀)
#         #G가 v시작정점 w 뺑뺑이돔 이게 1(인접하여있고) 그 인접한정점이 0(방문안했으면) dfs를 w를 가지고 돌려라
#         if G[v][w] == 1 and visited[w]==0: #인접해있고 방문을 안했으면
#             dfs(w)
# 
# # 정점, 간선
# N, E = map(int,input().split())
# #간선들..
# temp = list(map(int,input().split()))
# #인접행렬
# G = [[0] * (N+1) for _ in range(N+1)]
# #방문체크
# visited = [0] * (N+1)
# #간선들을 인접행렬에 저장
# for i in range(E): #8쌍(Edge만큼)을 받아올거야
#     s,e = temp[2*i], temp[2*i+1] #start,end
#     # 인접행렬 이어져 있다고 표시하기 위해
#     # s->e 가 1이고, e->s 도 1이라고 표시함
#     G[s][e] = 1
#     G[e][s] = 1
# 
# dfs(1)
# 
# '''
# input
# 7 8
# 1 2 #여기부터는 연결되어 있는 두 정점
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
# '''
# 
# def DFS(v):
#     print(v, end = ' ')
#     visited[v] = 1 #방문을 했기 때문에 바꿔줌
#     for i in range(1, V+1): #global이 아니라도 V를 쓸수 있는건 수정이 아니라 읽어올거기 때문
#         #현재 내 정점 v와 연결되어 있는지 확인
#         if arr[v][i] == 1 and visited[i] == 0: #1 : 연결이 되어있다면, 0: 방문하지 않았다면
#             DFS(i) #DFS(i)를 출력
# 
# 
# # input
# # 정점수(꼭지점), 간선수(연결된 선들)
# V, E = map(int, input().split())
# #인접행렬 초기값을 만듦
# #한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해
# #0번 idx따위 버려버리기
# arr = [[0]*(V+1) for _ in range(V+1)] #V+1을 하는 이유는? V까지의 idx를 쓰기위해
# 
# for i in range(E):
#     st, ed = map(int, input().split())
#     #그래프가 방향이 없기 때문에 서로 이어져 있다고 표시해줌
#     #방향이 정해져있는건 arr[st][ed] = 1만 해도됨
#     #무향그래프이기 떄문에 서로 연결되어있음을 표시
#     arr[st][ed] = arr[ed][st] = 1
# 
# #방문 배열 선언
# visited = [0] * (V+1)
# 
# DFS(1) #1번부터 출발할거야
# 

#DFS 스택 이용한 버전
#input
# 정점수(꼭지점), 간선수(연결된 선들)
V, E = map(int, input().split())
#인접행렬 초기값을 만듦
#한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해
#0번 idx따위 버려버리기
arr = [[0]*(V+1) for _ in range(V+1)] #V+1을 하는 이유는? V까지의 idx를 쓰기위해

for i in range(E):
    st, ed = map(int, input().split())
    #그래프가 방향이 없기 때문에 서로 이어져 있다고 표시해줌
    #방향이 정해져있는건 arr[st][ed] = 1만 해도됨
    #무향그래프이기 떄문에 서로 연결되어있음을 표시
    arr[st][ed] = arr[ed][st] = 1

#방문배열
visited = []
#스택
stack = []
#시작정점을 담는다
stack.append(1)

#stack이 빌때까지 무한히 반복
while len(stack)>0:
    #정점을 하나 꺼냄
    v = stack.pop() #-1을 쓰지않아도 자동으로 들어감()
    #해당 정점이 방문한 정점이 아니라면
    if v not in visited: #visited 안에 v가 안들어있다면
        print(v, end = ' ') #경로를 보기위한 출력(그리 중요치않음)
        #정점을 방문체크
        visited.append(v)
        #현재 내 정점에서 연결돼있는 모든 정점을 탐색하기 위한 반복문
        for i in range(1,V+1):
            # 현재정점과 연결되어 있으면서 방문하지 않은 정점i가 있다면
            if arr[v][i] == 1 and i not in visited:
                #모두 다 스택에 push
                stack.append(i) #스택에 담겠다