import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
'''
5개 항목 중 정답인 항목 고름
오지선다 형식 객관식 총 M개 문제 주어짐
맞힌 문제 하나당 1점, 연속으로 맞출 경우 1점 가산
가장 높은 점수 받은 학생과 가장 낮은 점수를 받은 학생의 점수차를 출력
정답 list를 받음
N명의 학생들이 제출한 답지를 훑어보면서 답이 맞다면 +1 
그다음 것도 맞다면 연속으로 맞은 개수만큼 곱한값을 더해주다가
틀리면  점수0, cnt도 0
'''

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    score = list(map(int,input().split()))
    # print(score)
    students=[]
    for j in range(N):
        students.append(list(map(int,input().split())))
    # pprint(students)
    students_score=[]
    for student in students:
        S = 0#점수
        cnt = 0
        for i in range(M):
            #정답이라면
            if score[i] == student[i]:
                cnt += 1
                S += 1 *cnt
                # print(S,'정딥',end=' ')
            #오답이라면
            else:
                cnt=0
                # S = 0
                # print(S,'오답',end=' ')
        students_score.append(S)
        # print()
    # print(students_score)
    print('#{} {}'.format(tc,max(students_score)-min(students_score)))