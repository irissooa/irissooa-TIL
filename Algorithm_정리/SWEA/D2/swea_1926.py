#간단한 369게임
#숫자1부터 차례대로 말하되 3,6,9가 들어있는 수는 '-(박수)'표시
#박수는 해당 들어간 숫자의 개수만큼! 36은 --(공백없이) 이렇게!

#N번까지 수를 문자로 입력 받는다
#해당 문자에 3,6,9가 들어있는지 확인한다
#들어있다면,  -를 그 개수만큼 출력한다
#-가 만약 2개이상이면 --를 공백없이 출력한다
N = int(input())
for n in range(1,N+1):
    str_n = str(n)
    cnt = 0
    for n in str_n:
        if ('3' in n) or ('6' in n) or ('9' in n):
            cnt += 1
    if cnt > 1:
        str_n = '--'
    elif cnt == 1:
        str_n = '-'
    print(str_n,end = ' ')

#병훈오빠 코드 핳......잘풀었당
for number in range(1,int(input())+1):
    count = 0
    for n  in str(number):
        if '3' == n or'6' == n or'9' == n:
            count+=1
    if count:ans = '-'*count
    else:ans = number
    print(f'{ans}',end = ' ')