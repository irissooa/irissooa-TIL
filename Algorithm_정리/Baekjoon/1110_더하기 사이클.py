'''
수를 입력 받고, 각 자리수 더하고, 해당 수의 1의 자릿수와 더한 결과값의 1의 자릿수끼리 더한뒤
원래의 수로 돌아오려면 몇번의 사이클이 돌아야되는가
'''
#내가함
N = input()
ans = ''
result = ''
n = N
cnt = 0
while True:
    if result == N:
        break
    ans = str(int(n[0]) + int(n[1]))
    #1의자리수 일 경우 앞에 0 붙이기
    if len(ans) == 1:
        ans = '0' + ans
    #새로운 숫자
    result = n[1] + ans[1]
    n = result
    cnt += 1

print(cnt)

#2.
N = int(input())
# N = 26
ans = N
result = 0
while True:
    a = ans % 10
    #각 자리수 더한 뒤, 1의 자리수
    b = (ans//10 + ans % 10) % 10
    c = str(a) + str(b)
    result += 1
    ans = int(c)
    if int(c) == N:
        break

print(result)