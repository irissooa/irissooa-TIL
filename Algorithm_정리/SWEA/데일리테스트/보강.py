# import sys
# sys.stdin = open('input.txt','r')
# T = int(input())
# for tc in range(1,T+1):
#     t = int(input())
#     num_list = list(map(int,input().split()))
#     # print(num_list)
#     count_num = [0]*101
#     for i in num_list:
#         #num_list의 요소를 count_num index에 넣어라:
#         count_num[i] += 1
#     MAX = count_num[0]
#     MAX_idx = count_num.index(MAX)
#
#     for n in count_num:
#         if MAX <= n:
#             MAX = n
#             MAX_idx = count_num.index(MAX)
#
#     print('#{} {}'.format(tc,MAX_idx))
import sys
sys.stdin = open('input.txt','r')


def solve(arr1, arr2):  # 첫번째 짧은 두번째 긴, 함수의 정의
    len1 = len(arr1)
    len2 = len(arr2)
    MAX = 0
    '''
    12345
    123
     123
      123
    비교 시작 위치?
    0,1,2 ->바깥쪽 for문의 범위 -> 0 - (긴문자열길이-짧은문자열길이) => 5-3 = 2
    '''
    for i in range(0, len2 - len1 + 1):  # 비교시작점
        SUM = 0
    for j in range(0, len1):  # 짧은 문자열 반복
        num = arr1[j] * arr2[j + i]  # 짧은 : 0,1,2,반복
        # 긴 문자열 : 0,1,2,,,2,3,4,,2,3,4,,,짧은 + 0,1,2,,
        SUM += num


        if SUM > MAX:
        MAX = SUM
    return MAX

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 숫자열 길이를 비교해서
    # 짧은 숫자열, 긴 숫자열 순으로 매개변수로 해서 함수에 넘김
    result = 0
    if len(A) < len(B):
        result = solve(A, B)  # 첫번째: 짧은, 두번째 : 긴
    else:
        result = solve(B, A)

    print('#{} {}'.format(tc,result))