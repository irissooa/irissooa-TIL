'''
3
2 7
3 15
36 1007

#1 3
#2 4
#3 8

자연수 N에 몇번의 연산을 통해 자연수 M을 만듦
사용할 수 있는 연산 +1,-1,*2,-10
최소 몇번의 연산을 거쳐야 하는가
+1 -1 *2 -10으로 dfs로 다 보냄! 그러다가 M이 되면 최소 값 갱신, 그 전에 MIN보다 더 크면 return
# 병훈오빠's idea -> N,M을 반대로 받고, 거꾸로 연산을 함!-> num이 홀수일때 계산을 안하니까 훨씬 빨라짐
'''
import sys
sys.stdin = open('input.txt','r')

def calc(num,operator):
    if operator == 1:
        num += 1
    elif operator == 2:
        num -= 1
    elif operator == 3:
        if num %2 == 0:
            num //= 2
    else:
        num += 10
    return num

def find(num):
    q = [num]
    while q:
        # print(len(q),len(set(q)))
        p = q.pop(0)
        # print(p)
        if p == M:
            return
        for i in range(4):
            ans = calc(p,i)
            if ans == M:
                dist[ans] = dist[p] + 1
                return
            if ans < 0 or ans > 1000000:
                continue
            if dist[ans]:
                continue
            q.append(ans)
            dist[ans] = dist[p] + 1




T= int(input())
for tc in range(1,T+1):
    M,N = map(int,input().split())
    MIN = 987654321
    dist = [0 for i in range(1000001)]
    # print(N,M)

    find(N)

    print('#{} {}'.format(tc,dist[M]))
    # print('----')