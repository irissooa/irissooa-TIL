# SWEA

## 1204. 최빈수구하기

```python
#수학 성적 점수 입력받음
#점수들의 빈도와 점수를 딕셔너리로 받는다 {점수:cnt}
#cnt가 가장 많은 것의 점수를 뽑는다 같다면 큰 수를 뽑는다

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    print(f'#{int(input())}',end = ' ')
    arr = list(map(int,input().split()))
    arr_dict = {}
    #점수:개수로 dict만들기
    for i in arr:
        if i not in arr_dict: #점수가 dict안에 없다면 key와 value설정을해라
            arr_dict[i] = 1
        else:
            arr_dict[i] += 1 #있다면 개수를 1 추가해라
    #개수가 가장 많은 것의 key를 뽑기
    max_cnt = 0 #초기값
    bin = 0 #초기 최빈점수값
    for key,value in arr_dict.items():
        if value > max_cnt: # value값이 max_cnt보다 높다면 갱신
            max_cnt = value
            bin = key
        elif value == max_cnt: # value값이 max_cnt와 같다면 더 높은 값의 키 저장
            if key > bin:
                bin = key
    print(f'{bin}')
```

- 다른코드

```python
#하영
from collections import Counter
T = int(input())
for tc in range(1, T + 1):
    i = input()
    score = list(map(int, input().split()))
    com = Counter(score).most_common(1)[0][0]
    print(f'#{i} {com}')
```

- 

```python
# 이건 딕셔너리 키 밸류 값으로 풀어볼까?
# get 함수도 써봐야겠넹
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split())) # 우선 숫자들 입력받자 1000개...
    grades = {} # 빈 딕셔너리 초기화
     
    for num in numbers: # 숫자 받은거 하나씩 돌려보자
        # .get(x, default)를 이용해 key 값이 없다면 그 value 값을 0으로 한다.
        grades[num] = grades.get(num, 0) + 1 # 그후 + 1을 해주어 새롭게 딕셔너리에 key = num 과 value = 1 로 저장한다.
     
    # lambda에 대해서는 인터넷 검색을 통해서 꼭 공부하자
    # sorted lambda 를 이용해 value를 내림차순으로 먼저 정렬하고 동일한 값이 있다면 key 값을 이용해 내림차순으로 하자.
    # 딕셔너리를 정렬하여 튜플형태로 새로운 grade_list에 넣자
    grades_list = sorted(grades.items(), key = lambda x : (-x[1], -x[0]))
     
    # 모두 내림차순으로 정렬 했으니 가장 첫번째 튜플의 첫번째 값이 최빈수가 된다.
    print(f'#{tc} {grades_list[0][0]}')
```



## 1928. Base64 Decoder

- 의수오빠 도움받고 풀었당....ㅎ

```python
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
```



- 다른코드

```python
#병훈
# 1byte = 8bit
# 문자를 3 byte 넣으면 24 bit
# 문제에서 얘기하는 Base64 Encoding은
# 3 byte의 문자를 각각 아스키코드로 변환하여 해당하는 숫자를
# 8bit의 2진수로 변환하고 이어서 24bit로 만든다.
# 이후 24 bit의 2진수를 6bit 씩 잘라 각각 해당하는 숫자를 표에서 확인하여
# 해당하는 문자로 바꿨을 때 이를 Base64 Encoding이라 한다.
# Encoding을 하면 3개의 문자가 4개로 바뀐다.
 
# 하지만 문제에서는 Decoding을 원한다. 즉 반대의 과정을 해야한다.
# 4개의 문자를 입력 받아 3개의 문자로 바꾸는 과정을 해야한다.
# 4개의 문자는 각각 decodes에 해당하는 값을 6bit로 바꾸고, 이어서 24bit로 만든다.
# 24bit를 다시 8bit로 잘라 10진수로 변환하고, 그 값을 아스키코드 변환하여 결과를 출력한다.
 
def splited_words_by4():
    #입력받은 input 문자를 4의 배수로 자른다.
    #제약사항에서  
    #문자열의 길이는 항상 4의 배수로 주어진다. 라고 명시되어 있다
    result = []
    for i in range(0,len(words),4):
        result.append(words[i:i+4])
    return result
 
 
def decoding_4words(arr):
    #4개의 배수로 자른 문자를 decoding한다.
    #decoding 한다는 것은
    #문제의 표에 나와있는 숫자로 문자를 변환한다는 것
    result = []
    for words in arr:
        tmp=[]
        for char in words:
            for i in range(64):
                if decodes[i]==char:
                    tmp.extend([i])
        result.append(tmp)
    return result
 
 
def num_to_6bits(num):
    #decoding한 숫자를 6bit로 나타낸다.
    bit_place = 5
    btis6 = [0]*6
    i=0
    while bit_place>=0:
        if num // (2 ** bit_place):
            btis6[i] = num // (2 ** bit_place)
            num -= (2 ** bit_place)
        bit_place -= 1
        i+=1
    return btis6
 
 
def bits24_to_nums(bits24):
    #6bit로 나타낸 수를 4개 이어서 24bit 변환했다. 그것을 입력으로 받아
    #24bit를 8bit로 쪼개 8bit가 나타내는 숫자 3개를 반환한다.
    bit_place = 7
    num = 0
    result = []
    for bit in bits24:
        if bit_place < 0 :
            result.append(num)
            num = 0
            bit_place = 7
        if bit==1:
            num += (bit+1)**(bit_place)
        bit_place-=1
    else:
        result.append(num)
    return result
 
 
decodes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for t in range(1,int(input())+1):
    words = input()
 
    splited =splited_words_by4()
    splited_nums_by4 = decoding_4words(splited)
 
    splited_nums_by_24bits = []
    for nums4 in splited_nums_by4:
        tmp = []
        for num in nums4:
            tmp.extend(num_to_6bits(num))
        splited_nums_by_24bits.append(tmp)
 
 
    splited_24bits_by_nums=[]
    for bits24 in splited_nums_by_24bits:
        splited_24bits_by_nums.extend(bits24_to_nums(bits24))
 
    # print를 통해 어떻게 변환되고 싶으면 밑의 print 주석 실행
 
    # print(splited)
    # print(decoding_4words(splited))
    # print(splited_nums_by_24bits)
    # print(splited_24bits_by_nums)
 
    result = ''
    for num in splited_24bits_by_nums:
        result+=chr(num)
    print(f'#{t} {result}')
```

- 

```python
#의수
'''
문제에는 Encoding 과정을 설명해놨다 우리는 이것을 꺼꾸로 해야한다. (Encoding <-> Decoding)
 
우선 Encoding 과정에 대해 설명
문자 3개를 아스키코드로 변환하고 (이건 월말평가 때도 나옴)
(아스키코드는 0 ~ 127까지 있다.즉 2진수로 바꾸면 8자리까지 표현가능 127 = 11111111, 0 = 00000000 8자리로 표현)
즉 문자 3개를 이어 붙이면 8 X 3 = 24 24자리의 2진수 표현식이 된다! 24자리의 2진수 표현식이 버퍼? 라고 한다.
여기서 24자리의 2진수 버퍼를 6개씩 다시 쪼개버린다. 그 6개씩 쪼갠 6자리의 2진수를 다시 10진수로 바꾸자
10진수로 바꾼뒤 문제에 나와있는 해당하는 값의 문자를 출력한다.
 
이것을 꺼꾸로 하면 Decoding 과정이 되는 것이다!!
1. 문자 4개를 잘라서 각 4개의 문자를 표를 보고 10진수의 값으로 보고
2. 10진수 4개를 각각 6자리의 2진수로 변환하여 이어붙여 24자리의 버퍼를 만든다.
3. 버퍼 24자리를 8개 단위로 잘르고
4. 10진수로 변환한뒤, 아스키코드로 변환하여
5. 문자를 출력한다.!!
6. 계속 반복하면 디코딩 과정 끝.
'''
 
 
def bin_maker(z):
    res = bin(z)[2:] # bin(x) 하면 0b00000형태로 앞에 2자리가 2진수를 표현하는 식으로 나오기 때문에 잘라서 없앤다
    res = '0'*(6-len(res)) + res # 6자리를 맞추기 위해 만들어 놓은 식 1000이 들어오면 001000으로 바꿔준다
    return res
 
T = int(input())
index ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' # 표의 값을 찾기위해 인덱스를 설정(문제참고)
for tc in range(1, T + 1):
    code = input()
    result = ''
    for x in range(0, len(code), 4): # 4자리씩 잘라서 확인해야 하기 때문에 4자리씩 돌린다.
        bin_str = ''
        word = code[x:x+4] # 입력받은 코드를 4자리씩 잘라서 word에 저장
        for y in range(4): # 자른 4자리 코드를 하나하나 2진수로 바꾼다.
            temp = index.find(word[y]) # 각자리의 문자를 index와 비교해서 값을 확인하여 temp에 저장
            bin_str += bin_maker(temp) # 저장된 10진수의 숫자(0~63)을 2진수로 변환하는 함수 불러와 이어 붙인다.
         
        result += chr(int(bin_str[:8], 2)) # 이어붙여진 24자리의 문자의 0~7 8개를 10진수로 바꾸고 앞에 2개는 잘라 아스키코드로 변환시킨다.
        result += chr(int(bin_str[8:16], 2)) # int('11110000', 2) 2의 위치는 2진수인거를 확인
        result += chr(int(bin_str[16:], 2)) # 확인한걸 계속 해서 이어 붙여서 반복하자.
    print(f'#{tc} {result}') 
```









