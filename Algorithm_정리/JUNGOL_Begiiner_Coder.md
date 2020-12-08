# JUNGOL_Begiiner_Coder

[toc]

## 도형만들기

### 1291_구구단

```python
'''
구간의 처음과 끝을 입력받고
입력된 구간은 항상 처음이 작은건 아님
증가하거나 감소하는 순서 그대로 출력
'''
import sys
input = sys.stdin.readline

while True:
    s,e = map(int,input().split())
    if s <2 or s>9 or e <2 or e >9:
        print('INPUT ERROR!')
        continue
    else:
        break
if s <= e:
    for i in range(1,10):
        start = s
        while start<=e:
            if start*i<10:
                print('{} * {} =  {}'.format(start,i,start*i),end='   ')
            else:
                print('{} * {} = {}'.format(start,i,start*i),end='   ')
            start+=1
        print()
else:
    for i in range(1,10):
        start = s
        while start >= e:
            if start*i < 10:
                print('{} * {} =  {}'.format(start,i,start*i),end='   ')
            else:
                print('{} * {} = {}'.format(start,i,start*i),end='   ')
            start -=1
        print()
```



### 1341_ 구구단2

```python
'''
구간의 처음과 끝을 입력받고
입력된 구간은 항상 처음이 작은건 아님
증가하거나 감소하는 순서 그대로 출력
'''
import sys
input = sys.stdin.readline

while True:
    s,e = map(int,input().split())
    if s <2 or s>9 or e <2 or e >9:
        print('INPUT ERROR!')
        continue
    else:
        break
if s <= e:
    start = s
    while start<=e:
        for i in range(1,10):
            if start*i<10:
                print('{} * {} =  {}'.format(start,i,start*i),end='   ')
            else:
                print('{} * {} = {}'.format(start,i,start*i),end='   ')
            if i %3==0:
                print()
        print()
        start +=1
else:
    start = s
    while start >= e:
        for i in range(1,10):
            if start*i < 10:
                print('{} * {} =  {}'.format(start,i,start*i),end='   ')
            else:
                print('{} * {} = {}'.format(start,i,start*i),end='   ')
            if i%3==0:
                print()
        print()
        start -=1
```



### 1303_숫자사각형1

```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = 1
for i in range(n):
    for j in range(m):
        print(num,end = ' ')
        num += 1
    print()
```



### 1856_숫자사각형2

```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = 1
for i in range(n):
    if i%2:
        for j in range(m-1,-1,-1):
            print(num+j,end=' ')
            # num += 1
        num = num+m
    else:
        for j in range(m):
            print(num,end = ' ')
            num += 1
    print()
```





### 1304_숫자사각형3

```python
import sys
input = sys.stdin.readline

n = int(input())
num = 1
arr = [[0 for j in range(n)] for i in range(n)]
for j in range(n):
    for i in range(n):
        arr[i][j] = num
        num += 1
for i in range(n):
    for j in range(n):
        print(arr[i][j],end =' ')
    print()
```





### 2046_숫자사각형4

```python
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
if m == 1:
    num = 1
    for i in range(n):
        cnt = 0
        while cnt <n:
            print(num,end =' ')
            cnt+=1
        num+=1
        print()
elif m== 2:
    for i in range(n):
        if i %2:
            num = n
        else:
            num =1
        cnt = 0
        while cnt<n:
            if i%2:
                print(num,end = ' ')
                num-=1
            else:
                print(num,end = ' ')
                num+=1
            cnt +=1
        print()
else:
    num = 1
    for i in range(n):
        cnt = 1
        while cnt <= n:
            print(num*cnt,end = ' ')
            cnt += 1
        num+= 1
        print()
```





### 1307_문자사각형1

```python
import sys
input = sys.stdin.readline
'''
아스키 A:65~Z:90
'''

n = int(input())
arr= [['' for j in range(n)] for i in range(n)]
num=65
for j in range(n-1,-1,-1):
    for i in range(n-1,-1,-1):
        arr[i][j] = chr(num)
        num += 1
        if num ==91:
            num = 65
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
```





### 1314_문자사각형2

```python
import sys
input = sys.stdin.readline
'''
아스키 A:65~Z:90
'''

n = int(input())
arr= [['' for j in range(n)] for i in range(n)]
num=65
for j in range(n):
    if j%2:
        for i in range(n-1,-1,-1):
            arr[i][j] = chr(num)
            num += 1
            if num ==91:
                num = 65
    else:
        for i in range(n):
            arr[i][j] = chr(num)
            num += 1
            if num ==91:
                num = 65
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
```





### 1338_문자삼각형1

```python
'''
삼각형 높이n
1.arr 배열을 만든다
2. i :0,1,2,3,4 -> 1,2,3,4 -> 2,3,4 -> 3,4 ->4
j : 4,3,2,1,0 -> 4,3,2,1 -> 4,3,2 -> 4,3 -> 4
i,j모두 바뀌는데 반대로 움직임,
for문 하나를 쓰는데 (num,n) num =0 -> n-1까지 감
3.arr[i][(n-1)-i+num]에 ans를 담아줌(65->+=1->90넘으면65초기화)
'''
import sys
input=sys.stdin.readline
n = int(input())
num = 0
ans = 65
arr = [[' ' for j in range(n)] for i in range(n)]
while num < n:
    for i in range(num,n):
        # print(i,(n-1)-i+num)
        arr[i][(n-1)-i+num] = chr(ans)
        ans+=1
        if ans >90:
            ans = 65
    # print('---')
    num +=1


for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
```





### 1339_문자삼각형2

```python
'''
1. 입력범위 초과시 (1~100, 홀수)INPUT ERROR 출력
2. j : (N//2,-1,-1)하는동안 ,i : s=0(i다하면+1) (N//2-s,N//2+s+1)
3. ans = 65로 하고 i넘어가면서 +=1 90 넘어가면 65로 리셋
'''
import sys
input = sys.stdin.readline

n = int(input())
if n < 1 or n > 100 or not n%2:
    print('INPUT ERROR')
else:
    arr = [[' ' for j in range(n)] for i in range(n)]
    ans = 65
    s = 0
    for j in range(n//2,-1,-1):
        for i in range(n//2-s,n//2+s+1):
            arr[i][j] = chr(ans)
            ans+=1
            if ans > 90:
                ans = 65
        s += 1

    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
```

