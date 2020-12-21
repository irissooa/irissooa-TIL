'''
20-12-11 16:15-16:18
주어진 정수 중 입력받은 수의 약수와 배수의 합 각각 출력
입력받은 정수 중 주어진 정수를 나누어떨어지게 하는 것 약수의 합
주어진 정수가 해당 수를 나누어떨어지게하는 것 배수의 합
'''
# 정수개수
N = int(input())
numbers = list(map(int,input().split()))
M = int(input())

ans = 0
result = 0
for i in numbers:
    if not M % i:
        ans += i
    if not i % M:
        result += i
print(ans,result,sep='\n')