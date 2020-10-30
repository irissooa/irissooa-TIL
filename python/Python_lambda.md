# Python_lambda

[toc]

## lambda와 map

함수는 입력을 받아 어떤 처리를 한다. 다른 입력으로 함수결과를 보려면 보통 입력을 바꿔서 함수를 다시 호출하는 식이다. 만약 입력이 여러개라면 for문을 돌면서 함수를 여러번 호출을 할 수 있지만 맵(map)을 통하여 좀 더 쉽게 할 수 있다. 즉

```
map(함수, 반복 가능한 자료형)
```

이렇게 사용하면, 입력들(입력 리스트) 만큼 입력을 바꾸면서 함수를 호출할 수 있다. 1에서 5까지 제곱을 구하는 간단한 예제로 살펴보겠습니다. 일반적으로 다음과 같이 코드를 작성할 수 있습니다.

```python
def calc(x):
    return x*x

for i in range(1, 6):
    print(calc(i))
```

함수를 정의하고, for문을 돌면서 입력을 바꿔가며 함수를 호출하는 식이다. 이를 map을 이용하여 입력 개수만큼 함수를 여러 번 호출할 수 있다. 아래와 같이 map의 첫번째 인자에 함수 이름을 넣고, 두번째 인자에는 입력들(입력 리스트)를 지정한다.

```python
def calc(x):
    return x*x

list(map(calc, range(1,6)))
```

람다는 일시적으로 사용하고 버리는 함수라 map의 첫번째 인자에 그냥 람다로 지정하면 된다. 그럼 아래 코드와 같이 한 줄로 간단하게 된다.

```python
list(map(lambda x:x*x, range(1,6)))
```

하나의 입력에 두 개의 인자를 넘기고 싶을 때도 가능하다. 아래 예제인 경우 두 리스트에서 입력값을 하나씩 가지고와서 함수를 호출.

```python
in1 = [1, 3, 5, 7]
in2 = [2, 4, 6, 8]

list(map(lambda x,y:x+y, in1, in2))
```





### 입력을 받는데 사용한 예시

#### 입력받은 수들에 각 0.01곱해서 표시!

> `*map`은 map 객체를 벗겨줌

```python
p=[[*map(lambda x:x*.01,map(int,input().split()))]for _ in range(n)]
```







## Reference

https://tykimos.github.io/2019/12/25/Python_Lambda/