'''
1. code 배열을 열을 뒤부터 읽어오면서 1이 나오면 그때부터 7개씩 list에 담아줌(그 행만담으면됨)
2.그 codelist를 다시 뒤집어 처음부터 읽어오면서 수로 변환(str로 변환한다)
3. 변환한 code를 홀수자리 합*3+짝수자리합(마지막자리제외) +마지막자리를 했을 때 10의 배수이면 암호코드 출력
아니라면 0 출력
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    #세로크기 N 배열의 가로크기 M
    N,M = map(int,input().split())
    code = []
    for i in range(N):
        code.append(list(input()))
    codeNum=[]
# 1. code 배열을 열을 뒤부터 읽어오면서 1이 나오면 그때부터 7개씩 list에 담아줌(그 행만담으면됨)
    start = -1
    # print(code)
    for i in range(N):
        for j in range(M)[::-1]:
            if code[i][j] == '1':
                start = j
                # print('start',start,i,j)
                break
        if start >= 0:
            for s in range(start-55,start+1,7):
                # print(s)
                codeNum += code[i][s:s+7]
            break
    # print(''.join(codeNum))
# 2.그 codeNum를 처음부터 읽어오면서 수로 변환(str로 변환한다)
    trans = {
        '0001101':'0',
        '0011001':'1',
        '0010011':'2',
        '0111101':'3',
        '0100011':'4',
        '0110001':'5',
        '0101111':'6',
        '0111011':'7',
        '0110111':'8',
        '0001011':'9'}
    real_code=''
    for n in range(0,len(codeNum),7):
        for t in trans:
            num = ''.join(codeNum[n:n+7])
            if num == t:
               real_code += trans[t]
    # print(real_code)
# 3. 변환한 code를 홀수자리 합*3+짝수자리합(마지막자리제외) +마지막자리를 했을 때 10의 배수이면
    oSum,eSum=0,0
    #마지막자리 제외
    for c in range(1,len(real_code)):
        #홀수자리
        if c % 2:
            oSum += int(real_code[c-1])
            # print('o',oSum)
        #짝수자리
        else:
            eSum += int(real_code[c-1])
            # print('e',eSum)
    SUM = oSum*3 + eSum + int(real_code[7])


    #10의배수라면 암호코드 출력 아니라면 0 출력
    if SUM % 10:
        print('#{} 0'.format(tc))
    else:
        result = 0
        for r in range(8):
            result += int(real_code[r])
        print('#{} {}'.format(tc,result))


