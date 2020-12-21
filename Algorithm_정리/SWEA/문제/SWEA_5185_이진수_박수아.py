'''
#1. 16진수를 입력받는다(문자열로)
#2. 입력받은 각 자릿수를 2진수로 변환한다!
#3. 답을 출력!
'''
import sys
sys.stdin = open('input.txt','r')

def binary(number):
    global result,idx
    if number == 0:
        return result
    result[3-idx] = str(number%2)
    number //= 2
    idx+=1
    binary(number)

alpha = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

T = int(input())
for tc in range(1,T+1):
    #16진수를 입력받음
    N,num = input().split()
    N = int(N)
    # print(N,num)
    binary_num = ''
    #16진수 각 자릿수는 2진수 4자리로 표시되니까 0000에 각 변환한 2진수를 넣음
    for n in num:
        result = ['0']*4
        idx = 0
        if n.isalpha():
            for a in alpha:
                val = alpha[n]
            binary(val)
        else:
            binary(int(n))
        binary_num += ''.join(result)
    print('#{} {}'.format(tc,binary_num))