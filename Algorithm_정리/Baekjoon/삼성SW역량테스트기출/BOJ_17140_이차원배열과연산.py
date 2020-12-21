'''
23:00
R연산 : 배열의 모든 행에 대해서 정렬 수행, 행의 개수 >= 열의 개수일 때 적용
C연산 : 배열의 모든 열에 대해서 정렬 수행, 행의 개수 < 열의 개수인 경우 적용
각 수가 몇 번 나왔는지, 그 다음 등장 횟수가 커지는 순으로, 여러가지라면 수가 커지는 순으로 정렬 (수,등장횟수)
연산이 끝난 뒤, R ->가장큰행 기준, C->가장 큰 열 기준으로 0이 채워짐
수를 정렬할 떄는 0을 무시해야됨
행 또는 열의 크기가 100을 넘어가면 처음 100개를 제외하고는 버림
100초가 지나도 A[r][c]=k가 안되면 -1출력

1. R연산을 하는 함수 만들기
행의 개수가 열의 개수보다 같거나 클 때  한행당 열을 둘러보면서 (수,개수)를 나열하는데
등장횟수가 적은것부터 나열 만약 횟수가 같다면 수가 작은것부터! 그렇게 크기가 가장 큰 행을 기준으로 0을 붙임
(배열을 읽을때 0은 제외)
2. C연산을 하는 함수는 1과 마찬가지니까 배열을 돌리는 함수 만들기!(zip사용->그냥 함수도 만들어보기)
3. 연산을 계속하면서 행 또는 열의 크기가100을 넘어가면 100개 제외하고 버림
4. 100초가 지나기전까지 A[r][c] = k가 되는 최소값 찾기
'''
import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

#배열돌리는 함수
def rotate(arr):
    temp = [[0 for j in range(len(arr))] for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp[j][i] = arr[i][j]
    return temp

#연산함수
def calc(arr):
    result = []
    MAX_len= 0
    #수를 셈
    for i in range(len(arr)):
        cntNums = [0]*101
        l = 0
        for j in range(len(arr[i])):
            ans = arr[i][j]
            if ans:
                l += 1
                cntNums[ans] += 1
            if l >= 100:
                break
        temp = []
        for k in range(1,101):
            if cntNums[k]:
                temp.append((k,cntNums[k]))
        #적게나온 횟수로정렬, 같다면 수가 큰 순으로 정렬
        temp.sort(key = lambda x:(x[1],x[0]))
        # print(temp)
        #가장 긴것만큼 0을 붙여줘야돼서 수를 세어준다
        if MAX_len < len(temp)*2:
            MAX_len = len(temp)*2
        bin = []
        for i in range(len(temp)):
            bin.extend([temp[i][0],temp[i][1]])
        result.append(bin)
    #0을붙여줌
    # print(MAX_len)
    for i in range(len(result)):
        if len(result[i]) < MAX_len:
            result[i].extend([0]*(MAX_len-len(result[i])))
    # for x in result:
    #     print(x)
    # print('-----돌리기전')
    return result



# 왜 cnt를 return했는데 none값이 나오지??
#arr[r][c] = k값을 차는 함수
def find(arr,i,j,findnum):
    global time
    # print(cnt)
    #찾은지 100초가 넘어가면 끝냄
    if time > 100:
        time = -1
        return
    #행이 열보다 같거나 길다면 R연산, 아니라면 C연산(배열돌린뒤연산)
    if len(arr) >= len(arr[0]):
        result = calc(arr)
        time += 1
        # for x in result:
        #     print('r',x)
    else:
        result = rotate(calc(rotate(arr)))
        time+=1
        # for x in result:
        #     print('c',x)
    # print()
    if len(result) > i and len(result[0]) >j:
        if result[i][j] == findnum:
            return
    find(result,i,j,findnum)


r,c,k = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(3)]
# print('r',r-1,'c',c-1,k)
time=0
if r <= 3 and c <= 3:
    if nums[r-1][c-1] == k:
        print(0)
    else:
        ans = find(nums,r-1,c-1,k)
        print(time)
else:
    ans = find(nums,r-1,c-1,k)
    print(time)