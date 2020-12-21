'''
num_list에서 수의 부분집합 중 더해서 합이 S가 되는 경우의 수 출력!
부분집합 구하는 함수 만들고,
그 sel의 합이 S인 것!
'''



import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('input.txt','r')

def powerset(idx):
    global cnt
    #idx가 끝까지 갔으니 부분집합 조건 확인
    if idx == N:
        #부분집합 합을 구할 변수
        total = 0
        for i in range(N):
            #부분집합 포함 표시가 있다면
            if sel[i]:
                total += num_list[i]
        #해당 부분집합 합이 S라면! 그리고 공집합이 아니라면!(S가 0일수도 있어서)
        if sum(sel) and total == S:
            cnt += 1
        return
    #포함
    sel[idx] = 1
    powerset(idx+1)
    #포함안함
    sel[idx] = 0
    powerset(idx+1)

#정수의 개수, 정수S
N,S = map(int,input().split())

#N개의 정수
num_list = list(map(int,input().split()))

#부분집합을 표시할 변수
sel = [0]*N
#합이 S인 부분집합 개수를 세어줄 변수
cnt = 0
powerset(0)
print(cnt)
