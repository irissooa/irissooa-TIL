'''
V개의  작업
해야할 V개의 작업
어떤 작업은 특정 작업이 끝나야 시작할 수 있음(선행관계)
선행관계를 나타낸 그래프
각 작업은 하나씩 정점으로 표시됨
선행 관계는 방향성을 가진 간선으로 표현
사이클은 존재하지 않음(한 정점에서 시작해서 같은 정점으로 돌아오는 경로)
한번에 하나의 작업씩 처리
가능한 작업순서 중 하나만 제시하면 됨!
선행관계만 잘 지켜서 출력하면 됨!

선행관계를 잘 지켜야되니..bfs아닐까...?ㅎ

+지형오빠 도움
정점을 1부터 도는데 1로 향하는 다른 인접 정점을 찾고 만약에 그 정점에 방문하지 않았다면 q에 담아주고 while문을 돌게함
while문을 나왔을 땐 1의 모든 부모 정점들이 거꾸로 담겨있음, 그것을 ans라는 임시로 정점을 담을 list에 담아준 뒤 거꾸로 뒤집어줌

+채린's
while문을 돌면서 해당 정점을 향한 간선이 있는지 확인하고 만약 방문하지 않았다면 continue를 해줌, 
그렇게 방문하지 않은 부모 정점이 있으면 전부 뛰어넘고 방문한 정점들만 출력해주고 전부 True가 될때까지 계속 반복함
'''
import sys
sys.stdin = open('input.txt','r')
#
# def BFS(v):
#     q = [v]
#     ans = [v] #임시로 v를 담을 리스트
#     visited[v] = True
#     # print(v,'v',end = ' ')
#     while q:
#         #종료조건 만약 0을 제외한 정점들을 전부 돌았다면 멈춰라!
#         #만약 정점 모두 방문을 했다면 그만!
#         if visited[1:V+1] == [True for _ in range(V)]:
#             # print(visited)
#             # print('여기들어옴')
#             break
#         pv = q.pop(0)
#         #w를 돌면서 pv와 연결된 것이 있는지 찾는다
#         for w in range(1,V+1):
#             #w가 pv와 연결된 것이 있는데 만약 w에 방문을 하지 않았다면 w를 q에 넣어줌
#             if G[w][pv] == 1:
#                 #그 이전의 정점이 방문하지 않았다면
#                 if visited[w] == False:
#                     visited[w] = True
#                     q.append(w)
#         #q에 담긴 가지 않았던 정점들을 ans에 추가해줌
#         ans += q
#     # print(pv)
#     # print(ans)
#     # print(visited)
#     # print()
#     #ans는 뒷 순서부터 담겼기 때문에 뒤집어줌
#     ans = ans[::-1]
#     #ans에 마지막으로 연결된 v를 담아줌
#     return ans

#채린's idea로 해보기
# def BFS(v):
#     global result
#     cnt = V
#     while cnt:
#         #전부 True가 되면 끝
#         for i in range(1,V+1):
#             #해당 정점에 방문하지 않았다면 진행!
#             if visited[i] == False:
#                 for w in range(1,len(G[i])):
#                     #pv로 향하는 정점을 아직 방문하지 않았다면 넘어가라!
#                     if visited[w] == False:
#                         break
#                 else:
#                     visited[i] = True
#                     result += str(i) + ' '
#                     cnt -= 1
#     return result


for tc in range(1,11):
    #정점의 총 V와 간선의 총 수 E가 주어짐
    V,E = map(int,input().split())
    #인접행렬
    G = [[0]*(V+1) for _ in range(V+1)]
    temp = list(map(int,input().split()))
    # print(temp)
    visited = [False for _ in range(V+1)]
    for i in range(0,len(temp),2):
        st,ed = temp[i],temp[i+1]
        # print(st,ed)
        G[st][ed] = 1
        # G[ed][st] = 1
    # result = []
    result = ''
    # for i in range(1,V+1):
    #     if visited[i] == False:
    # BFS(1)
            # result.extend(BFS(i))
            # print(visited)
            # print()

    cnt = V
    while cnt:
        # 전부 True가 되면 끝
        for i in range(1, V + 1):
            # 해당 정점에 방문하지 않았다면 진행!
            if visited[i] == False:
                for w in range(1, len(G[i])):
                    # pv로 향하는 정점을 아직 방문하지 않았다면 넘어가라!
                    if visited[w] == False:
                        break
                else:
                    visited[i] = True
                    result += str(i) + ' '
                    cnt -= 1

    print('#{} {}'.format(tc,result))
    # print('#{}'.format(tc),end = ' ')
    # for r in result:
    #     print(r, end = ' ')
    # print()