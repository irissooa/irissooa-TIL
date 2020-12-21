'''
20-12-11 16:40-16:53
두개의 자연수 입력받아 최대공약수, 최소공배수 출력 프로그램
두 수 중에 큰수로 정수를 나누면서 동시에 나누어떨어지는 수 중 큰수로 갱신
두 수의 배수를 한 set에 담아주고 다음 수가 set안에 있으면 최소공배수
'''
N,M = map(int,input().split())
MAX = 0
for i in range(1,max(N,M)+1):
    if not N % i and not M % i:
        if i > MAX:
            MAX = i
print(MAX)

gop = 1
nums=set()
while True:
    nans = N*gop
    mans = M*gop
    if nans not in nums:
        nums.add(nans)
        nans = 0
    if mans not in nums:
        nums.add(mans)
        mans = 0
    if nans:
        print(nans)
        break
    if mans:
        print(mans)
        break
    gop += 1


