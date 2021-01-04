'''
같은 색의 공을 한곳에 모을 수 있는 최소 횟수
움직이는 색은 한개밖에 없음
1. 각 색 별 idx를 담는다
2. 연속된 수의 개수를 세고 그 수 중 0이나 N-1이 있다면 연속되지 않은 수의 개수만 세고
처음과 끝이 아니라면 모든 수를 세줘야된다 그 중 최소 구하기
'''
def check(arr):
    if 0 not in arr and N-1 not in arr:
        return len(arr)
    cnt =1
    MIN =987654321
    idx = []
    for r in range(1,len(arr)):
        idx.append(arr[r-1])
        if abs(arr[r-1]-arr[r]) == 1:
            cnt += 1
            idx.append(arr[r])
        else:
            cnt = len(arr) - cnt
            if 0 not in idx and N-1 not in idx:
                cnt += len(idx)
            if cnt < MIN:
                MIN = cnt
            cnt = 1
            idx = []
    cnt = len(arr) - cnt
    if 0 not in idx and N - 1 not in idx:
        cnt += len(idx)
    if cnt < MIN:
        MIN = cnt
    return MIN

N = int(input())
arr = list(input())
red = []
blue = []
MIN = 987654321
for i in range(N):
    if arr[i] == 'R':
        red.append(i)
    else:
        blue.append(i)
rcnt = check(red)
bcnt = check(blue)
# print(red,blue)
print(min(rcnt, bcnt))