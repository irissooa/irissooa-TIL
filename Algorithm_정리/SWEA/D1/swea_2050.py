import sys
sys.stdin = open("input.txt", "r")

# T = input()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# T에 문자가 주어지고 그것을 하나씩 띄운다
# word = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}
# a = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

# dict = {}
# for index,v in enumerate(a):
#     dict[v] = b[index]
# # print(dict)
# for i in range(len(T)):
#     for key in dict:
#         if T[i] == key:
#             print(dict[key],end = ' ')
for i in input():print(ord(i.upper())-64, end = ' ')
#그냥 숫자 출력하는건데 왜 나는 어렵게 했을 까..
#input받은 i값을 upper(대문자로 변환) 해서 아스키 숫자 받은 것의 -64한 값...