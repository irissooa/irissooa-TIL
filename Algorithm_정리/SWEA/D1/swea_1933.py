N = int(input())
if 1 <= N <= 1000:
    for i in range(1,N+1):
        if N % i == 0:
            print(i,end = ' ')