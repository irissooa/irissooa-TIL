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