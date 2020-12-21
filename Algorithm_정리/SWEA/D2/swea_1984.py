import sys
sys.stdin = open("input.txt", "r")

#10개의 수를 입력받아 그 중 최대의 수와 최소의 수를 제외한 나머지 평균값을 출력하는 프로그램
#소수점 첫째지리에서 반올림

for tc in range(1,int(input())+1):
    arr = list(map(int,input().split()))
    MAX = max(arr)
    MIN = min(arr)
    avg = int(round((sum(arr)-MAX-MIN)/(len(arr)-2),0))
    print(f'#{tc} {avg}')


#병훈
for t in range(1,int(input())+1):
    num = sorted(list(map(int,input().split())))[1:9] #정렬을 해서 제일 큰값,작은값빼기
    print(f'#{t} {round(sum(num)/len(num))}')
