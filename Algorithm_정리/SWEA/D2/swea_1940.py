# RC카가 현재속도를 유지할지(0) 가속(1)을 하는지 감속(2)을 하는지와 가속도의 값을 추가로 입력받는다
#초기속도인 0m/s에 더하거나 뻄
#거리 = 속도*시간
#N초를 입력받고 매초마다 한줄씩 속도를 어떻게 할지와 가속도가 주어짐
#0부터 시작해서 가속을 한다면 가속도값을 더해주고, 감속을한다면 빼주되 0보다 내려가면 0이다, 유지한다면 그대로 유지시켜라
#시간은 모두 1초씩 곱하고 거리를 계산해서 계속 더해줘라
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    RC_v = 0
    s = 0 #거리 초기값
    for n in range(int(input())):
        command_list= list(map(int,input().split()))
        if command_list[0] == 1:
            RC_v += command_list[1] #가속도 값을 더함
        elif command_list[0] == 2:
            RC_v -= command_list[1] #감속하니까 가속도값을 뺌
            if RC_v <= 0:
                RC_v = 0 #0보다 속도가 작아지면 0으로 함
        s += 1 * RC_v #거리 = 시간(1초) * 속도
    print(f'#{tc} {s}')