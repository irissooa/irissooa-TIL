import sys
sys.stdin = open('input.txt','r')
# str1과 str2가 주어진다
# str1에 포함된 글자 중 str2에서 가장 많이 나오는 문자의 횟수를 출력
# str1의 글자를 dict의 key로 만들고 그 횟수를 value로 str2를 보면서 횟수를 세어라

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    str_dict = {}
    # str1의 문자를 key로 만들고, str2의 그 key값들의 개수를 세어서 value로 넣어라

    for i in str1:
        cnt = 0
        for j in str2:
            if i==j:
                cnt +=1
            str_dict[i] = cnt
    MAX = 0
    for value in str_dict.values():
        if value > MAX:
            MAX = value
    print('#{} {}'.format(tc,MAX))





#체크배열, 카운트배열
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    check_arr = [0]*26
    count_arr = [0]*26

    #1. str을 순회하면서 알파벳 체크
    for i in str1:
        check_arr[ord(i)-ord('A')] = 1
    #2. 체크된 알파벳의 카운트 세기
    for i in str2:
        if check_arr[ord(i)-65] == 1:
            count_arr[ord(i)-65] += 1
    print('#{} {}'.format(tc, max(count_arr)))


#2방법
    dict = {}
    for i in str1:
        if i not in dict:
            dict[i] = str2.count(i)
    print('#{} {}'.format(tc,max(dict.values())))