'''
20-12-11 16:20-16:23
어떤 자연수 p,q
p의 약수들 중 q번쨰로 작은 수 출력
N의 약수가 K개보다 적어서 약수가 존재하지 않을 경우 0을출력
'''
N, K = map(int,input().split())
num = []
for i in range(1,N+1):
    if not N%i:
        num.append(i)

if len(num) >K:
    print(num[K-1])
else:
    print(0)