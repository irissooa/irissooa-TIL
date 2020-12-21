#시험장 개수 N
N = int(input())
#각 시험장 응시자 수
students = list(map(int,input().split()))
#총 감독관 감시가능 수, 부감독관 감시가능 수
B,C = map(int,input().split())
cnt = 0
for i in range(N):
    students[i] -=B
    cnt += 1
# print(students)
for i in range(N):
    if students[i] > 0:
        if students[i]%C:
            cnt += students[i]//C +1
        else:
            cnt += students[i]//C
print(cnt)