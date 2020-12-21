'''
20-12-17 11:33-13:03
카드 4장, 뽑기 36장중 5장뽑음
R,B,Y,G
점수 규칙
1. 카드 5장 모두 같은색, 숫자가 연속적, 점수는 가장 높은 숫자에 900 더함
2. 카드 5장 중 4장 숫자가 같음, 점수는 같은 숫자에 800을 더함
3. 같은 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을때, 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700더함
4. 5장의 카드 색깔이 모두 같을 댸 점수는 가장 높은 숫자에 600을 더함
5. 카드 5장의 숫자가 연속적일때 점수는 가장 높은 숫자에 500을 더함
6. 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
7.카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때
점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
8. 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다.
9.위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다.
'''
import sys
sys.stdin = open('input.txt','r')
# 같은색개수 return
def samecolor():
    return len(card)

# 숫자가 연속적인지 확인
def continuous():
    for n in range(4):
        if numbers[n] != numbers[n+1] -1:
           return False
    return True

# 같은 수 개수와 숫자
def samenum():
    ans = 0
    MAX = 0
    number = 0
    for n in range(1,10):
        ans = numbers.count(n)
        if ans > MAX:
            MAX = ans
            number = n
    return MAX,number

card = dict()
numbers = []
for _ in range(5):
    a,num = input().split()
    numbers.append(int(num))
    if a not in card:
        card[a] = [int(num)]
    else:
        card[a].append(int(num))
# print(card)
numbers.sort()
result = 0
if continuous():
    # 카드 5장 같은색
    if samecolor() == 1:
        ans = max(numbers)+900
    # 연속적이기만할때
    else:
        ans = max(numbers) + 500
    if result < ans:
        result = ans
if samecolor()==1:
    ans = max(numbers)+600
    if result < ans:
        result = ans
same,samenumber=samenum()
# print(same,samenumber)
if same == 4:
    ans = samenumber + 800
elif same == 3:
    # 나머지2장도 같을때
    check =0
    for n in numbers:
        if n != samenumber and not check:
            check = n
        elif check == n:
            ans = samenumber*10 + check+700
            break
    else:
        ans = samenumber+400
elif same == 2:
    # 또다른 2장이 같을 때
    check,checknum = 0,''
    for n in numbers:
        if n != samenumber and not check:
            checknum = n
            check += 1
        elif n != samenumber and check == 1:
            if checknum == n:
                ans = max(samenumber,checknum)*10 + min(samenumber,checknum) +300
                break
            else:
                checknum = n
    else:
        ans = samenumber + 200
    if result < ans:
        result = ans
else:
    ans = max(numbers) + 100
if result < ans:
    result = ans
print(result)
