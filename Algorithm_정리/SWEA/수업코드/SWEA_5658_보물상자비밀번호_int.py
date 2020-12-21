for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())  # 숫자의 수, K번째 크기
    L = N // 4  # N은 4의 배수 이므로 하나의 비밀번호 길이는 L
    password = list(input())
    ans = set()  # 중복제거

    # N번 회전하면 원래대로 돌아오므로 N-1번만 회전
    for i in range(N - 1):
        for j in range(0, N, L):
            # L의 크기로 잘라서 ans에 넣기 (10진수로 변환)
            ans.add(int("".join(password[j:j + L]), 16))
        # 가장 뒤의 값을 꺼내 맨 앞에 삽입 (시계방향 회전 효과)
        password.insert(0, password.pop())
    # 정렬하기 위해 list로 바꾸기
    ans = list(ans)
    ans.sort(reverse=True)  # 내림차순 정렬
    print("#{} {}".format(tc, ans[K - 1]))
