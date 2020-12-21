'''
#실패...
#1.선택정렬 함수를 만듦
#2. 앞일수록 큰숫자!, 제일 큰 수를 찾고 제일 앞과 swap, 뒤로 훑어보면서 더 큰수가 앞에 오게 만들기(횟수만큼)
#3. 만약 더이상 큰 수로 만들수 없는데 횟수는 남았다면 가장 작은 자리 두개를 계속 바꿈, 짝수면 그대로 돌아오고 홀수이더라도 다음 큰수가 됨!

#다시...이번엔 while로 cnt가 0일때까지 돌아가게 만들어보자
#1. numbers를  크기순으로 idx를 list에 담음...그리고 그 순서로 앞으로 swap
#2. 여기서 cnt가 남았는데 이미 큰수라면? 제일작은 오른쪽 끝 두숫자를 계속 바꿈...cnt세줌

#다시... 완탐!!+백트래킹
#1. cnt개수만큼 순열을 돌림!, 거기서 제일 큰 값!......ㅠ

#swap방식으로 순열을 만들어서 세기!!

'''
import sys
sys.stdin = open('input.txt','r')

#순열!
#sel과 numbers를 비교했을 때 달라진거 개수만큼...........
def perm(idx):




T = int(input())
for tc in range(1,5):
    arr = list(input().split())
    numbers = list(map(int,arr[0]))
    N = len(numbers)
    print('numbers',numbers)
    changeNum = int(arr[1])
    MAX = 0
    cnt = 0
    result = []
    perm(0)
    print('#{} {}'.format(tc,MAX))
