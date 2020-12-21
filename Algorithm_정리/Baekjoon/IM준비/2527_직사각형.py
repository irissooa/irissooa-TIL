'''
시간:2020/10/18/19:34
직사각형 왼쪽 아래 좌표, 오른쪽 위 좌표가 두개 주어짐
겹치는 부분이 직사각형(a)인지 선분(b)인지 점(c)인지 겹치는 부분이 없(d)는지 판단
'''

import sys
sys.stdin = open('input.txt','r')

def check(x1,y1,p1,q1,x2,y2,p2,q2):
    ans = 'a'
    #d
    if x2 > p1 or y2 >q1 or x1 >p2 or y1>q2:
        ans = 'd'
    #c
    elif (x2==p1 or x1==p2) and (y1==q2 or y2==q1):
        ans = 'c'
    #b
    elif (p1==x2 or x1==p2) or (y2==q1 or y1==q2):
        ans ='b'
    #그외는 a
    return ans

#4개의 줄
for _ in range(4):
    #x,y,p,q가 두개 입력됨
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    print(check(x1,y1,p1,q1,x2,y2,p2,q2))
