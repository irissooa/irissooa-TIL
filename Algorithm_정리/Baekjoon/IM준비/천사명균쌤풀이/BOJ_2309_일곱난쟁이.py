def combination(idx, sidx):
    global ans
    if ans:#이미 구했다면 수행 x
        return
    if sidx == 7:
        if sum(sel) == 100:
            ans = sel[:]
        return
    if idx == 9:
        return
    sel[sidx] = height[idx]
    combination(idx + 1, sidx + 1)#뽑고가고
    combination(idx + 1, sidx)#안뽑고가고


height = [int(input()) for _ in range(9)]

ans = []
sel = [0] * 7
height.sort()
combination(0, 0)
print("\n".join(map(str, ans)))#출력
