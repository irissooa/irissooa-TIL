stack = []

stack.append(1) #push
stack.append(2)
stack.append(3)

if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())
if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())
if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())
if stack: #len(stack) != 0 이란 뜻, 비어있지 않으면 뽑아라!
    print(stack.pop())


def func2():
    print('함수 2 시작')
    print('함수 2 종료')
def func1():
    print('함수 1 시작')
    func2()
    print('함수1 종료')

print('메인시작')
func1()
print('메인끝')
