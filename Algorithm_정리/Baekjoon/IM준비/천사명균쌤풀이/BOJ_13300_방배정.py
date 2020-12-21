N, K = map(int, input().split())

student = [[0] * 7 for _ in range(2)]

for i in range(N):
    gender, grade = map(int, input().split())

    student[gender][grade] += 1

room = 0

for i in range(2):
    for j in range(1, 7):
        room += student[i][j] // K
        if student[i][j] % K:
            room += 1

print(room)
