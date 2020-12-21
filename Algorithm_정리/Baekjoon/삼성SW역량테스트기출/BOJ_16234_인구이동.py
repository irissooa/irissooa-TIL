'''
2020-12-01 16:45
NxN 땅이 있음
각 칸 A[r][c]명이 산다
인구이동
1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상,R명이하
2. 국경선이 모두 열렸다면 인구이동시작
3. 국경선이 열려있다면 인접한칸으로 연합이라고 하고,
연합의 각 칸 인구수 = (연합의 인구수) // (연합을 이루고 있는 칸의 개수)
4. 연합을 해체하고 모든 국경선을 닫음
각 나라 인구수가 주어졌을때 인구 이동이 몇번 발생하나?
각 칸(a)을 돌면서 인접한 칸(b)이 인구이동 조건 1에 맞다면 국경선이 열린 좌표를 set([i,j,인구수])에 b를 담아줄건데
담아줄때 a가 이미 list안에 있으면 b만 넣어주면 되고, 만약에 없으면 새로운 연합! a와 b를 넣은 list을 list에 추가
모든 국경선을 다 연뒤에 인구이동 시작!
연합 list를 돌면서 조건에 맞게 인구이동시킨뒤 다시 값을 넣어줌
그리고 반복
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

di = [-1,1,0,0]#상하좌우
dj = [0,0,-1,1]
def checkunion(i,j,num):
    # print('연합있니',unionlist,i,j,num)
    for union in unionlist:
        for u in union:
            if [i,j,num] == u:
                # print(u,union,'같냐?')
                return union
    return False

def findunion(i,j,num):
    # print('연합찾아라',i,j,num)
    pi,pj = i,j
    for d in range(4):
        ni = pi + di[d]
        nj = pj + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        ans = abs(country[ni][nj] - num)
        if ans < L or ans > R:
            continue
        # pi,pj가 연합에 있다면 다음 연합 추가
        # print(pi,pj,num,'-->',ni,nj,country[ni][nj])
        punion = checkunion(pi, pj, num)
        nunion = checkunion(ni,nj,country[ni][nj])
        if punion:
            for u in punion:
                if [ni,nj,country[ni][nj]] == u:
                    break
            else:
                if nunion:
                    punion.extend(nunion)
                    unionlist.remove(nunion)
                else:
                    punion.append([ni,nj,country[ni][nj]])
                # print('--punion연합추가요--')
                # for x in unionlist:
                #     print(x)
            continue
        if nunion:
            for u in nunion:
                if [pi, pj, num] == u:
                    break
            else:
                if punion:
                    nunion.extend(punion)
                    unionlist.remove(punion)
                else:
                    nunion.append([pi, pj, num])
                # print('--nunion연합추가요--')
                # for x in unionlist:
                #     print(x)
            continue
        #연합에 없다면 새로운 연합 list에 넣어줌
        newunion = []
        newunion.append([pi,pj,num])
        newunion.append([ni,nj,country[ni][nj]])
        unionlist.append(newunion)
        # print('--연합추가요--')
        # for x in unionlist:
        #     print(x)


def move(ulist):
    global cnt
    # print('인구이동')
    cnt += 1
    for union in ulist:
        # print(union)
        if not union:
            continue
        people = 0
        for u in union:
            people+=u[2]
        ans = people //len(union)
        for u in union:
            i,j,num = u[0],u[1],u[2]
            country[i][j] = ans
    # for x in country:
    #     print(x)
    return

N,L,R = map(int,input().split())
country = [list(map(int,input().split())) for _ in range(N)]
unionlist = []
cnt =0
while True:
    # print(cnt+1,'여긴몇번')
    # for x in country:
    #     print(x)
    if cnt > 2000:
        break
    for i in range(N):
        for j in range(N):
            findunion(i,j,country[i][j])
    if unionlist:
        move(unionlist)
        unionlist=[]
    else:
        print(cnt)
        break
