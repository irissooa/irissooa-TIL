'''
1m^2의 참외 개수를 육각형 전체 넓이에서 비율로 전체 수확할 수 있는 참외 수를 구함
둘레를 각 방향에 리스트로 담는다.
각 방향 리스트에 담긴 길이가 하나인 것이 가장 긴 사각형의 가로, 세로-> 전체 사각형 넓이 구함

'''
import sys
sys.stdin = open('input.txt','r')
#1m^2 넓이에 자라는 참외의 개수
K = int(input())
#임의의 한꼭지점에서 반시게방향 둘레 변의 방향과 길이
dist = [[] for _ in range(5)]
order=[]
for k in range(6):
    #1 동 2 서 3 남 4 북
    dir,width = map(int,input().split())
    dist[dir].append(width)
    order.append(width)
# print(dist)
# print(order)
#큰 사각형 넓이
BIG = 1
#긴사각형 시작되는 idx에서 3번째가 작은 사각형 idx
idx = []
for d in dist:
    if len(d) == 1:
        BIG *= d[0]
        idx.append(order.index(d[0]))
# print(idx)
#작은 사각형 넓이
small = order[(idx[0]+3)%6]*order[(idx[1]+3)%6]
# print(BIG,small)
print((BIG-small)*K)