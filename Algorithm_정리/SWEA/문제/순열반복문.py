arr = [1,2,3]
#1부터 3까지 반복을 돌면서
for a in range(1,4):
    for b in range(1,4):
        #a와 b가 같은것은제외
        if a == b:
            continue
        for c in range(1,4):
            #a,c가 같거나 c,b가 같은건 제외
            if a == c or c == b:
                continue
            print(a,b,c)

#순열 방문체크
arr = [1,2,3]
N = 3
sel = [0] * N
visited = [0] *N
def perm(idx): #몇번째 원소인지를 인자로 받음
    if idx == N:
        print(sel)
        return
    for i in range(N):
        #방법1
        # if visited[i]: #True라면
        #     continue
        #방법2
        if not visitied[i]:
            sel[idx] = arr[i]
            #뽑았다고 내려보내고
            visited[i] = 1
            perm(idx+1)
            #다음 꺼도 시도 해봐야되니까 원상복귀 시켜놓음
            visited[i] = 0
    #암묵적으로 반복문이끝났을 때 return함
    #return
perm(0)

#비트
arr=[1,2,3]
N = 3
sel = [0] * N
def perm(idx,check): #몇번째 원소인지를 인자로 받음
    if idx == N:
        print(sel)
        return
    for i in range(N):
        if (check & (1<<i))!=0:
            continue
        sel[idx] = arr[i]
        perm(idx+1,check |(1<<i))

perm(0,0)