data = [7,4,2,0,0,6,0,7,0] #오른쪽에서 자기보다 작은쪽의 개수를 세면 그 개수가 낙차가 된다. 중력으로 떨어지기 때문에 왼쪽은 셀 필요 없음 자기보다 하나 큰 idx부터 끝까지
max = 0

for i in range(9): #idx가 0부터 8번까지 있음
    cnt = 0
    for j in range(i+1,9): #자기보다 1큰 idx부터 끝까지 중 자기보다 작은 것의 수를 계산
        if data[i] > data[j]:
            cnt += 1
    if max < cnt:#구해지는 낙차값중 가장 큰 최대값을 찾아라
        max = cnt
print(max)