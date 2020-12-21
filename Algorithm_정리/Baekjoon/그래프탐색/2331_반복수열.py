'''
D에 D[0]=A를 넣고 시작
D[n] = D[n-1]의 각 자리 숫자에 P를 곱한뒤 더한 값을 넣고
while문을 돌리는데
종료조건으로 D에 이미 들어간 숫자가 들어가면 break한 뒤 그 숫자의 앞에 있는 숫자들 개수 출력!
'''
import sys
sys.stdin = open('input.txt','r')
A,P = map(int,input().split())
D = [A]
num = 1
flag=False
while True:
    SUM = 0
    #문자열로 바꿔서 각 자리수를 분리시킴
    for n in range(len(str(D[num-1]))):
        SUM += int(str(D[num-1])[n])**P
        # print(SUM)
    #종료조건
    #D에 이미 들어간 숫자가 있다면 break!
    if SUM in D:
        # print(D)
        #D[num]이 D에 들어있는 수 중 앞에 있는걸 찾아서 그 앞의 수 개수를 출력
        for d in range(len(D)):
            if D[d] == SUM:
                print(len(D[:d]))
                flag=True
                break
        if flag:
            break
    #D[n] = D[n-1]의 각 자리 숫자에 P를 곱한뒤 더한값
    D.append(SUM)
    num+=1
