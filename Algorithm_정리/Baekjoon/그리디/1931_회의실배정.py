'''
방문배열을 만들어서
회의 시작시간~끝나는 시간에 표시해줌!
표시한 뒤, ans = []에 넣어줌
for문을 돌리는데 ans의 첫값부터 선택했다고 했을 떄 그다음 선택은 종료시간보다 같거나 커야됨! 그렇게 수를 세고 MAX갱신
'''

import sys
sys.stdin = open('input.txt','r')

#회의 수
N = int(input())
#회의 정보
conf = []
final = 0
for i in range(N):
    #시작시간, 끝나는시간
    start, end = map(int,input().split())
    conf.append([start,end])

#끝나는 시간이 빠른 순으로 정렬하고, 제일 처음 것을 선택한뒤, 그다음부터는
# print(conf)
# conf.sort(key=lambda x:(x[1],x[0]))
# print(conf)
s,e = conf[0]
cnt = 1
for c in range(1,len(conf)):
    if conf[c][0] >= e:
        # print(conf[c])
        cnt += 1
        s,e = conf[c]
print(cnt)