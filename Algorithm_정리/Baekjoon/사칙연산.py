# A,B = map(int,input().split())
# print(A+B, A-B ,A*B, A//B, A%B, sep='\n')

# A,B,C = map(int, input().split())
# print((A+B)%C,((A%C) + (B%C))%C,(A*B)%C,((A%C) * (B%C))%C,sep='\n')
# A,B='472','385'
# A=input()
# B=input()
# SUM=0
# for b in B[::-1]:
#     SUM += int(A)*int(b)
#     print(SUM)
#     SUM = 0
# print(int(A)*int(B))

# A,B = map(int,input().split())
# if A>B:
#     print('>')
# elif A<B:
#     print('<')
# else:
#     print('==')

# TOTAL = int(input())
# if TOTAL >=90:
#     print('A')
# elif TOTAL >= 80:
#     print('B')
# elif TOTAL >= 70:
#     print('C')
# elif TOTAL >=60:
#     print('D')
# else:
#     print('F')

# YEAR = int(input())
# if (YEAR%4==0) and (YEAR%100!=0) or (YEAR%400==0):
#     print(1)
# else:
#     print(0)

# x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print(1)
# elif x<0 and y>0:
#     print(2)
# elif x<0 and y<0:
#     print(3)
# elif x>0 and y<0:
#     print(4)

H, M =map(int,input().split())
alarm=M-45
if alarm<0:
    H -= 1
    alarm = 60+alarm
    if H < 0:
        H = 24+H
        print(H,alarm)
    else:
        print(H,alarm)
else:
    print(H,alarm)