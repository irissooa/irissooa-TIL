arr = [1,2,3]
N = len(arr) #n:원소의 개수
for i in range(1 << N) : #1<<n:부분집합의 개수 0에서 2^n전까지 움직임
    for j in range(N): #원소의 수만큼 비트를 비교함
        if i & (1 << j): #i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end = ',') #0이 아니면 True
        print()
    print() #부분집합끼리 구분을 하기위해
