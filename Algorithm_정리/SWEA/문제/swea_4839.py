import sys
sys.stdin = open("input.txt", "r")

#이진탐색을 이용
#전체 쪽수와 A와 B가 찾아야될 숫자를 입력받는다
#A의 이진탐색과 B의 이진탐색 횟수를 비교해서 적은 사람이 이긴다, 비기면 0

def bin_search(P,key):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end) // 2

        #key 값과 같은 경우
        if middle == key:
            return cnt
        #key값보다 큰 경우
        elif middle > key:
            end = middle
        #key값보다 작은 경우
        else:
            start = middle


T = int(input())
for tc in range(1,T+1):
    P, Pa, Pb = map(int,input().split())

    A = bin_search(P,Pa)
    B = bin_search(P,Pb)

    #A의 cnt가 B보다 클때
    if A > B:
        print(f'#{tc} B')
    elif A == B:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A')