T = int(input())
for tc in range(1,T+1): #테스트케이스 수
    N = int(input())
    ajs = list(map(int,input().split()))
    max_num = ajs[0]
    min_num = ajs[0]
    for aj in ajs:
        if aj > max_num:
            max_num = aj
        elif aj < min_num:
            min_num = aj
    print(f'#{tc} {max_num - min_num}')




