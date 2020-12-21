#내장함수 사용안하고
#문자열을 int형으로 전환

def atoi(line):
    num = 0
    for i in range(len(line)):
        #아스키코드로 만든 문자를 10곱해서 1의자리에 다음 숫자를 넣어야되기 때문
        num *=10
        #문자를 아스키코드로 숫자로 만들건데 아스키코드를 보면 문자가 숫자 뒤에 있기 떄문에
        #0의 아스키코드번호를 빼주면 전환가능.....
        num +=ord(line([i]))-ord('0')
    return num


def atoi(str):
    value = 0
    for i in range(len(str)):
        c = str[i]
        #0~9
        #if c>= '0' and c<='9':
        if '0' <= c <= '9': #파이썬이라 이렇게 적는거 가능
            digit = ord(c)- ord('0')
        else:
            break
        #이부분 중요
        value = vlaue *10 +digit
        #숫자로 들어온다고 확신하면
        #if필요없고 그냥 value = value *10 +ord(c)- ord('0')이렇게 적으면 끝
    return value

num = atoi('1234')
print(type(num),num)

#int형을 문자열로 전환
def itoa(num):
    line = ''
    tmp = num
    while tmp >0:
        number = tmp % 10
        #0을 아스키코드값으로 바꾼 것을 더하면 지금 숫자의 아스키코드값을 알 수 있음
        #다음값을 이전 문자 앞에 더해줘도 되고, 다 만든 뒤 아까 배운 문자 뒤집기해도딤
        line = chr(number+ord('0')) + line
        tmp //= 10
    return line
line = itoa(1234)
print(type(line),line)



#2
def itoa(num):
    x = num #몫
    y = 0 #나머지가 들어갈 변수
    arr = []
    while x: #x가 0이 아닌동안 반복문 돌림
        y = x % 10
        x = x//10 # x//=10
        arr.append(chr(y+ord('0'))) #나머지를 문자열로 넣기
    arr.reverse() #뒤집음
    str = ''.join(arr) #뒤집은걸 문자열로 바꿈
    return str

   while x: #x가 0이 아닌동안 반복문 돌림
        y = x % 10
        x = x//10 # x//=10
        # arr.append(chr(y+ord('0'))) #나머지를 문자열로 넣기
        arr.append(y)
    arr.reverse() #뒤집음
    # str = ''.join(arr) #뒤집은걸 문자열로 바꿈
    return arr
x = 123
print(x,type(x))
str = itoa(x)
print(str,type(str))