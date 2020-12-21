import sys
sys.stdin = open('input.txt', 'r')


def calc(psel):
    ans = numbers[0]
    for i in range(len(psel)):
        if psel[i] == 1:
           ans += numbers[i+1]
           # print('+',ans)
        elif psel[i] == 2:
            ans -= numbers[i+1]
            # print('-',ans)
        elif psel[i] == 3:
            ans *=numbers[i+1]
            # print('*',ans)
        elif psel[i] == 4:
            ans = int(ans/numbers[i + 1])
    # print(ans)
    return ans

def perm(idx,check):
    if idx == N-1:
        return
    for i in range(N-1):
        if (check & (1<<i)):
            continue
        if operator[idx]:
            operator[idx] -= 1
            perm(idx+1,check|(1<<i))
            operator[idx] += 1







T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #+ - * // 개수
    operator = list(map(int,input().split()))
    print('o',operator)
    numbers = list(map(int,input().split()))
    MAX,MIN = -987654321,987654321
    sel =[0]*(N-1)
    perm(0,0)
    # print(MAX,MIN)
    print('#{} {}'.format(tc,MAX-MIN))