'''
주사위를 쌓는데 겹친 부분의 수가 같으면 됨
그렇게 쭉 쌓았을 때 옆면의 숫자의 합이 최대인 값을 구해라
겹친숫자가 1부터~6일때 모두 구함
그리고 각 경우의 수에서 옆면의 합중 최대값을 구함
옆면은 아래 위만 빼고 하나씩 뽑아서 다 더한 값의 최대값을 구하면 됨
A(0)-F(5) // B(1)-D(3) // C(2)-E(4)
아래 위가 정해지면 옆면들을 list에 담음...그리고 각 하나씩 값을 더해보면 되려나?
주사위 밑면은 1~6으로 6가지 경우의수를 가짐
예) 밑면이 1일때 해당 idx에 마주보는 면의 idx를 제외한 옆면들을 옆면list에 담는다
다음 주사위는 아래 주사위의 윗면과 같은 수의 idx와 해당 idx와 마주보는 idx를 제외하고 옆면 list에 담는다
이거반복....

선생님 풀이보고 힌트
각 idx의 반대면 idx를 만들고
옆면들 중 최대값만 뽑음!
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

#주사위 밑면 idx와 주사위번호를 넣었을 때 그 주사위 옆면의 최고값 반환
def choice(idx,dice_num):
    max_num = 0
    oidx = o_index[idx]
    # print('idx',idx,'oidx',oidx)
    for i in range(6):
        if i == idx or i == oidx:
            continue
        if dice[dice_num][i] > max_num:
            max_num = dice[dice_num][i]
    # print('옆면 max',max_num)
    return max_num

#주사위개수
N = int(input())
dice = []
for _ in range(N):
    arr = list(map(int,input().split()))
    dice.append(arr)
# pprint(dice)
o_index = [5,3,4,1,2,0]

ans = 0
#경우의 수
for num in range(1,7):
    next = num
    temp = 0
    #주사위번호
    for n in range(N):
        #0~5까지의 idx
        for i in range(6):
            if dice[n][i] == next:
                temp += choice(i,n)
                # print(temp)
                next = dice[n][o_index[i]]
                break
    if temp > ans:
        ans = temp
print(ans)