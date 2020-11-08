# Algorithm(보충)

> 표준입력

- `input()`: 한줄을 읽어옴

```python
#한줄을 읽어서 정수로 변환
#int() : 정수로 변환
N = int(input())
print(N,type(N))
```

- 한줄을 읽어서 공백으로 구분된 문자를 입력받기
- 한줄 읽고 구분문자로 나눠서 문자로 이뤄진 리스트 반환

```python
#input().split() #split('') default값이 공백임
print(input().split()) #['a','b','c']
```

- 한줄을 읽고 공백으로 구분된 문자 -> 개수가 정해져 있음

```python
N, M = input().split()
print(N,M)
print(type(N),type(M)) #<class 'str'> <class 'str'>
```

- `map(형식,데이터)`: 리스트에 있는 데이터를 형식에 맞춰 변환

```python
N, M = map(int,input().split())
print(N,M) #map은 주소를 출력함...list로 변환시켜줘야됨 list()
print(type(N),type(M)) #<class 'int'> <class 'int'>
```



#### 1차원 배열 입력받기

- 입력을 받네? `input()`
- 공백으로 주네? `.split()`
- 숫자로 변환시켜야되네? `map(int,input().split())`
- list로 변환시키자! `list(map(int,input().split()))`



_____

## 중간값 찾기

- 정렬을 내장함수 사용하지 않고 만들어보기

- 버블정렬

```python
N = int(input())
arr = list(map(int,input().split()))
for i in range(0,N-1):
    for j in range(i+1,N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr) # 정렬된 arr를 볼 수 있음
print(arr[N//2]) #중간값
```

