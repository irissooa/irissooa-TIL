'''
20-12-12 11:50-(12:30밥-13:00)-13:54(잠시멈춤..뷰..)-18:30(다시시작)-
N부터 M까지의 소수의 개수를 구하는 프로그램

1.num은 N부터 M까지의 수로 정함
2. 각 num에서 2~int(num**0.5)+1까지 나누어떨어지는게 없다면 cnt+=1 -> 역시나 70퍼에서 시간초과..
이건 시간을 어떻게 줄이지

[Hint]에라토스테네스의 체
에라토스테네스의 체(Eratosthenes' sieve) 에라토스테네스가 일정 범위까지의 소수를 간단하게 구하기 위해 고안한 방법으로
자연수를 ‘체’로 쳐서 걸러내고 ‘소수’만 골라내는 방법이라고 해서 에라토스테네스의 체라고 한다.
예) 즉, 5보다 작은 수를 곱해서 생기는 5의 배수는 5를 처리하기 이전에 모두 제거가 되었다는 것이다.
따라서 5를 처리할 때에는 5의 제곱인 25부터만 처리하면 된다.
이렇게 에라토스테네스의 체를 이용하여 어떤 수(N)까지의 소수를 구하기 위해서,
N의 제곱근까지만 배수를 걸러내는 작업을 하면 되므로 매우 빠른 속도로 소수를 구해 낼 수 있다.

1. 2부터 M까지 방문배열을 만들고 소수가 아니면 True로 변환
+소수를 찾는 범위는 해당 수의 제곱근까지
2. 소수를 찾았다면 그 소수의 배수들을 다 True로 변환
3. 다음 소수를 찾으면 배수들을 다 True로 변환하는데 그 소수의 제곱수부터 찾으면됨!(이전수는 이 이전 소수가 체크함)
4. 그렇게해서 N~M사이의 False인 소수의 개수만 구하면 끝
-> 이렇게 하면 90퍼부터 시간초과,,,ㅠ
#방문배열을 비트로 바꿔볼까...ㅠ 비트 어떻게 쓰닝...
'''
import sys
input = sys.stdin.readline

#비트로 풀어보려다가 망한코드
def prime_list(n):
    visit = 1<<(M-1)
    for i in range(2,int(M**0.5)+1):
        if not visit&(1<<i):
            for j in range(i+1,M+1,i):
                print(j,'dd')
                visit = visit|1<<j
    return visit


N,M = map(int,input().split())
visit = str(bin(prime_list(M)))[2:M+1]
print(visit,len(visit))

cnt = 0
for i in range(len(visit)):
    print(M-i,visit[i])
    if visit[i] == '0':
        cnt+=1
print(cnt)
# 0과 1은 소수가 아니니까 index맞춰주려고
# visit = [True,True]+[False for i in range(M-1)]
# print(bin(visit))
# 0과 1을 1으로 방문처리
# visit = visit|3
# print(bin(visit))



# 시간초과코드
for num in range(2,int(M**0.5)+1):
    if visit[num]:
        continue
    # 소수를 찾았으니 그 배수들을 표시
    for i in range(num,M//num+1):
        if not visit[i*num]:
            # print(num*i)
            visit[i*num] = True
            # 범위안의 수들 중 합성수를 세어준다, 그런뒤에 M-N+1개 안의 수에서 합성수를 빼주면 소수! 근데도 시간초과..후
            if N<=i*num<=M:
                cnt += 1

# 1은소수도 합성수도 아니니까 빼줌
if N != 1:
    print(M-N-cnt+1)
else:
    print(M-N-cnt)

M, N = map(int, input().split())


## 통과코드
def prime_list(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(M, n + 1) if sieve[i] == True]
li = prime_list(N)
cnt = 0
if 1 in li:
    li.remove(1)
    for k in li:
        cnt +=1
        # print(k)
else:
    for _ in prime_list(N):
        cnt += 1
        # print(_)
print(cnt)