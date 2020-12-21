'''
20-12-12 10-10:32 => 정수로 받는다고 돼있으면 정수로 받아야된다...ㅠㅁ
양의 정수를 입력받아 역으로 보여주고 각 숫자의 합을 구하는 프로그램
21억 이해 양의 정수, 새로운 입력을 받다가 0이 입력되면 프로그램 종료
입력받은 수의 역과 각 자리 숫자의 합을 공백으로 구분하여 출력
유효하지 않은 0은 출력하지 않음
'''
import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if not N:
        break
    N = str(N)
    print(int(N[::-1]),end = ' ')
    ans = 0
    for i in N:
        ans += int(i)
    print(ans)
