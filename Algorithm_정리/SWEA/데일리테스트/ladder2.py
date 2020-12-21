#음!ladder풀듯 풀어보자!
#ladder 일단 2차배열을 입력받는다
#ladder 0행-> 첫줄에서 1인 값들을 start list에 넣는다
#그리고 배열을 체크할건데(함수만듦)
#방문배열을 이용할거야!!
#idx가 나가거나 방문한곳이 아닌곳을 볼건데
#양옆 중에 1이 있다면 방향을 전환하고(델타이동을 이용할거야)
#없다면 계속 아래로 내려갈거야
#근데 여기가 아니라면 그냥 다음 start로 넘어가보자!
#이제 만들어보아요~
#근데 문제가 있음!
#종료조건이 틀렸네?
#i가 99일때 이동거리가 가장 짧은 거!!!!!!뽑기!!!!
#거리랑, 시작점을 어딘가에 저장해 둬야됨!(global 사용)

import sys
sys.stdin = open('input.txt','r')

di = [0,0,1] #오,왼,아래
dj = [1,-1,0]

def check(i,j,dist):
    global min_dist, flag #global 사용, 값형(전역변수) 수정 가능해짐

    #방문한 곳은 True로 바꾸기
    visited[i][j] = True
    # print(i,j)
    #종료조건
    #i 마지막 칸에 도달했을 때 도착. min_dist 확인
    if i == 99:
        if min_dist > dist:
            min_dist = dist
            flag = True
            return #값을 리턴해줄 필요없음 왜냐면 flag로 표시해주니까(True이면 START값이 저장됨)
    #범위 체크도 해줄거야
    # D = len(di)
    else:
        for d in range(3):
            #다음 위치 지정
            ni = i + di[d]
            nj = j + dj[d]
            #idx가 벗어나지 않고, 그 값이 0이 아니면 방문하지 않았던 곳으로 갈거야
            # print(ni,nj,visited[ni][nj])
            # print('로 갈라함')

            # if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0 and visited[ni][nj] == False:
            #     # 양옆중 1이 있는지 확인, 있다면 그 곳으로 방향 전환
            #     return check(ni,nj) #반복

            #현우오빠 방식 조건을 반대로 줘서 하나라도 해당되면 continue를 함
            if ni < 0 or ni >= 100 or nj < 0 or nj >= 100:
                continue #continue를 쓰면 밑에 무시하고 바로 다음 for문으로 감
            if ladder[ni][nj] == 0:
                continue
            if visited[ni][nj] == True:
                continue
            return check(ni,nj,dist+1) #다음으로 넘어갈때 거리1을 더해줌!
            break #이미 찾았으니까 break

for tc in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    #어차피 밑에 리셋시켜놓으니까 여기서 안적어도됨
    # visited = [[False for j in range(100)] for i in range(100)]
    start = [] #start지점들을 넣어줄거야
    min_dist = 9999999999999999 #최소거리 초기값
    START = 0 #시작점
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    #start지점들을 돌면서 체크할거야
    for s in start:
        flag = False #출발점 저장하기 위해 쓰는 표시
        #start마다 방문체크 리셋
        visited = [[False for i in range(100)] for j in range(100)]
        check(0,s,0) #(0,s)는 출발점 돌거야, dist는 아직 안움직였으니 0부터 시작
        if flag: #표시된flag가 True이면
            START = s
    print('#{} {}'.format(tc, START))


#선생님 풀이
#왼쪽 오른쪽
dc = [-1.1]

def dir_check(r,c):
    #왼쪽 오른쪽 확인
    for i in range(2):
        nc = c + dc[i]
        #범위안에 들어왔을 때 그 값이 1이면
        if 0 <= nc < 100 and ladder[r][nc] == 1:
            return i #그방향으로갈거야
    #왼쪽 오른쪽 걸리지 않으면 2로 리턴
    return 2 #아래로 갈거야

def go(st):
    #열
    col = st_pos[st]
    cnt = 0
    #인덱스
    idx = st
    #아래로 100칸 이동
    for i in range(100):
        d = dir_check(i,col)
        if d <2:#왼쪽 오른쪽이동
            # 인덱스위치개선
            idx += dc[d]
            #한번에 이동
            #바로 옆 idx값으로 뛰어넘는것!(위에 방향체크할떄 연결됐는지 확인했음)
            cnt += abs(col - st_pos[idx])
            #현재사다리 갱신
            col = st_pos[idx]
        cnt += 1 #d= 2일때 밑으로 내려간것..

    return cnt #시작점마다 cnt구함

for tc in range(10):
    #테스트케이스 번호 입력
    tc_ num = int(input())
    #2차원 리스트 입력
    ladder = [list(map(int,input().split())) for _ in range(100)]
    #시작 좌표를 담을 리스트
    st_pos = []
    #시작좌표를 다 담는다 -> 그리고 idx로 컨트롤 해서 바로 뛰어넘을거야!
    for i in range(100):
        if ladder[0][i] == 1:
            st_pos.append(i)
    #임의의 큰 값으로 초기화
    min_value = 987654321 #최소값초기값 아무거나 큰값으로 줌
    #어차피 정답으로 사용안될거니 안 쓰이는 수 아무거나로 초기화
    ans_idx = -1 #시작점초기값 -1


    for i in range(len(st_pos)):
        tmp = go(i)
        if tmp <= min_value:
            min_value = tmp
            ans_idx = st_pos[i]

    print('#{} {}'.format(tc_num, ans_idx))