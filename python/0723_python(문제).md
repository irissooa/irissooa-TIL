# Python(2020-07-23)

> 함수 
>
> **문제를 풀 때 막히면 다른 문제 풀거나 답을 보고, 이해한 뒤 다시 풀거나 다른 유사 문제 풀기
>
> 효율성 높이기.

## 1. 복소수 문제

- 복소수이면 그 값의 벡터 길이,  정수나 실수이면 음수 양수에 따라 부호 표시

``` python
def my_abs(x):  
    if type(x)==complex: #isinstance(x,complex)이렇게 해도됨(google영어로 검색)
        return (x.real**2+x.imag**2)**(1/2) #x의 real 실수부 , imag 허수부
    else :
        if x<0:
            return -x
        elif x==0:
            return 0 #x**2해도 무방 0일때 부호없이 하기 위해
        
        return x #이렇게나 else적고  밑에 return x 해도 똑같다.
 
```

- 오답정리
- 오답1안

```python
#1안
def my_abs(x):
     a=0 
     b=0 #여기에 b=0j로 고치면 괜찮을까..
     x=a+bj #->오류
     if b==0:
         if type(x)==int:
             return abs(x)
         else:
             return abs(x)
     else:
         return (a**2+b**2)**0.5
#NameError: name 'bj' is not defined-> 왜? 복소수 표현 ex)3+4j(공백없이)
```

- `bj` 를 변수로 인식해 정의되지 않았다고 오류뜸
- 오답2안

```python
#2안
def my_abs(x):
    x=a+bj #->오류
    a=0 
    b=0
    if b==0:
        if type(x)==int:
            return abs(x)
        else:
            return abs(x)
    else:
        return (a**2+b**2)**0.5
#UnboundLocalError: local variable 'a' referenced before assignment
```

- Why?  범위 내에서 변수에 할당을 할때 변수는 자동적으로 파이썬에 의해서 그 범위에서의 `로컬 변수`로 간주됨->컴파일러가 로컬변수로 인지->`UnboundLocalError` 가 발생

- `x=a+bj`밑에 `a=0`을 적었기 때문에 오류가 난 것 같음

-  `x의 real 실수부 , imag 허수부`를 몰라서 못 풀었다...

  

## 2. all() ,any()

- `all()`의 인자로 받는 iterabld(range,list)의 모든 요소가 참이거나 비어있으면 True

```python
def my_all(elements):
    result=True #초기값 설정 하나라도 나오면 True이기 때문
    for element in elements:
        if bool(element) ==False:
        # if not bool(element): 이렇게 써도 됨 이렇게 적으면 False일때 들어감
        #if not element: element가 False일때 라는 뜻 이렇게 줄여 쓸수도 있음
            result=False
            break
    return result

#위와 같은 코드지만 코드 길이를 이렇게 최대한 줄여 쓸수도 있음
def my_all(elements):
    for element in elements:
        if not element:
            return False
    return True
```

- 오답노트
- 이건 초기 설정부터 잘못함.. `*args`가 아니라 `elements(리스트)`

```python
def my_all(*args):

    if all(args)==True:
        return True
    elif :
        return True
    else:
        return False
```

- `any()`는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환

```python
def my_any(elements):
    result=False
    for element in elements:
        #bool(element)==True 이 과정이 숨겨져있음
        if element: #하나라도 참이면
            result =True
            break
    return result
         
#위와 같은 코드지만 코드 길이를 이렇게 최대한 줄여 쓸수도 있음
def my_all(elements):
    for element in elements:
        if not element:
            return False
    return True
```



## 3. 달팽이

```python
#하루가 시작되면
#달팽이가 낮시간동안 기둥을 올라감
#만약에 기둥을 다 오르면 count 리턴
#만약에 다 오르지 못하면
#밤에 잠을 자면서 어느정도 거리만큼 미끄러짐(낮 시간 동안 올라간 거리보다는 적게)

def snail(height, day, night):
#범위가 정해져있지 않았기 때문에 while 사용
    count=0 # 초기화
    while True: #true를 하고 밑에 조건식을 적어도 되고, True자리에 height<=0을 넣어도 됨
        count+=1
        height-=day
        if height<=0:
            return count #return을 쓰면 break안써도 됨
        height+=night

#snail_height=0 #이런식으로 변수를 또 작성해도 되고,기존의 height에 조건을 걸어도됨        
def snail(height, day, night):
    count=0
    snail_height=0
    while True:
        count+=1
        snail_height+=day
        if snail_height >=height:
            return count
        snail_height-=night
```



## 4. 자릿수 더하기

- 접근법1

```python
#문자로 바꿔서 
#하나하나씩 다시 숫자로 바꿔서 더하기
def sum_of_digit(number):
    number_str = str(number)
    total=0
    for digit in number_str:
        total+=int(digit)
    return total
```

- 접근법2->재귀함수로도 바꿀 수 있음(도전해보기.....)

```python
#접근법2
#숫자의 특성 이용하기
#끝에서부터 추출하기
#1234%10=>4
#1234//10=>123
#123%10=>3
#123//10=>12
#12%10=>2
#12//10=>!
#1%10=>!
#1//10=>0 반복문 종료

def sum_of_digit(number):
    total=0
    while True:
        remainder=number%10
        total+=remainder
        number= number//10 #위의 number가 몫으로 써야되기 때문
        if number==0:
            return total
        
```

- 재귀함수

```python
#sod(4321)=>1+sod(432)=>1+2+sod(43)=>1+2+3+sod(4)=>1+2+3+4

def sum_of_digit(number):
    
    if number<10: #마지막 남은 number가 1의 자리가 될 경우 이값을 바로 리턴함
        return number
    else:#else안적어도 되지만 보기 좋게 하려고 적음
        remainder=number%10 #1분리
        number=number//10 #1을뺀 나머지 432
        return remainder+ sum_of_digit(number) #1과 sum_of_digit(432)의 반복
```

- 오답

```python
#number에서 10을 나눈 나머지->1의자리 
#그 number에서 또 10을 나눈 나머지->10의 자리 
#계속 반복 나머지가 0이하면 멈춤
def sum_of_digit(number):
    total=0
    while number%10: 
        if number//10<=0:
            break
        else:
            total+=number%10
            continue
    return total

KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-20-6d366ffb58af> in <module>
      1 # 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
----> 2 print(sum_of_digit(1234))
      3 print(sum_of_digit(4321))

<ipython-input-19-46a511ea7f1b> in sum_of_digit(number)
     16             break
     17         else:
---> 18             total+=number%10
     19             continue
     20     return total

KeyboardInterrupt: 
```

-  while을 사용했는데, 생각처럼 안됨 => 식이 부족했다.. 나머지 추출한 뒤 number의 몫을 다음 number로 해야됨



## 5. 함수 분리

- 디버그 과정에서 유용하게 잘 쓰임
- 함수를 부분별로 나누어서 사용, 오류가 났을 시 해당 부분만 고치면 됨

```python
#선생님
def get_secret_number(word):
    number=0#초기화
    for char in word :
        number+=ord(char)
    return number
print(get_secret_number('tom'))

#선생님1안
def get_strong_word(word1,word2):
    number1=0
    number2=0
    for char in word1:
        number1+=ord(char)
    
    for char in word2:
        number2+=ord(char)
        
    #조건표현식
    return word1 if number1>=number2 else word2 

#선생님 2안 함수 분리!
#이미 위에 만든 함수 사용
#이렇게 역할을 분배해서 함수를 분리시키면 좋음
#풀이가 제대로 되지 않을 때 어느 함수가 잘못됐는지, 그거만 고치면 됨
def get_strong_word(word1,word2):
    return word1 if get_secret_number(word1)>=get_secret_number(word2) else word2


```





