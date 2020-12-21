def selectionSort(a):
    # i : 0 ~ len(a)-1
    for i in range(len(a)-1): #0,1,2,3 
        #최소값 찾기
        min = i
        for j in range(i+1,len(a)): #자기보다 하나 큰거부터 끝까지
            if a[min] > a[j]:
                min = j #min은 idx
        #바꿔치기를 한다
        a[i], a[min] = a[min], a[i]

arr = [64,25,10,22,11]
selectionSort(arr)
print(arr)

#seliection 알고리즘
def selection(a,k):
    # i : 0 ~ len(a)-1
    for i in range(len(a)-1): #0,1,2,3 
        #최소값 찾기
        min = i
        for j in range(i+1,len(a)): #자기보다 하나 큰거부터 끝까지
            if a[min] > a[j]: #a[min] < a[i]이거 바꿔주면 내림차순으로 바꿀 수 있음
                min = j #min은 idx
        #바꿔치기를 한다
        a[i], a[min] = a[min], a[i]
    return a[k-1] #0부터시작했기 때문에 -1을 해줌
arr = [64,25,10,22,11]
selectionSort(arr)
print(selection(arr,3))