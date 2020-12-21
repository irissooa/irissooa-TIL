#arr.sort():오름차순 정렬
#arr.sort(reverse = True):내림차순 정렬

#N개의 정수가 주어짐
#제일 앞 가장 큰 수 , 가장 작은수, 2번째 큰수 반복 정렬..
#idx가 짝수이면 내림차순정렬한 aj의 idx를 뽑고, 홀수이면 오름차순정렬한 aj의 idx를 뽑는다.
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    aj = list(map(int,input().split()))
    lis = []
    aj_s = sorted(aj) #오름차순
    aj_b = sorted(aj,reverse = True) #내림차순
    # print(aj_s)
    # print(aj_b)
    for i in range(10): #idx개수만큼 돌거야
        if i % 2 :  #홀수
            lis.append(aj_s[i//2])

        else: #짝수
            lis.append(aj_b[i//2])
    word = ''
    for s in lis:
        word += ' ' + str(s)

    print(f'#{tc}{word}')