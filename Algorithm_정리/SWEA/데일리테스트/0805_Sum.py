import sys
sys.stdin = open("input.txt", "r")
#100X100의 2차원 배열이 주어짐
#각 행의 합, 각열의 합, 각 대각선의 합 중 최댓값을 구함
#각 행의 합은 integer 범위를 넘어가지 않음
#동일한 최댓값이 있을 경우, 하나의 값만 출력
TC = 10
for tc in range(1,TC+1): #100*100
#각 행값을 입력받음
    N_list = []
    T = int(input())#테스트케이스 번호
    for i in range(100):#100*100배열을 list에 한 행씩 담는다
        N = list(map(int,input().split()))
        N_list.append(N)

    SUM = [] #합을 저장할 list

#1)같은 행끼리 합[(열+1씩)을 행 idx개수만큼]=가로
    for x in range(len(N_list)):#한 행이 더해지고 +1씩 행이 넘어감
        sum_row = 0 #한 행당 합 초기화
        for y in range(len(N_list)): #반복될 열 개수
            sum_row += N_list[x][y] #같은 행의 데이터를 더함
        SUM.append(sum_row) #SUM에 합을 추가함

#2)같은 열끼리 합[(행+1씩)을 열 idx개수만큼]=세로
    for y in range(len(N_list)):#한 열이 더해지고 +1씩 열이 넘어감
        sum_col = 0
        for x in range(len(N_list)): #같은 열의 데이터를 더함 원소
           sum_col += N_list[x][y] #행1칸씩 다음으로 넘어가며 합함
        SUM.append(sum_col) #한 행 다 더하면 SUM에 담음

# 3)(행+1씩,열+1씩) 합1개=대각선
    hap1 = 0
    for x in range(len(N_list)):#+1씩늘어나는 행 idx
        for y in range(len(N_list)): #+1씩 늘어나는 열 idx
            if x == y: #(0,0)(1,1) 행 열 idx 같을때
                hap1 += N_list[x][y]
    SUM.append(hap1)

# 4)(행+1씩,열-1씩) 합1개=대각선
    hap2 = 0
    for x in range(len(N_list)):#+1씩 늘어나는 행 idx
        for y in range(len(N_list)): #찾아 볼 열idx
            if y == (len(N_list)-1-x) : #열의 개수-1=idx값에서 행 idx를 뺸 값
                #**여기서 -1-x가 아니라 -x만 해도 값이 같음 왜???
                hap2 += N_list[x][y]
    SUM.append((hap2))
    print('#{} {}'.format(tc,max(SUM)))



##병훈오빠 코드..나랑 너무너무 다름..ㅠ대단해..ㅎ
# for _ in range(10):
#     MAX1 = MAX2 = MAX3 = MAX4 = 0
#     t = int(input())
 
#     col=[0] * 100 #열을 담을 리스트
#     for i in range(100):#100개의 행을 돌림
#         numbers = list(map(int, input().split())) #한행
#         MAX1 += numbers[i] #정방향대각선
#         MAX2 += numbers[99 - i] #역방향대각선
 
#         if MAX3 < sum(numbers): #행끼리 더함
#             MAX3 = sum(numbers) #다음행이 더 크면 MAX 갱신
 
#         for j in range(100):
#             col[j] += numbers[j]
             
#     MAX4 = max(col)#열의합 중 max
#     print(f'#{t} {max(MAX1,MAX2,MAX3,MAX4)}')
