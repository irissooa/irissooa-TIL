# #100x100크기의 2차원배열을 받는다
# # '0'으로 채워져있고 연속된 사다리는 '1', 도착지점은 '2'로 표현됨
# # 출발점 x=0~x=9가 있는데 세로 방향의 두 막대 사이에 임의의 막대들이 랜덤 간격으로 추가됨
# #아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향을 전환함
# #방향 전환 후 다시 아래 방향으로만 이동, 바닥에 도착하면 멈춤
#
# #dfs로 풀어야되는문제.........
# #1.2차원배열을 입력받는다
# #2.첫줄에서 1인 값 찾기 -> list에 담아두기,아닐때 그다음값으로 바로 넘어감
# #3.양 옆중 1이 나올때까지 밑으로 내려감 -> 복잡한거 함수로 만들면 편함
# #옆에 1이 나왔다면 방향전환
# #방향전환 후 다시 옆에 1이 나올때까지 내려감
# #만약 2가 없다면 다시 첫줄에 방문하지 않은 1로 들어감
# #반복...............................?
#
# #위에 계속 써먹을 것들을 올리고
# #그밑에 함수를 만들어야 함수에서도 적용이 됨!
#
import sys
sys.stdin = open('input.txt','r')
#
#
# #방향..델타...
# di = [0,0,1,-1] #오른쪽, 왼쪽, 아래, 위 #여기서 위는 필요없음
# dj = [1,-1,0,0]
# ladder = [] #함수에서 사용될 ladder선언
# #ni는 다음 위치, ni=i+di[방향] 그러면 옮겨짐!, nj도 마찬가지
#
# def check(i,j,dir): #x,y,방향 인자로 받음
#     #종료조건!!!!(중요)
#     if ladder[i][j] == 2:
#         return True #종료이면 True...본문에서 조건식으로 시작지점 나오게함
#
#     #종료조건 1개더인데 끝일때!!! 2가아니면 False를 반환
#     elif i == 99:
#         return False
#
#     else:
#         #방향을 설정해줄거야
#         #초반 방향은 무조건 아래부터 시작!!
#         #오른쪽, 왼쪽으로 갈때 그 방향을 우선시해줌! 아래로 내려갈땐 옆을 봐줌...ㅠㅠ
#         #dir은 방향의 idx임, idx가 0이면 오른쪽, 1이면 왼쪽, 2면 아래
#         #di[dir]
#         if (dir == 0) or (dir == 1): #오른쪽이나 왼쪽을 볼때 해당 방향을 우선시해줄거야
#             #다음 위치를 변수로 만들건데 현위치(i)에 방향을 더함..ㅎ
#             ni, nj = i + di[dir], j + dj[dir]
#             #그 다음 위치가 out of idx가 됐는지 아닌지 체크해줘야됨, 그리고 옆이 1일때!!!!
#                   #ladder[ni][nj] != 0이렇게 써야되는 이유는 만약에 2를만나면 False가 됨, 그러면 갈수 없음..
#                   근데 여기선 양옆만 보기 떄문에 ladder[ni][nj] ==1 이라고 적어도 답은 구해졌음..
#             if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0:
#                 return check(ni,nj,dir)
#             else: #못갔어, 그러면 아래로(dir=2) 내려감!!!!
#                 return check(i+1,j,2)
#
#         else:#애초에 아래로 내려가는 중...dir=2
#             #양옆을 우선 확인!!! 배열밖인지 ,1인지 확인한뒤, 1이면 방향전환 아니면 내려감!!!!
#             #오른쪽(0) 왼쪽(1)이기 때문에 for문을 돌릴거야!
#             for d in range(2): #d가 dir
#                 ni,nj = i + di[d], j + dj[d]
#                 if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0:
#                     return check(ni,nj,d)
#                 #만약 if가 false면 그냥 다음으로 넘어감!
#             #for문이 끝났는데, return이 안됐다는건 idx가 밖이거나 양옆이 1이 아니라는것! 그럼 내려가....!
#             return check(i+1,j,2) #아래로 내려가!!!!!!!
#
#
#
# for tc in range(1,11):
#     T = int(input())
#     #1 이차원배열 받기
#     ladder = [list(map(int,input().split())) for _ in range(100)]
#     #2 출발점들을 start 리스트에 넣기! 열이기 떄문에 j...
#     start = []
#     for j in range(100):
#         if ladder[0][j] == 1:
#             start.append(j)
#     #3 출발점을 하나씩 빼올거야! s가 j임
#     for s in start:
#         #기본방향은 밑으로 내려갈거고, 출발점은 행이 0이고, 열이 s임
#         #check의 return 값이 True니까...if로...해줌....답을 찾았으니 그 출발점인 s를 출력하게 해라!
#         if check(0,s,2):
#             print('#{} {}'.format(tc,s))
#             break #답을 찾았기 떄문에 나가줌!!!!


#이제 방문배열로 해볼거야!!!!!!!
#100x100인 False 2차배열을 만든다
#방문하면 True로 바꿔줌(이걸 함수로 만들거야!)

di = [0,0,1] #오른쪽, 왼쪽, 아래
dj = [1,-1,0]
ladder,visited = [],[]

def check_v(i,j):
    #방향을 for문으로 오,왼,아래순서로 둘러볼거야
    #idx 안벗어나는지, 1인지, 방문하지 않았으면(False) 그 방향으로 갈거야!!!

    #방문한 곳을 다 True로 체크 먼저 해줘야됨!!! 이미 들어가 있으니까
    visited[i][j] = True
    # print(i,j)
    #종료조건!!!
    if ladder[i][j] == 2:
        return True
    elif i == 99: #끝까지 왔는데 못찾음
        # print('{} 에 도착'.format(i))
        return False
    else:
        #방향을 정함
        for d in range(3): #만약에 len(di)를 쓰면 계속 함수를 호출하니까 그냥 변수에 할당에서 지정해주던지, 3을 쓰던지 하자!!
            ni, nj = i + di[d], j+dj[d]
            #범위 정하는 것을 반드시 앞에 둬야 idx에러가 안뜸! idx넘어가면 False라 뒤 조건을 보지 않고 바로 else로 가기때문
            if ni >=0 and ni<100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0 and visited[ni][nj] == False: #방문하지 않았으면!
                return check_v(ni,nj)



for tc in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # print(ladder)
    #방문배열도 선언해줌 j가 열
    visited = [[False for j in range(100)] for i in range(100)]
    # print(visited)
    #1인지, False인지, idx밖인지 체크
    #아니라면 그 방향으로 가면됨
    #오, 왼, 아래 순서로 돌면서 체크...! -> 함수로 만들거ㅑㅇ
    start = []
    #스타트지점들을 list에 넣음
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    # print(start)
    for s in start:
        #start 도는데 만약 못찾았어! 그러면 visited를 초기화 해줘야됨!!!!
        # if s != 67:
        #     continue
        visited = [[False for j in range(100)] for i in range(100)]
        # print('{} 에서 출발'.format(s))
        if check_v(0,s): #시작점이 true면 찾은거!
            print('#{} {}'.format(tc,s))
            break #찾았으니 끝!!
        # print(visited[99][57],)
    # else:
    #     print('못찾음')


def check(x,y):
    #범위를 벗어나는지
    if x < 0 or x >= 100 or y < 0 or y >= 100:
        return  False
    #길인지아닌지 보고
    if arr[x][y] ==0:
        return False
    #맞다면 true
    return True



 for tc in range(1,11):
     case_num = input()
     arr = [list(map(int,input().split())) for _ in range(100)]

     #도착점을 찾는다
     x = y = 0
     for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break
    dir = 0 #방향정보 저장 0:위, 1:좌, 2:우

    while x: #0이되면 False가 됨, 99부터 올라감
        #가던 방향으로 계속 가고, check가 True일때
        #왼쪽으로 가는 경우
        if dir != 2 and check(x,y-1):
            y -= 1
            dir = 1
        #오른쪽으로 가는 경우
        elif dir != 1 and check(x,y+1):
            y += 1
            dir = 2
        #그외, 위로 가는 경우
        else:
            x -= 1
            dir = 0
    print(y)

    #2번 방법 방향정보 필요없고 벽 부딛칠때까지 계속 한쪽으로 직진
    while x:
        if check(x,y-1): #왼쪽으로 가는 경우
            while check(x,y-1):
                y -= 1
            x -= 1
        elif check(x,y+1): #오른쪽으로 가는 경우
            while check(x,y+1):
                y += 1
            x -= 1
        x -= 1
    print(y)

    #3번 사다리를 지움, 그럼 옆에 오른쪽 판단안하고 갔던곳은 벽으로 막히고 한쪽 방향으로 감(이거를 아래 재귀함수로 만듦)
    while x:
        arr[x][y] = 0
        if check(x,y-1): #왼쪽으로 가는 경우
            y -= 1
        elif check(x,y+1): #오른쪽으로 가는 경우
            y += 1
        else:
            x -= 1
    print(y)

    #4번 재귀
    def ladder(x,y):
        if x == 0:
            global ans
            ans = y #시작지점을 저장
        else:
            arr[x][y] = 0
            if check(x, y - 1):  # 왼쪽으로 가는 경우
                ladder(x,y-1)
            elif check(x, y + 1):  # 오른쪽으로 가는 경우
                ladder(x,y+1)
            else:
                ladder(x-1,y)
            arr[x][y] = 1 #지우면서 갔던것들을 원상복구함
    ans = 0
    ladder(x,y)
    print(ans)


#이거는 반환하는 값이 필요하니까 return 해줌!-> 다시이해필요
def ladder(x,y):
        if x == 0:
            return y #ladder2를 풀때는 return 0하고 아래 return들에 전부 +1해주면 됨
        else:
            arr[x][y] = 0 #길 따라가면서 0으로 지웠다가 아래에서 다시 원상복구 '=2'
            if check(x, y - 1):  # 왼쪽으로 가는 경우
                return ladder(x,y-1)
            elif check(x, y + 1):  # 오른쪽으로 가는 경우
                return ladder(x,y+1)
            else:
                return ladder(x-1,y)
    print(ladder(x,y))
    print(ans)















