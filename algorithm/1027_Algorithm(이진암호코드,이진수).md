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

