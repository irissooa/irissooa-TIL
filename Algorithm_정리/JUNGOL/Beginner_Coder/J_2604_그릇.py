'''
20-12-14 18:10-18:25
( 이건 그릇이 바닥에 바로 놓인 모양 ) 는 거꾸로 놓인 모양
( 이거하나당 10cm, ((는 +5cm해서 15cm ()는 +10해서 20cm

1. 그릇을 입력받아 앞에서 부터 읽음
2. 제일 처음 것을 pop해서 모양을 기억하고, ans+=10을 한다
3. 그다음부터 pop하면서 모양이 다르면 +10, 같으면 +5를 한 뒤, 처음값을 다음값으로 바꿔주고 그 다음  값을 pop 반복
'''
bowls = list(input())
# bowls = list('()()()))(')
b = bowls.pop(0)
ans = 10
while bowls:
    next = bowls.pop(0)
    if next == b:
        ans += 5
    else:
        ans += 10
    b = next
print(ans)