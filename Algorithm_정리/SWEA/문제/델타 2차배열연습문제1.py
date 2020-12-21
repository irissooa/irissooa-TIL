#델타차를 이용한 2차배열
#무작위로 5행 5열 만듦->randint함수 써도됨
#인덱스에 벗어나지 않게 if문 처리
#상하좌우를 보며 요소와의 차를 구함(절댓값 abs함수)
#구한 차를 모두 더함

dx = [-1,0,0,1]
dy = [0,-1,1,0]

arr = [[1,2,3,4,5],
       [5,6,7,8,9],
       [2,3,4,5,6],
       [5,6,7,3,6],
       [20,40,3,4,5]
       ]

N = 5 #행
M = 5 #열

res = 0
for x in range(N): #x=0,1,2,3,4
    for y in range(M): #y=0,1,2,3,4
        for i in range(4): #이건 항상 4, 상하좌우dxdy
            testX = x + dx[i] #새로운좌표 x
            testY = y + dy[i] #새로운 좌표 y
            #2중리스트안의 인덱스체크(인덱스 벗어나면 안됨)
            if testX > 0 and testX < N and testY >= 0 and testY < M:
                res += abs(arr[x][y]-arr[testX][testY])

print(res)