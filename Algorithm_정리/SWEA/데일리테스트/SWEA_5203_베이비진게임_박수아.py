'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때,
연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
6장의 카드가 run과 triplet으로만 이루어진 것을 babyginㅇ리ㅏ고 함
babygin인지 판단하는 프로그램
여기서는 6장 되기전에 먼저 run이나 triplet이 되는 사람이 승자가됨!
두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램작성
무승부인 경우 0을 출력

#1. babygin인지 체크하는 함수만들기
인자로 준 list를 0~9까지 수를 cnt하고, 같은수가 3개 이상 있는지, 연속하는수 3개이상 있는지 확인

#2. 플레이어 1과 2가 뽑은 카드가 순서대로 list에 append되면서 계속 체크를 함!
#3. 만약에 6장을 채우기 전에 먼저 run이나 triplet이 나오면 승자 출력,
#4. 모두 가져갈때까지 run이나 triplet이 없으면 무승부 0

'''
import sys
sys.stdin = open('input.txt','r')
def check(arr):
    #0~9의수를 세고 담을 cnt배열
    numbers = [0]*10
    for i in arr:
        numbers[i] += 1
    # print(numbers)
    cnt = 0
    for n in range(10):
        #같은 수 3개 이상 있으면 True
        if numbers[n] >= 3:
            return True
        #연속된 수 3개 이상 있으면 True
        if numbers[n]:
            cnt+=1
        else:
            cnt = 0
        if cnt >=3:
            return True
    return False



T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    one= []
    two = []
    #카드를 1과2가 번갈아가면서 뽑음
    for c in range(len(cards)):
        #2가뽑을 카드
        if c %2:
            two.append(cards[c])

        #1이 뽑을 카드
        else:
            one.append(cards[c])

        if check(one):
            print('#{} 1'.format(tc))
            break
        if check(two):
            print('#{} 2'.format(tc))
            break
    #아니라면 무승부! 0 출력력
    else:
        print('#{} 0'.format(tc))

