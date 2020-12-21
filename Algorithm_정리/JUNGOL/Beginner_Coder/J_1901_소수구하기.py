'''
20-12-12 11:04-11:48
임의의 값 M에 대하여 M에 가장 가까운 소수를 구하는 프로그램
N : 처리할 수의 개수
M개의 수 list
Mi값에 대해 차이가 가장 작은 소수를 구하여 출력
만약 차이가 같은 소수가 여러개이면 작은수부터 모두 출력 -> M보다 큰수도 봐야되넹..
M까지의 소수 구한 뒤, 차이 가장 적은 값만큼 더한 값만 더 보면 된다

40%에서 시간초과..ㅠ
M과 가까운수부터 보고 MIN찾으면 break, M보다 큰수에서는 작은수부터!
이렇게 하니까 시간초과 안남!!

'''
import sys
input = sys.stdin.readline
def isPrime(a,b):
    global MIN,prime
    if b <=num:
        for p in range(a,b)[::-1]:
            for i in range(2,int(p**0.5)+1):
                if not p % i:
                    break
            else:
                MIN = abs(p-num)
                prime.append(p)
                return
    else:
        for p in range(a,b):
            for i in range(2,int(p**0.5)+1):
                if not p % i:
                    break
            else:
                if MIN > abs(p-num):
                    MIN = abs(p-num)
                    prime = [p]
                elif MIN == abs(p-num):
                    prime.append(p)
                return


N = int(input())
for _ in range(N):
    num = int(input())
    prime = []
    MIN = 987654321
    if num == 1:
        continue
    isPrime(2,num)
    isPrime(num,num+MIN+1)
    # prime.sort()
    print(*prime)
