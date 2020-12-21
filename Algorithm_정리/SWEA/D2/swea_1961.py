#N*N행렬의 N을 입력받는다
#행렬을 입력받는다
#2차원배열을 만든다
#90도씩 돌아가는 함수를 만들수 있을까?
#90도 -> 180도 -> 270도 -> 360도(원점) 모두 90도씩 돌아가니까...
#2차배열을 90도로 전부 재배열
#배열을 계속 90도씩 재배열하며 한줄씩 출력을 함

import sys
sys.stdin = open("input.txt", "r")

# #내꺼..다시풀어보기
def turnArr(arr):
    temp = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = arr[N-j-1][i]#90도 돌아가면 원래 위치에 뒤에서부터 행과 열이 바뀐상태로 들어온다
    return temp

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [input().split() for i in range(N)] #2차배열을 숫자들을 문자로 받음
    # 2차배열을 각각 재설정 해줌
    turn90 = turnArr(arr)
    turn180 = turnArr(turn90)
    turn270 = turnArr(turn180)
    print(f'#{tc}')
    for i in range(N):
        #각각 90도로 돌아간 배열들의 각 idx리스트들을 구분자 없이 문자열로 변환시킴
        a = ''.join(turn90[i])
        b = ''.join(turn180[i])
        c = ''.join(turn270[i])
        print(f'{a} {b} {c}')


# def turnArr(arr):
#     temp = [[0]*N for i in range(N)]
#     for i in range(N):
#         for j in range(N):
#             temp[j][N-i-1] = arr[i][j]#90도 돌아가면 arr의 원래 위치는 새로운 temp의 저 위치로 감
#     return temp
#
# for tc in range(1,int(input())+1):
#     N = int(input())
#     arr = [input().split() for i in range(N)] #2차배열을 숫자들을 문자로 받음
#     #2차배열을 각각 재설정 해줌
#     turn90 = turnArr(arr)
#     turn180 = turnArr(turn90)
#     turn270 = turnArr(turn180)
#     print(f'#{tc}')
#     for i in range(N):
#         a = ''.join(turn90[i])
#         b = ''.join(turn180[i])
#         c = ''.join(turn270[i])
#         print(f'{a} {b} {c}')

#의수
# def rotate90(li):
#     new = [[0 for x in range(N)] for y in range(N)]
#     for i in range(N):
#         for j in range(N):
#             new[j][N - i - 1] = li[i][j]
#     return new
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [[str(x) for x in input().split()] for _ in range(N)]
#     ro90 = rotate90(arr)
#     ro180 = rotate90(ro90)
#     ro270 = rotate90(ro180)
#     print(f'#{tc}')
#     for i in range(N):
#         a = ''.join(ro90[i])
#         b = ''.join(ro180[i])
#         c = ''.join(ro270[i])
#         print(f'{a} {b} {c}')

#병훈
def print_rot():
    end = N - 1
    print(f'#{t}')
    for i in range(N):
        [print(arr[end - j][i], end='') for j in range(N)]
        print(end=' ')
        [print(arr[end - i][end - j], end='') for j in range(N)]
        print(end=' ')
        [print(arr[j][end - i], end='') for j in range(N)]
        print()


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print_rot()