'''
병합과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
병합정렬 함수를 만들고, 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우를 세어준다!
result에 정렬한 원소들을 append하면 시간초과!!!
인덱스로 다뤄보자...ㅠㅠ
'''
import sys
sys.stdin = open('input.txt','r')

def mergesort(arr):
    #사이즈가 0이거나 1인 경우, 리턴
    if len(arr) <= 1:
        return arr

    #1. divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # print('left',left,'right',right)
    #리스트의 크기가 1이 될 때까지 mergesort재귀호출
    left = mergesort(left)
    right = mergesort(right)

    # print('left',left,'right',right)
    #2. conquer: 분할된 리스트들 병합
    return merge(left,right)
    
#두개의 분할된 리스트를 병합하여 result를 만듦 -> 처음엔 빈리스트에 append했는데, 그러면 시간초과가남! 
#result는 left와 right의 원소 개수만큼 만들어질거니까 index로 다뤄보자!
def merge(left,right):
    global cnt
    result = [0]*(len(right)+len(left))
    left_idx = 0
    right_idx = 0
    result_idx =0
    #오른쪽,왼쪽 idx벗어나지 않을때까지
    while left_idx < len(left) and right_idx < len(right):
        #left리스트 값보다 right리스트 값이 같거나 클때 그 값을 넣어주고 idx+1
        if left[left_idx] <= right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
            # print('left',result)
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
            # print('right',result)
        #값을 넣었으니 다음 idx로 넘김
        result_idx += 1

    #왼쪽 리스트에 아직 정렬되지 않은 값들이 있을 경우
    #병합과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 셈
    if left_idx < len(left):
        cnt += 1
        result[result_idx:] = left[left_idx:]
    #오른쪽 원소가 남아있을 경우
    else:
        result[result_idx:] = right[right_idx:]
    return result


#병합!
# def merge(left,right):
#     global cnt
#     #두개의 분할된 리스트를 병합하여 result를 만듦 -> 처음엔 빈리스트에 append했는데, 그러면 시간초과가남! 
#     #result는 N개만큼 만들어질거니까 index로 다뤄보자!
#     result = []
#     while len(left) > 0 and len(right) > 0:
#     #right, left리스트에 원소가 남아있을 때까지
#     while len(left) > 0 and len(right) > 0:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
# 
#     #왼쪽 리스트에 원소가 남아있는 경우
#     #병합과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 셈
#     if len(left) > 0:
#         cnt+=1
#         result.extend(left)
#         
#     #오른쪽 리스트에 원소가 남아있는 경우
#     if len(right) > 0:
#         result.extend(right)
#     return result






T= int(input())
for tc in range(1,T+1):
    #정수의 개수
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    ans = mergesort(arr)
    print(ans)
    print('#{} {} {}'.format(tc,ans[N//2],cnt))