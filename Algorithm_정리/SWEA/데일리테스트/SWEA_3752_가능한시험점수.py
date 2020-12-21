'''
영준이 N개의 문제를 만들었음
각 문제의 배점은 문제마다 다를 수 있고, 틀리면 0점
받을 수 있는 점수로 가능한 경우의 수 몇가지?
모든 경우를 체계적으로 조사하는 방법 -> 백트래킹 활용
모든 문제의 부분집합의 합을 구해서 경우의 수르 구하면 된다!
너비우선탐색을 이용해서 풀기
같은 위치의 중복을 제거해가며 풀기
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    #문제 수
    N = int(input())
    score = list(map(int,input().split()))
    #방문표시에 해당 idx에 나온 값을 저장해줌
    visited = [0] * (sum(score)+1)

    #너비우선탐색으로 풀건데 Q에 각 레벨별로 값들을 추가! 만약 이미 방문했다면 지나가!
    Q = [0]

    for val in score:
        #Q의 길이만큼 돌거야!
        for i in range(len(Q)):
            if visited[Q[i] + val]: #Q에 들어있는 수들과 val의 합이 이미 나왔다면, 방문을 했다면 지나가라아
                continue
            #방문하지 않았다면 방문표시를 해줌
            visited[Q[i] + val] = 1
            #해당 합을 추가해줘라
            Q.append(Q[i] + val)
    print('#{} {}'.format(tc,len(Q)))


#유튜브 선생님 풀이
T = int(input())
for tc in range(1,T+1):
    #문제 수
    N = int(input())
    score = list(map(int,input().split()))

    #마지막단 중복을 제거하기 위해, set을 이용하던지 방문표시
    #나온 위치를 마크해서 그 점수가 나왔나 안나왔나 표시
    visit = [0] * (sum(score) + 1)

    def DFS(k,s):
        if k == N:
            # print(s,end = ' ')
            visit[s] = 1 #이 점수가 나왔다는 것을 표시
        else:
            DFS(k+1,s) #k번 문제 틀린경우
            DFS(k+1,s + score[k]) #k번 문제가 맞은 경우

    DFS(0,0)
    print(sum(visit))

    #2. 위 방식은 N이 커지면 시간초과 나옴
    #레벨 별로 방문을 만들어 중복 제거!

for tc in range(1,T+1):
    #문제 수
    N = int(input())
    score = list(map(int,input().split()))

    #마지막단 중복을 제거하기 위해, set을 이용하던지 방문표시
    #나온 위치를 마크해서 그 점수가 나왔나 안나왔나 표시
    visit = [[0] * (sum(score) + 1) for _ in range(N+1)]

    def DFS(k,s):
        if visit[k][s]:
            return
        visit[k][s] = 1
        if k == N:
            return

        DFS(k+1,s) #k번 문제 틀린경우
        DFS(k+1,s + score[k]) #k번 문제가 맞은 경우

    DFS(0,0)
    print(sum(visit[N]))



    #3.상태공간트리를 너비우선 탐색으로 탐색함
for tc in range(1,T+1):
    #문제 수
    N = int(input())
    score = list(map(int,input().split()))
    visit = [0] * (sum(score) + 1)
    Q = [[0,0]] #점수, 높이 필요(k,s) 중간에 끊기 위해
    while Q:
         k,s = Q.pop(0)
         if k == N:
             print(s,end = ' ')
             visit[s] = 1
        else:
            #틀린경우
            Q.append([k+1,s])
            #맞은경우
            Q.append([k+1,s+score[k]])
    print(sum(visit))

    #4.너비우선탐색 +시간줄이기 위해 중복 제거
for tc in range(1,T+1):
    #문제 수
    N = int(input())
    score = list(map(int,input().split()))
    visit = [0] *(sum(score) + 1)
    Q = [0]

    #Q에서 빼지 않고 계속 새로운 것만 추가하는 방식으로 만들기
    for val in score:
        for i in range(len(Q)):
            if visit[Q[i] + val] :
                continue
            visit[Q[i] + val] = 1
            Q.append(Q[i] + val)

