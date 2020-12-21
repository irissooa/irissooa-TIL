stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0: #항상 스택이 비어있는지 확인! 이게 isEmpty임
        print('Stack is empty!!')
    else:
        return stack.pop()

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())
print(pop())