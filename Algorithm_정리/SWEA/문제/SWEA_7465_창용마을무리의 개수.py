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
