def calc(idx, sum_honey, sum_cost):
    global max_cost
    if sum_honey > C: return
    # 여기서 갱신을 하기 때문에 아래와 같이 반복문을 통해 모든경우 구할 수 있다.
    max_cost = max(max_cost, sum_cost)

    for i in range(idx, M):
        calc(i + 1, sum_honey + honey[i], sum_cost + honey[i] ** 2)


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())  # 한변의길이, 채취벌통길이, 한일꾼 최대벌꿀

    arr = [list(map(int, input().split())) for _ in range(N)]  # 벌통입력
    honey_list = []  # 일꾼이 캘수있는 모든 벌통을 담기 위한 리스트

    # 순회하면서 벌통을 뽑기
    for i in range(N):
        # 가로로 M길이의 통을 뽑으므로
        for j in range(N - M + 1):
            honey = arr[i][j:j + M]
            max_cost = 0
            calc(0, 0, 0)
            # 해당 통에서 구한 값 넣기
            honey_list.append((max_cost, i, j))

    # 내림차순 정렬
    # 가장 앞의 값이 가장 큰값
    honey_list.sort(reverse=True)
    first = honey_list.pop(0)
    for cost, r, c in honey_list:
        # first 통과 겹친다면 넘어가기
        if r == first[1] and first[2] - M < c < first[2] + M: continue
        # 아니라면 second 값넣고 끝내기
        second = [cost, r, c]
        break
    print("#{} {}".format(tc, first[0] + second[0]))
