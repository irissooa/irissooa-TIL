'''
평면에 색이 서로 다른 직사각형 색종이 N장
비스듬 X
서로 평행, 수직 둘중 하나
순서대로 색종이가 쌓이면서 이전 것을 가림
N장의 색종이가 주어진 위치에 차례로 놓인 후 각 색종이가 보이는 부분의 면적을 구하는 프로그램 작성
N이 놓일 수 있는 곳의 배열은 100x100
첫번째 색종이부터 숫자를 입력(1)
두번째 -> 2
이렇게 해서 1인거 개수, 2인거 개수,,,N인거 개수 세서 출력!
'''
import sys
sys.stdin = open('input.txt','r')
# from pprint import pprint

#평면 배열
arr = [[0 for j in range(101)] for i in range(101)]
#색종이 장수
N = int(input())
for n in range(1,N+1):
    #색종이 x좌표(열), y좌표(행), 너비, 높이
    x, y, w, h =map(int,input().split())
    #좌표에 순서(n)를 입력
    #행 좌표(y)에서 높이(h)만큼
    for i in range(y,y+h):
        #열 좌표(x)에서 너비(w)만큼
        for j in range(x,x+w):
            #해당 순서를 배열에 넣어줌
            arr[i][j] = n
# pprint(arr)
#순서대로 숫자 개수 세어서 list에 담아주기
area = [0] *(N+1)
for n in range(1,N+1):
    for i in range(101):
        for j in range(101):
            if arr[i][j] == n:
                area[n] += 1
#순서대로 넓이 출력
for a in range(1,N+1):
    print(area[a])