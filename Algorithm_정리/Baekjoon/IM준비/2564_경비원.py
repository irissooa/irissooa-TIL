'''
블록의 가로, 세로 길이가 주어짐
상점의 개수와 위치, 동근이의 위치도 주어짐(이동할 때 가로지를수 없음)
동근의 위치와 각 상점사이의 최단 거리 합을 구함
'''
import sys
sys.stdin=open('input.txt','r')
from pprint import pprint

def clockwise(x,pos):
    if x == 1:#북
        return pos
    elif x == 2:#남
        return c+r+c-pos
    elif x == 3: #서
        return c+r+c+r-pos
    else: #동
        return c+pos

#가로와 세로
c,r = map(int,input().split())
N = int(input())
dist = []
for i in range(N+1):
    x,pos = map(int,input().split())
    dist.append(clockwise(x,pos))
my_dist = dist[-1]
cir = (r+c)*2
ans = 0
result = 0
for i in range(N):
    ans =abs(my_dist-dist[i])
    result += min(ans,cir-ans)
print(result)