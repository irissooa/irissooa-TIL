'''
#1. 시작시간과 완료시간에서 완료시간이 빠른순으로 정렬!, 같다면 앞이 작은 순서로 나열!
#2. 다음 차례는 그 전차례의 완료시간보다 시작시간은 같거나 크면됨!(cnt+1)
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    times = []
    for n in range(N):
        s,e = map(int,input().split())
        times.append([s,e])
    times.sort(key=lambda x:(x[1],x[0]))
    # print(times)
    start,end = times[0]
    cnt = 1
    for t in range(1,len(times)):
        if times[t][0] >= end:
            start,end = times[t]
            cnt+=1
    print('#{} {}'.format(tc,cnt))
