#모두 0을 가진 10*10배열이 주어짐
#N개의 영역이 주어지고
#다음줄에 왼쪽 위 모서리 인덱스 r1,c1, 오른쪽 아래 모서리 r2,c2와 색상 정보 color가 나옴
#가로(row) : |r1-r2|,세로(col) : |c1-c2| =>range(c1,c2+1) for문 밑에 range(r1,r2+1) for문으로 사각형을 만들며 수를 넣음
#color = 1(빨강) color = 2(파랑)
#보라색 3이 된것의 개수를 구하라

#1을 가진 영역을 0->+1로 수를 바꿔줌
#2를 가진 영역을 0->+2로 수를 바꿔줌
# 이중 3의 값을 가진 것의 개수를 구함

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    temp = [[0 for col in range(10)] for row in range(10)] # 10*10 2차원배열 0으로 채우기

    N = int(input()) #N개 영역
    puple = 0
    for n in range(N):
        r1,c1,r2,c2,color = map(int,input().split())
        for col in range(c1,c2+1): #세로만큼 가로를 출력해줄거야
            for row in range(r1,r2+1): #세로1당 출력할 가로1
                temp[row][col] += color #열이 같을때 해당하는 컬러만큼을 temp위치에 더함
    for cnt in temp: #temp에 적힌 숫자가 3인것 개수세기
        for i in cnt:
            if i == 3:
                puple += 1
    print(f'#{tc} {puple}')



    