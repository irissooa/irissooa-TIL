'''
40점이상 내성적됨
40점 미만 무조건 보충수업듣고 전부 40점
5명학생 점수 평균점수?
'''
SUM = 0
for i in range(5):
    s = int(input())
    if s < 40:
        s = 40
        SUM += s
    else:
        SUM += s
print(SUM//5)