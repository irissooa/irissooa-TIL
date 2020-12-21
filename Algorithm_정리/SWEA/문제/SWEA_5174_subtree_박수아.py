'''
트리의 일부 서브트리라 함
이진트리 노드 N을 루트로 하는 서브트리에 속한 노드의 개수를 알아내는 프로그램
노드 N을 포함한 노드의 개수를 출력!
'''
import sys
sys.stdin = open('input.txt','r')
def preOrder(node):
    # print(node,end = ' ')
    global cnt
    cnt += 1
    if L[node]:
        preOrder(L[node])
    if R[node]:
        preOrder(R[node])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))
    L = [0] *(E+1+1)
    R = [0]*(E+1+1)
    P = [0]*(E+1+1)
    #두칸씩 자르고 처음칸 부모, 두번째는 자식
    cnt = 0
    for i in range(0,len(arr),2):
        p, c = arr[i], arr[i+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p
    preOrder(N)
    print('#{} {}'.format(tc,cnt))



#유튜브선생님풀이
for tc in range(1,int(input())+1):
    E, N = map(int,input().split()) #E 간선수, 정점수 E+1
    #정점번호 1~E+1

    L = [0] *(E+2)
    R = [0] *(E+2)
    P = [0] *(E+2)

    arr = list(map(int,input().split()))
    for i in range(0,E*2,2): #arr[i]-->arr[i+1]
        p,c = arr[i], arr[i+1]
        #p의 왼쪽자식이 차있으면 오른쪽에 채우고
        if L[p]:
            R[p] =c
        #비어있다면 왼쪽에 채우자
        else:
            L[p] = c
        #부모정보는 c의 부모정보를 채우자
        P[c] = p

    ans = 0 #노드셀거야
    def traverse(v):
        global ans
        #단말노드는 왼쪽자식,오른쪽자식 0으로 저장돼있을거니까 끊으면 됨
        if v== 0:
            return
        ans += 1 , 이렇게 쓰는 경우에 함수 내의 어디에 쓰든 똑같음
        #왼쪽 자식 부름
        traverse(L[v])
        #오른쪽자식을 부름
        traverse(R[v])

    traverse(N)
    print(ans)

#retuurn value로 답을 줘보자! -> 후위순회 이용
    def traverse(v):
        #공백노드가 되면 어떻게 해줘야 될까? 밑에 아무것도 없으니 0을 리턴해줌
        if v== 0:
            return 0
        #왼쪽 자식 부름
        l = traverse(L[v])
        #오른쪽자식을 부름
        r = traverse(R[v])
        #왼쪽 오른쪽 노드수를 구해서 현재 자신v(1)도 더함
        return l + r + 1
        #아래와 같이 코드를 줄일 수 도 있음
        # return traverse(L[v]) + traverse(R[v]) + 1

#노드 선언으로도 할 수 잇음
    ans = 0
    Q = [N]
    while Q:
        v = Q.pop(0)
        if v == 0 : return
        ans += 1
        #1.
        Q.append(L[v])
        Q.append(R[v])
        #2.
        if L[v]:
            Q.append(L[v])
        if R[v]:
            Q.append(R[v])
