'''
사칙연산, 후위로 계산이라고 수업때 그랬는데 중위인것같구.....음...ㅎ몰라..ㅎ
중간과정에서 연산은 실수 연산으로 하되, 최종 결과값이 정수로 떨어지지 않으면 정수부만 출력
정점번호는 1부터 N까지의 정수로 구분, 루트 정점번호는 반드시1
정점번호, 해당 값, 자식노드 주어짐!
출력 답은 항상 정수값
중위로 차례대로 값들을 넣고! 나중에 앞에서부터 계산을 하면 되지 않을까???
-->후위로 입력받고 예전에 배웠던 후위계산기 이용
'''
import sys
sys.stdin = open('input.txt','r')

def postOrder(v):
    global num
    if v == 0:
        return
    postOrder(int(L[v]))
    postOrder(int(R[v]))
    # print(v,end = ' ')
    tree[num] = P[v]
    num += 1


for tc in range(1,11):
    N = int(input())
    tree = ['0']*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    P = [0]*(N+1)
    num = 1
    for i in range(N):
        info = list(input().split())
        #각노드의 값들을 넣어줌!
        P[int(info[0])] = info[1]
        if len(info) == 4:
            L[int(info[0])] = info[2]
            R[int(info[0])] = info[3]
    # print(P)
    # print(L,R)
    postOrder(1)

    result = 0
    stack = []
    #계산을 후위로 해야되나...?ㅎ......
    for i in tree:
        # print(i)
        if i.isdigit():
            # print(i)
            stack.append(int(i))
        # 연산자이면 꺼내서 연산 후 다시 삽입
        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+':
                stack.append(A + B)
            elif i == '-':
                stack.append(A - B)
            elif i == '*':
                stack.append(A * B)
            elif i == '/':
                stack.append(A / B)
    print('#{} {}'.format(tc,int(stack.pop())))

#유튜브 선생님 풀이
for tc in range(1,11):
    N = int(input())
    T = [[]]

    for i in range(1,N+1):
        #순서가 바뀌어서 뒤죽박죽 들어올수 있어 위험함!,아니면 미리 만들어 놓고, 첫번째 노드 번호 보고 입력받음!
        T.append(list(input().split()))
        if len(T[i]) == 4: #연산자
            T[i][2] = int(T[i][2])
            T[i][3] = int(T[i][3])
        else: #피연산자
            T[i][1] = int(T[i][1])

    def calc(v):
        if len(T[v]) == 2: #피연산자  = 단말노드
            return T[v][1]
        else: #연산자
            l = calc(T[v][2])
            r = calc(T[v][3])

            if T[v][1] == '+':
                return l+r
            elif T[v][1] == '-':
                return l-r
            elif T[v][1] == '*':
                return l*r
            else :
                return l/r


    print(int(calc(1)))