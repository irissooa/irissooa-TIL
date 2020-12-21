N = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sel = [0] * N


# 부분집합은 각 idx(0,1,2,3)를 선택하냐 안하냐 차이
def powerset(idx):
    # 도착을 했을 때 지금까지 고른것을 출력
    if idx == N:
        total = 0
        #뽑은 것들의 합을 구함
        for i in range(N):
            if sel[i]:
                total += arr[i]
        #합이 10일 경우만 출력
        if total == 10:
            print(sel)
        return
    # 해당자리를 뽑고가고
    # idx를 선택
    sel[idx] = 1
    # idx를 선택한채로 재귀
    powerset(idx + 1)
    # 해당자리를 안뽑고 가고
    # idx 선택안함
    sel[idx] = 0
    # idx를 선택 안한채로 재귀
    powerset(idx + 1)


powerset(0)

#백트래킹으로 부분집합의 합 구함

# 부분집합은 각 idx(0,1,2,3)를 선택하냐 안하냐 차이
def powerset(idx,sum_num):
    #지금까지 더한 값들을 들고 다니는데
    if sum_num > 10:
        #이미 벗어나면 더이상 수행할 필요가 없음
        return 
    # 도착을 했을 때 지금까지 고른것을 출력
    if idx == N:
        total = 0
        #뽑은 것들의 합을 구함
        for i in range(N):
            if sel[i]:
                total += arr[i]
        #합이 10일 경우만 출력
        if total == 10:
            print(sel)
        return
    # 해당자리를 뽑고가고
    # idx를 선택
    sel[idx] = 1
    sum_num += arr[idx]
    # idx를 선택한채로 재귀
    powerset(idx + 1,sum_num)
    # 해당자리를 안뽑고 가고
    # idx 선택안함
    sel[idx] = 0
    sum_num -= arr[idx]
    # idx를 선택 안한채로 재귀
    powerset(idx + 1,sum_num)


powerset(0,0)
