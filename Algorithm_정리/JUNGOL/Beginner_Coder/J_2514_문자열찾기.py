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