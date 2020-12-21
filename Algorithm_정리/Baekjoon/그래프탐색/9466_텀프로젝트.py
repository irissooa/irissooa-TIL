'''

'''
import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**8)

def DFS(node):
    global result
    visited[node] = True
    #사이클을 이루는 팀을 확인하기 위함
    q.append(node)
    next= info[node]

    #다음 node가 이미 방문한곳이라면
    if visited[next]:
        if next in q:#사이클 가능 여부
            result += q[q.index(next):]#사이클이 되는 구간부터만 팀을 이룸
        return

    DFS(next)

    #q안에 node를 담아줌
    # #만약에 node가 자기자신을 선택하면 방문표시해주고 리턴
    # if node == info[node]:
    #     visited[node] = 1
    #     return
    #q리스트 안에 info[node]값이 이미 잇다면 어딘가는 반복된다는 것! 그 값부터 한팀! 그전의 값들은 방문표시안함
    # if node in q:
    #     #q안의 node들 모두 방문표시, 다시 못가게
    #     for i in q:
    #         visited[i] = 1
    #     #어느 위치가 반복되는지 찾고, 그 위치부터는 쭉 cnt를 표시해줌
    #     idx = q.index(node)
    #     for p in range(idx,len(q)):
    #         cnt+=1
    #     return
    # #q안에 info[node]값이 없다면 일단 q에 넣어줌
    # q.append(node)
    # #그 node의 값이 방문하지 않았다면 info[node]로 DFS돌림
    # if not visited[info[node]]:
    #     DFS(info[node])

T = int(input())
for tc in range(1,T+1):
    #학생의 수
    N = int(input())
    #index를 맞추기 위해 앞에 0 삽입
    info = [0]+list(map(int,input().split()))
    visited = [True]+[False for _ in range(N)]

    result = []
    # #자기자신을 가리키는 node는 방문처리
    # for i in range(1,N+1):
    #     if i == info[i]:
    #         visited[i] = 1
    #         cnt += 1
    for i in range(1,N+1):
        if not visited[i]:
            q = []#잠시 팀원들을 담을 리스트
            DFS(i)
            # print(q)
        # print(visited)
    print(N-len(result))