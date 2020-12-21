'''
N개의 수 N-1연산자 더하기 빼기 곱하기 나누기로 주어짐
순서대로 수를 계산하고, 음수나누기는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꿈
나올수 있는 수들의 최대 최소 값을 구함

1. 연산자들을 보면서 0이 아닌 수 들 중 빼면서 순열!을 구함
2. 계산하는 함수를 만들어서 계산한 뒤, 최대 최소 값을 구함
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
INF = sys.maxsize

#계산하는 함수
def calc(opr):
    ans = numbers[0]
    # print(opr,'연산자')
    for s in range(N-1):
        o_idx = opr[s]
        if o_idx == 0:
            ans += numbers[s+1]
        elif o_idx == 1:
            ans -= numbers[s+1]
        elif o_idx== 2:
            ans *= numbers[s+1]
        else:
            if ans >= 0:
                ans //= numbers[s+1]
            else:
                ans = -(abs(ans)//numbers[s+1])
        # print(numbers[s],ans)
    return ans

#순열
def perm(idx):
    global MAX,MIN
    if idx == N-1:
        ans = calc(sel)
        if MAX < ans:
            MAX = ans
        if MIN > ans:
            MIN = ans
        return
    for o in range(4):
        if operators[o]:
            sel[idx] = o
            operators[o] -= 1
            perm(idx+1)
            operators[o] += 1
            sel[idx] =0




N = int(input())
numbers = list(map(int,input().split()))
# + - * //
operators = list(map(int,input().split()))
# print('연산자',operators)
sel = [0]*(N-1)
MAX,MIN = -INF,INF
perm(0)
print(MAX)
print(MIN)