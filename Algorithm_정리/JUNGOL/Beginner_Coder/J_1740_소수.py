'''
20-12-12 10:51-11:03
자연수 M,N주어짐, M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램
그 범위 내에서 1과 자기자신을 제외한 나머지 수들 사이에 나누어떨어지는것이 있는지 확인
소수가 없다면 -1 출력
'''
M = int(input())
N = int(input())
MIN = 987654321
SUM = 0
for num in range(M,N+1):
    if num ==1:
        continue
    for i in range(2,int(num**0.5)+1):
        if not num % i:
            break
    else:
        if MIN > num:
            MIN = num
        SUM += num
if MIN == 987654321:
    print(-1)
else:
    print(SUM,MIN,sep='\n')

