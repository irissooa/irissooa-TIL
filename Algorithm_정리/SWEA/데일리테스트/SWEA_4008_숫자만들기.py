'''
연산자를 순열로 한 뒤  다 넣어봄!
이건 안됨.....ㅠ
operator에서 직접 뺴주고, 다시 넣어주고....해야됨....ㅠ
# '''
import sys
sys.stdin = open('input.txt','r')

def calc(psel):
    ans = numbers[0]
    for i in range(len(psel)):
        if psel[i] == 1:
           ans += numbers[i+1]
           # print('+',ans)
        elif psel[i] == 2:
            ans -= numbers[i+1]
            # print('-',ans)
        elif psel[i] == 3:
            ans *=numbers[i+1]
            # print('*',ans)
        elif psel[i] == 4:
            ans = int(ans/numbers[i + 1])
    # print(ans)
    return ans


# def perm(idx,check):
#     global MAX,MIN,permlist
#     if idx == len(operator):
#         temp = sel[:]
#         if temp not in permlist:
#             permlist.append(temp)
#             ans = calc(sel)
#             # print(sel,ans)
#             if ans > MAX:
#                 MAX = ans
#             if ans < MIN:
#                 MIN = ans
#         return
#     for i in range(len(operator)):
#         if (check & (1<<i)):
#             continue
#         sel[idx] = operator[i]
#         perm(idx+1,check|(1<<i))

# def perm(idx):
#     global MAX,MIN
#     if idx == N-1:
#         ans = calc(sel)
#         # print(sel,ans)
#         if ans > MAX:
#             MAX = ans
#         if ans < MIN:
#             MIN = ans
#         print(sel)
#         return
#     for i in range(idx,N-1):
#         sel[i],sel[idx] = sel[idx],sel[i]
#         perm(idx+1)
#         sel[i],sel[idx] = sel[idx],sel[i]







T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #+ - * // 개수
    operator = list(map(int,input().split()))
    print('o',operator)
    numbers = list(map(int,input().split()))
    MAX,MIN = -987654321,987654321
    sel =[0]*(N-1)
    perm(0)
    # print(MAX,MIN)
    print('#{} {}'.format(tc,MAX-MIN))