#  SWEA_1221

- 입력받을 값들을 딕셔너리의 key로 만들고 순서를 value값으로 만든다
- 입력받은 list들을 볼건데, VAL[idx]는 num(딕셔너리)의 key값이니 num[key]=value값이 나온다.
- 그 value의 크기를 비교해서 뒤에 값이 앞의 값보다 작으면 앞으로 위치를 이동시키는 `버블정렬`을 이용해 푼다.

```python
#딕셔너리를 만든다
#키값을 읽고 밸류값 크기를 본뒤 작은 것을 앞으로 옮긴다
import sys
sys.stdin = open("input.txt", "r")


num = {'ZRO':0, 'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}

for tc in range(1,int(input())+1):
    N,M = input().split()
    print(N) ##n뽑기
    VAL = list(map(str,input().split()))
    for i in range(int(M)-1):
        for j in range(i,int(M)):
            #버블정렬 VAL list에서 뒤에값이 더 작으면 바꿔주기
            if num[VAL[i]] > num[VAL[j]]: 
                VAL[i],VAL[j] = VAL[j],VAL[i]
    STR = ' '.join(VAL)
    print(STR)
```

- 다른 코드
- `enumerate` : 이터레이터를 순회하면서 이터레이터에서 각 아이템의 인덱스를 얻어오는 간결한 문법을 제공
- range로 루프를 실행하고 시퀀스에 인덱스로 접근하기보다는 enumerate를 사용하는게 좋음
- enumerate에 두 번째 파라미터를 사용하면 세기 시작할 숫자를 지정할 수 있음(기본값0)

```python
#병훈
GNS=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1,int(input())+1):
    tc = input().split()
    words = input().split()
    #입력에 들어있는 GNS 요소 단어들의 수를 나타내는 배열
    number=[0]*10
 
    for word in words:
        for idx,element in enumerate(GNS):
            if element == word:
                #입력에 있는 단어가 어떤 단어인지 확인 후 
                #그 단어 수를 하나 증가
                number[idx]+=1
                break
 
    print(tc[0])
    
    for i in range(10):
        #리스트의 요소들을 cnt만큼 나열
        print((GNS[i]+' ')*number[i],end=' ')
    print()
```

- `sorted(key=lambda x: 식` => 그 식의 값을 기준으로 오름차순으로 정렬
- `sorted(words, key=lambda x: ref[x])` words의 각 인자 x를 `ref[x]`(value값나옴)로 오름차순 정렬함 

```python
#현우
ref = {'ZRO' : 0 , 'ONE' : 1 , 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for tc in range(1,T+1):
    num,N = input().split()
    N = int(N)
    words = list(input().split())
    words = sorted(words, key=lambda x: ref[x])
    print(f'#{tc}' , end = ' ')
    for i in range(N):
        print(words[i], end = ' ')
```

- `chr()` 을 이용해 숫자를 문자로 표현함

```python
#지형
dic={
    'ZRO':0,'0':'ZRO',
    'ONE':1,'1':'ONE',
    'TWO':2,'2':'TWO',
    'THR':3,'3':'THR',
    'FOR':4,'4':'FOR',
    'FIV':5,'5':'FIV',
    'SIX':6,'6':'SIX',
    'SVN':7,'7':'SVN',
    'EGT':8,'8':'EGT',
    'NIN':9,'9':'NIN'
}
T=int(input())
for _ in range(T):
    tc,n=input().split()
    arr=input().split()
    result=[]
    # print(dic[arr[0]])
    for i in range(int(n)):
        result.append(dic[arr[i]])
    result.sort()
    for i in range(int(n)):
        result[i]=dic[chr(result[i]+48)]
    print(tc)
    for num in result:
        print(num,end=' ')
```

- 

```python
#의수
# 딕셔너리로 풀어보자
# input에 #1도 입력받는거 주의하고
# 입력테이터를 리스트로 저장받고
# 딕셔너리의 dict_num[key] = get(key, default) + 1를 이용해서 {'ZRO': 213, 'ONE': 123...}이런식으로 저장되게 한다.
# 출력이 조금 생각할 시간이 필요했다
# #을 포함한 test_case는 일단 받았고
# 다음줄부터 for 문을 이용해 출력을 한다.
# 순서가 없는 dict를 순서대로 출력하기 위해 index_num 이라는 비교데이터를 만들어준다
# 그 후 차례대로 불러오면 끝이겠지
 
 
for tc in range(1, int(input())+1):
    test_case, N = input().split() 
    number_list = list(input().split()) # 입력받자 입력을 받아 
    index_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"] # 비교를 위해 인덱스를 준다.
    dict_num = {} # dict로 풀자
 
    # 딕셔너리의 dict_num[key] = get(key, default) + 1를 이용한 결과 -> {'ZRO': 213, 'ONE': 123...}
    #key가 없을경우 none인데 그 대신에 default값으로 0을 줬당
    #그 key값이 나오면 +1을 해준다(count를 하는거)
    for number in number_list: # 데이터가 들어있는 number_list에서 하나하나꺼내서 확인
        dict_num[number] = dict_num.get(number, 0) + 1 # dict에 값을 저장하자
 
    print(test_case)  # #1을 출력한다
    for i in range(10):
        a = dict_num[index_num[i]] # dict_num의 key 값인 index_num[i] => 순서대로 위의 인덱스를 불러오자,,,
        print(f'{index_num[i]} '*a, end='')
    print() # 테스트 케이스 마다 띄워줘야 하니 추가
```

- 선생님 풀이
- 입력값을 받고 개수를 세서 그만큼 수를 출력시키면 됨

```python
#선생님 풀이
num_list = ['ZRO','ONE','THR','FOR','FIV','SIX','SVN','EGT','NIN']
num_dict = {'ZRO':0, 'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
T = int(input())
for tc in range(1,T+1):
    a,b = input().split() #split(' ')이게 디폴트
    arr = list(input().split())
    cnt = [0] * 10 #0~9까지 개수를 세야됨
    for key in arr:
        cnt[num_dict[key]] += 1 #key값으로 value값으로 변환해 cnt리스트의 idx값들에각각 더해줌
    print('#{}'.format(tc))
    for i in range(10):
        print(num_list[i] * cnt[i],end='')
    print()
```

