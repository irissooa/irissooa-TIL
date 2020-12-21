'''
삼각형 높이n
1.arr 배열을 만든다
2. i :0,1,2,3,4 -> 1,2,3,4 -> 2,3,4 -> 3,4 ->4
j : 4,3,2,1,0 -> 4,3,2,1 -> 4,3,2 -> 4,3 -> 4
i,j모두 바뀌는데 반대로 움직임,
for문 하나를 쓰는데 (num,n) num =0 -> n-1까지 감
3.arr[i][(n-1)-i+num]에 ans를 담아줌(65->+=1->90넘으면65초기화)
'''
import sys
input=sys.stdin.readline
n = int(input())
num = 0
ans = 65
arr = [[' ' for j in range(n)] for i in range(n)]
while num < n:
    for i in range(num,n):
        # print(i,(n-1)-i+num)
        arr[i][(n-1)-i+num] = chr(ans)
        ans+=1
        if ans >90:
            ans = 65
    # print('---')
    num +=1


for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()