'''
1은 스위치 켜져있음
0은 스위치 꺼져있음
학생들 1이상, 스위치 개수 이하인 자연수 나눠줌
학생들은 자신의 성별과 받은 수에 따라 스위치 조작
남-스위치번호가 자기가 받은 수의 배수이면 그 스위치 상태를 바꿈
여-자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭이면서
가장 많은 스위치를 포함하는 구간을 찾아서 그 구간에 속산 스위치 상태 바꿈
스위치들 처음 상태 주어짐, 각 학생의 성별과 받은 수 주어짐 -> 스위치 마지막 상태 출력
'''
import sys
sys.stdin = open('input.txt','r')

#스위치 상태 바꾸는 함수
def change(num):
    #1, 켜져있으면 0으로
    if switch[num]:
        switch[num] = 0
    #0꺼져있다면
    else:
        switch[num] = 1
    return

#남학생 스위치 바꾸는 함수
def boy(num):
    #num의 배수들을 바꿈
    gop = num
    while num <= N:
        change(num)
        # print(num,'boy',gop)
        #이건 두배지 배수가 아니잖아....
        # num *= 2
        num += gop
    return


#여학생 스위치 바꾸는 함수
def girl(num):
    #방문한곳 방문 표시 후, 전부 바꿔줌
    visited = [False for _ in range(N+1)]
    #받은 num 방문표시
    visited[num] = True
    #그다음 idx에 지정해줄 값
    next = 1
    while True:
        #종료조건
        #범위를 벗어나거나 (num+next,num-next)까지 볼거니까
        if num-next <= 0 or num+next > N:
            break
        #좌우대칭일때까지 계속 상태를 바꿈
        # print(num-next,num+next)
        if switch[num-next] == switch[num+next]:
            visited[num-next] = True
            visited[num+next] = True
            #다음 idx로 넘어감
            next += 1
        #좌우대칭이 아니면 바로끝냄
        else:
            break
    #방문한 곳을 change함
    for v in range(len(visited)):
        #방문했다면
        if visited[v]:
            change(v)
    return

#스위치 개수
N = int(input())

#스위치 상태, index와 숫자 맞춤
switch = [0] + list(map(int,input().split()))

#학생 수
students = int(input())

for student in range(students):
    #학생 상별, 받은 숫자
    sex, num = map(int,input().split())

    #남학생(1) -> 받은숫자 배수 스위치 상태 바꿈
    if sex == 1:
        boy(num)
    #여학생(2) -> 좌우대칭, 가장 스위치 많이 포함 시킨 뒤-> 스위치 상태 바꿈
    else:
        girl(num)

    # print(switch)
# print()
# print(switch)
#20개까지 출력해야됨
s = 1
while s <= N:
    print(switch[s],end=' ')
    if s % 20 == 0:
        print()
    s += 1

#한 줄에 20개까지 1~50을 출력
#for
# num = 1
# for j in range(10):
#     if num == 50:
#         print('50!!')
#         # exit()
#         break
#
#     for i in range(1,21):
#         print(num,end=' ')
#         num += 1
#         if num == 50:
#             print('50이라교옹')
#             break
#     print()
#
# while
# num = 1
# while num <=50:
#     print(num,end= ' ')
#     if num % 20 == 0:
#         print()
#     num+=1