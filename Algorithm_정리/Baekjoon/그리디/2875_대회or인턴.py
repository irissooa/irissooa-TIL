'''
1. 여2 남1로 구성된 최대로 만들 수 있는 팀을 구함
2. K명을 한팀에서 빼오고 만약 한팀이상 필요하면 다음 팀에서 빼옴
'''
N,M,K = map(int,input().split())
cnt= 0
total = N + M
while N > 1 and M > 0:
    N -= 2
    M -= 1
    cnt += 1
# print(cnt)
total -= cnt*3
#K가 1팀보다 수가 적으면 그 팀만 뻄
while K > 0:
    if total > 0:
        total -=1
        K -=1
    else:
        cnt-=1
        K-=3
print(cnt)
