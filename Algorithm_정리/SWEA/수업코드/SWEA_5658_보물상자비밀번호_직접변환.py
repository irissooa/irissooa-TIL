def hex_to_dec(num16):
    # 16진수 값 10진수화 시키기
    value = 0
    for i in range(len(num16)):
        if '0' <= num16[i] <= '9':
            tmp = ord(num16[i]) - ord('0')
        else:
            tmp = ord(num16[i]) - ord('A') + 10

        # 최대차수 부터 감소하면서 값이 구해진다.
        value += tmp * (16 ** (L - 1 - i))
    return value


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())  # 숫자의 수, K번째 크기
    L = N // 4  # N은 4의 배수 이므로 하나의 비밀번호 길이는 L
    password = list(input())
    ans = set()  # 중복제거

    # N번 회전하면 원래대로 돌아오므로 N-1번만 회전
    for i in range(N - 1):
        for j in range(0, N, L):
            # L의 크기로 잘라서 ans에 넣기 (16진수 형태)
            ans.add("".join(password[j:j + L]))

        # 가장 뒤의 값을 꺼내 맨 앞에 삽입 (시계방향 회전 효과)
        password.insert(0, password.pop())

    # 정렬하기 위해 list로 바꾸기
    ans = list(ans)
    ans.sort(reverse=True)  # 내림차순 정렬 숫자의 값이 문자보다 작으므로 가능
    print("#{} {}".format(tc, hex_to_dec(ans[K - 1])))
