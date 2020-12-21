A,B = map(int,input().split())
#가위1 바위2 보3
# 가위 바위 => 바위 #가위 보=>가위 #바위 보=>보
if abs(A-B) == 1:
    if A > B:
        print('A')
    else:
        print('B')
else :
    if A > B:
        print('B')
    else:
        print('A')