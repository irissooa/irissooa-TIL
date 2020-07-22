# Python(2020-07-21)

> 내장함수보다 기본 알고리즘을 먼저 연습하자.
>
> 알고리즘을 먼저 글로 써보기!

## 1. 데이터 & 제어문

- 리스트의 요소 

```python
#len(menus) 함수를 써도 되고, 없다고 가정했을 때 아래 코드
#menus를 쭉 보는데,
#한 메뉴씩 나올때마다  
#count+1한다. count의 초기값은 0

menus=['라면','떡볶이','김밥']
count=0
for menu in menus:
    count+=1
print(count)
# 3
```

- 중복 구하기

```python
#투표결과를 보는데, 
#메뉴이름이 김치찜이면,count+1한다.

menus=['김치찜','라면','김밥','김치찜','오징어순대','매운탕','김치찜']
count=0
for menu in menus:
    if menu=='김치찜':#중복된 숫자를 구할때는 num==5 이런식으로 바꿈
        count+=1
print(count)
#3
```

- 최댓값 구하기/최솟값구하기

```python
#sorted(numbers)[-1] #정렬한 뒤 제일 마지막
#max(numbers) #내장함수
#-------------------------------------
# 먼저 맨 처음 값을 최대값을 생각한다.
#숫자를 하나하나 살피면서 만약 기존 최대보다 큰 값이 등장하면 최대값을 갱신한다.
#숫자를 다 볼때까지 반복한다.
numbers = [5,4,11,35,436,64,896,432]
max_number= numbers[0]
for number in numbers:
    if max_number<number:#최솟값은 min_number>number:이 가정
        max_number=number
print(max_number)
#896
```

- 최댓값 등장횟수 구하기

```python
#최대값과 등장횟수를 기억하고 있어야 함
#최대값은 기존 최대값보다 더 큰 값이 나오면 갱신,이때 등장횟수도 1로 초기화
#최대값과 같은 숫자가 나오면 등장횟수를 +1
numbers = [5,4,11,35,436,64,896,432]
max_num=numbers[0]
count=0 #아직 잘 모를 때 for문 작성할 때 하나씩 생각해보고 정하면 됨
for number in numbers:
    if max_num<number:
        #print('최대값갱신:',number) #에러났는지 확인하기 위한 것
        max_num=number
        count=1
    elif max_num==number:
        #print('count갱신:',count)
        count+=1    
print(max_num,count)
```

- 원하는 영어단어 제외하기

```python
# 아래에 코드를 작성하시오.
#사용자 입력이:dsalkklfjsakldfjslkdfhaijdslifjaeald 이렇게길다
# 문자를 하나하나 보면서 p인지 확인 후
#p가 아니라면 답안에 작성

word = input(' 영어단어를 입력하세요: ')
result=''
for char in word:
    if char!='p':
        #print(char,result)
        result=result+char#다음 문자가 이전문자 뒤에 와야되기 때문에 result+char
        #print(char,result)
print(result)
```

- 단어 뒤집기

```python
#단어를 뒤집어서 작성할 때
#1. 맨 뒷문자부터 확인해서 작성
#2. 맨처음부터 확인하긴하는데, 작성을 맨 뒤부터

word = input('영어단어를 작성하시오: ')

#1. 맨 뒷문자부터 확인해서 작성
reversed_word=''
for index in range(len(word)-1,-1,-1): 
#in word를 할 경우 앞에서부터 보기 때문에 range사용
#(word제일끝index에서 0번째까지 -1스탭으로)
    char=word[index] #index로 한문자를 뽑아옴
    reversed_word+=char
print(reversed_word)

#2. 맨처음부터 확인하긴하는데, 작성을 맨 뒤부터
reversed_word=''
for char in word:
    reversed_word=char+reversed_word
print(reversed_word)
```

- 소수 판별

```python
number = int(input('number를 입력하시오.(2 ≤ number ≤ 1,000) : '))
#1.플래그 이용
#(플래그)초기값을 줌, 한번이라도 나누어떨어지면 N이 나오고 아니면 Y
is_prime='Y' #(플래그)
for i in range(2,number):
    if number % i==0:
        is_prime='N'
        break #여기서 속도면에서 더 향상시킬 수 있음
              #(이후의 쓸데없는 반복문은 돌지 않아도 됨)
print(is_prime)
```

```python
#2.for_else통해 판별
numbers = [36, 59, 41, 33, 17, 69, 85]

for number in numbers:
    for i in range(2,number):
        if number % i ==0:
            print(f'{number}는 소수가 아닙니다. {i}는 {number}의 인수입니다.')
            break
    else: 
        print(f'{number}는 소수입니다.')
```

