'''
조합! 함수사용
#1. first_numbers에서 K를 N에서부터 뒤로 내려오면서 NCk 만큼 뽑고 second_numbers에서도 NCk만큼 뽑는데 두 집합이 같으면 출력!

#DFS로 풀기
#1.인접리스트를 만드는데, 유향으로 first->second로 만듦! 여기서 만약 양방향이 된다면 cnt!

#idea
#상대배열에 값이 똑같으면 result 넣고, 만약에 N까지 갔는데 내값이 상대 배열에없으면 둘다 지움...
'''
from itertools import combinations

import sys
sys.stdin = open('input.txt','r')

def DFS(num):
    global result
    visited[num] = True
    cycle.append(num)
    next = linked[num]
    # print(num,next)
    if visited[next]:
        if next in cycle:
            result += cycle[cycle.index(next):]
        return
    DFS(next)

#DFS로 풀기
N = int(input())
linked = [0 for _ in range(N+1)]

for n in range(1,N+1):
    linked[n]=int(input())
# print(linked)


result = []
visited = [False for j in range(N+1)]
for i in range(1,N+1):
    if not visited[i]:
        cycle = []
        DFS(i)
        # print(i,visited)
print(len(result))
# print(*result,sep='\n')
for i in sorted(result):
    print(i)

#조합으로 풀기
# first_numbers = [i for i in range(1,N+1)]
# second_numbers = []
# for n in range(N):
#     second_numbers.append(int(input()))
# print(first_numbers)
# print(second_numbers)

# flag = False
# MAX = 0
# for k in range(N,0,-1):
#     first = []
#     second = []
#     cnt = 0
#     for i in list(combinations(first_numbers,k)):
#         first.append(i)
#     for j in list(combinations(second_numbers,k)):
#         second.append(j)
#     # print(k,first,second)
#     for f in first:
#         for s in second:
#             #순서가 상관없어야되니가 f와 s가 같은지 확인하는것!!
#             if set(f) == set(s):
#                 MAX = k
#                 flag = True
#                 print(MAX)
#                 print(*f,sep='\n')
#                 break
#         if flag:
#             break
#     if flag:
#         break
