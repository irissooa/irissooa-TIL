'''
20-12-11 16:24-16:38
한개의 정수를 입력받아 입력받은 정수의 약수 모두 출력
이렇게하면 N이 21억개까지라서 시간초과가 난다....
다른 규칙을 찾아야됨
1다음으로 찾은 약수는 N과나눴을때의 수도 약수! 그 수까지만 보면됨!
그리고 작은 수부터 약수를 찾을때마다 N과 나눈 몫도 같이 저장해줌
그러다가 지정된 끝 수까지 가면 멈춤
'''
import sys
input = sys.stdin.readline
N = int(input())
numbers = []
MAX = -1
for i in range(1,N+1):
    if i == MAX or i in numbers:
        break
    if not N%i:
        if i not in numbers and (N//i) not in numbers:
            if i != N//i:
                numbers.append(i)
                numbers.append(N//i)
            else:
                numbers.append(i)
        if MAX == -1:
            MAX = N//i
numbers.sort()
print(*numbers)