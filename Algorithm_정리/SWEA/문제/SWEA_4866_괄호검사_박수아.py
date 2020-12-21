#괄호가 짝을 제대로 이루고 있는지 검사
#입력은 한줄의 파이썬 코드일 수 있고, 괄호만 주어질 수 있음
#정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력
#이거도 스택으로
#어제 한거니까 한번 내가 해보자!!!!
#짝을 이뤘는지 봐야되니까 일단 여는 괄호일때 스택에 넣기
#닫는 괄호일때 비교하고 같은 괄호유형이면 pop
#남은 stack이 있다면 짝을 이루지 못했으니 0, 없으면 1
import sys
sys.stdin = open('input.txt','r')
def check(code):
    top =''
    stack = []
    for i in range(len(code)):
        # print(code[i])
        if code[i] == '(' or code[i] == '{':
            stack.append(code[i])
            # print('{}을 추가했습니다'.format(stack))
        elif code[i] == ')' or code[i] == '}':
            #닫는괄호가 나왔는데 만약에 stack이 비었다면 짝이 안맞으니 0반환
            if len(stack) == 0:
                return 0
            #stack에 뭔가가 들어있다면 그건 어떤 형태이든 여는괄호!
            #그중 stack[-1]값을 top에 할당
            else:
                top = stack.pop()
                # print('{}을 제거했습니다'.format(stack))
            #짝이 맞는지 확인!
            if code[i] == ')' and top == '(':
                continue
            elif code[i] == '}' and top == '{':
                continue
            return 0
    #검사 다끝났는데 stack에 뭔가가 남아있다면 그건 짝이 안맞는것
    if len(stack) > 0:
        return 0
    #짝맞춤!
    return 1


T = int(input())
for tc in range(1,T+1):
    code = input()
    print('#{} {}'.format(tc,check(code)))




#선생님풀이
for tc in range(1, int(input())+1):
    arr = input()
    S = [] #스택
    ans = 1
    #한문자씩 읽어서 처리
    for ch in arr:
        #여는 괄호 push
        if ch == '(' or ch == '{':
            S.append(ch)
        #닫는 괄호
        if ch == ')' or ch == '}':
            #빈 스택일 경우
        if len(S) == 0:
            break
        #1.방법
        t = S.pop() #여기서 비교해도됨
        #ch와 S[-1]비교해서 다르다 (짝이 같은지 안같은지 비교)
        if (ch == ')' and t != '(') or (ch == '}' and t != '{'):
            break
        #2.방법
        # if (ch == ')' and S[-1] != '(') or (ch == '}' and S[-1] != '{'):
        #     ans = 0
        #     break
        # t = S.pop() #여기 왔다는건 정상적인 경우
            #같다면 스택에서 제거
        #괄호문자가 아닌 경우

    #빈스택인지 조사 ->남아있다면 잘못된것
    if len(S) == 0:
        ans = 0
    print(ans)

#딕셔너리 만드는 방법
paren = {'(':')','{':'}',')':'(','}':'{'} #딕셔너리 만들어 사용
for tc in range(1, int(input())+1):
    arr = input()
    S = [] #스택
    ans = 1
    #한문자씩 읽어서 처리
    if ch not in paren:continue
    for ch in arr:
        #여는 괄호 push
        if ch == '(' or ch == '{':
            S.append(ch)
        #닫는 괄호
        if ch == ')' or ch == '}':
            #빈 스택일 경우
        if len(S) == 0:
            break
        #1.방법
        t = S.pop() #여기서 비교해도됨
        if paren[ch] != t:
            ans = 0
            break
    #빈스택인지 조사 ->남아있다면 잘못된것
    if len(S) == 0:
        ans = 0
    print(ans)
