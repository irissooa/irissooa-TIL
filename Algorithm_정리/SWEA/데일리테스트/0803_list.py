#자기중심 오른쪽 두개 왼쪽두개 4칸 중 최대값을 찾고
#현재 i idx보다 작으면 자기 값-최대값 세대 조망권 확보,
# 아니면 없다.
import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))  # 입력받을 곳
    cnt = 0

    for i in range(2, N - 2):  # 앞두개 뒤두개는 0이다
        #1)max사용
        MAX = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        # 2)max사용 안함
        # if arr[i-2] > arr[i-1]:
        #     MAX = arr[i-2]
        #     if arr[i] > MAX:
        #         cnt += (arr[i] - MAX)

        if arr[i] > MAX:
            cnt += (arr[i] - MAX)

    print('#{} {}'.format(tc, cnt))