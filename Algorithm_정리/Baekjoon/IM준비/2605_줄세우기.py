'''
첫번째 ->무조건 0번
2번째-> 0또는 1(0: 그자리그대로, 1: 바로 앞의 학생 앞)
3->0,1,2(뽑은 번호만큼 앞자리로 가서 줄섬)
각자 뽑은 번호는 자기 번호보다 1 작은 범위 내
뽑은 번호를 순서대로 하나씩 보면서 뒤에들어온 수만큼 앞으로 보냄,
idx를 순서대로 기록!...
'''

import sys
sys.stdin = open('input.txt','r')

N = int(input())
num = list(map(int,input().split()))
ans = []

for n in range(len(num)):
    #idx는 ans의 길이(뒤에서) 내가 뽑은 수만큼 앞으로 간곳
    idx = len(ans) - num[n]
    # print(idx)
    ans.insert(idx,n+1)
print(*ans)