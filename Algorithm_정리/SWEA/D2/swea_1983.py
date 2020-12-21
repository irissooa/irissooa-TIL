import sys
sys.stdin = open("input.txt", "r")
#학점은 상대평가
#총 10개의 평점
#학점: 총범 = 중간고사(35%)+기말(45%) + 과제(20%
#10개의 평점은 총번이 높은순
#각각 평점은 같은 비율로 부여될 수 있음 N명의 학생이 있다면 N/10명의 학생들에게 평점 무여
#학점을 알고 싶은 K번째 학생의 번호가 주어짐, 학점 출력
#N은 항상 10의 배수
#K번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 주어지지 않음

# N명과 K학생 번호를 받음
# 아래의 중간고사, 기말, 과제 점수를 받고 총점을 계산
#총점을 하나의 list에 담음
#그 리스트의 학생수/10한 만큼 각 학점을 부여함
#k번째 학생과 동일한 점수는 없으니, 그 점수를 저장해 놓고
#점수가 높은 순으로 내림차순 해서, 비율만큼 자르고, 학점을 부여함
#k의 점수가 있는 부분의 학점을 출력

for tc in range(1,int(input())+1):
    N, K = map(int,input().split())
    arr = []
    for i in range(N):
        mid, final, hw = map(int,input().split())
        total = mid*0.35 + final*0.45 + hw*0.2
        arr.append(total)
    res = arr[K-1] #K번째는 idx값으로는 1빼줘야됨, k번째 점수를 grade에 저장해둠
    arr_b = sorted(arr,reverse = True) #내림차순으로 정렬
    ratio = N//10 #학점을 줄 비율
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0', 'C-','D0']
    for i in range(len(grade)): # grade는 N/10 비율로 나눈 것이기 때문에 그만큼 범위를 나눌거야
        for idx in range(ratio*i,ratio*(i+1)): #ratio에서 ratio만큼 범위까지
            # arr의 ratio범위만큼 grade 설정
            if arr_b[idx] == res: #K번째 값이 들어오면 그 grade를 출력해라
                print(f'#{tc} {grade[i]}')
                break

#병훈 천사님...
def get_total_score(scores):  # 입력받은 점수를 비율에 따라 총점 만들기
    rates = [0.35, 0.45, 0.2]
    score = 0
    for j in range(3):
        score += scores[j] * rates[j]
    return score


final_score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, int(input()) + 1):

    N, K = map(int, input().split())  # 학생의 수, 출력하고 싶은 학생의 번호
    arr = []  # N 명의 학생들 점수를 총점으로 변환한 점수를 담고 있는 배열

    for i in range(N):
        score = get_total_score(list(map(int, input().split())))
        arr.append([score, i])
        # 나중에 K 번째 학생의 점수를 찾기 위해 i를 같이 append한다,
        # enumerate 함수를 써도 된다!

    arr.sort(key=lambda x: x[0], reverse=True)
    # 학생들의 총점을 내림차순으로 정렬한다.
    # 이때 arr 배열에는 [[74.6,0],[92.5,1],[88.8,2]...] 이렇게 자료가 있는데
    # 총점을 기준으로 정렬하고 싶기 때문에 sort함수의 key argument를 활용해 기준을 정한다
    # 그 기준은 각각의 요소들 [74.6,0] [92.5,1]...[score,i] 에서 첫 번째 요소인 score가 기준이다
    # key = lambda x : x[0] 를 통해서 score를 기준으로 정렬하도록 만든다.
    # 또한 내림차순으로 정렬하기 때문에 reverse = True
    for i in range(N):
        if arr[i][1] == K - 1:
            # 총점을 기준으로 내림차순으로정렬된 arr 안에서 K 번째 학생을 찾는다.
            print(f'#{t} {final_score[i // (N // 10)]}')
            # 그 K 번째 학생의 성적을 입력하기 위해서는
            # 10명의 학생이 있다면 각각 성적 A+, A0, A- ... 은 1명
            # 20명의 학생이 있다면 각각 성적 2명
            # N명의 학생이라면 N//2 명씩이다

            # 내림차순으로 정렬되어 있기 때문에 i 는 등수를 의미한다.
            # 10명 중 i 등이면 [A+, A0, A- ..] 의 i 번째 성적을 받는다.
            # 20명 중 i 등이면 [A+, A0, A- ..] 의 i//2 번째 성적을 받는다. (1등도 A+ 2등도 A+)
            #  N명 중 i 등이면 [A+, A0, A- ..] 의 i//(N//10)  번째 성적을 받는다.





