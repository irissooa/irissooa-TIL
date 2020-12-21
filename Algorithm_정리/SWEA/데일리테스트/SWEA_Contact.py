'''
비상연락망과 연락을 시작하는 당번에 대한 정보가 주어짐
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성
BFS이용, 방문하면 +1을 하여 최단 거리를 기록함
거리가 가장 먼 사람들을 구함! 그리고 같을 때 번호가 큰사람!!
인접행렬이든 리스트든 1부터 100까지 쓸 수 있게 만들어야됨!

(아래 : 문제푸는데 중요하지않음)
같은 값이 계속 반복되는데
인접 리스트로 만약에 받는다면 같은 시작과 끝임에도 계속 들어옴->쓸데없는 짓
여러번 중복해서 저장하는게 싫으면, 이미 들어가있는값이라면 중복해서 넣지 않는 처리해줌
'''
import sys
sys.stdin = open('input.txt','r')


def BFS(s):
    q = []
    #시작점을 넣는다
    q.append(s)
    visited[s] = 1

    while q:# q가 있다면
        #queue는 선입선출, 제일 앞 정점을 뽑음
        p = q.pop(0)
        for i in range(1,101):
            #인접한 정점이고, 그 정점을 방문하지 않았다면
            if arr[p][i] and not visited[i]:
                #queue에 append를 하고 방문표시
                q.append(i)
                visited[i] = visited[p] + 1



for tc in range(1,11):
    L,S = map(int,input().split())
    temp = list(map(int,input().split()))
    #인접행렬, 최대 인원 100이기 때문
    arr = [[0 for j in range(101)] for i in range(101)]
    #데이터의 길이만큼 시작점, 끝점 이어진 것 표시, 2개씩 시작,끝 시작 끝 반복
    for i in range(0,L,2):
        arr[temp[i]][temp[i+1]] = 1

    visited = [0] * (100+1) #정점+1개의 방문배열 만듦,0idx는 사용안함
    MAX_idx = 1#제일 큰값을 담을 변수
    BFS(S)
    for i in range(2,101):
        #크거나 같을때 , 같다면 더 idx가 큰 값!
        if visited[MAX_idx] <= visited[i]:
            MAX_idx = i

    print('#{} {}'.format(tc,MAX_idx))

#선생님 풀이
for tc in range(1,11):
    N, s = map(int,input().split())
    arr = list(map(int,input().split()))

    G = [[0] * 101 for _ in range(101)] #정점번호 1~100
    for i in range(0,N,2): #arr[i]-->arr[i+1]
        #유향그래프
        G[arr[i]][arr[i+1]] = 1
    visit = [0] *101
    Q = [s]
    visit[s] = 1

    while Q:
        v = Q.pop(0)
        #인접정점 w
        for w in range(1,101):
            #인접정점이면서 방문하지 않은 것들을 둘러볼거야
            if G[v][w] and not visit[w]:
                visit[w] = visit[v] + 1 #이건 가장 큰 값을 구할거니까 굳이 나중에 1안빼줘도됨
                Q.append(w)
    ans = 1
    for i in range(2,101):
        #크거나 같을때 , 같다면 더 idx가 큰 값!
        if visit[ans] <= visit[i]:
            ans = i
    print(ans)





#의수
# def bfs(x):
#     q = []
#     q.append(x)
#     visited[x] = 1
#     while q:
#         x = q.pop(0)
#         for nx in range(1, 101):
#             if arr[x][nx] and not visited[nx]:
#                 q.append(nx)
#                 visited[nx] = visited[x] + 1
#
#
# for tc in range(1, 11):
#     N, st = map(int, input().split())
#     lines = list(map(int, input().split()))
#     arr = [[False] * 101 for i in range(101)]
#     visited = [0] * 101
#     for i in range(0, N, 2):
#         arr[lines[i]][lines[i + 1]] = True
#     bfs(st)
#     maxx = 0
#     res = 0
#     for idx, num in enumerate(visited):
#         if maxx < num:
#             maxx = num
#             res = idx
#         elif maxx == num:
#             res = idx
#     print('#{} {}'.format(tc, res))

#현우
# for tc in range(1, 11):
#     N, start = list(map(int, input().split()))
#     link_input = list(map(int, input().split()))
#     link_list = [[False for j in range(101)] for i in range(101)]
#     for i in range(0, N, 2):
#         a, b = link_input[i], link_input[i + 1]
#         link_list[a][b] = True
#     q = []
#     visited = [False for _ in range(101)]
#     visited[start] = True
#     q.append([start, 0])
#     # print(q)
#     ans, ans_idx = start, 0
#     while q:
#         ls = q.pop(0)
#         node, idx = ls[0], ls[1]
#         # print(node,idx)
#         if ans_idx < idx:
#             ans = node
#             ans_idx = idx
#         if ans_idx == idx:
#             # print(node,ans,'ans_idx == idx')
#             if node > ans:
#                 # print('{} = {}'.format(ans,node))
#                 ans = node
#         # print(node,idx)
#         # print(node)
#         for k in range(1, 101):
#             if link_list[node][k] and not visited[k]:
#                 visited[k] = True
#                 q.append([k, idx + 1])
#
#     print('#{} {}'.format(tc, ans))