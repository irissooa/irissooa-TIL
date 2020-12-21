A=int(input())
B = int(input())
C = int(input())

STR = list(str(A*B*C))
# print(STR)

for i in range(10):
    print(STR.count(str(i)))
