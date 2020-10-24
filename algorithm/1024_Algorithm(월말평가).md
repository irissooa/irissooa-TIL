# Algorithm

## SWEA_1961_숫자배열회전

> [SWEA_1961_숫자배열회전](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq)
>
> 예전에 풀었던건데........오래걸림.........ㅠㅠㅠㅠㅠㅠㅠㅠㅠ휴ㅠㅠㅠㅠㅠㅠ
>
> 일단 이렇게 풀었는데, 예전풀이보고 좀더 수정해봄

```python
'''
소요시간 2020/10/24/17:25~18:30

'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

#90도 돌리는 함수
def switch(arr,temp):
    for i in range(N):
        for j in range(N):
            temp[i][N-j-1] = arr[j][i]
    return


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    temp1 = [[0 for j in range(N)] for i in range(N)]
    temp2 = [[0 for j in range(N)] for i in range(N)]
    temp3 = [[0 for j in range(N)] for i in range(N)]

    # 90도를 돌림
    switch(arr,temp1)
    switch(temp1,temp2)
    switch(temp2,temp3)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(temp1[i][j],end='')
        print(' ',end='')
        for j in range(N):
            print(temp2[i][j],end='')
        print(' ',end='')
        for j in range(N):
            print(temp3[i][j],end='')
        print()

```

- 예전풀이

> 이건 문자열로 수를 받아서 join을 써서 각 회전한 배열들을 한줄씩 붙였다. 이걸 어떻게 생각했을깡....퇴보함....ㅠ왜지...ㅠㅠㅠㅠㅠㅠ흐아ㅏㅏㅠㅠㅠㅠ

```python
#N*N행렬의 N을 입력받는다
#행렬을 입력받는다
#2차원배열을 만든다
#90도씩 돌아가는 함수를 만들수 있을까?
#90도 -> 180도 -> 270도 -> 360도(원점) 모두 90도씩 돌아가니까...
#2차배열을 90도로 전부 재배열
#배열을 계속 90도씩 재배열하며 한줄씩 출력을 함


def turnArr(arr):
    temp = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = arr[N-j-1][i]#90도 돌아가면 원래 위치에 뒤에서부터 행과 열이 바뀐상태로 들어온다
    return temp

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [input().split() for i in range(N)] #2차배열을 숫자들을 문자로 받음
    # 2차배열을 각각 재설정 해줌
    turn90 = turnArr(arr)
    turn180 = turnArr(turn90)
    turn270 = turnArr(turn180)
    print(f'#{tc}')
    for i in range(N):
        #각각 90도로 돌아간 배열들의 각 idx리스트들을 구분자 없이 문자열로 변환시킴
        a = ''.join(turn90[i])
        b = ''.join(turn180[i])
        c = ''.join(turn270[i])
        print(f'{a} {b} {c}')
```

- 챌's code

```python
import sys
sys.stdin=open('input.txt','r')

def rotate(arr):
    tmp=[['']*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            tmp[c][N-1-r]=arr[r][c]
    return tmp

#각 배열을 돌린 행들을 각 col로 넣어줌!
def result(arr,col):
    for r in range(N):
        for c in range(N):
            ans[r][col]+=arr[r][c]
    return ans



if __name__=='__main__':
    for tc in range(1,int(input())+1):
        N=int(input())
        #왜 문자열로 받냐면, 이걸 나중에 다 하나씩 붙여줄건데, int로 받으면 연산이 됨
        arr=[input().split() for _ in range(N)]

        ans=[['']*3 for _ in range(N)]

        #rotate 3번 돌려야지 90도, 180도, 270도
        #그리고 ans에 하나씩 넣어야 한다.
        for i in range(3):
            arr=rotate(arr)
            ans=result(arr,i)

        print('#{}'.format(tc))
        for r in range(N):
            for c in range(3):
                print(ans[r][c],end=' ')
            print()
```





## BOJ_16038 배열 돌리기1

> [BOJ_16038 배열 돌리기1](https://www.acmicpc.net/problem/16926)
>
> - 깊은 복사(deep copy)
>
>   - 깊은 복사는 내부에 객체들까지 모두 새롭게 copy 되는 것입니다.
>   - copy.deepcopy메소드가 해결해줍니다.
>
>   ```python
>   import copy
>   a = [[1,2],[3,4]]
>   b = copy.deepcopy(a)
>   a[1].append(5)
>   print(a)
>   #[[1, 2], [3, 4, 5]]
>   print(b)
>   #[[1, 2], [3, 4]]
>   ```

- 풀긴 풀었는데....시간초과ㅠㅠㅠㅠㅠㅠㅠ찾아보니 파이썬으로 푼 사람이 7명...

> 선생님 조언은 for문을 행2개 열2개로 나눠서 이중포문이 아닌 포문 한개씩 4개로 돌려보라고 하셨다....어떻게 할지 생각해보자

```python
'''
배열을 돌릴때 배열의 테두리만 돌리고 N과 M중 작은 값의 2를나눈 몫만큼 돌아가면서 for문의 범위가 줄어든다.
for의 범위를 num(한번돌면 +1해서 돌아가는 배열을 좁힐 변수)~배열의크기-num으로 돌림
그리고 temp라는 배열을 만들어서 
제일 처음 열이고 행이 처음부터 마지막-1행은 아래(행+1)로 이동
행이 마지막이고 열이 처음부터 마지막-1열은 오른쪽(열+1)로 이동
열이 마지막이고 행이 처음+1부터 마지막행은 위쪽(행-1)로 이동
행이 처음이고 열이 처음을 제외하고 왼쪽(열-1)으로 이동

이렇게 하면 한번 회전됨!
이거를 함수로 만들어서 회전 수 R번이 주어지면 그만큼 돌게 만들자!
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
# import copy

def rotate(arr):
    num = 0
    #돌린 arr을 담을 배열
    temp = [[0 for j in range(M)] for i in range(N)]

    while min(N,M)//2 > num:
    # for n in range(min(N,M)//2):
        for i in range(num,N-num):
            for j in range(num,M-num):
                # 제일 처음 열이고 행이 처음부터 마지막-1행은 아래(행+1)로 이동
                if j == num and i != N-num-1:
                    temp[i+1][j] = arr[i][j]
                # 행이 마지막이고 열이 처음부터 마지막-1열은 오른쪽(열+1)로 이동
                elif i == N-num-1 and j !=M-num-1:
                    temp[i][j+1] = arr[i][j]
                # 열이 마지막이고 행이 처음+1부터 마지막행은 위쪽(행-1)로 이동
                elif j == M-num-1 and i != num:
                    temp[i-1][j] = arr[i][j]
                # 행이 처음이고 열이 처음을 제외하고 왼쪽(열-1)으로 이동
                elif i == num and j != num:
                    temp[i][j-1] = arr[i][j]
        #한범위의 테두리를 전부 돌면 num을 +1해서 범위를 좁혀줌
        num += 1
    return temp

#배열의 크기 N,M, 회전수 R
N,M,R = map(int,input().split())

#배열
arr = [list(map(int,input().split())) for _ in range(N)]
# temp = copy.deepcopy(arr)
for r in range(R):
    ans = rotate(arr)
    arr = ans
# print(ans)
for i in range(N):
    for j in range(M):
        print(ans[i][j],end=' ')
    print()


```



