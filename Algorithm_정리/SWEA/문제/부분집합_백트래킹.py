arr = [1,2,3]
N = len(arr)
A = [0] * N #1,0

def powerset(n,k,cursum):
    if cursum>10:
        return
    if n == k:
        for i in range(n):
            if A[i]:
                print(arr[i],end = ' ')
        print()
    else:
        #k번째 선택
        A[k] = 1
        powerset(n,k+1,cursum+arr[k])
        #k번째 비선택
        A[k] = 0
        powerset(n,k+1,cursum)

powerset(N,0,0)