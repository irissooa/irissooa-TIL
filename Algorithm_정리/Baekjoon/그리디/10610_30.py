'''
30의 배수가 되는 가장 큰 수 조합
1. 0을 포함해야됨
2. 다 더했을 때 3의 배수
3. 내림차순 정렬! 가장 큰수
'''
import sys
sys.stdin = open('input.txt','r')





#문자열로 받아야 따로 분리가능
# N = sorted(input(),reverse=True)
N = input()
numbers = sorted(N,reverse=True)
LEN = len(N)
#0을 포함해야됨
if '0' in numbers:
    total = 0
    result = ''
    for i in range(LEN):
        total += int(numbers[i])
        # result += numbers[i]
    if total %3 ==0:
        # print(*numbers,sep='')
        # print(result)
        ans = ''.join(numbers)
        print(ans)
    #여기에 else를 안적어줘서 답이 계속 틀렸다고 나옴!!! 3의배수가 아닐때 값을 지정해주지 않음..
    else:
        print(-1)
else:
    print(-1)