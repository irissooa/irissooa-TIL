'''
수열중에서 다음 수가 연속해서 커지는 것 세고
연속해서 작아지는 것 세고
더 긴것 출력
'''
N = int(input())
# N = 6
arr = list(map(int,input().split()))
# arr = [3, 2, 1, 2, 3, 4]
MAX = 1
MIN = 1
len_list = []
for i in range(1,N):
    #다음수가 크거나 같다면
    if arr[i-1] <= arr[i]:
        # print(arr[i])
        MAX += 1
    #작은수가 나오면 0
    else:
        len_list.append(MAX)
        # print(len_list)
        MAX = 1
len_list.append(MAX)
for i in range(1,N):
    #다음수가 더 작은수가 나온다면
    if arr[i-1] >= arr[i]:
        MIN += 1
    else:
        len_list.append(MIN)
        # print(len_list)
        MIN = 1
len_list.append(MIN)
print(max(len_list))

'''
6
3 2 1 2 3 4
'''