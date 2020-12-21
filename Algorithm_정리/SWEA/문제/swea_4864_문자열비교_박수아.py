#문자열 비교
#str2안에 str1과 일치하는 부분이 있는지 찾는 프로그램
#두개의 문자열이 주어질 첫 문자열이 두번째에 존재하면 1 존재하지 않으면 0출력

#문자열을 입력받는다
#bruteforce검색방법 이용
#while문 이용
#str1과 str2의 각각의 idx를 넘지 않는 범위에서
#패턴이 다르면 i(str1)를 shift이동
#j를 초기화
#i,j를 1씩 더해주며 비교
#j가 M가지 가게된다면 검색에 성공한것! 1
#아니면 존재하지 않음 0

import sys
sys.stdin = open("input.txt", "r")

def BruteForce(pattern,total):
    i = 0 #str2,t(전체 패턴)의 idx
    j = 0 #str1,p(찾을 패턴)의 idx
    while i < len(total) and j < len(pattern):
        if total[i] != pattern[j]: #패턴이 같지 않다면
            i = i-j # i를 shift이동
            j = -1 #j초기화
        i += 1
        j += 1
    if j == len(pattern):
        return 1 #검색성공
    else:
        return 0 #검색실패

N = int(input())
for tc in range(1,N+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc,BruteForce(str1,str2)))

def check(str1,str2):
    #본문에서 패턴길이를 빼고 +1하여 반복
    for i in range(len(str2)-len(str1)+1):
        #패턴의 길이만큼
        for j in range(len(str1)):
            #만약 현재사이클에 다르다면 브레이크
            if str2[i+j] != str1[j]
                break
        #중간에 브레이크 걸리지 않았다면 완벽히 찾은것
        else:
            return 1
    #완벽히 찾지 못했다면 리턴 0
    return 0

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, check(str1,str2)))

    #2. in활용하여 체크
    if str1 in str2:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,0))


    #3. find 활용
    ans = 0
    if str2.find(str1) != -1:
        ans = 1
    print('#{} {}'.format(tc,ans))

