#시와 분이 2개씩 주어지고 그값들을 더한값을 출력한다
#시와 분을 입력받는다
#시는 시끼리 분은 분끼리 더하는데 분끼리 더했을 때 60이 넘으면 -60을 하고, 시에+1을 해줌
#시가 12시가 넘으면 -12를 한 값을 출력함

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    h1,m1,h2,m2 = map(int,input().split())
    m_sum = m1 + m2
    h_sum = h1 + h2
    if m_sum >= 60: #분끼리 더했을 때 60이상이면 -60을 하고, 1+시간 더해줌
        m_sum -= 60
        h_sum += 1
    if h_sum >= 12:
        h_sum -= 12
    print(f'#{tc} {h_sum} {m_sum}')

#병훈
for t in range(1,int(input())+1):
    h1,m1,h2,m2 = map(int,input().split())
    m = m1+m2
    h = h1+h2+m//60
    if h>12: h -=12
    print(f'#{t} {h} {m%60}')