import sys

sys.stdin = open("input5658.txt", "r")
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())  # 숫자의 수, K번째 크기
    L = N // 4  # N은 4의 배수 이므로 하나의 비밀번호 길이는 L
    password = input()
    ans = set()  # 중복제거
    password += password[:L - 1]
    for i in range(N):
        # L의 크기로 잘라서 ans에 넣기 (10진수로 변환)
        ans.add(int(password[i:i + L], 16))
    # 정렬하기 위해 list로 바꾸기
    ans = list(ans)
    ans.sort(reverse=True)  # 내림차순 정렬
    print("#{} {}".format(tc, ans[K - 1]))
