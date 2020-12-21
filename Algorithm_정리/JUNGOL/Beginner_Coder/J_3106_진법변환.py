'''
20-12-13 13:42-14:04
A진법의 수를 입력받아 B진법 수로 출력하는 프로그램
테스트 케이스 끝 0 주어짐
세수 A,N,B가 공백으로 주어짐
A진법 수 N을 B진법수로 변환

1. A진법의 수로 N을 10진수로 만들고, B로 나눈 나머지로 바꿈
'''
def change(num,how):
    global result
    if num == 0:
        return
    if num % how >= 10:
        result.append(chr(num%how+55))
    else:
        result.append(num%how)
    change(num//how,how)

def ten(word,how):
    ans = 0
    for w in range(len(word))[::-1]:
        if word[w].isalpha():
           ans+=(ord(word[w])-55)*how**(len(word)-1-w)
        else:
            ans += int(word[w])*how**(len(word)-1-w)
    return ans

while True:
    info = list(input().split())
    if len(info) == 1:
        break
    A,N,B = int(info[0]),info[1],int(info[2])
    if N=='0':
        print(0)
        continue
    result = []
    change(ten(N,A),B)
    print(*result[::-1],sep='')

