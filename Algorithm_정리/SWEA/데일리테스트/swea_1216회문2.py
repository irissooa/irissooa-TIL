#100X100에 회문이 있는지 확인하고, 회문이 있다면 가징 긴 길이를 출력
#회문인지 판별하는 함수를 만든다
#세로일 때 90도로 돌리는 함수를 만든다
#회문의 길이를 지정하는 함수를 만든다(100에서 작아짐, 진범님 idea)
import sys
sys.stdin = open('input.txt','r')

# def pal_len(arr):
#     for m in range(100,0,-1): #회문의 길이가 100에서부터 줄어든다
#         M = m
#         if palindrome(arr):
#             return M


def palindrome(arr):
    for i in range(100):
        for k in range(100-M+1):
            if arr[i][k:k+M] == arr[i][k:k+M][::-1]: #회문 길이 M만큼 slicing하고 역순이랑 같은지 확인
                return M #같다면 회문의 길이 반환
    return 0 #회문이 아니면 0

def rota90(arr):
    temp = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            temp[j][100-i-1] = arr[i][j]
    return temp

for tc in range(1,11):
    MAX_len = 1 #초기값, 1단어도 회문1
    M = 100 #초기 LEN값, 줄어들예정
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    while M > 0 :#M값은 1~100사이
        if palindrome(arr) or palindrome(rota90(arr)): #가로, 세로 중 값이 true이면 그 값이 최고 회문값
            MAX_len = M
            print('#{} {}'.format(tc,MAX_len))
            break #최고를 찾았으니 멈춤
        else:
            M -= 1 #초기LEN값을 줄여준다


#선생님 코드
def check(M):
    for i in range(N):
        for j in range(N-M+1):
            #가로
            tmp = words[i][j:j+M]

            #세로
            tmp2 = zwords[i][j:j+M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0


for tc in range(10):
    tc_num = int(input())
    N = 100
    words = [list(input()) for _ in range(N)]
    zwords = list(zip(*words)) #2중 리스트이니까 언패킹해서 zip으로 묶어줌(열)

    for k in range(100, 0, -1): #최대 회문 길이를 100부터 봄
        ans = check(k)
        if ans != 0:
            break
    print('#{} {}'.format(tc,ans))