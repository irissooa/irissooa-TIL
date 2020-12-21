'''
#1.주어진 N을 *2했을때 그 값의 1의 자리가 2진수!!!
#2. 만약 13자리이상 넘어간다면 overflow
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    #실수로 받음
    N = float(input())
    binary = ''
    while True:
        #종료조건
        if N <= 0:
            break
        if len(binary) >=13:
            binary='overflow'
            break
        #1.주어진 N을 *2했을때 그 값의 1의 자리가 2진수!!!
        result = N*2
        if result >= 1:
            binary += '1'
            N = result - 1
        else:
            binary += '0'
            N = result
    print('#{} {}'.format(tc,binary))
