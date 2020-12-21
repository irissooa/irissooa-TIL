#수학 성적 점수 입력받음
#점수들의 빈도와 점수를 딕셔너리로 받는다 {점수:cnt}
#cnt가 가장 많은 것의 점수를 뽑는다 같다면 큰 수를 뽑는다

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    print(f'#{int(input())}',end = ' ')
    arr = list(map(int,input().split()))
    arr_dict = {}
    #점수:개수로 dict만들기
    for i in arr:
        if i not in arr_dict: #점수가 dict안에 없다면 key와 value설정을해라
            arr_dict[i] = 1
        else:
            arr_dict[i] += 1 #있다면 개수를 1 추가해라
    #개수가 가장 많은 것의 key를 뽑기
    max_cnt = 0 #초기값
    bin = 0 #초기 최빈점수값
    for key,value in arr_dict.items():
        if value > max_cnt: # value값이 max_cnt보다 높다면 갱신
            max_cnt = value
            bin = key
        elif value == max_cnt: # value값이 max_cnt와 같다면 더 높은 값의 키 저장
            if key > bin:
                bin = key
    print(f'{bin}')

