def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(': #왼쪽괄호면 push
            stack.append(arr[i])
        elif arr[i] == ')': #오른쪽괄호면 pop, 비교해야됨(두개밖에없으니안해도됨)
            #stack이 비었는지 확인
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack :return False #다 끝났는데 비어있지 않으면 false
    else: return True

def check2(arr):
    #인자로 넘어온 괄호들을 순회하면서 검사
    #여는 괄호라면 무조건 push
    #닫는 괄호라면 스택에 top위치와 비교하여 짝이면 pop
    #짝이 아니라면 False
    #끝까지 순회했을 떄 스택의 길이가 0이 아니라면 False
    stack = []

    for i in range(len(arr)):
        if arr[i] == '[' or arr[i] == '{' or arr[i] == '(': #왼쪽괄호면 push
            stack.append(arr[i])
        elif arr[i] == ']' or arr[i] == '}' or arr[i] == ')': #오른쪽괄호면 pop, 비교해야됨(두개밖에없으니안해도됨)
            #stack이 비었는지 확인
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
            if arr[i] == ')' and top == '(':
                continue
            elif arr[i] == '}' and top == '{':
                continue
            elif arr[i] == ']' and top == '[':
                continue
            return False
    if len(stack)>0:
        return False
    return True

stack = []
arr1 = '()()((()))'
arr2 = '((()((((()()((()())((())))))'
print(check(arr1))
print(check(arr2))

arr3 = '{()}{[]}'
arr4 = '([)](())'
arr5 = '(][())'
print(check2(arr3))
print(check2(arr4))
print(check2(arr5))
