T = int(input())
for tc in range(1,T+1):
    score = input()
    SUM = 0
    cnt = 0
    for i in score:
        if i =='O':
            cnt+=1
            SUM += cnt
        else:
            cnt = 0
            # SUM += cnt
    print(SUM)
