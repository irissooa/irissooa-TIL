'''
자석의 개수는 4개, 각 자석은 8개의 날을 가짐
자석 회전시키는 횟수 K
하나의 자석 1칸 회전, 붙어있는 자석은 서로 붙어있는 날의 자성이 다를 경우에만 반대방향 1칸회전
자석을 회전시키는 방향은 시계방향이 1로 반시계방향이 -1
날의 자성 N극 0 S극이 1로 주어짐
각 자석의 날 자성정보는 빨간색 화살표 위치의 날부터 시계방향 순서대로 주어짐
'''
import sys
sys.stdin = open('input.txt','r')

def func(idx,d):
    check[idx] = 1
    #오른쪽 자석을 돌릴 수 있다면

    #왼쪽 자석을 돌릴 수 있다면

for tc in range(1,int(input())+1):
    #자석을 회전시키는 횟수 K가 주어짐
    K = int(input())
    ans = 0#정답 담을 변수
    #1번부터 4번 자석 까지 8개의 날의 자성정보, 0을 넣어줘서 인덱스를 맞춤
    magnet = [[0]+list(map(int,input().split())) for _ in range(4)]
    for k in range(K):
        #자석 번호, 회전방향
        #몇번자석을 어디방향으로?
        idx,dir = map(int,input().split())

        #자석이 돌았는지를 체크하는 리스트
        check = [0]*5
        func(idx,d)