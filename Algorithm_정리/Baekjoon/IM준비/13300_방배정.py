'''
성별이 다르고, 학년이 같아야되고, K명을 넘을 수 없다
방의 최소 개수구하기
'''
N,K = map(int,input().split())
#학생의 성별S(0:여,1:남), 학년 Y
#학년별 idx
G_arr = [0 for _ in range(7)]
B_arr = [0 for _ in range(7)]
for _ in range(N):
    S,Y = map(int,input().split())
    #남자
    if S:
        B_arr[Y] += 1
    #여자
    else:
        G_arr[Y] += 1
# print(B_arr)
# print(G_arr)
#학년이 idx
room = 0
# cnt = 0
for i in range(1,7):
    if B_arr[i] > K:
        if B_arr[i]%K:
            room += B_arr[i]//K + 1
        else:
            room += B_arr[i]//K
    elif B_arr[i]:
        room += 1
    if G_arr[i] > K:
        if G_arr[i] % K:
            room += G_arr[i] // K + 1
        else:
            room += G_arr[i] // K
    elif G_arr[i]:
        room += 1
print(room)

'''
5 2
0 1
0 1
0 1
0 1
0 1
'''