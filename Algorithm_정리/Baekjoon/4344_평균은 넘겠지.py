C = int(input())
for tc in range(1,C+1):
    score = list(map(int,input().split()))
    ans = sum(score[1:])/score[0]
    cnt = 0
    for i in score[1:]:
        if i > ans:
            cnt += 1
    result = round(cnt/score[0]*100,3)
    # print('{}%'.format(result))
    print("%.3f"%result + "%")

