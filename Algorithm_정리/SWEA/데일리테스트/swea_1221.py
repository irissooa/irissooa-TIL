#딕셔너리를 만든다
#키값을 읽고 밸류값 크기를 본뒤 작은 것을 앞으로 옮긴다
import sys
sys.stdin = open("input.txt", "r")


num = {'ZRO':0, 'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}

for tc in range(1,int(input())+1):
    N,M = input().split()
    print(N) ##n뽑기
    VAL = list(map(str,input().split()))
    # for val in VAL: #key값들을 value값으로 변환
    #     # chg_val = num[val]
    for i in range(int(M)-1):
        for j in range(i,int(M)):
            if num[VAL[i]] > num[VAL[j]]: #VAL list에서 뒤에값이 더 작으면 바꿔주고
                VAL[i],VAL[j] = VAL[j],VAL[i]
    STR = ' '.join(VAL)
    print(STR)

#선생님 풀이
num_list = ['ZRO','ONE','THR','FOR','FIV','SIX','SVN','EGT','NIN']
num_dict = {'ZRO':0, 'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
T = int(input())
for tc in range(1,T+1):
    a,b = input().split() #split(' ')이게 디폴트
    arr = list(input().split())
    cnt = [0] * 10 #0~9까지 개수를 세야됨
    for key in arr:
        cnt[num_dict[key]] += 1 #key값으로 value값으로 변환해 cnt리스트의 idx값들에각각 더해줌
    print('#{}'.format(tc))
    for i in range(10):
        print(num_list[i] * cnt[i],end='')
    print()



#정현우오빠
ref = {'ZRO' : 0 , 'ONE' : 1 , 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for tc in range(1,T+1):
    num,N = input().split()
    N = int(N)
    words = list(input().split())
    words = sorted(words, key=lambda x: ref[x])
    print(f'#{tc}' , end = ' ')
    for i in range(N):
        print(words[i], end = ' ')