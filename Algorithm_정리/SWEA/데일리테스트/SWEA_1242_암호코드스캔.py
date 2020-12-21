'''
#1. 입력받은 list를 앞에서부터 읽는데(16진수 0부터시작안함)0이 아닌 것이 나오면 거기부터 0이 나올때까지 자르고 표시,
그 표시 이후에도 0이 아닌수가 있는지 확인!(암호코드가 1개이상 있을수 있어서)
#2. 추출한 16진수를 2진수로 변환
#3. 그 길이가 56의 몇배인지 확인(비율을 봐야되니까)한 뒤, 그 배수만큼  gop값을 바꿔주고 키를 변경한 뒤 수로 변환
#4. 수로 변환된 코드를 리스트에 담고, 그 리스트의 홀수자리합*3+짝수자리합 +마지막자리가 10의 배수인지 확인하고, 코드 출력
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

gop = 1
#비율에 따라 달라질 키....값....ㅎ...ㅎ...ㅎ..ㅎ..ㅎ...ㅠ
code = {
    ('000'*gop+'11'*gop+'0'*gop+'1'*gop):0,
    ('00'*gop+'11'*gop+'00'*gop+'1'*gop):1,
    ('00'*gop+'1'*gop+'00'*gop+'11'*gop):2,
    ('0'*gop+'1111'*gop+'0'*gop+'1'*gop):3,
    ('0'*gop+'1'*gop+'000'*gop+'11'*gop):4,
    ('0'*gop+'11'*gop+'000'*gop+'1'*gop):5,
    ('0'*gop+'1'*gop+'0'*gop+'1111'*gop):6,
    ('0'*gop+'111'*gop+'0'*gop+'11'*gop):7,
    ('0'*gop+'11'*gop+'0'*gop+'111'*gop):8,
    ('000'*gop+'1'*gop+'0'*gop+'11'*gop):9}
print(code)
alpha = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

T = int(input())
for tc in range(1,2):
    #배열 세로크기 N, 가로의 크기M
    N,M = map(int,input().split())
    codeList = []
#1. 입력받은 list를 앞에서부터 읽는데(16진수 0부터시작안함)0이 아닌 것이 나오면 거기부터 0이 나올때까지 자르고 표시,
# 그 표시 이후에도 0이 아닌수가 있는지 확인!(암호코드가 1개이상 있을수 있어서)
    for n in range(N):
        codeList.append(list(input()))
    # print(codeList)
    start = []
    for i in range(N):
        #해당 행이 전부 0이면 건너뜀!
        if codeList[i].count('0') == M:
            # print(i)
            continue
        #0말고 다른게 있다면 살펴봄!
        for j in range(M):
            if codeList[i][j]!=0:
                start.append((i,j))
                break


    #16진수를 2진수로 바꾸고 암호코드로 바꿔보쟈!!!
    # B = ''
    # for t in temp:
    #     idx = 0
    #     result = ['0'] * 4
    #     if t.isalpha():
    #         for a in alpha:
    #             val = alpha[t]
    #         binary(val)
    #     else:
    #         binary(int(t))
    #     B += ''.join(result)
    #
    # # B를 알맹이만 남기고 앞뒤로 0을 잘라준 뒤, 뒤에서부터 읽는데
    # B = B.strip('0')
    # # B의 길이가 56의 배수가 될때까지 앞에 0을 붙여줌!
    # cnt = 1
    # while len(B) % 56:
    #     B = '0' * 1 + B
    #     cnt += 1
    # print(len(B), B)
    #
    # gop = len(B) // 56
    # codeNum = []
    # # 뒤에서부터 잘라야됨!!
    # for b in range(len(B) - 1, -1, -(7 * gop)):
    #     ans = code[B[(b - (6 * gop)):(b + 1)]]
    #     # print(B[(b - (6 * gop)):(b + 1)])
    #     codeNum.append(ans)
    # print(codeNum[::-1])
