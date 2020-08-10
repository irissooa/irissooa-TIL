# SWEA

## 달팽이 숫자(SWEA_1954)

- 값을 하나하나 주고 했다....다른 방법이 있을 텐데...ㅎ

```python
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

```

- 다른코드

```python
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
        print(*dalpang[i])  # 아주 좋아 이 표현식(요게뭐징)
```

- `print(*dalpang[i])` 물어보쟈..
- 색다르게 푼 코드

```python
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
        mode%=4 #방향 전환을 위해?
for t in range(1,int(input())+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    snail()
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()

```



## 날짜계산(SWEA_1948)

- 노가다..ㅎ

```python
#날짜계산
#월 일 월 일을 입력받고, 첫번째 날짜와 두번째 날짜의 차이를 구하라
#월일을 숫자로 바꿔라! 그러고 두개 빼고 1더하기...노가다밖에 생각안남...큰일ㅠ

Days = [31,28,31,30,31,30,31,31,30,31,30,31] #날짜들 나중에 (월-1)idx로 찾기

for tc in range(1,int(input())+1):
    M1, D1, M2, D2 = map(int,input().split())
    SUM1 = 0
    SUM2 = 0
    result = 0
    #M1+D1 구하기
    for i in range(M1-1): #해당 월은 날짜를 더하지 않고 D1를 더함
        SUM1 += Days[i] #해당 월 전까지 일 다 더하기
    SUM1 += D1 #M1전까지 모두 더한 것 + D1

    #M2+D2 구하기
    for i in range(M2-1):
        SUM2 += Days[i]
    SUM2 += D2

    #두 일의 차 구하기
    result = SUM2 - SUM1 +1 # 해당날도 더하기
    print(f'#{tc} {result}')

```

- 훨씬 짧게 줄인 코드

```python
#병훈 와...이래풀면 되는구낭...
days = [31,28,31,30,31,30,31,31,30,31,30,31]
for t in range(1, int(input())+1):
    m1,d1,m2,d2 = map(int,input().split())
    print(f'#{t} {sum(days[m1-1:m2-1])-d1+d2+1}')
```



## 압축하기(SWEA_1946)

- 이게 제일 어려웠다...어떻게 할지는 알겠는데 구현하기가 어려웠당...더 많이 풀어보쟈💪💪

```python
#단어 10개만 공백없이 들어가는 공간이 있다
#입력되는 단어를 공백없이 개수만큼 이어지게 만들어라(10개단위로 끊어야됨)
#2차원 배열로 단어와 수를 str로 받기

for tc in range(1,int(input())+1):
    N = int(input())
    chars = [input().split() for _ in range(N)] #tc하나당 출력할 문자들과 개수 입력받음
    cnt = 0
    print(f'#{tc}')
    #10개씩 cnt를 세고 10개가 되면 print()를 해서 한칸 띄워주기
    for i in range(N): # chars에 들어있는 원소 수만큼 돌아가야됨
        for j in range(int(chars[i][1])): #수가 str로 돼있기 때문에 int를 해줌
            cnt += 1
            print(chars[i][0],end = '')
            if cnt == 10:#cnt가 10이 되면 print()로 한줄 띄우고cnt리셋
                print()
                cnt = 0
    print() #tc끼리는 구분돼야되기 때문

```

- 생각은 했는데 제대로 구현이 안돼서 참고를 한 코드

```python
#병훈
for t in range(1,int(input())+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    count = 0
    print(f'#{t}')
    for i in range(N):
        for j in range(int(arr[i][1])):
            print(arr[i][0],end='')
            count +=1
            if count==10:
                count =0
                print()
                continue
    print()
```

- slicing으로 잘라서 다르게 푼 코드

```python
#의수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lists = [[str(x) for x in input().split()] for _ in
             range(N)]  # N개의 알파뱃을 2차원 배열 스트링형태로 저장 ex) [['A', '3'], ['B', '2']]
    tmp = []
    for i in range(N):
        tmp.extend(lists[i][0] * int(lists[i][1]))  # tmp = ['A', 'A', 'A', 'B', 'B']

    print(f'#{tc}')
    for x in range(len(tmp) // 10 + 1):  # tmp만들어진 것의 길이를 10로 나눈 몫의 수만큼 for문 반복
        res = tmp[10 * x:10 * (x + 1)]  # tmp를 10개씩 슬리이싱한다.
        res = ''.join(res)  # 리스트 10개를 join함수로 합친다
        print(res)  # 한줄 출력
```

