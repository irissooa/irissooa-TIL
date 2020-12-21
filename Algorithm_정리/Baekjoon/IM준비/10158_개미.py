'''
소요시간 10/22/9:25
p,q가 주어지면 +1,+1로 좌표가 커지고 벽을 만나면 다음 방향중 갈수있는 방향으로 방향전환
di = [1,1,-1,-1]
dj = [1,-1,-1,1]
범위가 벗어나면 ni = i+di[d], nj=j+dj[d]에서 d=(d+1)%4로 방향을 바꿈
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

#다른방법 ->수학을 이용해서 품(명균쌤힌트)
#1.중복을 제외시켜줘라
#2.행과 열을 따로지줭해줘라
# 행,열 따로 생각 둘다 처음 주어진 q,p값에서 시간을 더한 뒤
# 행과 열의 길이를 나눈 몫이 짝수면 + 홀수면 -방향
#그리고 나머지는 이동할 값
def ant(idx,length):
    dir = (idx+t) // length
    dist = (idx+t) % length
    #dir 홀수면 해당 length에서 나머지만큼 빼줌
    if dir % 2:
        return length-dist
    #dir가 짝수면 방향 그대로에서 나머지만큼 더해줌
    else:
        return dist



#w: 가로, 열, h : 세로, 행
w,h = map(int,input().split())
#개미 초기 위치값 p, q
p,q = map(int,input().split())

#개미가 움직일 시간t
t = int(input())

print(ant(p,w),ant(q,h))


#배열
arr = [[0 for j in range(w)] for i in range(h)]
# pprint(arr)
#델타 이용 -> 시간초과
di = [1,1,-1,-1]
dj = [1,-1,-1,1]
i,j,d = q,p,0
#이전방향
bi,bj = i,j
#벽을 만나면 방향전환
while t>=1:
    ni = i + di[d]
    nj = j + dj[d]
    # print(i,j)
    if ni < 0 or ni > h or nj < 0 or nj > w:
        d = (d+1) % 4
        continue
    if ni == bi and nj == bj:
        d = (d+1) % 4
        continue
    t-=1
    bi,bj = i,j
    i,j = ni,nj
    # print('t',t,'d',d,'i',i,'j',j)
print(i,j)

