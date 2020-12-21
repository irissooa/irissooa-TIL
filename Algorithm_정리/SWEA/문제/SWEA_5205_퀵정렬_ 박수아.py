'''
퀵정렬 함수를 만들어보자
'''
import sys
sys.stdin = open('input.txt','r')

#list, 시작idx,끝idx
def quicksort(A,left,right):
    if left < right:
        pivot = hoare_partition(A,left,right)
        #pivot = lomuto_partition(A,left,right)
        quicksort(A,left,pivot-1)
        quicksort(A,pivot+1,right)

def hoare_partition(A,left,right):
    pivot = A[left]
    i = left
    j = right

    while i <= j:
        #피봇보다 큰게 나올때까지
        while (i <= j and A[i] <= pivot):
            i += 1

        #피봇보다 작은게 나올때까지
        while (i <= j and A[j] >= pivot):
            j -= 1

        #i,j가 역전되지 않았으면, 피봇보다 큰값이랑 작은값 swap(뒤에 있는 작은값이앞으로옴)
        if i < j:
            A[i], A[j] = A[j],A[i]

    #i,j가 역전됐으면 피봇이랑 j(피봇보다 작은값) 바꿔주기
    A[left],A[j] = A[j],A[left]
    return j

def lomuto_partition(A,left,right):
    pivot = A[right]
    i = left-1
    for j in range(left,right):
        #A[j]보다 pivot이 작을때 i값 +1을 늘려주고
        if A[j] <= pivot:
            i += 1
            #피봇보다 작은값들이 있는곳으로 옮김
            A[i],A[j] = A[j],A[i]
    #j가 피봇 전까지 다 돌고난 뒤, 피봇보다 큰값이 있는곳과 피봇을 바꿈
    A[i+1],A[right] = A[right],A[i+1]
    return i+1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quicksort(arr,0,N-1)
    print('#{} {}'.format(tc,arr[N//2]))