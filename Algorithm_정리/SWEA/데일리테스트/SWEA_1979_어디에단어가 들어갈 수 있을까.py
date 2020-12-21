#NXN 단어배열 특정 길이 K를 갖는 단어가 들어갈수 있는 자리수를 출력
# 테스트케이스
#N,K입력받음
#배열 입력받음
#가로에 K길이가 들어갈 수 있는지 개수 확인(K랑 길이가 같아야됨. 크면안됨)
#세로(zip사용해보자)에도 K길이가 들어갈 수 있나!
import sys
sys.stdin = open('input.txt','r')

def check(arr):
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else: #0이 나왔을 때 그 길이가 K면 ans를 +1해주고 cnt를 리셋해줌
                if cnt == K:
                    ans += 1
                    cnt = 0
                else:#길이가K가 아니면, cnt를 다시 리셋
                    cnt = 0 #연속된 1의 개수를세야됨
        if cnt == K:
            ans += 1
    return ans

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    #가로
    words = [list(map(int,input().split())) for _ in range(N)]
    # print(words)
    #세로
    z_words = list(zip(*words))
    # print(z_words)
    #가로를 탐색하는 함수를 쓸건데 ans를 return하는 함수만들거야
    result = check(words) + check(z_words)
    print('#{} {}'.format(tc,result))

