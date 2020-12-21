#{1,2,3}을 포함하는 모든 순열을 생성하는 함수
#원소개수가 늘어날수록 for문이 늘어남...재귀로 푸는게 좋음
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                #여기까지 한다면 중복순열
                if i3 != i1 and i3 != i2: #중복을 제거해줌
                    print(i1,i2,i3)
data = [1,2,3]
for i1 in range(len(data)):
    for i2 in range(len(data)):
        if i2 != i1:
            for i3 in range(len(data)):
                #여기까지 한다면 중복순열
                if i3 != i1 and i3 != i2: #중복을 제거해줌
                    print(data[i1],data[i2],data[i3])