'''
그림에서 빨간색은 :1(N이라 S로감) 파란색은 :2(S라 N으로 감)
교착상태 : 빨강과 파랑이 겹쳐진 모서리 수만 구하면 됨!

A로 표시된 붉은 자성체의 경우 S극에 이끌리면서 테이블 아래로 떨어짐(걸리는 것없이 떨어짐 : 1)
B 푸른 자성체 N극에 이끌리면서 테이ㅣ블 아래로 떨어짐(B:2 N극에 이끌려감)
나머지 자성체들은 서로 충돌하며, 교착 상태에 빠져 움직이지 않게 됨
D로 표시된 자성체들에서 알 수 있듯 한 쪽 방향으로 움직이는 자성체의 개수가 많더라도
반대 방향으로 움직이는 자성체가 하나라도 있으면 교착 상태에 빠져 움직이지 않음
D로 표시된 자성체들과 같이 셋 이상의 자성체들이 서로 충돌하여 붙어있을 경우에도 하나의 교착상태로 봄
C와 D는 좌우로 인접하여 있으나 각각 다른 교착상태로 판단하여 2개의 교착상태로 봄
E의 경우와 같이 한 줄에 두 개 이상의 교착 상태가 발생할 수 있음
F의 경우 각각 다른 교착상태로 판단하여 2개의 교착상태로 봄
자성체는 테이블 앞 뒤쪽에 있는 N극 S극에만 반응, 자성체끼리는 전혀 반응하지 않음
테이블의 크기는 100X100으로 주어짐
(입력)
각 테스트케이스 첫번째 줄에는 정사각형 테이블 한변의 길이 주어짐
10개 테스트케이스
1은 N
2는 S
테이블 윗부분에 N극이 아랫부분에 S극이 위치함
(출력)
교착상태의 개수
'''
import sys
sys.stdin = open('input.txt','r')
for tc in range(1,11):
    #NXN배열
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 한 열이 같을 때 행이 움직여야됨
    cnt = 0 #교착상태 개수
    for j in range(N):
        check = 0 # 여기에 1을 만났을 때 표시해주고 확인
        for i in range(N):
            if arr[i][j] == 0:
                continue #0이면 지나감
            elif check == 0 and arr[i][j] == 2: #그전에 1이 없는데 2를 만났다면? 지나감!
                continue
            elif check == 1 and arr[i][j] == 2: # 그전에 1이 있는데 2를 만났다면 교착상태 +=1
                cnt += 1
                check = 0 #그전에 1표시 리셋
            elif arr[i][j] == 1:
                check = 1 #1을 만났다고 표시
    print('#{} {}'.format(tc, cnt))






    #다시....모르겠다...
    # for j in range(N):
    #     stack = []
    #     #한 열을 stack에 담고, 위는(N극)은 2를 끌어들임, 2를 만나면 pop/ 아래(S극)은 1을 끌어들이고 1을 만나면 pop 다른 숫자를 만나면 멈춤
    #     #0이아닌 것들을 담는다
    #     for i in range(N):
    #         if arr[i][j] != 0:
    #             stack.append(arr[i][j])
    #     print(stack,f'{j}열의 stack')
    #     #끝에서부터본다 1이면 계속 돌아가면서 pop
    #     while stack[-1] == 1:
    #         print('끝에서부터팝')
    #         stack.pop()
    #     #위에서부터 본다 2면 계속 돌아가면서 pop
    #     while stack[0] == 2:
    #         print('처음부터 팝')
    #         stack.pop(0)
    #     # print(stack)
    #     #교착상태 확인
    #     #stack이 있을때까지
    #     while stack:
    #         #같은 숫자가 붙어있다면 pop하고 112일때 1한개팝
    # #다른 극이면

'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''



#선생님 풀이
for tc in range(1,11):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    ans = 0
    for i in range(N):
        #내가 만나야될 컬러
        state = 1
        for j in range(N):
            #내가 빨강을 만나야하고 마친 내자리가 빨강이라면
            if state == 1 and arr[j][i] == '1':
                state = 2
            #내가 파랑을 만나야하고 마침 내자리가 파랑이라면 교착상태 1증가
            elif state == 2 and arr[j][i] == '2':
                state = 1
                ans += 1
    print('#{} {}'.format(tc,ans))