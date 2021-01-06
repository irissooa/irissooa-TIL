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



### J_1707_달팽이사각형

```python
'''
20-12-11 09:58-10:08
정사각형 크기 입력 후 시계방향 돌면서 출력
가장왼쪽 위부터 아래 왼쪽 위 오른쪽 순서
1.n배열을 만들고 0으로 둘러싼다
2.우하좌상으로 델타로 움직임, 배열이 0 이아니면 기록 반복
'''
n = int(input())
num =1
di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
arr = [[0 for j in range(n+2)] for i in range(n+2)]
i,j,d = 1,1,0
arr[i][j] = num
num+=1
cnt = 0
while num<=n*n:
    ni=i+di[d]
    nj = j+dj[d]
    if 1<=ni<=n and 1<=nj<=n and not arr[ni][nj]:
        arr[ni][nj] = num
        i,j = ni,nj
        num+=1
    else:
        d=(d+1)%4
for x in range(1,n+1):
    print(*arr[x][1:n+1])
```



### J_1331_문자마름모

```python
'''
20-12-11 11:29-13:45
마름모 한번의 길이ㅣ N
1) 첫번쨰 행의 중앙부터 출발하여 시계반대 방향으로 A부터 채워나감,Z다음은 A
2) 바깥 부분이 다 채워지면 두번째 행 중앙부터 다시 같은 작업 반복
3) 같은 방법으로 마름모 다 채워지도록 출력

1.첫시작 chr(65)부터 좌하대->우하대->우상대->좌상대 순서로 채워나감!
1) squ = 1
n만큼 문자입력, d= 0
2)squ = 2
n-1만큼 문자입력 , d = 1
3) squ = 3
n-1만큼 문자입력, d=2
4) squ = 4
n-2만큼 문자입력, d=3
5)squ가 4인데 cnt가 0이되면 i는 그대로, j-1로 옮김, squ = 1로 초기화하고, n-=1로 함
6)반복
2. 범위를 벗어나지 않게, 배열에 들어있지 않은 것, n*n개수만큼 반복
3. Z가 끝나면(91이되면 65로 초기화)
'''
n = int(input())
N = n
arr = [['' for j in range(n*2-1)] for i in range(n*2-1)]
di = [1,1,-1,-1] #좌하대,우하대,우상대,좌상대
dj = [-1,1,1,-1]
num = 65
cnt = n
i,j,d =0,n-1,0
squ = 1
arr[i][j] = chr(num)
num += 1
cnt-=1
while n >=1:
    if squ == 1 and cnt ==0:
        d=1
        squ += 1
        cnt = n-1
    if squ == 2 and cnt ==0:
        d= 2
        squ += 1
        cnt = n-1
    if squ == 3 and cnt ==0:
        d= 3
        squ += 1
        cnt = n-2
    if squ == 4 and cnt ==0:
        d= 0
        n-=1
        squ  = 1
        cnt = n
        i,j = i-1,j
    ni = i+di[d]
    nj = j+dj[d]
    arr[ni][nj] = chr(num)
    # print(ni,nj,cnt,arr[ni][nj],squ,n)
    num += 1
    cnt-=1
    i,j = ni,nj
    if n== 1:
        break
    if num > 90:
        num = 65
idx=2*N-2
for x in range((2*N)-1):
    print(' '*idx,end='')
    for y in range(2*N-1):
        if arr[x][y]:
            print(arr[x][y],end=' ')
    print()
    if x <N-1:
        idx -=2
    else:
        idx+=2

```





### J_1495_대각선지그재그

```python
'''
2020-12-11 13:50-15:40
정사각형
가장 왼쪽 위 좌표부터 대각선으로 수를 입력함
이동 순서를 잘 생각해보면 다음과 같이 6가지 형태가 반복된다.
1) 아래로 한 번 이동 (불가능하면 오른쪽으로)
2) 오른쪽 위로 가능한 만큼 이동 (가장 위나 가장 오른쪽에 도달하면 종료)
3) 오른쪽으로 한 번 이동 (불가능하면 아래로)
4) 왼쪽 아래로 가능한 만큼 이동 (가장 왼쪽이나 가장 아래쪽에 도달하면 종료)

#넘 오래 걸림...ㅠ
1. 첫행을 1이라고 할때 홀수 행 i는 idxlist 순서, j는 역순
2. 짝수행은 i는 idxlist 역순, j는 순서
3. N지나기 전까지 idx-1를 append 행이 N이 지나면 idxlist에서 젤 앞 숫자 pop(행지날떄마다)
'''
N = int(input())
arr = [[0 for j in range(N)] for i in range(N)]
num=1
di = [-1,1]#우상대,좌하대
dj = [1,-1]
idxlist = [0]
idx = 1
while idx < N*2:
    # print(idxlist)
    if idx%2:
        pj = len(idxlist)-1
        for i in range(len(idxlist)):
            # print(i,pj)
            arr[idxlist[i]][idxlist[pj]] = num
            pj -= 1
            num += 1
    else:
        pi = len(idxlist) -1
        for j in range(len(idxlist)):
            arr[idxlist[pi]][idxlist[j]] = num
            pi -= 1
            num += 1
    if idx < N:
        idxlist.append(idx)
        idx += 1
    else:
        idxlist.pop(0)
        idx+=1
for x in arr:
    print(*x)
```



### J_2074_홀수마방진

```python
'''
2020-12-11 15:42-16:03

다음의 순서에 따라 각 위치에 차례대로 값을 넣는다.

1. 첫 번째 숫자인 1을 넣는 위치는 첫 번째 행 가운데이다.

2. 숫자가 N의 배수이면 바로 아래의 행으로 이동하여 다음의 수를 넣고

3. 그렇지 않으면 왼쪽 위로 이동하여 다음의 숫자를 넣는다.
만약 행이 첫 번째를 벗어나면 마지막 행으로 이동하고, 열이 첫 번째를 벗어나면 마지막 열로 이동한다. -> 델타이동

첫숫자를 첫번째 행 가운데 넣는다
num이 N으로 나누어떨어지지 않으면 왼쪽 위로 이동(델타->(i-1)%N,(j-1)%N)
나누어 떨어진다면 아래로 이동((i+1)%4,j)
num += 1 num이 N*N이될때까지 반복
'''

N = int(input())
arr=[[0 for j in range(N)] for i in range(N)]
num = 1
i,j = 0,N//2
arr[i][j] = num
num =1
while num <N*N:
    num += 1
    if num % N !=1:
        ni = (i-1)%N
        nj = (j-1)%N
        # print(ni,nj,num)
    else:
        ni = (i+1)%N
        nj = j
        # print(ni,nj,num,'배수')
    arr[ni][nj] = num
    i,j = ni,nj

for x in arr:
    print(*x)
```



## 수학

### J_1692_곱셈

```python
'''
2020-12-11 16:07-16:10
세자리수 x 세자리수 곱하기
1. 2번째 수의 1의자리와 1번째수의 곱하기
2. 10의자리와 1번쨰수곱하기
3. 백의 자리와 1번째수 곱하기
4. 1 + 10*2 + 100*3 한 값 구하기
'''
first = int(input())
second = input()

third = first * int(second[2])
fourth = first * int(second[1])
fifth = first * int(second[0])

sixth = third + fourth* 10 + fifth * 100
print(third)
print(fourth)
print(fifth)
print(sixth)

```



### J_1430_숫자의개수

```python
'''
2020-12-11 16:13-16:14
세개의 자연수 A,B,C주어짐, A*B*C를 계산한 결과 0~9까지ㅣ 몇번씩 쓰였는지 구해라
'''
A = int(input())
B = int(input())
C = int(input())
ans = str(A*B*C)

for i in range(10):
    print(ans.count(str(i)))
```



### J_1071_약수와배수

```python
'''
20-12-11 16:15-16:18
주어진 정수 중 입력받은 수의 약수와 배수의 합 각각 출력
입력받은 정수 중 주어진 정수를 나누어떨어지게 하는 것 약수의 합
주어진 정수가 해당 수를 나누어떨어지게하는 것 배수의 합
'''
# 정수개수
N = int(input())
numbers = list(map(int,input().split()))
M = int(input())

ans = 0
result = 0
for i in numbers:
    if not M % i:
        ans += i
    if not i % M:
        result += i
print(ans,result,sep='\n')
```



### J_1402_약수구하기

```python
'''
20-12-11 16:20-16:23
어떤 자연수 p,q
p의 약수들 중 q번쨰로 작은 수 출력
N의 약수가 K개보다 적어서 약수가 존재하지 않을 경우 0을출력
'''
N, K = map(int,input().split())
num = []
for i in range(1,N+1):
    if not N%i:
        num.append(i)

if len(num) >K:
    print(num[K-1])
else:
    print(0)
```



### J_2809_약수

```python
'''
20-12-11 16:24-16:38
한개의 정수를 입력받아 입력받은 정수의 약수 모두 출력
이렇게하면 N이 21억개까지라서 시간초과가 난다....
다른 규칙을 찾아야됨
1다음으로 찾은 약수는 N과나눴을때의 수도 약수! 그 수까지만 보면됨!
그리고 작은 수부터 약수를 찾을때마다 N과 나눈 몫도 같이 저장해줌
그러다가 지정된 끝 수까지 가면 멈춤
'''
import sys
input = sys.stdin.readline
N = int(input())
numbers = []
MAX = -1
for i in range(1,N+1):
    if i == MAX or i in numbers:
        break
    if not N%i:
        if i not in numbers and (N//i) not in numbers:
            if i != N//i:
                numbers.append(i)
                numbers.append(N//i)
            else:
                numbers.append(i)
        if MAX == -1:
            MAX = N//i
numbers.sort()
print(*numbers)
```



### J_1658_최대공약수와최소공배수

> **유클리드 호제법(Euclidean algorithm)** : 
>
> A를 B로 나눈 나머지가 r이라면 A와 B의 최대공약수는 B와 r의 최대공약수와 같다. GCD(A, B) = GCD(B, r) 이 원리를 이용하면 두 수의 최대공약수를 간단하게 구할 수 있다. 
>
> 이 방법으로 24과 16의 최대공약수를 구하는 과정을 살펴보면 다음과 같다. 
>
> GCD(30, 18) = GCD(18, 12) = GCD(12, 6) = 6 * 30을 18로 나눈 나머지는 12, 18을 12로 나눈 나머지는 6, 12를 6으로 나눈 나머지는 0이므로, 30과 18의 최대공약수는 12와 6의 최대공약수인 6과 같다. 
>
> 코드2는 유클리드 호제법을 이용하여 최대공약수를 구하는 함수이다. 
>
> 코드3은 같은 내용을 재귀함수를 이용하여 더 간단하게 구현한 것이다. 
>
> 최대공약수나 최소공배수등과 관련된 문제를 해결하기 위해 항상 편리하게 활용할 수 있으므로 잘 익혀두는 것이 좋다.
>
> - 코드2
>
> ```c
> int gcd_get(int x, int y)
> {
>     int r;
>     while (y!=0)   // y 0이면 x가 최대공약수이므로 종료한다.
>     {
>         r = x % y; // 나머지를 구한후
>         x = y; // x를 y로
>         y = r; // y를 r로 바꾸고 다시 반복한다.
>     }
>     return x; // 최대공약수를 리턴한다.
> }
> ```
>
> 
>
> - 코드3
>
> ```c
> int gcd_get(int x, int y)
> {
>     if(y == 0) return x; // y 0이면 x가 최대공약수이다.
>     return gcd_get(y, x % y); // x와 y의 최대공약수는 y와 x % y 의 최대공약수와 같다.
> }
> ```
>
> 

```python
'''
20-12-11 16:40-16:53
두개의 자연수 입력받아 최대공약수, 최소공배수 출력 프로그램
두 수 중에 큰수로 정수를 나누면서 동시에 나누어떨어지는 수 중 큰수로 갱신
두 수의 배수를 한 set에 담아주고 다음 수가 set안에 있으면 최소공배수
'''
N,M = map(int,input().split())
MAX = 0
for i in range(1,max(N,M)+1):
    if not N % i and not M % i:
        if i > MAX:
            MAX = i
print(MAX)

gop = 1
nums=set()
while True:
    nans = N*gop
    mans = M*gop
    if nans not in nums:
        nums.add(nans)
        nans = 0
    if mans not in nums:
        nums.add(mans)
        mans = 0
    if nans:
        print(nans)
        break
    if mans:
        print(mans)
        break
    gop += 1
```

- 다른코드

```python
from math import gcd
def lcm(x,y):
return x * y // gcd(x,y)
a = input()
temp = a.split(' ')
print(gcd(int(temp[0]), int(temp[1])))
print(lcm(int(temp[0]), int(temp[1])))

```



### J_1002_최대공약수와최소공배수

```python
'''
20-12-11 16:55-17:30
n개의 정수를 입력받아서 최대공약수, 최소공배수 구함
최대공약수
첫 두수의 최대공약수를 구한 뒤, 그 수와 다음 수의 최대공약수를 구하는 식으로 진행

최소공배수
두수의 곱을 최대공약수로 나눈것과 같음

첫 번째 수를 최대공약수(gcd)로 정하고 두 번째 수부터 이전까지의 최대공약수(gcd)와 현재 배열의 값(a[i])의 최대공약수를 구하여 다시 gcd에 저장한다.

이러한 작업을 마지막까지 반복하면 모든 수의 최대공약수가 구해진다.

최소공배수도 같은 방법으로 구할 수 있다.
'''
import sys
input = sys.stdin.readline

# 최대공약수구하는 공식 :A를 B로 나눈 나머지가 r이라면 A와 B의 최대공약수는 B와 r의 최대공약수와 같다
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

# N = int(input())
N = 3
# numbers = list(map(int,input().split()))
numbers = [2,8,10]
MAX = numbers[0]
MIN = numbers[0]
for i in range(1,N):
    MAX = gcd(MAX,numbers[i])
    # 최소공배수 = 최대공약수 * 정수1 * 정수2
    MIN = MIN // gcd(MIN,numbers[i]) * numbers[i]
print(MAX,end=' ')
print(MIN)

```



### J_1009_각자리수의역과합

```python
'''
20-12-12 10-10:32 => 정수로 받는다고 돼있으면 정수로 받아야된다...ㅠㅁ
양의 정수를 입력받아 역으로 보여주고 각 숫자의 합을 구하는 프로그램
21억 이해 양의 정수, 새로운 입력을 받다가 0이 입력되면 프로그램 종료
입력받은 수의 역과 각 자리 숫자의 합을 공백으로 구분하여 출력
유효하지 않은 0은 출력하지 않음
'''
import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if not N:
        break
    N = str(N)
    print(int(N[::-1]),end = ' ')
    ans = 0
    for i in N:
        ans += int(i)
    print(ans)
```



### J_2811_소수와합성수

```python
'''
20-12-12 10:34-10:50
소수는 1보다 큰 자연수 중 1과 자기자신만 약수로 갖는 수
합성수는 3개이상 약수
1은 소수도 합성수도 아님
5개의 자연수, 소수, 합성수인지 판단하라

[Hint]
시간을 줄이기 위해 약수를 구할 때 제곱근을 이용해 보자.
a * b = n (a > 1, b> 1)이라 할 때 a와 b는 n의 약수이다.
그러므로 a와 b중 작은 수 쪽만 확인해 보아도 n이 합성수임을 알 수 있는데 작은 수의 범위는 n의 제곱근 이하이다.
작은수가 n의 제곱근보다 클수가 없기 때문!
'''
num=list(map(int,input().split()))
for i in num:
    if i == 1:
        print("number one")
        continue
    for j in range(2,int(i**0.5)+1):
        if not i%j:
            print("composite number")
            break
    else:
        print("prime number")
```





### J_1740_소수

```python
'''
20-12-12 10:51-11:03
자연수 M,N주어짐, M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램
그 범위 내에서 1과 자기자신을 제외한 나머지 수들 사이에 나누어떨어지는것이 있는지 확인
소수가 없다면 -1 출력
'''
M = int(input())
N = int(input())
MIN = 987654321
SUM = 0
for num in range(M,N+1):
    if num ==1:
        continue
    for i in range(2,int(num**0.5)+1):
        if not num % i:
            break
    else:
        if MIN > num:
            MIN = num
        SUM += num
if MIN == 987654321:
    print(-1)
else:
    print(SUM,MIN,sep='\n')
```



### J_1901_소수구하기

```python
'''
20-12-12 11:04-11:48
임의의 값 M에 대하여 M에 가장 가까운 소수를 구하는 프로그램
N : 처리할 수의 개수
M개의 수 list
Mi값에 대해 차이가 가장 작은 소수를 구하여 출력
만약 차이가 같은 소수가 여러개이면 작은수부터 모두 출력 -> M보다 큰수도 봐야되넹..
M까지의 소수 구한 뒤, 차이 가장 적은 값만큼 더한 값만 더 보면 된다

40%에서 시간초과..ㅠ
M과 가까운수부터 보고 MIN찾으면 break, M보다 큰수에서는 작은수부터!
이렇게 하니까 시간초과 안남!!

'''
import sys
input = sys.stdin.readline
def isPrime(a,b):
    global MIN,prime
    if b <=num:
        for p in range(a,b)[::-1]:
            for i in range(2,int(p**0.5)+1):
                if not p % i:
                    break
            else:
                MIN = abs(p-num)
                prime.append(p)
                return
    else:
        for p in range(a,b):
            for i in range(2,int(p**0.5)+1):
                if not p % i:
                    break
            else:
                if MIN > abs(p-num):
                    MIN = abs(p-num)
                    prime = [p]
                elif MIN == abs(p-num):
                    prime.append(p)
                return


N = int(input())
for _ in range(N):
    num = int(input())
    prime = []
    MIN = 987654321
    if num == 1:
        continue
    isPrime(2,num)
    isPrime(num,num+MIN+1)
    # prime.sort()
    print(*prime)

```



### J_2813_소수의개수

> 에라토스테네스체
>
> ```
> [Hint]에라토스테네스의 체
> 에라토스테네스의 체(Eratosthenes' sieve) 에라토스테네스가 일정 범위까지의 소수를 간단하게 구하기 위해 고안한 방법으로
> 자연수를 ‘체’로 쳐서 걸러내고 ‘소수’만 골라내는 방법이라고 해서 에라토스테네스의 체라고 한다.
> 예) 즉, 5보다 작은 수를 곱해서 생기는 5의 배수는 5를 처리하기 이전에 모두 제거가 되었다는 것이다.
> 따라서 5를 처리할 때에는 5의 제곱인 25부터만 처리하면 된다.
> 이렇게 에라토스테네스의 체를 이용하여 어떤 수(N)까지의 소수를 구하기 위해서,
> N의 제곱근까지만 배수를 걸러내는 작업을 하면 되므로 매우 빠른 속도로 소수를 구해 낼 수 있다.
> ```

- 다른사람 코드 보고 품...

```python
def prime_list(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(M, n + 1) if sieve[i] == True]
li = prime_list(N)
cnt = 0
if 1 in li:
    li.remove(1)
    for k in li:
        cnt +=1
        # print(k)
else:
    for _ in prime_list(N):
        cnt += 1
        # print(_)
print(cnt)
```

- 이건 90퍼에서시간초과됨

```python
# 시간초과코드
for num in range(2,int(M**0.5)+1):
    if visit[num]:
        continue
    # 소수를 찾았으니 그 배수들을 표시
    for i in range(num,M//num+1):
        if not visit[i*num]:
            # print(num*i)
            visit[i*num] = True
            # 범위안의 수들 중 합성수를 세어준다, 그런뒤에 M-N+1개 안의 수에서 합성수를 빼주면 소수! 근데도 시간초과..후
            if N<=i*num<=M:
                cnt += 1

# 1은소수도 합성수도 아니니까 빼줌
if N != 1:
    print(M-N-cnt+1)
else:
    print(M-N-cnt)
```

### J_2814_이진수

```python
'''
20-12-13 13:26-13:30
이진수를 입력받아 10진수로 변환하여 출력하는 프로그램 작성
1. 이진수를 입력받는다
2. 뒤에서부터 읽으면서 1이면 2*idx를 해서 더해줌
'''
n = input()
bin=0
for i in range(len(n))[::-1]:
    bin += int(n[i])*2**(len(n)-i-1)
print(bin)
```



### J_1534_10진수를2,8,16진수로

```python
'''
20-12-13 13:31-
10진수를 입력 받아서 2, 8, 16진수로 바꾸어 출력하는 프로그램을 작성하시오.
입력의 첫줄에는 10진수 N(1≤N≤100,000)과 바꿀 진수 B(2, 8, 16)가 공백으로 구분하여 입력된다.
16진수에서 10이상의 수는 순서대로 'A', 'B', 'C', 'D', 'E', 'F'로 나타낸다.

10진수를 n진수로 바꾸는 함수를 만듦
10을 n으로 나눈 나머지를 리스트에 담음
여기서 16진수 일때 10이상이라면 A,B,C,D,E,F로 나타냄
'''
def change(ten,how):
    global result
    if ten == 0:
        return
    if ten%how >= 10:
        result.append(chr(55+ten%how))
    else:
        result.append(ten%how)
    change(ten//how,how)


n,num = map(int,input().split())
result = []
change(n,num)
print(*result[::-1],sep='')
```

### J_3106_진법변환

```python
'''
20-12-13 13:42-14:04
A진법의 수를 입력받아 B진법 수로 출력하는 프로그램
테스트 케이스 끝 0 주어짐
세수 A,N,B가 공백으로 주어짐
A진법 수 N을 B진법수로 변환

1. A진법의 수로 N을 10진수로 만들고, B로 나눈 나머지로 바꿈
'''
def change(num,how):
    global result
    if num == 0:
        return
    if num % how >= 10:
        result.append(chr(num%how+55))
    else:
        result.append(num%how)
    change(num//how,how)

def ten(word,how):
    ans = 0
    for w in range(len(word))[::-1]:
        if word[w].isalpha():
           ans+=(ord(word[w])-55)*how**(len(word)-1-w)
        else:
            ans += int(word[w])*how**(len(word)-1-w)
    return ans

while True:
    info = list(input().split())
    if len(info) == 1:
        break
    A,N,B = int(info[0]),info[1],int(info[2])
    if N=='0':
        print(0)
        continue
    result = []
    change(ten(N,A),B)
    print(*result[::-1],sep='')
```



## 문자열

### J_2604_그릇

```python
'''
20-12-14 18:10-18:25
( 이건 그릇이 바닥에 바로 놓인 모양 ) 는 거꾸로 놓인 모양
( 이거하나당 10cm, ((는 +5cm해서 15cm ()는 +10해서 20cm

1. 그릇을 입력받아 앞에서 부터 읽음
2. 제일 처음 것을 pop해서 모양을 기억하고, ans+=10을 한다
3. 그다음부터 pop하면서 모양이 다르면 +10, 같으면 +5를 한 뒤, 처음값을 다음값으로 바꿔주고 그 다음  값을 pop 반복
'''
bowls = list(input())
# bowls = list('()()()))(')
b = bowls.pop(0)
ans = 10
while bowls:
    next = bowls.pop(0)
    if next == b:
        ans += 5
    else:
        ans += 10
    b = next
print(ans)
```

### J_2514_문자열찾기

```python
'''
20-12-14 18:26-18:37
주어진 문자열, 연속 3개의 문자가 IOI이거나 KOI인 문자열이 각각 몇 개 있는지 찾는 프로그램
1. 문자열을 앞에 3개를 list로 초기값으로 word에 저장 후 IOI or KOI인지 확인
2. 그다음 수를 볼때 word의 앞글자 pop, 다음 문자 뒤에 append,해서 확인 반복
'''
words = list(input())
word = words[:3]
ioi,koi = 0,0
idx = 2
while True:
    # print(''.join(word))
    if ''.join(word) == 'IOI':
        ioi += 1
    elif ''.join(word) == 'KOI':
        koi += 1
    word.pop(0)
    idx+=1
    if idx == len(words):
        break
    word.append(words[idx])

print(koi,ioi,sep='\n')
```

### J_2857_세로읽기

```python
'''
20-12-14 18:38-18:53
1. 글들을 배열로 입력받는다
2. 세로로 읽으면서 만약 빈칸이면 지나감, 계속 읽음
+여기서 제일 긴 줄을 기록한 뒤, 그 MAX만큼 5번 돌림
+ 해당 행에 index가 넘어갔다면 지나감
3. 첫줄부터 입력받은 글들을 붙여서 줄력
'''
words =[list(input()) for _ in range(5)]
MAX = 0
word = []
for x in words:
    if len(x) > MAX:
        MAX = len(x)
for j in range(MAX):
    for i in range(5):
        if j >= len(words[i]):
            continue
        word.append(words[i][j])
print(''.join(word))
```



### J_1880_암호풀기

> 이거 답 나오는데 왜 제출하면 아무것도 안뜰까...ㅠㅠㅠ

```python
'''
20-12-15 15:30-16
26개 알파벳 소문자, 순서대로 복호화 키 대치
암호화된 문자는 대소문자 혹은 공백이 올 수 있고 , 대문자느 ㄴ대문자로, 소문자는 소문자로 치환, 규칙에 맞게 출력 공백은 그대로 출ㄹ력
암호화키, 복호화키 모두 줌
아래 복호화키는 a->e b->y이런식 으로 대치됨
eydbkmiqugjxlvtzpnwohracsf
아래의 문자를 바꿔야됨
Kifq oua zarxa suar bti yaagrj fa xtfgrj
1. 복호화키를 list에 담고
2. 바꿀 문자를 읽으면서 ord() <=90이면 대문자 복호화리스트[ord()-65]을 해서 바꾼뒤 다시 대문자(-32)로 바꿔줌
97>=이면 [ord()-97]을 함
3. 공백은 공백 그대로 넣음
'''
codes = list(input())
secrets = list(input())
words = []
while secrets:
    w = secrets.pop(0)
    if w == " ":
        words.append(w)
    elif ord(w) >= 97:
        ans = codes[ord(w)-97]
        words.append(ans)
    else:
        ans = codes[ord(w)-65]
        words.append(chr(ord(ans)-32))
# print(''.join(words))
print(*words,sep='')
```

- 이렇게 하니까 된다...ㅎ...why..?

```python
codes = input()
secrets = input()
words = []
for w in secrets:
    if w == " ":
        print(w,end='')
    elif ord(w) >= 97:
        ans = codes[ord(w)-97]
        words.append(ans)
        print(ans,end='')
    else:
        ans = codes[ord(w)-65]
        words.append(chr(ord(ans)-32))
        print(chr(ord(ans)-32), end = '')
```





### J_1516_단어세기

```python
'''
20-12-15 16:57-17:11
임의의 문장 입력받아 각 단어별로 나눈 후, 단어들의 중복되는 개수 구하는 프로그램작성
1. 입력된 스트링 글자 제한 없음, 알파벳 , 대소문자 공백, ,등도 입력으로 들어옴
2. 단어사이 구분은 공백
3. 공백을 제외한 모든 문자들이 포함됨

문장 입력받음(문장의 길이 200이하)
하나의 결과가 나온 후에도 계속 새로운 입력을 받다가, END가 입력되면 프로그램 종료(문장의 개수가 30 넘지 않음)
각 문장 단위로 단어들의 발생 빈도를 오름차순(아스키코드순으로 출력)

1. 문장을 입력받는다. 공백을 기준으로 나눔
2. 각 단어들을 키로하는 dict를 만들고, 순서를 센다
3. 아스키코드 순으로 정렬을 한 뒤, 출력

'''
while True:
    result = dict()
    words = list(input().split())
    if ''.join(words) == "END":
        break
    for w in words:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
    resultkey = sorted(result)
    for k in resultkey:
        print(k, ':', result[k])
```



### J_3699_변장

> 안풀림....ㅠ



## 여러가지

### J_1438_색종이(초)

```python
'''
가로 세로 크기 100 정사각형
색종이가 붙은 검은 영역 넓이 구하기
색종이를 좌표에 올려 1로 바꿈
1인것 개수 세기
'''
N = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
for n in range(N):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            ans+=1

print(ans)
```



### J_1671_색종이(중)

```python
'''
가로세로 크기 100도화지
종이 둘레 길이 구하기
색종이를 1로 전부 만들고
상하좌우 dfs돌리면서 범위 벗어나고, 0인것 개수 구하기
'''
import sys
sys.setrecursionlimit(10**8)
#상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]
def dfs(i,j):
    global ans
    visited[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= 100 or nj <0 or nj >= 100:
            ans+=1
            continue
        if visited[ni][nj]:
            continue
        if not arr[ni][nj]:
            ans+=1
            continue
        dfs(ni,nj)

N = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
visited = [[False for j in range(100)] for i in range(100)]
ans = 0
for n in range(N):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1
for i in range(100):
    for j in range(100):
        if arr[i][j] and not visited[i][j]:
            dfs(i,j)
print(ans)
```



### J_1311_카드게임

```python
'''
20-12-17 11:33-13:03
카드 4장, 뽑기 36장중 5장뽑음
R,B,Y,G
점수 규칙
1. 카드 5장 모두 같은색, 숫자가 연속적, 점수는 가장 높은 숫자에 900 더함
2. 카드 5장 중 4장 숫자가 같음, 점수는 같은 숫자에 800을 더함
3. 같은 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을때, 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700더함
4. 5장의 카드 색깔이 모두 같을 댸 점수는 가장 높은 숫자에 600을 더함
5. 카드 5장의 숫자가 연속적일때 점수는 가장 높은 숫자에 500을 더함
6. 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
7.카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때
점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
8. 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다.
9.위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다.
'''
import sys
sys.stdin = open('input.txt','r')
# 같은색개수 return
def samecolor():
    return len(card)

# 숫자가 연속적인지 확인
def continuous():
    for n in range(4):
        if numbers[n] != numbers[n+1] -1:
           return False
    return True

# 같은 수 개수와 숫자
def samenum():
    ans = 0
    MAX = 0
    number = 0
    for n in range(1,10):
        ans = numbers.count(n)
        if ans > MAX:
            MAX = ans
            number = n
    return MAX,number

card = dict()
numbers = []
for _ in range(5):
    a,num = input().split()
    numbers.append(int(num))
    if a not in card:
        card[a] = [int(num)]
    else:
        card[a].append(int(num))
# print(card)
numbers.sort()
result = 0
if continuous():
    # 카드 5장 같은색
    if samecolor() == 1:
        ans = max(numbers)+900
    # 연속적이기만할때
    else:
        ans = max(numbers) + 500
    if result < ans:
        result = ans
if samecolor()==1:
    ans = max(numbers)+600
    if result < ans:
        result = ans
same,samenumber=samenum()
# print(same,samenumber)
if same == 4:
    ans = samenumber + 800
elif same == 3:
    # 나머지2장도 같을때
    check =0
    for n in numbers:
        if n != samenumber and not check:
            check = n
        elif check == n:
            ans = samenumber*10 + check+700
            break
    else:
        ans = samenumber+400
elif same == 2:
    # 또다른 2장이 같을 때
    check,checknum = 0,''
    for n in numbers:
        if n != samenumber and not check:
            checknum = n
            check += 1
        elif n != samenumber and check == 1:
            if checknum == n:
                ans = max(samenumber,checknum)*10 + min(samenumber,checknum) +300
                break
            else:
                checknum = n
    else:
        ans = samenumber + 200
    if result < ans:
        result = ans
else:
    ans = max(numbers) + 100
if result < ans:
    result = ans
print(result)

```



### J_1997_떡먹는호랑이

```python
'''
20-12-17 13:05-13:40
오늘 떡 = 어제 받은 떡의 개수 + 그저께 받은 떡의 개수
호랑이를 만나서 무사히 넘어온 D일째, 떡의 개수 K개
할머니가 호랑이를 처음 만난 날의 떡의 개수A
그 다음날 호랑이에게 준 떡의 개수B 계산

1. for문2개, 마지막전날 개수를 임의로 정하고, 그전날 떡의 개수(K-마지막전날)를 로 정하고 그 전날은 두값의 차 값으로 해서 0일째 0가 되는지 확인
'''
D,K = map(int,input().split())
ans = 0
for a in range(10,K)[::-1]:
    d =D
    A = a
    B = K-A
    d-=2
    flag = False
    while d>=0 and A > B and B > 0:
        next = A-B
        d-=1
        if d == 0:
            print(B,A,sep='\n')
            flag = True
            break
        A = B
        B = next
    if flag:
        break

```



### J_1733_오목

```python
'''
20-12-18 10:05
오목 검정바둑알 1, 흰바둑알 1, 빈자리0, 19줄 19개숫자
가로,세로,대각선, 여섯알 이상 연속적으로 놓인 경우 이긴것아님, 5알이면 이김, 검정흰색 동시에 이기는 경우 엉ㅄ음
검정 이기면1, 흰색 2, 아직 승부가 결정되지 않으면 0
이긴 바둑돌의 가장 왼쪽에 있는 바둑알 출력

1. 0이아닌 수를 만났을때, 가로만 확인, 세로만 확인, 대각선만 확인하는 for문을 만들어 5개면 출력!
각 방문배열을 따로 만듦,
'''
from collections import deque
import sys
sys.stdin = open('input.txt','r')
di = [0,1,1,1] #가로(우),세로(하),대각선(좌하대, 우하대)
dj = [1,0,-1,1]

def check(i,j,color):
    hor.add((i,j))
    ver.add((i,j))
    ldia.add((i,j))
    rdia.add((i,j))
    H,V,R,L = deque(),deque(),deque(),deque()
    H.append((i,j,color))
    V.append((i,j,color))
    R.append((i,j,color))
    L.append((i, j, color))
#     가로
    garo = 1
    ans =[i,j]
    while H:
        pi,pj,pc = H.popleft()
        ni,nj = pi+di[0], pj+dj[0]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in hor:
            break
        garo += 1
        H.append((ni,nj,pc))
        hor.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if garo == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
#     세로
    sero = 1
    ans =[i,j]
    while V:
        pi,pj,pc = V.popleft()
        ni,nj = pi+di[1], pj+dj[1]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in ver:
            break
        sero += 1
        V.append((ni,nj,pc))
        ver.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if sero == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
    # 좌대각선
    ldae = 1
    ans =[i,j]
    while L:
        pi,pj,pc = L.popleft()
        ni,nj = pi+di[2], pj+dj[2]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in ldia:
            break
        ldae += 1
        L.append((ni,nj,pc))
        ldia.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if ldae == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
    # 우대각선
    rdae = 1
    ans =[i,j]
    while R:
        pi,pj,pc = R.popleft()
        ni,nj = pi+di[3], pj+dj[3]
        if ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
        if arr[ni][nj] != pc:
            break
        if (ni,nj) in rdia:
            break
        rdae += 1
        R.append((ni,nj,pc))
        rdia.add((ni,nj))
        if ans[1] > nj:
            ans = [ni,nj]
    if rdae == 5:
        print(arr[i][j])
        print(ans[0]+1,ans[1]+1)
        return True
    return False





arr = [list(map(int,input().split())) for _ in range(19)]
flag = False
hor, ver, ldia, rdia = set(), set(), set(), set()
for i in range(19):
    for j in range(19):
        if arr[i][j]:
            if check(i,j,arr[i][j]):
                flag = True
                break
    if flag:
        break
if not flag:
    print(0)

```

- 다른코드

```python
dr = [-1, 0, 1, 1]  # 우상, 우, 우하, 하
dc = [1, 1, 1, 0]


def checker(r, c, n):
    for d in range(4):
        cnt = 1
        nr = r + dr[d]
        nc = c + dc[d]
        while board[nr][nc] == n:
            cnt += 1
            nr += dr[d]
            nc += dc[d]
        if cnt == 5:
            nr2 = r - dr[d]
            nc2 = c - dc[d]
            if board[nr2][nc2] != n:
                return True
    return False


def omok():
    global ans
    for i in range(1, 20):
        for j in range(1, 20):
            if board[i][j] != 0:
                if checker(i, j, board[i][j]):
                    ans = board[i][j]
                    print(ans)
                    print(i, j)
                    return


board = [[0] * 21]
for _ in range(19):
    board += [[0] + list(map(int, input().split())) + [0]]
board += [[0] * 21]
ans = 0
omok()
if ans == 0:
    print(ans)
```



### J_1761_숫자야구

```python
'''
20-12-18 11:38-12
1~9까지ㅣ 서로 다른 숫자 세개
3개 물어봄, 동일한 자리, 스트라이크, 다른자리 볼
영수가 생각하고 있을 가능성이 있는 답의 개수
1. 1~9까지 3자리를 임의로 만들어서 확인하는데
2. 주어진 조건과 모두 맞는 것의 개수를 구해라
'''
import sys
sys.stdin = open('input.txt','r')
N = int(input())
infos=[]
for _ in range(N):
    infos.append(list(map(int,input().split())))
ans = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or i == k or j ==k :
                continue
            temp = str(100*i+10*j+k)
            for info in infos:
                num,s,b = info
                num = str(num)
                S,B = 0,0
                for n in range(3):
                    if num[n] == temp[n]:
                        S += 1
                    elif int(num[n]) in [i,j,k]:
                        B+= 1
                if S != s or B != b:
                    break
            else:
                ans += 1
                # print(temp,num)
print(ans)
```



### J_1836_연속부분합찾기

```python
'''
20-12-21 12:50-13:17
N개 정수 배열, 가능한 연속 부분합 찾기
연속된 숫자들을 선택해서 합했을떄, 가장 큰 연속 부분합 출력
'''
N = int(input())
arr =list(map(int,input().split()))
dp = [0]*N
dp[0] = arr[0]
for i in range(N-1):
    if arr[i+1] > arr[i+1] + dp[i]:
        dp[i+1] = arr[i+1]
    else:
        dp[i+1] = arr[i+1] + dp[i]
print(max(dp))
```



### J_3427_볼모으기

> 생각보다 너무 오래걸림ㅜ

```python
'''
같은 색의 공을 한곳에 모을 수 있는 최소 횟수
움직이는 색은 한개밖에 없음
1. 각 색 별 idx를 담는다
2. 연속된 수의 개수를 세고 그 수 중 0이나 N-1이 있다면 연속되지 않은 수의 개수만 세고
처음과 끝이 아니라면 모든 수를 세줘야된다 그 중 최소 구하기
'''
def check(arr):
    if 0 not in arr and N-1 not in arr:
        return len(arr)
    cnt =1
    MIN =987654321
    idx = []
    for r in range(1,len(arr)):
        idx.append(arr[r-1])
        if abs(arr[r-1]-arr[r]) == 1:
            cnt += 1
            idx.append(arr[r])
        else:
            cnt = len(arr) - cnt
            if 0 not in idx and N-1 not in idx:
                cnt += len(idx)
            if cnt < MIN:
                MIN = cnt
            cnt = 1
            idx = []
    cnt = len(arr) - cnt
    if 0 not in idx and N - 1 not in idx:
        cnt += len(idx)
    if cnt < MIN:
        MIN = cnt
    return MIN

N = int(input())
arr = list(input())
red = []
blue = []
MIN = 987654321
for i in range(N):
    if arr[i] == 'R':
        red.append(i)
    else:
        blue.append(i)
rcnt = check(red)
bcnt = check(blue)
# print(red,blue)
print(min(rcnt, bcnt))
```

