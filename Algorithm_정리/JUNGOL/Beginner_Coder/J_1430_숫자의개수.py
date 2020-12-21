'''
2020-12-11 16:13-16:14
세개의 자연수 A,B,C주어짐, A*B*C를 계산한 결과 0~9까지ㅣ 몇번씩 쓰였는지 구해라
'''
A = int(input())
B = int(input())
C = int(input())
ans = str(A*B*C)

for i in range(10):
    print(ans.count(str(i)))