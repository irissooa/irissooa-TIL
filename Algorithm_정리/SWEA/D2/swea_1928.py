#입력받은 문자를 4개로 자름(24개씩)
#그 문자를 base24의 idx로 변환한다
#변환한 숫자를 2진수로 바꾼다 '0b/뒤의 숫자를 자르고,앞에 빈 곳은 0으로 채움
#앞에서 8개씩 자름(3문자-아스키코드는 2^8이기 때문)
#그 2진수를 숫자로 변환한다
#변환한 숫자를 아스키코드의 문자열로 바꿈

import sys
sys.stdin = open("input.txt", "r")

Base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

for tc in range(1,int(input())+1):
    STR = input()
    #입력받은 문자들을 4개씩 자름
    four = ''
    bin_base = ''
    for i in range(0,len(STR),4):
        four = STR[i:i+4]
        CODE = ''
        # print(four)
        for str in four:
            res = bin(Base64.index(str))[2:] #입력받은 문자를 2진법으로 만듦
            #6자리를 채워주기 위해 앞의 빈부분은 0으로 채움
            bin_base += '0'*(6-len(res)) + res
            # print(bin_base)
        #8개씩자르고 십진수로 변환한 뒤 chr로 아스키코드 변환
        for e in range(0,len(bin_base),8):
            CODE += chr(int(bin_base[e:e+8],2))

    print(f'#{tc} {CODE}')
