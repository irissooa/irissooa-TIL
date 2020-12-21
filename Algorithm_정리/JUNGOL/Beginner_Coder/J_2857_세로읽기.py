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