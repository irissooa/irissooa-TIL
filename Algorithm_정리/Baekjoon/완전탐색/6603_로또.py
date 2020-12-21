'''
집합 S와 K가 주어질때 수를 고르는 모든 방법!
#1. S에 kC6으로 조합 구하고 출력!
#2. 조합함수만들기
'''
def comb(idx):
    if idx == K:
        if sum(sel) == 6:
            for i in range(K):
                if sel[i]:
                    print(K_list[i],end = ' ')
            print()
        return
    sel[idx] = 1
    comb(idx+1)
    sel[idx] = 0
    comb(idx+1)


while True:
    K_list = list(map(int,input().split()))
    K = K_list[0]
    if K:
        K_list = K_list[1:]
        sel = [0]*K
        comb(0)
        print()
    else:
        break