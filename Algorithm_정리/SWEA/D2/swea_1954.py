#N을 입력받는다
#왼쪽에서 오른쪽으로 가는 코드를 만든다 열제일 끝에 갔을 때 start_행을 +1해줌
#위에서 아래로 가는 코드를 만들고 행 제일 끝에 갔을 때 end_열을 -1해줌
#오른쪽에서 왼쪽으로 가게 함 start_col로 왔을 떄 end_row를 -1해줌
#아래에서 위로 오르게 함 start_row로 왔을 때 start_col를 +1해줌 반복(whil문 start row&col이 end를 넘지 않게 함)

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)] #0*0배열을 만듦
    start_row = 0
    start_col = 0
    end_row = N-1
    end_col = N-1 #idx이기 때문에 1 작음
    cnt = 1
    
    while start_row <= end_row and start_col <= end_col:
        # 왼쪽->오른쪽
        for i in range(start_col,end_col+1):
            arr[start_row][i] = cnt #숫자들이 나온 순서대로니까 cnt를 값에 넣어줌
            cnt += 1 #하나 더 추가 됐으니 cnt를 1더해줌
        start_row += 1 #끝까지 갔으면 한행이 채워졌으니 +1해줌
        
        #위->아래
        for j in range(start_row,end_row+1):
            arr[j][end_col] = cnt #숫자들이 열은 같고 행이 늘어남
            cnt += 1
        end_col -= 1 #제일 끝 열이 하나 채워졌으니 하나 빼줌

        #오른쪽->왼쪽(start_col을 포함해야되니-1해줌)
        for k in range(end_col,start_col-1,-1): #행은 같고 끝열에서 처음열까지 열이 역순으로 옴
            arr[end_row][k] = cnt
            cnt += 1
        end_row -= 1 #제일 끝 행이 채워졌으니 하나 빼줌

        #아래->위(start_row를 포함해야되니-1해줌)
        for l in range(end_row,start_row-1,-1): #열은 같고 끝행에서 재설정된 첫 행까지 올라옴
            arr[l][start_col] = cnt
            cnt += 1
        start_col += 1 #제일 첫열이 채워졌으니 하나 더해줌

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()

#병훈
modes = [(0,1), (1,0),(0,-1),(-1,0)]
def snail():
    count = 1
    mode = 0
    start_row=start_col=0
    end_row=end_col=N-1
    i=j=0
    while count <= N**2: #이건 뭘깡..
        arr[i][j]=count
        if mode == 0: #가로로 늘어남(0,1)->(0,2)->...
            i+=modes[mode][0]
            j+=modes[mode][1]
            if j == end_col:
                mode+=1
                start_row+=1 #1행이 이미 채워졌기 때문에 1더해줌
        elif mode == 1:
            i+=modes[mode][0]
            j+=modes[mode][1]
            if i == end_row:
                mode+=1
                end_col-=1
        elif mode == 2:
            i+=modes[mode][0]
            j+=modes[mode][1]
            if j == start_col:
                mode+=1
                end_row-=1
        else:
            i+=modes[mode][0]
            j+=modes[mode][1]
            if i == start_row:
                mode+=1
                start_col+=1
        count+=1
        mode%=4 #이거 왜???
for t in range(1,int(input())+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    snail()
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()

#의수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 1
    dalpang = [[0 for j in range(N)] for i in range(N)]  # 배열 0으로 초기화

    r_st = 0
    r_end = N - 1
    c_st = 0
    c_end = N - 1

    while c_st <= c_end and r_st <= r_end:
        for i in range(c_st, c_end + 1):  # 왼쪽에서 오른쪽
            dalpang[r_st][i] = cnt
            cnt += 1
        r_st += 1

        for i in range(r_st, r_end + 1):  # 위에서 아래
            dalpang[i][c_end] = cnt
            cnt += 1
        c_end -= 1

        for i in range(c_end, c_st - 1, -1):  # 오른쪽에서 왼쪽
            dalpang[r_end][i] = cnt
            cnt += 1
        r_end -= 1

        for i in range(r_end, r_st - 1, -1):  # 아래에서 위쪽
            dalpang[i][c_st] = cnt
            cnt += 1
        c_st += 1

    print(f'#{tc}')
    for i in range(N):
        print(*dalpang[i])  # 아주 좋아 이 표현식