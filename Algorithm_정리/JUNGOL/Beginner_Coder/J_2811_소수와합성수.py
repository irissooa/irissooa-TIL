'''
20-12-12 10:34-10:50
소수는 1보다 큰 자연수 중 1과 자기자신만 약수로 갖는 수
합성수는 3개이상 약수
1은 소수도 합성수도 아님
5개의 자연수, 소수, 합성수인지 판단하라

[Hint]
시간을 줄이기 위해 약수를 구할 때 제곱근을 이용해 보자.
a * b = n (a > 1, b> 1)이라 할 때 a와 b는 n의 약수이다.
그러므로 a와 b중 작은 수 쪽만 확인해 보아도 n이 합성수임을 알 수 있는데 작은 수의 범위는 n의 제곱근 이하이다.
작은수가 n의 제곱근보다 클수가 없기 때문!
'''
num=list(map(int,input().split()))
for i in num:
    if i == 1:
        print("number one")
        continue
    for j in range(2,int(i**0.5)+1):
        if not i%j:
            print("composite number")
            break
    else:
        print("prime number")