import sys
sys.stdin = open('input.txt','r')

def check(E,S,M):
    if E == S and S == M:
        return True
    return False

# T = int(input())
# for tc in range(1,T+1):
E,S,M = map(int,input().split())

while not check(E,S,M):
    if S > E:
        E += 15
    else:
        S += 28
    if check(E,S,M):
        break
    if M > E:
        E += 15
    else:
        M += 19
print(E)

