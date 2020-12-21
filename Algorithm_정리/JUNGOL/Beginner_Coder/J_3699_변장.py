'''
20-12-16 11:20
이전과 같은 조합의 의상을 입고 밖을 나가지 않는다
정올이가 가진 의상 정보  입력 받음
정올이가 적어도 하나 이상의 의상을 갖춘 상태로 밖을 나갈수 잇는 날 며칠?

3
mask face
sunglasses face
makeup face
30
a a
b b
c c
d d
e e
f f
g g
h h
i i
j j
k k
l l
m m
n n
o o
p p
q q
r r
s s
t t
u u
v v
w w
x x
y y
z z
ab ab
bb bb
cb cb
db db
'''
def pec(n,ans):
    if n == 1:
        return ans
    pec(n-1,ans*n)

T = int(input())
for tc in range(1,T+1):
    #의상수
    N = int(input())
    temp = [input().split() for _ in range(N)]
    clothes = dict()
    for t in temp:
        if t[1] in clothes:
            clothes[t[1]].append(t[0])
        else:
            clothes[t[1]] = [t[0]]
    # print(clothes)
    ans = 1
    temp = pec(len(clothes),1)
    bin = pec(30,1)
    # ans = temp//bin
    print(ans)
    print(temp,bin)
    # for c in clothes:
    #     if len(clothes) ==1:
    #         ans-=1
    #     ans += len(clothes[c])
    # print(ans)