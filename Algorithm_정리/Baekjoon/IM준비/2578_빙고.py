'''
25개 칸 빙고
사회자가 부르는 수 차례로 지워감
만약 가로,세로, 대각선 줄이 다 지워진 것이 3개이상 있다면 빙고!
사회자가 몇번쨰수를 부른 후 빙고를 외치는가
사회자가 부른 수를 0으로 바꿈!
for문을 돌면서 i가 같은데 다 0 이거나, j가 같은데 전부 0이거나, i==j인데 전부 0이거나, i==4-j 인데 전부0인것이
3개이상 있다면 빙고!
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

def check(arr):
    cnt = 0
    # pprint(bingo)
    #가로
    for i in range(5):
        garo = 0
        for j in range(5):
            if arr[i][j] == 0:
                # print('garo')
                garo+=1
            else:
                break
        if garo == 5:
            cnt+=1
            # break

    #세로
    for j in range(5):
        sero = 0
        for i in range(5):
            if arr[i][j] == 0:
                # print('sero')
                sero += 1
            else:
                break
        if sero == 5:
            cnt += 1
            # break

    #대각선
    r_line = 0
    l_line = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                if arr[i][j] == 0:
                    r_line += 1
                    # print('오른대각')
            if i == 4-j:
                if arr[i][j]==0:
                    l_line += 1
                    # print('왼대각')

    if r_line == 5:
        cnt += 1
    if l_line == 5:
        cnt += 1
    # print('cnt',cnt)
    if cnt >=3:
        # print('??')
        return True
    else:
        return False

def BINGO(bingo):
    idx= 0
    while idx < 25:
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == nums[idx]:
                    bingo[i][j] = 0
                    # print(i,j)
                    if check(bingo):
                        return idx
                    idx += 1
                    # print('idx',idx)

bingo = [list(map(int,input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums.extend(list(map(int,input().split())))

# pprint(bingo)
print(BINGO(bingo)+1)

