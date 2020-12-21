N = 3
arr = [1,2,3]
sel = [0] * N
#부분집합은 각 idx(0,1,2,3)를 선택하냐 안하냐 차이
def powerset(idx):
    #도착을 했을 때 지금까지 고른것을 출력
    if idx == N :
        print(sel, ':',end =' ' )
        for i in range(N):
            if sel[i]:
                print(arr[i],end = ' ')
        print()
        return
    #해당자리를 뽑고가고
    #idx를 선택
    sel[idx] = 1
    #idx를 선택한채로 재귀
    powerset(idx+1)
    #해당자리를 안뽑고 가고
    #idx 선택안함
    sel[idx] = 0
    #idx를 선택 안한채로 재귀
    powerset(idx+1)
    
powerset(0)