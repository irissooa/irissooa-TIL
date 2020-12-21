#V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
#특정한 두개의 노드에 경로가 존재하는지 확인하는 프로그램
#경로가 있으면 1 없으면 0 출력
#노드번호는 1번부터 존재, V개의 노드 중 간선으로 연결되지 않은 경우도 있음
#첫줄 테스트케이스
#테스트케이스의 첫줄에 V와 E가 주어짐
#둘째줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어짐
#E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어짐

#DFS, 이건 방향이 있음!
#input받기
#정점수(꼭지점), 간선수(연결된 선들) 주어짐
#인접행렬 초기값을 만듦
#한칸 더 크게 만드는 이유는 인덱스를 맞추어 주기 위해(0번 idx버림, V까지 idx로 쓰기 위해)
#그래프 방향이 있기 때문에 arr[st][ed] = 1만 해줘도 됨
#방문배열을 선언해주고
#방문(함수) , 방문을 했을 떄 1로 바꿔줌
# 현재 내 정점 v와 연결되어 있는지 확인
#연결이 되어있고 : 1, 방문하지 않았다면(0)
#DFS(i)로 반복
#그러다가 i == G(종점)으로 가면 이어진 거니까 1출력

import sys
sys.stdin = open('input.txt','r')

ans = 0 #global 변수 선언
def DFS(v):
    #이번 DFS는 return값이 없음, 그래서 도착지에 도착하면 표시를해줌(global 변수에)
    global ans
    visited[v] = True #방문을 했으니 True
    #종료조건!!, 못찾은건 어차피 ans = 0으로 끝날거니까 따로 조건지정안해도됨
    if v == G:
        ans = 1 #표시를 해준거야 이 함수는 리턴값이 없지만 global변수로 답을 찾았다고 표시를 해줌!(종료는 아님, 그 상위의 DFS 돌아가고있음)
    # 정점만큼 돌면서
    #Linked[v][i] 이게 1(이어져있고) 방문을 안했고(False)
    for i in range(1, V+1): #정점1번부터 볼거야아
        if Linked[v][i] == 1 and visited[i] == False:
            DFS(i) #이거 진심 이해0 -> 뭐냐고,,,,이건 그냥 쓰다보면...이해된대....ㅎ for문 돌듯...걍..재귀야.............




T = int(input())
for tc in range(1,T+1):
    ans = 0 #tc돌때마다 0으로 초기화 해줘야됨!!!
    V, E = map(int,input().split())
    #인접행렬 초기값
    Linked = [[0]*(V+1) for _ in range(V+1)]
    # print(arr)

    #방문배열 선언
    visited = [False for _ in range(V+1)] #배열의 idx를 표시해줘야되는데, 그러면 V까지 꼭 나와야함.
    # 근데 (1,V+1)을 하면 어차피 길이가 (V)와 같음 그래서 (V+1)로 1개 더 추가함
    # print(type(visited))
    # print(visited)

    for i in range(E): #간선수만큼 볼거야..
        st, ed = map(int,input().split()) #start, end
        #유향이기 때문에 st->end = 1만 해주면 됨
        Linked[st][ed] = 1

    S,G = map(int,input().split()) #E개의 줄 이후 출발노드,도착노드 주어짐
    DFS(S) #함수를 선언해줌(출발점), 값이없으니까 변수에 할당을 못함. 그래서 표시한 값을 지정해준거야!
    print('#{} {}'.format(tc,ans))

#선생님 풀이
def DFS(v):
    visit[v] = 1
    if v == e: #도착점과 같아
        return 1
    for w in range(1,V+1):
        if G[v][w] == 1 and visit[w] == 0:
            #현재방문한 정점 v라고 생각했을 때 w1,w2,w3,,,등등 갔다가 올건데
            #그중에 만약 1이 나온다면 굳이 반복문 다 돌지 않고 바로 끝내주면됨!!!!
            if DFS(w) == 1:
                return 1
    return 0


for tc in range(1,int(input())+1):
    V,E = mpa(int,input().split())
    #인접행렬, 정점번호 1~V
    G = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E) #간선 정보 읽기
        u,v = map(int,input().split())
        G[u][v] = 1

    s, e = map(int,input().split())
    visit = [0] * (V+1)
    # DFS(s)
    print(DFS(s))