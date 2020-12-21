import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input()))
    C = [0] * 10 #0~9까지 리스트 개수
    # print(nums)
    for i in range(len(nums)):
        C[nums[i]] += 1
    MAX = C[0]
    # cnt = 0
    for i in range(len(C)): # 처음 for i in C로 했을 때는 같은 것이 나오면 제일 처음 나오는 값이 계속 출력됨
        if C[i] >= MAX:
            MAX = C[i]
            cnt = i #max인 i의 idx
    print(f'#{tc} {cnt} {MAX}')
    
    