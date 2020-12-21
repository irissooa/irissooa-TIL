#문자열 s에서 반복된 문자들 지움
#지워진 부분은 다시 앞뒤를 연결
#만약 연결했는데 또 반복문자가 생기면 이부분 다시 지움
#반복문자를 지운 후 남은 문자열의 길이 출력
#남은 문자열이 없으면 0 출력

#문자열을 입력받는다
#앞에서부터 두개씩 보면서 반복된 문자가 있는지 찾는다
#반복된다면 그 두 문자를 지우고 이어 붙인다
#이어붙인 뒤 다시 두개씩 보면서 찾는다
#이 과정 반복 함수로 만들어야 되지 않을까?
#끝난 뒤 최종 문자열 길이

#근데 반복된애를 지우면..idx가 그만큼 줄어듬...이걸 어떻게 고치지?!
#재귀..? 문자도 재귀가 되나.............아냐 하영이가 스택이래
#스택으로 풀어보쟈
#어제 본거 참고함...ㅠ나중엔 혼자 풀수 있길........ㅠㅠㅠ
#check 함수를 만들건데
#만약 STR을 둘러보면서 문자를 담고 다음에 들어오는 문자랑 같은지 확인하고
#같다면 pop, 반복..
import sys
sys.stdin = open('input.txt','r')
STR = []
# def check(STR):
#     S = len(STR)
#     for i in range(S): #STR idx가 나가지 않게 S-1까지 해줌
#         if STR[i] == STR[i+1]:
#             STR[i] = STR.pop(i)
#             print(STR)
#             STR[i+1] = STR.pop(i+1) #지워줌
#             print(STR)
#     else:
#         return S

#넘 오래 못풀어서...결국 구글링...찾아보고..이해함..........후
def check(STR):
    stack = []
    N = len(STR)
    for i in range(N):
        #stack이 비었거나, 스택의 마지막 값이 데이터 내 값과 같지 않은 경우
        #=> stack에 저장(append)
        if not stack or stack[-1] != STR[i]:
            stack.append(STR[i])
        #stack에 값이 있고, 스택의 마지막 값과 데이터 내 값과 같은 경우
        #=> stack에서 제거(pop)
        elif stack and stack[-1] == STR[i]:
            stack.pop()
    return len(stack)

T = int(input())
for tc in range(1,T+1):
    STR = list(input())
    print('#{} {}'.format(tc,check(STR)))


#선생님 풀이
for tc in range(1,int(input)+1):
    arr = input()
    S = []

    for ch in arr:
        #빈스택인경우
        if not S:
            S.append(ch)
        #ch와 S[-1] 비교해서 다르면 push
        elif ch != S[-1]:
            S.append(ch)
        # if와 elif하는 일이 같네?
        # if not S or ch != S[-1]: #or은 앞에 것이 True라면 뒤에 안봄, 앞이 False면 뒤엘 봄, 근데 굳이 이런거하다가 실수할 수 있음!
        #     S.append(ch)
        #같으면 ch와 S[-1] 버림
        else:
            S.pop()
    print(len(S))