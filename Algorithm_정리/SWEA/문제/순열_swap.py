arr = [1,2,3]
N = 3

def perm(idx):

    if idx == N:
        print(arr)
        return

    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]

perm(0)

#순열
def perm(n,k):
    if k == n:
        print(arr)
    else:
        for i in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1)
            arr[k], arr[i] = arr[i],arr[k]
arr = [1,2,3]
N = len(arr)
perm(N,0)