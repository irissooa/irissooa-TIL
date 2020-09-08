# Algorithm

## 조합

- 조합_반복문

```python
arr = [1,2,3,4]
N = 4
R = 2
sel=[0]*R
#arr idx와 sel의 sidx
def combination(idx,sidx):
    if sidx == R:
        print(sel)
        return
    for i in range(idx,N):
        sel[sidx] = arr[i]
        combination(i+1,sidx+1)
combination(0,0)
```

- 조합_재귀

```python
arr = [1,2,3,4]
N = 4
R = 2
sel=[0]*R
#arr idx와 sel의 idx
def combination(idx,sidx):
    #순서도 중요! sidx 종료조건을 먼저 줘야됨!
    if sidx == R:
        print(sel)
        return
    if idx == N:
        return
   	sel[sidx] = arr[idx]
    #뽑고가고
    combination(idx+1,sidx+1)
    #안뽑고가고
    combination(idx+1,sidx)
    
combination(0,0)
```



## 러시아 깃발

```python
#선생님 풀이
T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    #각 행의 색 카운팅
    w = [0] * N
    b = [0] * N
    r = [0] * N

    for i in range(N):
        color = input()
        w[i] = color.count("W")
        b[i] = color.count("B")
        r[i] = M - w[i] - b[i] #M개에서 w의 개수, b의 개수를 뺀 값이 r의 개수
    #누적합을 구해서 나중에 한번에 계산하기 위해..
    for i in range(1,N):
        w[i] += w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1]

    ans = N*M
    #흰색의 경계를 정함.마지막에 파랑 빨강을 보장해야됨
    for i in range(N-2):
        #파란색의 경계를 정함
        for j in range(i+1,N-1):
            #흰색칠하기
            #i까지의 전체 개수를 구한 뒤 지금까지 칠해져 있는 화이트 개수를 빼기
            cnt = M *(i+1) -w[i]
            #파란색칠하기
            #j-1를 해서 유의미한 전체의 개수를 뽑고, b[j]-b[i]를 하여 해당 범위의 전체 파랑 개수를 뽑아내기
            cnt += M * (i+1) - (b[j] -b[i])
            #빨간색 칠하기
            #위와 마찬가지...ㅎ
            cnt += M * (N-1 -j)-(r[N-1]-r[j])
            ans = min(ans,cnt)
    print('#{} {}'.format(tc,ans))
```



- 다른풀이-조합

```python

#러시아 국기 조합으로 풀기
def combination(sel,idx,cnt):
    global ans
    if cnt == 2:
        print(sel)
        #각각의 1이 경계를 의미
        w = -1
        b = -1
        for i in range(N):
            if sel[i] == 1:
                if w == -1:
                    a = i
                else:
                    b = i
        count = 0
        #흰색 영역 칠하기
        for W in range(0,w+1):
            for k in range(M):
                if flag[W][k] != 'W':
                    count += 1
        for B in range(w+1,b+1):
            for k in range(M):
                if flag[B][k] != 'B':
                    count += 1
        for R in range(b+1,N):
            for k in range(M):
                if flag[R][k] != 'R':
                    count += 1
        return

    if idx >= N-1:
        return
    #경계 뽑고
    sel[sidx] = 1
    combination(sel,idx+1,cnt+1)
    #경계다시 원상복구
    sel[sidx] = 0
    combination(sel,idx+1,cnt)


T = int(input())
for tc in range(1,T+1):
    N,M =(int,input().split())
    #스트링도 idx가 있기 때문에 list로 안 바꿈
    flag = [input() for _ in range(N)]

    ans = M*N

    combination([0]*N,0,0)




```



## 격자판의 숫자 이어붙이기

```python
'''
4X4 크기 격자판
각 격 자판 0부처 9까지
동서남북 4방향으로 인접한 격자로 총 6번 이동
각 칸 숫자 차례로 이어붙이면 7자리
한번 거쳤던 격자칸 다시 거쳐도 됨
0으로 시작 가능
격자판 벗어나면 안됨
서로 다른 일곱자리 수 개수 구하기

음...DFS? -> RecursionError남
현우's hint
수를 입력받을떄 str로 받아라
DFS인자로 num을 주고 다음 num 은 num = num + arr[i][j]
if len(num)이 7이면 return
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
def DFS(i,j,num):
    # global num_set #리스트나 셋은 새로 만드는 거면 해줘야되지만, 변경하거나 참조하면 안해줘도됨
    #d 밑에다가 넣는다면 num이 계속 붙어버려서 밖에다 처음 등장햇을 떄! 처리해야됨
    num = num + arr[i][j]
    # print('i',i,'j',j,'num',num)
    if len(num) == 7:
        num_set.add(num)
        print(num_set)
        return
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
            continue
        DFS(ni,nj,num)

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    # print(arr)
    cnt = 0
    num = ''
    num_set = set()

    for i in range(4):
        for j in range(4):
            DFS(i,j,num)
    # DFS(0,0,arr[0][0])
    print('#{} {}'.format(tc,len(num_set)))
```

- 선생님 풀이

```python
#선생님 풀이
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c,line):
    if len(line) == 7:
        tmp = ''.join(line)
        if tmp not in ans:
            ans.append(tmp)
        return
    for i in range(4):
        nr = r + dr[i]    
        nc = c + dc[i]
        
        if nr < 0 or nr >=N or nc < 0 or nc >= N:
            continue
        line += [arr[nr][nc]]
        DFS(nr,nc,line)
        #다음 반복문을 위해 원상복귀
        line.pop()
            
T = int(input())
for tc in range(1,T+1):
    N = 4
    arr = [input().split() for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            DFS(i,j,[arr[i][j]])
    print('#{} {}'.format(tc,ans))
```





## SWEA_7465_창용마을무리의 개수

```python
'''
창용마을 N명
1~N번까지 사람 번호 붙어있음
서로 아는 관계라면 이어져있음 -> 하나의 무리
창용 마을에 몇 개의 무리가 존재하냐?
'''
import sys
sys.stdin = open('input.txt','r')

def DFS(i):
    visited[i] = True
    for j in range(N+1):
        if linked[i][j] == 1 and visited[j] == False:
            DFS(j)

T = int(input())
for tc in range(1,T+1):
    #마을사람의 수, 관계의 수(같은 관계는 반복해서 주어지지 않음->무향)
    N, M = map(int,input().split())
    linked = [[0]*(N+1) for _ in range(N+1)]
    for m in range(M):
        st,ed = map(int,input().split())
        linked[st][ed] = 1
        linked[ed][st] = 1
    visited = [False for _ in range(N+1)]
    cnt = 0
    #0번부터돌아서 한개 더 생김....
    for i in range(1,N+1):
        if visited[i] == False:
            DFS(i)
            cnt += 1
            # print(visited)
    print('#{} {}'.format(tc,cnt))
```



## SWEA_1861_정사각형 방

```python
'''
arr[i][j]방에 Aij가 적혀있음 이 숫자는 모든 방에 대해 서로 다름
이동하려는 방이 존재해야함, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야됨
처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는가?

출력
처음 출발해야 하는 방 번호, 최대 몇개의 방을 이동할수있는지.
이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그중 가장 작은 수 출력
dfs -> 재귀에러 뜸
bfs로 풀기
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
# def DFS(i,j):
#     global cnt
#     visited[i][j] = True
#     # print(i,j)
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         if ni < 0 or ni >= N or nj < 0 or nj >= N:
#             continue
#         #현재 값보다 1큰값이 아니면 지나감
#         if room[ni][nj] != room[i][j] + 1:
#             continue
#         if visited[ni][nj] == True:
#             continue
#         cnt += 1
#         DFS(ni,nj)

#재귀에러떠서... bfs로 풀기
def BFS(i,j):
    global cnt
    q = []
    #시작점 넣기
    q.append([i,j])
    # dist[i][j] = 1
    while q:
        #맨 앞의 원소를 담음
        temp = q.pop(0)
        pi,pj = temp[0],temp[1]
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            # 현재 값보다 1큰값이 아니면 지나감
            if room[ni][nj] != room[pi][pj] + 1:
                continue
            # if dist[ni][nj] != 0:
            #     continue
            cnt += 1
            q.append([ni,nj])
            # dist[ni][nj] = 1 + dist[pi][pj]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    #이동하는 방 최대 이동수
    MAX = 0
    for i in range(N):
        for j in range(N):
            # #몇개의 방을 이동할수 있는지 저장
            cnt = 1
            #방문배열 리셋
            # visited = [[False for j in range(N)] for i in range(N)]
            # dist = [[0 for j in range(N)] for i in range(N)]
            # DFS(i,j)
            BFS(i,j)
            if cnt > MAX:
                MAX = cnt
                START = room[i][j]
                # print(MAX_S,'최대값들')
            #같을 떄는 START값에 저장된 값보다 작은값에서 시작하면 START갱신
            elif cnt == MAX:
                if START > room[i][j]:
                    START = room[i][j]
    print('#{} {} {}'.format(tc,START,MAX))
```



## SWEA_1486_장훈이의 높은 선반

```python
'''
서점에는 높이가 B인 선반이 하나 있음
N명의 점원들, 각 점원의 키 Hi로 나타냄, 탑을 쌓아서 선반 위의 물건을 사용하기로 함
점원들이 쌓는 탑은 점원 1명 이상으로 이루어짐
탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명이상이면 그 탑을 만든 모든 점원의 키의 합과 같음
탑의 높이가 B이상, 선반 위의 물건을 사용하는데 탑의 높이가 높을수록 위험
높이가 B이상인 탑중에서 높이가 가장 낮은 탑은?

부분집합..이용..해서 sum이 B이상인 것 중 가장 작은 값!

'''
import sys
sys.stdin = open('input.txt','r')

def powerset(idx,sum_num):
    global MIN
    #이미 값이 MIN보다 크면 끝냄
    if sum_num > MIN:
        # print(sum_num)
        return
    if idx == N:
        total = 0
        for i in range(N):
            if ans[i]: #값이 존재할때
                total += height[i]
        # print(total)
        if total >= B:
            # print(total)
            if MIN > total:
                MIN = total
        return


    #k번째 선택
    ans[idx] = 1
    powerset(idx+1,sum_num)
    #k번째 비선택
    ans[idx] = 0
    powerset(idx+1,sum_num)

T = int(input())
for tc in range(1,T+1):
    #점원, 높이
    N,B = map(int,input().split())
    height = list(map(int,input().split()))
    #점원들 키의 합
    S = sum(height)
    ans = [0]*N
    MIN = S
    sum_num = 0
    # print(S)
    powerset(0,0)


    print('#{} {}'.format(tc,MIN-B))
```



## SWEA_1267_작업순서

- 아래 코드 10개 testcode 중 5개만 맞음...왜그럴까....ㅠ

```python
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

def BFS(v):
    q = [v]
    ans = [v] #임시로 v를 담을 리스트
    visited[v] = True
    # print(v,'v',end = ' ')
    while q:
        #종료조건 만약 0을 제외한 정점들을 전부 돌았다면 멈춰라!
        if visited[1:V+1] == [True for _ in range(V)]:
            # print(visited)
            # print('여기들어옴')
            break
        pv = q.pop(0)
        #w를 돌면서 pv와 연결된 것이 있는지 찾는다
        for w in range(1,V+1):
            #w가 pv와 연결된 것이 있는데 만약 w에 방문을 하지 않았다면 w를 q에 넣어줌
            if G[w][pv] == 1:
                #그 이전의 정점이 방문하지 않았다면
                if visited[w] == False:
                    visited[w] = True
                    q.append(w)
        #q에 담긴 가지 않았던 정점들을 ans에 추가해줌
        #만약 정점 모두 방문을 했다면 그만!
        ans += q
    # print(pv)
    # print(ans)
    # print(visited)
    # print()
    #ans는 뒷 순서부터 담겼기 때문에 뒤집어줌
    ans = ans[::-1]
    #ans에 마지막으로 연결된 v를 담아줌
    return ans

for tc in range(1,2):
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
    #결과를 담을 리스트
    result = []
    for i in range(1,V+1):
        if visited[i] == False:
            result.extend(BFS(i))
            # print(visited)
            # print()

    print('#{}'.format(tc),end = ' ')
    for r in result:
        print(r, end = ' ')
    print()
```

- 다른 코드

```python
#채린
for t in range(1,11):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited = [ False for _ in range(v+1)]
    temp_list= list(map(int,input().split()))
 
    #그래프 완성하기
    for i in range(0,len(temp_list),2):
        a=temp_list[i]
        b=temp_list[i+1]
        graph[b].append(a) #ed의 인접리스트에 왜 st를 넣을까? 거꾸로 받아서 한쪽으로만 가게하기 위해서?
    #print(graph)
 
    result='' #결과값
    count=v
    while count:#False(0)일때까지 반복
        for i in range(1,len(graph)):
            #현재 노드가 수행되지 않았다면
            if visited[i] == False:
 				
               for j in graph[i]:
                    #선행 노드 중에 False가 있다면 진행하지마라.
                    if visited[j]==False:
                        break
               #선행 노드 중 False가 없다면, 방문표시하고, 해당 정점을 저장한 뒤, 노드 수-1을 해라
               else:
                    visited[i]=True
                    result+=str(i)+' '
                    count-=1
    print('#{} {}'.format(t,result))
```

- DFS로 풀기

```python
#주아언니
def DFS(v):
    global result
    visited[v] = 1
    # 수행하면 추가
    result += str(v) + " "
 
    # 수행 후 해당 노드를 선행 노드로 둔 노드의 선행노드수 -1
    for i in range(1, V+1):
        if arr[v][i]:
            burdenList[i] -= 1
 
    # 수행한 노드에서 갈수있는 곳 & 수행하지 X & 선행노드수 0
    # 일 경우에 넘어갈 수 있음
    for i in range(1, V + 1):
        if arr[v][i] == 1 and visited[i]==0 and burdenList[i] == 0:
            DFS(i)
 
 
 
for T in range(1, 11):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
 
    # 일을 수행했는지 여부
    visited = [0]*(V+1)
 
    path = list(map(int, input().split()))
 	#인접행렬 표시
    for i in range(0, len(path),2):
        arr[path[i]][path[i+1]] = 1
 
    # 노드별로 선행노드가 몇갠지
    # 선행노드가 0개: 해당 노드 수행가능
    burdenList = [0]*(V+1)
 
    startList = []
 
    # 시작노드 구하기
    # 다른 노드에서 오는 간선이 없는 노드에서 시작가능
    for i in range(1, V+1):
        count = 0
        for j in range(1, V+1):
            count += arr[j][i]
        if count == 0:
            startList.append(i)
 
    # 노드별 선행노드 개수
    for i in range(1, V+1):
        burden = 0
        for j in range(1,V+1):
            burden += arr[j][i]
        burdenList[i] = burden
 
    # 시작점마다 DFS수행
    result = ''
    for i in startList:
        DFS(i)
 
    print("#{} {}".format(T, result))
```

- 

```python
#의수
for tc in range(1, 11):
    # V 노드갯수, E 간선개수
    V, E = map(int, input().split())
    # 입력받는 부분
    arr = list(map(int, input().split()))
    # 인접행렬 초기화
    work = [[] for _ in range(V+1)]
    # 도착 노드가 저장될 임시 리스트
    temp = []
    # 결과값들이 저장 될 리스트
    res = [False] * (V+1)
    # 2개씩 잘라서 저장
    for i in range(0, len(arr), 2):
        # 인접행렬 저장
        work[arr[i]].append(arr[i+1])
        # 도착노드 저장
        temp.append(arr[i+1])
 
    for n in range(1, V):
        if n not in temp:
            # 순서를 같이 저장하기 위해서 리스트 형태로 저장
            res[n] = [1, n]
            # BFS활용
            q = []
            q.append(n)
            while q:
                nn = q.pop(0)
                for w in work[nn]:
                    # 결과값이 저장되어 있지 않은 부분이라면
                    if not res[w]:
                        # 결과값에 저장 (전 순위보다 1증가시켜서 저장) ?????????
                        res[w] = [res[nn][0]+1, w]
                        q.append(w)
                    # 여러개의 간선이 있는 부분을 처리하기 위한 조건(이미 res에 저장되어 있다)
                    else:
                        if res[w][0] < res[nn][0] + 1:
                            res[w][0] = res[nn][0] + 1
                            q.append(w)
    # 인덱싱을 편하기 위해서 추가했던것을 제거
    res.pop(0)
    # 들어가는 순서에 따라 정렬한다.
    # 같은 순서일 때는 상관 없으므로 정렬 안함
    res.sort(key=lambda x: x[0])
    print('#{} '.format(tc), end='')
    for r in res:
        print(r[1], end=' ')
    print()
```

- 

```python
#지형
def dfs(node,r_graph,result):
   	#해당 인접리스트를 for로 돌려본다
    for r_node in r_graph[node]:
        #만약 결과에 해당 노드가 있으면 지나가라
        if r_node in result: continue
        #아니라면 해당 노드로 dfs반복
        dfs(r_node,r_graph,result)
    #for문이 끝나면 node를 결과값에 저장해라
    result.append(node)
for tc in range(1,11):
    v,e=map(int,input().split())
    node=list(map(int, input().split()))
    r_graph=[[] for _ in range(v+1)]
    result=[]
    for i in range(0,len(node),2):
        #st,ed를 거꾸로 받는다!
        r_graph[node[i+1]].append(node[i])
    for i in range(1,v+1):
        #i가 결과값에 이미 있다면 지나가라
        if i in result: continue
        #아니라면, dfs 진행
        dfs(i,r_graph,result)
    print('#{}'.format(tc),end=' ')
    for node in result:
        print(node,end=' ')
    print()
```



#### **다시풀어보기...!**