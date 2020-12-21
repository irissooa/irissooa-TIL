'''
후위 표기식으로 바꾸어 계산하는 프로그램 작성
문자열로 된 계산식을 후위 표기식으로 바꿈
연산자는 +,* 두 종류
문자열 중간에 괄호가 들어갈 수 있음
괄호는 항상 옳은 경우만 주어짐
피연산자는 0~9의 정수만 주어짐

1. 여는 괄호는 무조건 스택에 push
2. A는 피연산자이므로 출력
3. 연산자 우선순위를 비교, 여는 괄호의 우선 순위가 작으므로 +는 push
4. B는 피연산자이므로 출력
5. 닫는 괄호가 나왔음, 여는 괄호가 나올 때 까지 pop을 하고 출력(괄호 제외)
6. 스택이 비었으므로 연산자를 push함
7. 여는 괄호는 무조건 push
8. C는 피연산자, 출력
9. 연산자 우선순위를 비교, 여는 괄호의 우선순위가 작음, +는 push
10. D는 피연산자, 출력
11. 닫는 괄호가 나왔음, 여는 괄호가 나올 때까지 pop, 출력
12. 수식이 끝남, 스택에 있는 연산자들을 모두 pop하고 출력

1. 피연산자면 스택에 push함
2. 연산자를 만나면 pop을 두 번하고 각각 값을 저장한 후, 연산자에 맞는 계산을 함
3. 계산을 한 뒤, 결과 값은 다시 스택에 넣음, 과정을 수식이 끝날 때 까지 반복함
4. 수식이 끝났다면 스택에 마지막 남은 값이 결과 값이 됨
'''
import sys
sys.stdin = open('input.txt','r')
#
# for tc in range(1,11):
#     T = int(input())
#     temp = input()
#     stack = []
#     result = []
#     for t in temp:
#         #여는괄호라면 무조건 stack에 push
#         if t =='(':
#             stack.append(t)
#         elif t.isdigit():
#             result.append(t)
#         else:
#             #스택이 비어있으면 연산자를 push함
#             if len(stack) == 0:
#                 stack.append(i)
#             else:
#                 if t == '+':
#                     #스택에 여는 괄호 나오면 stack에 저장
#                     if stack[-1] == '(':
#                         stack.append(t)
#                     #스택에 같은 연산자가 있다면 스택에 있는 연산자를 pop출력한 후 현재 연산자를 push, 스택 pop하지 않음
#                     else: #둘다 아니면 스택에 push
#                         result.append(stack.pop())
#                         stack.append(t)
#                 elif t == '+':
#                     if stack[-1] == '+':
#                         result.append(stack.pop())
#                         stack.append(t)
#                     #곱하기가 이미 스택에 들어있거나 더하기가 안들어있으면 쌓을 수 있음
#                     else:
#                         stack.append(t)
#                 #스택에서 여는 괄호를 만날떄까지 pop해서 result에 넣음
#                 elif t == ')':
#                     #뒤에서 부터 봐야됨
#                     for j in stack[::-1]:
#                         if j != '(':
#                             result.append(j)
#     # print(result)
#     result_stack = []
#     for r in result:
#         #피연산자면 스택에 push
#         if r.isdigit():
#             result_stack.append(r)
#         #연산자를 만나면 pop을 두번해줌 연산자에 맞게 계산함
#         elif len(result_stack) > 1:
#             if r == '*':
#                 A = int(result_stack.pop())
#                 B = int(result_stack.pop())
#                 ans = B*A
#                 result_stack.append(ans)
#
#             else:
#                 A = int(result_stack.pop())
#                 B = int(result_stack.pop())
#                 ans = B+A
#                 result_stack.append(ans)
#     print('#{} {}'.format(tc,result_stack[0]))
#
# #다른사람 코드
# for tc in range(1,11):
#     N = int(input())
#     Data = input()
#     stack = []
#     num_lst = []
#      #우선순위를 미리 정해둠
#     icp = {'*':2, '+':1, '(':3} #넣을때
#     isp = {'*':2, '+':1, '(':0} #스택안
#
#     #Step 1: 중위 => 후위 표기법 변경
#     for i in range(N):
#         #피연산자인 경우: 숫자 리스트에 추가
#         if Data[i].isdigit():
#             num_lst.append(Data[i])
#
#         #연산자인 경우
#         else:
#             #stack이 빈 경우 => 무조건 append(여는 괄호의 case)
#             if not stack:
#                 stack.append(Data[i])
#                 continue
#
#             #stack이 비지 않은 경우
#             elif stack:
#                 #닫는 괄호인 경우, 여는 괄호가 나올 때 까지 pop
#                 if Data[i] == ')':
#                    while stack[-1] != '(':
#                        num_lst.append(stack.pop())
#                    stack.pop()
#
#                 #icp & isp 비교 해서 우선순위가 크면 append
#                 elif icp[Data[i]] > isp[stack[-1]]:
#                     stack.append(Data[i])
#
#                 else:
#                     #icp가 isp 보다 작으면 계속 pop & 연산자 리스트에 append
#                     while icp[Data[i]] <= isp[stack[-1]]:
#                         num_lst.append(stack.pop())
#                     stack.append(Data[i])
#
#     #print(num_lst)
#
#     #step 2: 계산
#     for i in range(len(num_lst)):
#         if num_lst[i].isdigit():
#             stack.append(num_lst[i])
#
#         else: #두개의 숫자를 pop
#             num2 = int(stack.pop())
#             num1 = int(stack.pop())
#             #+가 들어오면 더하고 *가 들어오면 곱해라
#             if num_lst[i] == "+":
#                 result = num1 + num2
#             elif num_lst[i] == "*":
#                 result = num1 * num2
#
#             stack.append(str(result))
#
#     print(f'#{tc} {stack[0]}') #결과값 출력
#

#선생님 풀이
priority = {'*':2,'/':2,'+':1,'-':1,'(':0}

for tc in range(1,11):
    input()
    line = input()
    ans = ''
    #스택준비
    stack = []

    for i in range(len(line)):
        #괄호라면
        if line[i]=='(' or line[i]==')':
            #여는 괄호는 우선순위가 제일 높으므로 무조건 삽입
            if line[i]=='(':
                stack.append(line[i])
            else:
                #여는괄호가 나올때까지 무조건 pop
                while stack[-1] != '(':
                    ans += stack.pop()
                #여는 괄호하나 버리기
                stack.pop()
        elif line[i].isdigit():
            ans += line[i]
        #연산자일떼
        else:
            if len(stack)==0:
                stack.append(line[i])
            else:
                #연산자 우선순위를 비교해서
                #스택에 탑에 있는 연산자가 현재 토큰의 우선순위보다 높거나 같다면
                while priority[stack[-1]] >= priority[line[i]]:
                    ans += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(line[i])
    #남아있는 스택 비우기
    while len(stack) > 0:
        ans += stack.pop()
###################### 중위표기식->후위표기식으로 바꿨다

    for i in ans:
        if i.isdigit():
            stack.append(int(i))
        #연산자이면 꺼내서 연산 후 다시 삽입
        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+':
                stack.append(A+B)
            elif i == '-':
                stack.append(A-B)
            elif i == '*':
                stack.append(A*B)
            elif i == '/':
                stack.append(A/B)
    print('#{} {}'.format(tc,stack.pop()))