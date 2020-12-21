#1~12 부분집합 원소
#집합 A의 부분집합 중 N개의 원소를 갖고있음
#원소의 합이 K인 부분집합개수

#집합 A에서 tc를 돌면서
#비트 연산자를 이용 부분집합을 만들고
#그 부분집합의 원소를 하나씩 더하면서 cnt를 하고
#합이 K이고 cnt가 N개인 것의 수를 세어라
# import sys
# sys.stdin = open("input.txt", "r")

# T = int(input())
# A = [1,2,3,4,5,6,7,8,9,10,11,12]
# n = len(A) # 원소의 개수
# for tc in range(1,T+1):
#     N, K = map(int,input().split())
#     res = 0
#     for i in range(1<<n): #부분집합의 개수 0에서 2^n전까지 움직임
#         SUM = 0# 부분집합 합
#         cnt = 0
#         for j in range(n+1): #원소 수만큼 비트를 비교함
#             if i & (1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
#                 SUM += A[j]
#                 cnt += 1
#         if SUM == K and cnt == N:
#             res += 1
#     print(f'#{tc} {res}')


#하영이가 가르쳐줌
# 부분집합 모두를 한 list에 넣고
# testcase를 그 밑에 돌리면서 거기서 len으로 개수를 센뒤 구하고자하는 것을 구함

T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(A) # 원소의 개수
sub = []
for i in range(1 << n): # 부분집합의 개수 0에서 2^n전까지 움직임
    bin =[]
    for j in range(n + 1):  # 원소 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            bin.append(A[j])
    if bin:
        sub.append(bin)


for tc in range(1,T+1):
    N, K = map(int,input().split())
    cnt = 0
    for s in sub:
        if len(s) == N:
            if sum(s) == K:
                cnt += 1
    print(f'#{tc} {cnt}')

