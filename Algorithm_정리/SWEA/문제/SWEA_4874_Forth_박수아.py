'''
Forth코드 연산 결과를 출력하라, 불가능한 경우 error를 출력
숫자는 스택에 넣고
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣음
'.'은 코드 마지막이란 뜻, 스택에서 숫자를 꺼내 출력
'''
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    forth = list(input().split())
    stack = []
    #숫자면 스택에 넣음, 연산자면 스택의 숫자를 두개꺼내 계산하고 결과를 다시 스택에 넣음
    for f in forth:
        #isdigit은 문자인애가 숫자인지 판별함
        if f.isdigit():
            stack.append(int(f))
        else:
            if len(stack) >= 2:
                A = stack.pop() #제일 마지막 숫자뺌
                B = stack.pop() #그다음 숫자 뺌
                if f == '+':
                    total = B+A
                    stack.append(total)
                elif f == '*':
                    total = B*A
                    stack.append(total)
                elif f == '/':
                    total = B//A
                    stack.append(total)
                elif f == '-':
                    total = B-A
                    stack.append(total)
                else:
                    result = 'error'
            elif f == '.':
                if len(stack) == 1:
                    result = stack[0]
                else:
                    result = 'error'
            else:
                result = 'error'
                break
    print('#{} {}'.format(tc,result))



