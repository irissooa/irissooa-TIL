# Algorithm(보충)

## 알파벳을 숫자로 변환

```python
ch_to_int = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #문자-> int로 맵핑하기 위한 문자열
#붙어있는입력을 받기
arr = list(input()) #한줄 읽고 리스트로 변환(문자)
for i in range(len(arr)):
    if arr[i] in ch_to_int: #문자열도 순회할 수 있다
        print(i+1, end = ' ')
print()
```



## 대각선 출력하기

> for문에 대한 이해 필요한 문제

```python
'''
#++++
+#+++
++#++
+++#+
++++#
'''
#5개 찍은 것을 5번 반복
for i in range(5):
    #한줄에 5개찍기
    for j in range(5):
    	if i==j:
            print('#',end='')
        else:
        	print('+',end = '')
    print() #한set하고 줄바꿈하기위해
```



## 2차원 배열

- 1차원 리스트를 묶어놓은 리스트

```python
#2차원 배열 선언
arr= [[0,1,2,3],[4,5,6,7]]
#초기화!
arr_1 = [0]*5 #1차원

#1.#for앞의 내용을 반복, 이거를 5번 반복할거야!
arr_2 = [[0]*5 for _ in range(5)] #2차원배열 선언
#2.
for row in arr_!:
    print(row)
```

- 2차원배열 입력받기

```python
'''
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''
N,M = map(int,input().split())
mylist = [0 for i in range(N)] #1차원배열 초기화

#list(map(int,input().split())) #1차원 배열입력받아서-<리스트(1차원)으로 만듦

#2차원배열
for i in range(N):
    my_list[i] = list(map(int,input().split()))

#2차원배열
MY_list = [list(map(int,input().split())) for_ in range(M)]
```





## 추가로 풀어보기

http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=712&sca=9010&page=3

```python
#가로 세로 크기가 각각 100인 정사각형 도화지
#가로, 세로 크기 각각 10인 정사각형
#여러장 색종이 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하기

#색종이 수 입력
#색종이 왼쪽 하단 점의 x값, y값 입력

T = int(input())
arr = [[0]*100 for _ in range(100)] #흰도화지

for tc in range(1,T+1):
    x, y = map(int,input().split())
    #푸는중...
```

