'''
4X4 크기 격자판
각 격 자판 0부처 9까지
동서남북 4방향으로 인접한 격자로 총 6번 이동
각 칸 숫자 차례로 이어붙이면 7자리
한번 거쳤던 격자칸 다시 거쳐도 됨
0으로 시작 가능
격자판 벗어나면 안됨
서로 다른 일곱자리 수 개수 구하기

음...DFS? -> RecursionError남
현우's hint
수를 입력받을떄 str로 받아라
DFS인자로 num을 주고 다음 num 은 num = num + arr[i][j]
if len(num)이 7이면 return
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,0,1,-1] #우좌하상
dj = [1,-1,0,0]
def DFS(i,j,num):
    # global num_set #리스트나 셋은 새로 만드는 거면 해줘야되지만, 변경하거나 참조하면 안해줘도됨
    #d 밑에다가 넣는다면 num이 계속 붙어버려서 밖에다 처음 등장햇을 떄! 처리해야됨
    num = num + arr[i][j]
    # print('i',i,'j',j,'num',num)
    if len(num) == 7:
        num_set.add(num)
        print(num_set)
        return
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
            continue
        DFS(ni,nj,num)

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    # print(arr)
    cnt = 0
    num = ''
    num_set = set()

    for i in range(4):
        for j in range(4):
            DFS(i,j,num)
    # DFS(0,0,arr[0][0])
    print('#{} {}'.format(tc,len(num_set)))
    
#선생님 풀이
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c,line):
    if len(line) == 7:
        tmp = ''.join(line)
        if tmp not in ans:
            ans.append(tmp)
        return
    for i in range(4):
        nr = r + dr[i]    
        nc = c + dc[i]
        
        if nr < 0 or nr >=N or nc < 0 or nc >= N:
            continue
        line += [arr[nr][nc]]
        DFS(nr,nc,line)
        #다음 반복문을 위해 원상복귀
        line.pop()
            
T = int(input())
for tc in range(1,T+1):
    N = 4
    arr = [input().split() for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            DFS(i,j,[arr[i][j]])
    print('#{} {}'.format(tc,ans))