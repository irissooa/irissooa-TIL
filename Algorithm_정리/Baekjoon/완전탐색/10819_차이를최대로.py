'''
#1. 선택정렬로 제일 앞에 제일 큰수, 2번쨰는 제일 작은수를 골라서 정렬
그렇게 0,1idx가 정해지고 그다음 2 idx부터 1번 반복
#2. 정렬시킨 뒤, 뻬주고 절댓값!(abs이용)
'''
import sys
sys.stdin = open('input.txt','r')

def selectSort(arr,idx):
    if idx == len(arr)-2:
        if arr[idx] < arr[idx+1]:
            arr[idx],arr[idx+1] = arr[idx+1],arr[idx]
        return
    MIN,MAX = idx+1,idx
    for i in range(idx+2,len(arr)):
        # print(idx,A,i,arr[MAX],arr[i],arr[MIN])
        if arr[i] > arr[MAX]:
            MAX = i
            # print('MAX',MAX)
        if arr[i] < arr[MIN]:
            MIN = i
            # print('MIN',MIN)
    arr[MAX], arr[idx] = arr[idx], arr[MAX]
    arr[MIN], arr[idx+1] = arr[idx+1],arr[MIN]
    selectSort(arr,idx+2)


def perm(idx,n):
    global MAX
    if idx == N:
        # print(sel)
        SUM = 0
        for a in range(0, len(A) - 1):
            SUM += abs(sel[a] - sel[a + 1])
        if SUM > MAX:
            MAX = SUM
        return MAX
    for i in range(N):
        if u[i] == 0:
            u[i] = 1
            sel[idx] = A[i]
            perm(idx+1,n)
            u[i] = 0

N = int(input())
A = list(map(int,input().split()))
sel = [0]*N
u = [0]*N
# selectSort(A,0)
MAX = 0
perm(0,N)
# print(A)

print(MAX)
