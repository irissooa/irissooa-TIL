#반복되는 단어의 문자열을 받는다
#1)병훈
#문자열의 문자들을 for문으로 돌아보면서 list에 담는다
#문자를 하나씩 보면서 list에 담는데 다음에 오는 문자가 연결되는지 본다!
#만약에 같은게 나오면 그 단어의 len을 출력하고, 다르다면 하나씩 추가를 해가며 같은지 비교한다.
# for t in range(1,int(input())+1):
#     words = input()
#     for pattern in range(1,11):
#         if words[:pattern]==words[pattern:pattern*2]:
#             print(f'#{t} {pattern}')
#             break
#2)하영
#첫단어를 보고 문자열에서 첫단어와 같은 단어가 나오는 곳까지 자름
#그 사이 단어가 바로 뒤의 문자열에서 다시 나오는지 확인
#나온다면 그 단어의 길이를 구하고
#아니라면 그 다음으로 오는 첫단어와 같은 단어까지 자름, 그리고 확인
# T = int(input())
#
# for i in range(1, T + 1):
#     res = 0
#     string = input()
#     start = string[0]
#     for j in range(1, 21):
#         if start == string[j]:
#             length = j
#             if string[: j] == string[j: j + length]:
#                 res = length
#                 break
#     print(f'#{i} {res}')
import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    words = input()

    for i in range(1,11): #마디의 최대길이는 10
        # 마디의 길이가 처음부터 i까지 했을 때랑 i부터 i만큼 잘랐을 떼 그 값이 같다면
        if words[:i] == words[i:i*2]:
            print(f'#{tc} {i}')
            break # 값을 찾았으니 멈춰라