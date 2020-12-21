T = input() #값을 str로 받음
add = 0 #더한값 초기값
for i in range(len(T)): #자릿수 만큼 idx를 돌건데
    add += int(T[i]) #각 자릿수를 int로 바꾼 값을 다 더해라
print(add)

#while문 이용
N = int(input()) #4321
ans = 0
while N:
    ans+=N %10 #1 2 3 4
    N //= 10 #432 43 4 0

print(ans)