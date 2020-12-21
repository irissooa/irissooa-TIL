def choose(dice, idx):
    oidx = opposite_dice[idx]

    max_num = 0
    for i in range(6):
        if i == idx or i == oidx:
            continue
        if max_num < dice[i]:
            max_num = dice[i]
    return max_num


opposite_dice = [5, 3, 4, 1, 2, 0]

N = int(input())

dices = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(6):
    tmp = choose(dices[0], i)
    pre = dices[0][opposite_dice[i]]

    for j in range(1, N):
        idx = dices[j].index(pre)
        tmp += choose(dices[j], idx)
        pre = dices[j][opposite_dice[idx]]

    if tmp > ans:
        ans = tmp

print(ans)
