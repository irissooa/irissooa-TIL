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



### 1523_별삼각형1

```python
'''
삼각형 높이 n과 종류 m을 입력 받음
종류1
별 한개씩 늘어남
i : 0,1,..,n, j:0,01,012,...,0123..n
while 돌면서 cnt=1부터 n까지 늘리는데 '*'*cnt한뒤 print();cnt+1

종류2
종류1의 반대

종류3
앞에 공백을 N만큼 추가하고 별을 찍는데 내려갈수록 -1
*은cnt가 2씩 증가

n 크기 100이하의 자연수 m 1,2,3

'''
n,m = map(int,input().split())
if n < 1 or n > 100 or m<1 or m>3:
    print('INPUT ERROR!')
else:
    if m == 1:
        cnt = 1
        while cnt <=n:
            print('*'*cnt)
            cnt+=1
    elif m == 2:
        cnt = n
        while cnt>0:
            print('*'*cnt)
            cnt -= 1
    else:
        blank = n-1
        cnt = 1
        while blank >=0:
            print(' '*blank+'*'*cnt)
            cnt += 2
            blank -= 1

```





### 1719_별삼각형2

```python
'''
종류1
n//2+1까지 '*'*cnt(+1)늘어나다가 지나면 줄어듦
종류2
n//2만큼 공백으로 시작해서 '*'*cnt(+1)늘어나다가 공백이 0이되면 출력하고 다시 공백 늘어남
종류3
'*'*n만큼 출력된뒤 공백이 1씩늘어나고 별은2씩 줄다가 1이되면 다시 공백줄어듦(공백이n//2)
종류4
'*'*(n//2+1)만큼 출력되고(-1) 공백이 1씩 늘어나다가 cnt가 n//2+1이되면 공백 유지 별개수는 +1
n,m범위 벗어나면 input error
'''
n,m = map(int,input().split())
if not n%2 or n < 0 or n >100 or m < 1 or m > 4:
    print('INPUT ERROR!')
else:
    if m == 1:
        cnt= 1
        idx = 0
        while idx < n:
            print('*'*cnt)
            if idx < n//2:
                cnt+=1
            else:
                cnt -= 1
            idx+=1
    elif m == 2:
        cnt= 1
        idx = 0
        blank = n//2
        while idx < n:
            print(' '*blank+'*'*cnt)
            if idx < n//2:
                cnt+=1
                blank-=1
            else:
                cnt -= 1
                blank+=1
            idx+=1
    elif m == 3:
        cnt= n
        idx = 0
        blank = 0
        while idx < n:
            print(' '*blank+'*'*cnt)
            if idx < n//2:
                cnt-=2
                blank+=1
            else:
                cnt += 2
                blank-=1
            idx+=1
    else:
        cnt= n//2+1
        idx = 0
        blank = 0
        while idx < n:
            print(' '*blank+'*'*cnt)
            if idx < n//2:
                cnt-=1
                blank+=1
            else:
                cnt += 1
            idx+=1
```



### 1329_별삼각형3

```python
'''
N을 입력받고
별개수cnt 1, idx=0
1. '*'*cnt출력
2. 공백+1 cnt+2 idx+1
3. idx == n//2가 되면 별-2,공백-1
'''
n = int(input())
if not n%2 or n < 0 or n > 100:
    print('INPUT ERROR!')
else:
    cnt = 1
    idx = 0
    blank = 0
    while idx < n:
        print(' '*blank+'*'*cnt)
        idx+=1
        if idx <=n//2:
            cnt +=2
            blank+=1
        else:
            cnt -=2
            blank -=1
```





### 1641_숫자삼각형

```python
'''
높이 n, 종류m
n100이하 홀수 m은 1~3정수
종류1
i 0,1,2,3,4,5..n
j 0,10,012,3210,01234
i가 홀수일때 j는 역순
j(0,i+1)

종류2
숫자는 idx번호 i
개수는 2*n-1부터 2씩 줄어들고 공백은0부터 1씩 늘어남

종류3
숫자는 1부터 n//2+1까지 각 행이1부터 시작이라고 생각했을때 행만큼 출력 n//2+1부터 줄어듦
'''
n,m = map(int,input().split())
if not n%2 or n<0 or n >100 or m <1 or m>3:
    print('INPUT ERROR!')
else:
    if m==1:
        num = 1
        arr = [['' for j in range(n)] for i in range(n)]
        for i in range(n):
            if i%2:
                for j in range(i+1)[::-1]:
                    arr[i][j] = num
                    num+=1
            else:
                for j in range(i+1):
                    arr[i][j] = num
                    num+=1
        for x in range(n):
            for y in range(x+1):
                print(arr[x][y],end =' ')
            print()
    elif m == 2:
        idx =0
        blank =0
        while idx <n:
            print(' '*blank,end='')
            for i in range(2*(n-idx)-1):
                print(idx,end=' ')
            print()
            idx+=1
            blank+=2
    else:
        for i in range(n):
            if i <= n//2:
                for j in range(1,i+2):
                    print(j,end=' ')
            else:
                for j in range(1,n-i+1):
                    print(j,end=' ')
            print()
```



### J_1337_달팽이삼각형

```python
'''
n높이
숫자 0부터 9까지(반복) 삼각형으로 출력
델타이동 [우하대,좌,상]
범위를 벗어나지 않고 숫자가 없으면 적어주기
범위 -> n범위밖 + j는 i까지만 갈수있다
'''
n = int(input())
arr = [['' for j in range(n)] for i in range(n)]
di = [1,0,-1]#우하대, 좌,상
dj = [1,-1,0]
num = 0
cnt = 0
for i in range(1,n+1):
    cnt += i
i,j,d=0,0,0
arr[i][j] = num
# print(cnt)
num+=1
while cnt >1:
    ni = i + di[d]
    nj = j + dj[d]
    if 0 <= ni < n and 0 <= nj <= i+1 and arr[ni][nj] == '':
        # print(i,j,ni,nj)
        i,j = ni, nj
        arr[ni][nj] = num
        num += 1
        cnt -= 1
        if num > 9:
            num = 0
    else:
        d = (d+1)%3
for i in range(n):
    for j in range(i+1):
        print(arr[i][j],end = ' ')
    print()
```



### J_2071_파스칼삼각형

```python
'''
2020-12-10 17:40
파스칼 삼각형 : 왼쪽 위와 오른쪽 위의 좌표 값을 더해서 값을 갱신해나가는 삼각형
1. 0으로 만든 2*n-1의 2차원배열
2.첫 행 n에 1넣음
3. 1행부터 n-1행까지 보는데 오른쪽 위, 왼쪽위를 더 한값으로 갱신(범위벗어나지않게 0 으로 오,왼 둘러쌈)
4. 출력은 종류에 따라 다름, 그전에 0이 아닌 것들만 따로 담아줌, 각행마다 0이아닌것만
종류 1
1.0이 아닌 그 리스트를 차례로 출력, 한칸 띄워서 출력하면 줄바꿈
종류2
1. 0이아닌 리스트 뒤에서부터 차례로 출력, blank도 1개씩 늘어남
종류3
1.0이아닌 리스트 뒤에서부터 새로운 배열을 만들어서 한 열씩 담아주고 출력
'''
n,m = map(int,input().split())
arr = [[0 for j in range(2*n+1)] for i in range(n)]
arr[0][n] = 1
pascal = [[1]]
for i in range(1,n):
    temp=[]
    for j in range(1,2*n):
        if arr[i-1][j-1] + arr[i-1][j+1]:
            temp.append(arr[i-1][j-1] + arr[i-1][j+1])
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
    pascal.append(temp)
if m ==1:
    for i in pascal:
        print(*i)
elif m ==2:
    blank = 0
    for i in pascal[::-1]:
        print(blank*' ',end='')
        print(*i)
        blank+=1
else:
    temp = [['' for j in range(n)] for i in range(n)]
    idx= 0
    for i in pascal[::-1]:
        # print(i,len(i))
        for j in range(len(i)):
            temp[n-j-1][idx] = i[j]
        idx+=1
    for x in range(n):
        for y in range(n):
            if temp[x][y]:
                print(temp[x][y],end=' ')
        print()
```

