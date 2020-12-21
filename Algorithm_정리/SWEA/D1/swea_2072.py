# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys 


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("input.txt", "r") #같은 폴더 내에 이 파일이 있으면 대신 input값을 입력해줌

#주어진 코드는 거의 건들 일이 없음(아마도...)
T = int(input()) #가장 첫줄 테스트 케이스가 몇줄인지 말해줌
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1): #T의 개수는 줄 수
    # result = input() #input으로 들어온 것은 str 타입
    #str을 list로 바꾸는 것이 편하지 않을까?/입력없으면 공백을 기준으로 나눔
    # results = input().split() 
    # results _int = []
    # for result in results: #문자로 리스트가 돼있으니 숫자로 바꾸자
    #     results_int.append(int(result))
    #  위 코드 4줄을 map으로 한줄로 표현
    numbers = map(int, input().split()) #실제로는 list가 아니라 map객체 타입임
    #input().split()의 item각각에 int를 처리한 것을 results에 넣어줌
    #담긴 수를 하나하나 봐서
    #홀수이면 total에 더함
    total = 0
    for number in numbers:
        if (number % 2 ) == 1: #1은 생랙가능, True이기 떄문
            total += number
    # return total #우린 보통 이렇게 해줬었는데 SWEA는 그렇지 않다. 양식에 맞게!
    print(f'#{test_case} {total}')
    


