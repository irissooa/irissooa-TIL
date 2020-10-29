# Algorithm

[toc]

## SWEA_1240_단순2진암호코드

> [SWEA_1240_단순2진암호코드](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV15FZuqAL4CFAYD&solveclubId=AXOKmQjq9ZgDFAXS&problemBoxTitle=APS%EC%9D%91%EC%9A%A9+start+%2810%EC%9B%94+23%EC%9D%BC%2C+26%EC%9D%BC%29&problemBoxCnt=1&probBoxId=AXVUWxxa3AMDFASe)
>
> 내코드 줄일수있다..
>
> start를 찾았을 때 거기부터 56자리가 코드니까 그만큼을 바로 str로 받고 딕셔너리의 키값으로 수를 찾으면 됨!
>
> 그리고 값도 문자열이 아니라 수로 받아도 된다.

```python
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
```

- LBH's 코드

```python
code = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}
 
for t in range(1,int(input())+1):
 
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    mycode = ''
 
    for a in arr:
        secret = []
        for i in range(M-1,-1,-1):
            if a[i] == '1':
                mycode = a[i-55:i+1]
                break
 
        if mycode:
            for k in range(0,50,7):
                secret+=[code[mycode[k:k+7]]]
            break
             
    odd_sum = even_sum = 0
     
    for i in range(len(secret)-1):
        if (i+1)%2:
            odd_sum+=secret[i]
        else:
            even_sum+=secret[i]
    total = odd_sum*3 + even_sum + secret[-1]
     
    print("#{} ".format(t),end='')
    if total % 10 == 0:
        print(sum(secret))
    else:
        print(0)
```

- 현우's 코드

```python
pattern = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
  
    code = []
    for i in range(N):
        #해당 행에 1이 있냐를 찾는것!!
        if arr[i].find('1') > 0:
            xpos = arr[i][::-1].index('1')
            ypos = i
            break
  
    xpos = (M-xpos) - 56
    for i in range(8):
        code.append(pattern[arr[ypos][xpos:xpos+7]])
        xpos += 7
  
    val = (code[0] + code[2] + code[4] + code[6])*3 + code[1] + code[3] + code[5] + code[7]
    if val%10 == 0:
        print('#{} {}'.format(tc, sum(code)))
    else:
        print('#{} {}'.format(tc, 0))
```



## SWEA_5185_이진수

> [SWEA_5185_이진수](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

```python
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
```

- 선생님 코드

```python
# int 내장 함수 이용
for tc in range(1, int(input()) + 1):
    N, HEX = input().split()
    HEX = int(HEX, 16)
    HEX = format(HEX, 'b')
    if len(HEX) != int(N) * 4:
        HEX = '0' * (int(N) * 4 - len(HEX)) + HEX
    print("#{} {}".format(tc, HEX))
```

> ### format함수 기능 추가로 알게 된 것!
>
> 1. `format()` 내장 함수를 이용하면 숫자를 다른 진수의 문자열로 바꿀 때 접두어를 제외할 수 있다. https://www.daleseo.com/python-int-bases/참고
>
> ``` python
> format(42, 'b')
> '101010'
> format(42, 'o')
> '52'
> format(42, 'x')
> '2a'
> format(42, 'X')
> '2A'
> format(42, 'd')
> '42'
> ```
>
> 접두어를 포함시키는 것도 가능 : 두번째 인자 앞에 `#`만 붙여 주면 됨
>
> ```python
> format(42, '#b')
> '0b101010'
> format(42, '#o')
> '0o52'
> format(42, '#x')
> '0x2a'
> format(42, '#X')
> '0X2A'
> ```
>
> 2. 문자열도 정렬할 수 있다.
>
>  https://blockdmask.tistory.com/424 참고
>
> ```python
> # 왼쪽 정렬
> s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
> print(s9)
>  
>  
> # 오른쪽 정렬
> s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')
> print(s10)
>  
>  
> # 가운데 정렬
> s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c')
> print(s11)
> ```
>
> ![image-20201029093443433](1027_Algorithm(이진암호코드,이진수).assets/image-20201029093443433.png)
>
> **왼쪽 정렬에는 기호 <** 를 사용하고, **오른쪽 정렬에는 >**, **가운데 정렬에는 ^**를 사용
> **{0:<10}** 이 뜻하는 것은 **{0} 값**을
>
>  ":<10" 10자리로 표현할건데 왼쪽 정렬을 할 것이다. 라는 뜻 이고
> **{1:>5}** 가 뜻하는 것은 **{1} 값**을
>
>  ":>5" 5자리로 표현할건데 오른쪽 정렬을 할 것이다."
>
> 3. 문자열에 공백이 아닌 값 채우기
>
> ```python
> # 왼쪽 정렬
> s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a')
> print(s12)
>  
>  
> # 오른쪽 정렬
> s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b')
> print(s13)
>  
>  
> # 가운데 정렬
> s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'c')
> print(s14)
> ```
>
> 이렇게 <, >, ^ 기호 앞에 특정 문자를 입력하면 공백 부분이 다른것으로 채워짐
>
> ![image-20201029093707931](1027_Algorithm(이진암호코드,이진수).assets/image-20201029093707931.png)
>
> 4. 자리수와 소수점 표현하기
>
> ```python
> # 정수 N자리
> s15 = '정수 3자리 : {0:03d}, {1:03d}'.format(12345, 12)
> print(s15)
>  
>  
> # 소수점 N자리
> s16 = '아래 2자리 : {0:0.2f}, 아래 5자리 : {1:0.5f}'.format(123.1234567, 3.14)
> print(s16)
> ```
>
> **s15** : 
>
> 정수의 자리수를 표현할때는 `0Nd` 로 표현
>
> N은 원하는 자릿수를 입력
>
> 자릿수가 부족한 경우는 자동으로 0으로 채워짐
> **s16** :
>
> 소수점 자리수를 표현할때는 `0.Nf` 로 표현
>
> N은 소수점 아래 표시할 자릿수를 입력
>
> 남는 부분은 0으로 표시
>
> ![image-20201029093906513](1027_Algorithm(이진암호코드,이진수).assets/image-20201029093906513.png)







## SWEA_5186_이진수2

```python
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

```

- 선생님 코드

```python
for tc in range(1, int(input()) + 1):
    N = float(input())
    ans = ''

    while True:
        N *= 2
        ans += str(N)[0]
        if N >= 1: N -= 1
        if N == 0:
            break

        if len(ans) >= 13:
            ans = 'overflow'
            break
    print("#{} {}".format(tc, ans))
```



## SWEA_4366_정식이의은행업무

> [SWEA_4366_정식이의은행업무](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd&categoryId=AWMeRLz6kC0DFAXd&categoryType=CODE)

```python
'''
#1. while문을 돌림,입력받은 2진수, 3진수의 값이 같아지면 break
#2. 2진수, 3진수 둘다 앞은 0이되면 안됨, 그럼 2진수는 2번쨰부터, 3진수는 1,2중 자신이 아닌수부터 바꾸고 확인
#3. 그렇게 계속 자신이 아닌수로 하나씩 바꿔보고 같아지면 끝!
'''
import sys
sys.stdin = open('input.txt','r')
import copy

#2진수 3진수가 같은지 확인하는 함수
def check(numList1,numList2):
    num1 = ''.join(numList1)
    num2 = ''.join(numList2)
    # print(num1,num2)
    if int(num1,2) == int(num2,3):
        return True
    return False


T = int(input())
for tc in range(1,T+1):
    binaryNum = list(input())
    ternaryNum = list(input())
    # print(int(binaryNum,2))
    # print(int(ternaryNum,3))
    BN = copy.deepcopy(binaryNum)
    TN = copy.deepcopy(ternaryNum)
    bidx = 0
    tidx = 0
    flag = False
    while not flag:
        for b in range(bidx,len(binaryNum)):
            if BN[b] == '0':
                BN[b] = '1'
            else:
                BN[b] = '0'
            #해당 idx는 봤으니 다음으로 넘김
            bidx += 1
            #3진수 숫자바꿈
            for t in range(len(ternaryNum)):
                #해당 값은 pop되고 계속 찾을거니까 리셋
                ternaryList=['0','1','2']
                ternaryList.pop(ternaryList.index(TN[t]))
                for tt in range(2):
                    TN[t] = ternaryList[tt]
                    if check(BN,TN):
                        result = ''.join(BN)
                        print('#{} {}'.format(tc, int(result, 2)))
                        flag = True
                        break
                #만약 못찾으면 원래값으로 돌려놓음
                TN[t] = ternaryNum[t]
                if flag:
                    break
            #BN도 만약에 값을 못찾으면 원래값으로 돌려놓음
            BN[b] = binaryNum[b]
            if flag:
                break
```



- 챌's code

```python
for tc in range(1,int(input())+1):
    binary=input()
    ternary=input()
    binarylist=[]
     
    for i in range(len(binary)):
        temp=list(binary)
        temp[i]=str((int(binary[i])+1)%2)
        #print(temp)
        binarylist.append(int(''.join(temp),2))
    #print(binarylist)
     
    for i in range(len(ternary)):
        temp=list(ternary)
        for j in range(1,3):
            temp[i]=str(((int(ternary[i])+j)% 3))
            #print(temp)
            if int(''.join(temp),3) in binarylist:
                res=int(''.join(temp),3)
                print('#{} {}'.format(tc,res))
                break
```

- 현우's code

```python
T = int(input())
for tc in range(1,T+1):
    bin = input()
    bin_sz = len(bin)
    trip = input()
    trip_sz = len(trip)
    bin_cost = 0
    trip_cost = 0
    bin_pos = []
    trip_pos = []
    
    #2진수를 10진수로 바꾼 값을 담음
    md = 1
    for each in bin[::-1]:
        bin_cost += int(each)*md
        md *= 2
    #이진수 값을 하나씩 바꿀때마다 그 값이 1로바뀌면 그만큼 더해주고, 아니면 빼줌
    md = 1
    for each in bin[::-1]:
        m = 0
        if each == '0':
            m = 1
        else:
            m = -1
        bin_pos.append(bin_cost + m * md)
        md *= 2
    #print(bin_pos)
    
    #3진수를 10진수로 바꾼값을 담음
    md = 1
    for each in trip[::-1]:
        trip_cost += int(each) * md
        md *= 3
    
    #3진수 값을 하나씩 바꾸는데 그 바꿨을 때의 값들을 하나씩 다 담아줌
    md = 1
    for each in trip[::-1]:
        if each == '0':
            trip_pos.append(trip_cost + md)
            trip_pos.append(trip_cost + 2*md)
        elif each == '1':
            trip_pos.append(trip_cost - md)
            trip_pos.append(trip_cost + md)
        else:
            trip_pos.append(trip_cost - md)
            trip_pos.append(trip_cost - 2*md)
        md *= 3
    #print(trip_pos)
    #바꾼 값들 중 같은 것이 있으면 출력!
    for each in bin_pos:
        if each in trip_pos:
            print('#{} {}'.format(tc,each))
            break
```

- 선생님 코드

```python
def check(num, notation):
    change_num = int(num, notation)

    idx = len(num)-1
    for i in map(int, num):
        for j in range(notation):
            if i == j:
                continue

            tmp = change_num - i * (notation **idx) + j *(notation**idx)
            if tmp not in ans:
                ans.append(tmp)
            else:
                return tmp

        idx -= 1



for tc in range(1, int(input())+1):
    num2 = input()
    num3 = input()

    #한비트식 바꾼 10진수를 저장할 리스트
    ans = []

    check(num2, 2)
    print("#{} {}".format(tc, check(num3, 3)))
```



## SWEA_1242_암호코드스캔

> [SWEA_1242_암호코드스캔](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXOKmQjq9ZgDFAXS&contestProbId=AV15JEKKAM8CFAYD&probBoxId=AXVnfHeKGFcDFAVE&type=PROBLEM&problemBoxTitle=APS%EC%9D%91%EC%9A%A9+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4+%2810%EC%9B%94+27%EC%9D%BC%29&problemBoxCnt=2)
>
> 풀려고 했으나....코드를 추출하는거에서 실패했다...ㅠㅠㅠ

```python
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

```

- 선생님 코드

```python
pattern = {(2, 1, 1): 0,
           (2, 2, 1): 1,
           (1, 2, 2): 2,
           (4, 1, 1): 3,
           (1, 3, 2): 4,
           (2, 3, 1): 5,
           (1, 1, 4): 6,
           (3, 1, 2): 7,
           (2, 1, 3): 8,
           (1, 1, 2): 9}

hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1], '4': [0, 1, 0, 0],
            '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1], '8': [1, 0, 0, 0],
            '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
            'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}


def find():
    ans = 0
    for i in range(N):
        idx = len(arr[i]) - 1
        while idx >= 55:
            # 바로 위행의 값이 없어야 처음만나거
            if arr[i][idx] and arr[i - 1][idx] == 0:
                pwd = []
                for _ in range(8):
                    c2 = c3 = c4 = 0

                    while arr[i][idx] == 0: idx -= 1 #0 버리기
                    while arr[i][idx] == 1: c4, idx = c4 + 1, idx - 1 #1카운트
                    while arr[i][idx] == 0: c3, idx = c3 + 1, idx - 1 #0카운트
                    while arr[i][idx] == 1: c2, idx = c2 + 1, idx - 1 #1카운트

                    #가장 작은 비율로
                    MIN = min(c2,c3,c4)
                    pwd.append(pattern[(c2//MIN, c3//MIN, c4 // MIN)])
                #암호코드 검증
                b = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                a = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                if(a * 3 + b) % 10 == 0:
                    ans += a+b
            idx -= 1
    return ans


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hexTobin[tmp[j]]

    print("#{} {}".format(tc, find()))
```

- 아스키코드와 비트연산 이용 풀이

```python
pattern = {(2, 1, 1): 0,
           (2, 2, 1): 1,
           (1, 2, 2): 2,
           (4, 1, 1): 3,
           (1, 3, 2): 4,
           (2, 3, 1): 5,
           (1, 1, 4): 6,
           (3, 1, 2): 7,
           (2, 1, 3): 8,
           (1, 1, 2): 9}

A = ord('A')
nine, zero = ord('9'), ord('0')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    #ch 문자하나
    def getVal(ch):
        t = ord(ch)
        # t>nine이란 말은 알파벳이라는 소리니까 거기에 A뺀거에 10을 더함!
        val = (t-A)+10 if t > nine else t - zero
        return val

    def find():
        ans = 0
        for i in range(N):
            idx = M - 1

            while idx >= 0:
                if arr[i][idx] != '0' and arr[i-1][idx] == '0':
                    pwd = []
					L = MIN = 0
                    val , cnt = getVal(arr[i][idx]), 0

                    for k in range(8):
                        c2 = c3 = c4 = 0
                        #0을찾고
                        while (val & 1) == 0:
                            #1과 &연산을 하는건 마지막 자리의 비트 비교
                            val, cnt = val >> 1, cnt+1
                            #16진수 1숫자는 2진수 4개니까 cnt 4
                            #16진수는 4자리로 바뀌니까 만약 4번 검사했다면
                            #새로운 val을 얻어온다.
                            if cnt == 4:
                                idx, cnt = idx - 1, 0
                                val = getVal(arr[i][idx])
                        #1을찾고
                        while val & 1 :
                            val, cnt, c4 = val >> 1, cnt + 1, c4 +1
                            if cnt == 4:
                                idx , cnt = idx - 1 , 0
                                val = getVal(arr[i][idx])
                        #0을찾고
                        while (val & 1) == 0 :
                            val, cnt, c3 = val >> 1, cnt + 1, c3 +1
                            if cnt == 4:
                                idx , cnt = idx - 1 , 0
                                val = getVal(arr[i][idx])
                        #1을 찾는다.
                        while val & 1 :
                            val, cnt, c2 = val >> 1, cnt + 1, c2 +1
                            if cnt == 4:
                                idx , cnt = idx - 1 , 0
                                val = getVal(arr[i][idx])
						#해당 코드의 비율을 알기위해 처음에 min값을 구함
                        if k == 0:
                            MIN = min(c2, c3, c4)

                        pwd.append(pattern[(c2//MIN, c3//MIN, c4//MIN)])

                        b = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                        a = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                        if (a * 3 + b) % 10 == 0:
                            ans += a + b
                    idx -= 1
        return ans

    print("#{} {}".format(tc, find()))
```

