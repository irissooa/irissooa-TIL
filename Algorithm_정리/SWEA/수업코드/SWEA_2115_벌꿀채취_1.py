def choose(r, c):
    global first, second
    honey = arr[r][c:c + M]  # 해당 벌통 슬라이싱
    max_cost = 0  # 이번 벌통의 최대값
    # 모든 벌통 경우의수 구해보기
    for i in range(1 << M):
        sum_honey = sum_cost = 0
        for j in range(M):
            if i & (1 << j):
                sum_honey += honey[j]
                sum_cost += honey[j] ** 2
        # 꿀의 채취양이 제한 법위를 넘지 않고,
        # 갱신 가능하다면 갱신
        if sum_honey <= C:
            max_cost = max(max_cost, sum_cost)

    # 첫번째 통보다 값이 크다면
    if max_cost > first[0]:
        # 행이 같으면서 첫번째 통과 겹친다면
        if r == first[1] and c < first[2] + M:
            # 과감하게 첫번째 통 갱신
            first = [max_cost, r, c]
        else:
            # 아니라면 첫번째통을 두번째통으로 밀고
            second = first[:]
            # 첫번째 통 갱신
            first = [max_cost, r, c]
    # 두번째 통보다 크다면
    elif max_cost > second[0]:
        # 첫번째 통과 행이다르거나 (절대 겹칠일 없음)
        # 첫번째 통과 열이 겹치지 않는다면
        if r != first[1] or c >= first[2] + M:
            # 두번째 통 갱신
            second = [max_cost, r, c]


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())  # 한변의길이, 채취벌통길이, 한일꾼 최대벌꿀

    arr = [list(map(int, input().split())) for _ in range(N)]  # 벌통입력

    # 값, 행, 열
    first = [0, 0, 0]  # 가장 값어치가 좋은 값
    second = [0, 0, 0]  # first의 벌통과 겹치지 않으면서 다음으로 큰 값

    # 순회하면서 벌통을 뽑기
    for i in range(N):
        # 가로로 M길이의 통을 뽑으므로
        for j in range(N - M + 1):
            choose(i, j)

    print("#{} {}".format(tc, first[0] + second[0]))
