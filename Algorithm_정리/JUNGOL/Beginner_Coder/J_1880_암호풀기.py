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
# print(*words,sep='')
for w in words:
    print(w,end='')