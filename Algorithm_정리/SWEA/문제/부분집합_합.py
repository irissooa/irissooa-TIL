# arr = list(map(int,input().split()))
arr = [-1,2,1]
N = len(arr) #n:원소의 개수
cnt = 0

for i in range(1 << N) : #1<<n:부분집합의 개수 0에서 2^n전까지 움직임
    SUM = 0
    sub = []
    for j in range(N): #원소의 수만큼 비트를 비교함
        #1개의 부분집합들이 계산됨
        if i & (1 << j): #i의 j번째 비트가 1이면 j번째 원소 출력
            sub.append(arr[j])
            SUM += arr[j]
    if SUM == 0 :
        cnt += 1
        print(sub)
print('{}'.format(cnt))