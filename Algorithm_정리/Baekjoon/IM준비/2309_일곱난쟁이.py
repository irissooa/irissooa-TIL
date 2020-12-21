'''
조합으로 하면 되지 않을깡
9개중에 7개를 뽑아서 그 합이 100인것 뽑기
'''
def combination(idx,sidx):
    if sidx == 7:
        if sum(R) == 100:
            for i in sorted(R):
                print(i)
            exit()
            return
        # print('못찾았나')
        return
    if idx == N:
        return
    R[sidx] = height[idx]
    combination(idx+1,sidx+1)
    combination(idx+1,sidx)

height = []
for t in range(9):
    height.append(int(input()))
# print(height)
N = 9
R = [0]*7
combination(0,0)