'''
스페이드 다이아 하트 클로버
1~13번까지 있음
같은 카드 나오면 error
각 카드 몇장이 더 필요한가?

input 받은 값 S01/D02/H03/H04 이런식으로 무늬와 번호가 주어짐
세개씩 잘라서 한 set에 넣어두고, len이 4가 아니라면 error!
'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    c_list ={'S':13,'D':13,'H':13,'C':13}
    card = input()
    card_set = set()
    result = ''
    for i in range(0,len(card)-3+1,3):
        # print(i,'i')
        #3개씩 슬라이싱해서 넣어줌
        card_set.add(card[i:i+3])
    # print(card_set,'set')
        # print(i)
    for c in c_list:
        # print(c,'key')
        if len(card_set) == len(card)//3: #겹치는 카드가 없다면!
            #무늬가 같다면 그 무늬의 value값을 -1함
            for i in range(0,len(card)-3+1,3):
                if card[i] == c:
                # print(card[i],'카드아이')
                    c_list[c] -= 1

        else: #겹치는 카드가 있다면!
            result = 'ERROR'

    #c_list의 value값들을 뽑아줌
    if result != 'ERROR':
        print('#{}'.format(tc),end= ' ')
        for v in c_list:
            print(c_list[v],end =' ')
        print()
    else:
        print('#{} {}'.format(tc,result))


#선생님 풀이
pattern = {'S':0, 'D':1, 'H':2, 'C':3}

T = int(input())

for tc in range(1, T+1):
    line = input()

    card = [[0] * 14 for _ in range(4)]

    #에러인지 아닌지를 위한 bool 변수
    is_error = False

    for i in range(0, len(line), 3):
        #패턴
        card_p = pattern[line[i]]
        #번호
        card_n = int(line[i+1:i+3])

        #이미 가지고 있는 카드라면 종료
        if card[card_p][card_n] == 1:
            is_error = True
            break
        #그게아니라면 카드 표시
        card[card_p][card_n] = 1
        #0인덱스는 카드 카운팅을 위해 사용
        card[card_p][0] += 1

    print("#{}".format(tc), end=" ")
    if is_error:
        print("ERROR")
    else:
        for i in range(4):
            print("{}".format(13-card[i][0]), end=" ")
        print()