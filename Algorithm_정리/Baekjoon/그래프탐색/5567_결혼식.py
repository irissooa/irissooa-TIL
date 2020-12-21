'''
6
5
1 2
1 3
3 4
2 3
4 5

#1.입력받고, 인접리스트를 만듦.

#2.BFS(1)로 출발
    이 프로그램은 친구 한명한명당 상근이와 얼마나 떨어져있는지 dist를 계산해줌
    => dist[] 있어야함
#3.그리고 프로그램 끝나면 dist에 다 추가 되있어야 함. dist의 value가 2인것만그 개수를 세줌
'''

import sys
sys.stdin = open('input.txt','r')
from collections import deque

def BFS(s):
    invite.append(s)
    while invite:
        ps = invite.popleft()
        for pe in friends[ps]:
            #0이아니면 방문!
            if dist[pe]:
                continue
            #아니라면 invite에 넣어줌
            dist[pe] = dist[ps] +1
            invite.append(pe)

#상근이 동기의 수n,
n = int(input())
#m 리스트 길이
m = int(input())
friends = [[]*(n+1) for _ in range(n+1)]
dist = [0]*(n+1)
invite = deque()
for _ in range(m):
    #친구관계
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
BFS(1)
# print(dist)
cnt = 0
for i in range(2,n+1):
    if 0 < dist[i] <=2:
        cnt+=1
print(cnt)