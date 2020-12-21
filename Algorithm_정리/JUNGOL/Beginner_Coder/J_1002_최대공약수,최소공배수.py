'''
20-12-11 16:55-17:30
n개의 정수를 입력받아서 최대공약수, 최소공배수 구함
최대공약수
첫 두수의 최대공약수를 구한 뒤, 그 수와 다음 수의 최대공약수를 구하는 식으로 진행

최소공배수
두수의 곱을 최대공약수로 나눈것과 같음

첫 번째 수를 최대공약수(gcd)로 정하고 두 번째 수부터 이전까지의 최대공약수(gcd)와 현재 배열의 값(a[i])의 최대공약수를 구하여 다시 gcd에 저장한다.

이러한 작업을 마지막까지 반복하면 모든 수의 최대공약수가 구해진다.

최소공배수도 같은 방법으로 구할 수 있다.
'''
import sys
input = sys.stdin.readline

# 최대공약수구하는 공식 :A를 B로 나눈 나머지가 r이라면 A와 B의 최대공약수는 B와 r의 최대공약수와 같다
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

# N = int(input())
N = 3
# numbers = list(map(int,input().split()))
numbers = [2,8,10]
MAX = numbers[0]
MIN = numbers[0]
for i in range(1,N):
    MAX = gcd(MAX,numbers[i])
    # 최소공배수 = 최대공약수 * 정수1 * 정수2
    MIN = MIN // gcd(MIN,numbers[i]) * numbers[i]
print(MAX,end=' ')
print(MIN)
