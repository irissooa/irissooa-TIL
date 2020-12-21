'''
20-12-17 13:05-13:40
오늘 떡 = 어제 받은 떡의 개수 + 그저께 받은 떡의 개수
호랑이를 만나서 무사히 넘어온 D일째, 떡의 개수 K개
할머니가 호랑이를 처음 만난 날의 떡의 개수A
그 다음날 호랑이에게 준 떡의 개수B 계산

1. for문2개, 마지막전날 개수를 임의로 정하고, 그전날 떡의 개수(K-마지막전날)를 로 정하고 그 전날은 두값의 차 값으로 해서 0일째 0가 되는지 확인
'''
D,K = map(int,input().split())
ans = 0
for a in range(10,K)[::-1]:
    d =D
    A = a
    B = K-A
    d-=2
    flag = False
    while d>=0 and A > B and B > 0:
        next = A-B
        d-=1
        if d == 0:
            print(B,A,sep='\n')
            flag = True
            break
        A = B
        B = next
    if flag:
        break
