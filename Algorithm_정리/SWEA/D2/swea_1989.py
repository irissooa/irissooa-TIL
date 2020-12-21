#단어를 앞에서 봤을 때랑 뒤부터 봤을때 같다면
#회문 1 출력, 아니라면 0 출력
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,int(input())+1):
    word = input()
    if word[:] == word[::-1]: #word를 그냥 본것과 거꾸로 본 것이 같다면
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')