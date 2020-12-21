import sys
sys.stdin = open("input.txt", "r")
T = int(input())
# print(T)
for i in range(1,T+1):
    a, b = input().split()
    # print(a)
    # print(b)
    moc = int(a) // int(b)
    remain = int(a) % int(b)
    print(f'#{i} {moc} {remain}')