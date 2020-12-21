import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    D = int(input()) #dump횟수
    height = list(map(int,input().split())) #각상자의 높이

    for dump in range(D): #D번 dump
        MAX = max(height) #MAX를 계속 제일 높은 값으로 reset
        height[height.index(MAX)] -= 1 #정해진 MAX에 1을 빼줌 밑의MIN도 마찬가지
        MIN = min(height)
        height[height.index(MIN)] += 1
        if MAX-MIN == 1:
            break
        MAX = max(height)
        MIN = min(height)

    # print(MAX,MIN)
    print(f'#{tc} {MAX-MIN}')