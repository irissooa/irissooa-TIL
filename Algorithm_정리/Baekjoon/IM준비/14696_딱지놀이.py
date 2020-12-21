'''
두 딱지의 별 개수가 다르면 별이 많은 쪽의 딱지가 이김
별의 개수가 같고 동그라미의 개수가 다르면 동그라미가 많은 쪽의 딱지가 이김
이런식으로
별(4) > 동그라미(3) > 네모(2) > 세모(1)의 순서!
A와 B의 딱지문양수를 리스트에 넣고 idx가 제일 큰게 더 클면 이김
'''
import sys
sys.stdin = open('input.txt','r')
#총 라운드 수
N = int(input())
arr = []
for _ in range(2*N):
    temp = list(map(int,input().split()))
    bin = [0]*4
    for i in range(1,len(temp)):
        bin[temp[i]-1] += 1
    arr.append(bin)
# print(arr)
for i in range(0,2*N,2):
    A = arr[i]
    B = arr[i+1]
    for j in range(3,-1,-1):
        if A[j] == B[j]:
            continue
        elif A[j] > B[j]:
            print('A')
            break
        else:
            print('B')
            break
    else:
        print('D')
