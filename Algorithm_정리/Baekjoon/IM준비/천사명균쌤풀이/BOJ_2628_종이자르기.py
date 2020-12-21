def cut(cutlist, end):
    st = 0
    length = 0
    for i in cutlist:
        tmp = i - st
        if length < tmp:
            length = tmp
        st = i

    return max(length, end - st)


C, R = map(int, input().split())

N = int(input())

row = []
col = []
for i in range(N):
    dir, idx = map(int, input().split())
    if dir:
        col.append(idx)
    else:
        row.append(idx)

row.sort()
col.sort()

maxRow = cut(row, R)
maxCol = cut(col, C)

print(maxCol * maxRow)
