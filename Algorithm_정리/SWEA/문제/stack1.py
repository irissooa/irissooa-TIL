# C style
def push(item):
    global top
    if top>100 -1:
        return
    else:
        top += 1
        stack[top] = item


def pop(): #isEmpty 인지 항상 확인해야됨!
    global top
    if top== -1:
        print('Stck is Empty!!')
        return
    else:
        result = stack[top]
        top -= 1
        return result


stack = [0] * 100 #고정(꽉차지 않고 넉넉하게 만들어야됨)
top = -1
push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())