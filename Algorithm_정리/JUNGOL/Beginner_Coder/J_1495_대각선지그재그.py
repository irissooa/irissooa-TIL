'''
2020-12-11 13:50-15:40
정사각형
가장 왼쪽 위 좌표부터 대각선으로 수를 입력함
이동 순서를 잘 생각해보면 다음과 같이 6가지 형태가 반복된다.
1) 아래로 한 번 이동 (불가능하면 오른쪽으로)
2) 오른쪽 위로 가능한 만큼 이동 (가장 위나 가장 오른쪽에 도달하면 종료)
3) 오른쪽으로 한 번 이동 (불가능하면 아래로)
4) 왼쪽 아래로 가능한 만큼 이동 (가장 왼쪽이나 가장 아래쪽에 도달하면 종료)

#넘 오래 걸림...ㅠ
1. 첫행을 1이라고 할때 홀수 행 i는 idxlist 순서, j는 역순
2. 짝수행은 i는 idxlist 역순, j는 순서
3. N지나기 전까지 idx-1를 append 행이 N이 지나면 idxlist에서 젤 앞 숫자 pop(행지날떄마다)
'''
N = int(input())
arr = [[0 for j in range(N)] for i in range(N)]
num=1
di = [-1,1]#우상대,좌하대
dj = [1,-1]
idxlist = [0]
idx = 1
while idx < N*2:
    # print(idxlist)
    if idx%2:
        pj = len(idxlist)-1
        for i in range(len(idxlist)):
            # print(i,pj)
            arr[idxlist[i]][idxlist[pj]] = num
            pj -= 1
            num += 1
    else:
        pi = len(idxlist) -1
        for j in range(len(idxlist)):
            arr[idxlist[pi]][idxlist[j]] = num
            pi -= 1
            num += 1
    if idx < N:
        idxlist.append(idx)
        idx += 1
    else:
        idxlist.pop(0)
        idx+=1
for x in arr:
    print(*x)