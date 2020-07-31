# Python

- 영화관입장권통합전상망 오픈 API
- 요청 URL xml 또는 json =>우리는 json쓸거니까 xml을 json으로 고치면 됨
- 주소를 복사해서 변수처럼 사용 -> 어디로 데이터를 보내야 되는지의 '어디로'
- URL은 어디로, 요청 parameter은 무엇을.
- 인터페이스
  - 요청인터페이스
    - 요청<->응답
    - key넣어줌(필수,무조건넣기,발급받은 key값)
    - targetDt(문자열 필수, 조회하고자 하는 날짜)
    - URL 안에 key와 targetDt는 필수라 들어가 있음
  - 응답 구조(요청인터페이스와 한쌍)

- url `?`를 기준으로 나눔,  왼쪽은 어디로, 오른쪽은 무엇을?
  - key, targetDt 같은 key와 `=` 뒤의 value로 이루어져있고, 키-벨류 쌍들을 `&`가 이어줌 
  - 더 이어주고 싶다면 `& <원하는 key값> = <value>`로 붙여주면 됨

- `requests` 파이썬 라이브러리 사용

```python
#requests_test// url 구성
import requests #ModulNotFoundError 뜸, bash에 pipinstall requests로 설치를 먼저 해줘야 됨
url = '영화진흥위원회API주소 적음' # ?를 기준으로 자름 앞은 주소, 뒤는 key와 value(?포함 지움, key value는 payload에 넣음)
payload = {'key' : 'value', 'key' : 'value'} #이런식으로 딕셔너리를 만듦
r = requests.get(url, params = payload) #r은 response를 줄여 적은 변수 // params는 파라미터
print(r.url) #지금 만든 url이 보일거야
print(r.text) #url의 data를 보여줌 #type은 str임
print(r.json()) #json data를 해석해줌 #type은 dict
```

- url을 만들어주는 기능(kobis.py)

```python
#kobis.py 여기에 모듈을 만들어줌
class URLMaker:
    url = '' #앞으로 구할 주소의 모든url이 다 공통으로 가진 주소를 복사해서 붙여넣기
    def __init__(self, key): #생성자함수
        self.key = key
        
    def get_url(self, category, feature): #어떤것인지 카테고리를 url뒤에 붙이고, feature도 붙일거야, 이렇게 새로운 url을 만들거야, 그건 json으로 만들거야/?뒤에 key값 = value값 나옴
        return f'{self.url}/{category}/{feature}.json?key={self.key}'
    
url_maker = URLMAker('이데이터가 key인자로 들어감') #url_maker 안의 key값으로 들어감
print(url_maker.key) #key출력
url_maker.get_url('<categroy이름>','<뒤에 올 feature>')
print(url) #완성된 url을 보여줌(공통url+구하고자하는 주소추가)
```

- 예시) problem_1

```python
import requests #이미 pip install 했다는 가정하에 불러옴
from kobis import URLMaker #kobis파일에서 URLMaker을 가져올거야

def sales(): #매출액만 볼건데 어떤 데이터를 가져올지 적고 조건 적어줌
    url_maker = URLMaker('내가 발급받은 key에 대한 정보 넣기') #모듈 인스턴스화
	print(url_maker.key)
	url = url_maker.get_url('원하는카테고리','원하는feature넣기') #새로운 url을 만들었음

	payload = {'targetDt' : '20200730'} #필수 입력 날짜를 적어줘야됨

	r = requests.get(url, params = payload)

	print(r.url) #url이 필수 값을 모두 포함하여 뜸
	print(r) #객체 자체를 출력하면 객체 자체가 응답됐다고 뜸
	print(r.json()) #파이썬에서는 json을 쓸수 없기 떄문에 .json으로 dict로 만듦, 실패를 했다면 뭐가 실패됐다고 친절하게 알려줌 #잘 입력됐다면 data들을 가져옴
 	movie_dict = r.json()
    movies = movies_dict.get('bocOfficeResult').get('dailyBoxOfficeList') #dict key값으로 들어감 #get은 dict의 key값에 접근하는 메소드, 장점: 대괄호를 썼을 때와 다르게 코드가 끊기지 않고 오류없이 진행됨, key가 없다면 None이 뜸, keyerror를 무시하고 넘어갈 수 있다. => list로 뽑아줌
    print(movies)
    
    result = [] #리스트로 가져올까해
    for movie in movies:
        print(movie) #dict 하나씩 출력이 됨
        result.append(movie.get('salesAmt')) #이 값을 가져와 list에 넣어줘
    return result
    
print(sales()) #박스오피스의 매출액만 출력됨    
```

