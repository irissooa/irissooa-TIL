'''
20-12-13 13:31-13:40
10진수를 입력 받아서 2, 8, 16진수로 바꾸어 출력하는 프로그램을 작성하시오.
입력의 첫줄에는 10진수 N(1≤N≤100,000)과 바꿀 진수 B(2, 8, 16)가 공백으로 구분하여 입력된다.
16진수에서 10이상의 수는 순서대로 'A', 'B', 'C', 'D', 'E', 'F'로 나타낸다.

10진수를 n진수로 바꾸는 함수를 만듦
10을 n으로 나눈 나머지를 리스트에 담음
여기서 16진수 일때 10이상이라면 A,B,C,D,E,F로 나타냄
'''
def change(ten,how):
    global result
    if ten == 0:
        return
    if ten%how >= 10:
        result.append(chr(55+ten%how))
    else:
        result.append(ten%how)
    change(ten//how,how)


n,num = map(int,input().split())
result = []
change(n,num)
print(*result[::-1],sep='')