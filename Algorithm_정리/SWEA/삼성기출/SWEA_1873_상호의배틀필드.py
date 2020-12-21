'''
2020-12-02 10:20-11:30
문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

문자	동작(사용자가 넣을 수 있는 입력의 종류)
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

전차가 만약 게임맵의 밖이라면 전차는 이동하지 않음
전차가 포탄을 발사하면 포탄은 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 게임 맵 밖으로 나갈때까지 직진
만약 벽에 부딪히면 포탄 소멸, 벽이 벽돌로 만들어진 벽이라면 이벽은 파괴되고 평지가 됨
강철로 만들어진 벽이라면 아무일도 일어나지 않음
게임 밖으로 나가면 아무일도 일어나지 않음
초기 게임 맴의 상태와 사용자가 넣을 입력이 순서대로 주어질때, 모든 입력을 처리하고 나면 게임 맴의 상태가 어떻게 되는가?

for 문을 돌리면서 ^ v < >모양이  전차의 위치와 바라보는 모양
그 방향대로 일단 움직이는데 앞에 .(평지)가 있을 때만 앞으로 갈 수 있다.
그전에 사용자의 입력에 따라 움직여야됨
포탄을 발사했을때 만나는게 벽돌로만들어진 벽이라면 그 벽은 평지가 됨
방향을 바꿨을때 그 칸이 평지라면 그 칸으로 이동, 아니라면 이동하지 않고 다음 input으로 넘어감
'''

di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]
def move(i,j,d):
    pi,pj,pd = i,j,d
    while userinput:
        STR = userinput.pop(0)
        # print(STR)
        # for x in MAP:
        #     print(x)
        if STR =='S':
            wi,wj = pi,pj
            while True:
                ni = wi + di[pd]
                nj = wj + dj[pd]
                if ni < 0  or ni >= H or nj < 0 or nj >= W:
                    break
                if MAP[ni][nj] == '*':
                    MAP[ni][nj] = '.'
                    break
                if MAP[ni][nj] == '#':
                    break
                wi,wj = ni,nj
            continue
        if STR == 'U':
            pd = 0
            dir ='^'
            MAP[pi][pj] = dir
        if STR == 'D':
            pd = 1
            dir = 'v'
            MAP[pi][pj] = dir
        if STR == 'L':
            pd = 2
            dir = '<'
            MAP[pi][pj] = dir
        if STR == 'R':
            pd = 3
            dir = '>'
            MAP[pi][pj] = dir
        ni = pi + di[pd]
        nj = pj + dj[pd]
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue
        if MAP[ni][nj] != '.':
            continue
        MAP[pi][pj] = '.'
        # print(MAP[pi][pj],pi,pj)
        pi,pj = ni,nj
        MAP[pi][pj] = dir
        # print(MAP[pi][pj],pi,pj)



T = int(input())
for tc in range(1,T+1):
    # 게임맵의 높이가 H, 너비가 W
    H,W = map(int,input().split())
    MAP = [list(input()) for _ in range(H)]
    # 사용자 입력 개수
    N = int(input())
    userinput = list(input())
    # print(userinput)
    # for x in MAP:
    #     print(x)
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == '^':
                move(i,j,0)
            if MAP[i][j] == 'v':
                move(i,j,1)
            if MAP[i][j] == '<':
                move(i,j,2)
            if MAP[i][j] == '>':
                move(i,j,3)
    # print('----전차이동----')
    print('#{}'.format(tc),end=' ')
    for x in MAP:
        print(''.join(x))