'''

'''
import sys
sys.stdin = open('input.txt','r')

def binarySearch(arr,key):
    start = 0
    end = len(arr)-1
    left = False
    right = False
    while start <= end:
        # middle = start + (end-start) // 2
        middle = (start + end) // 2
        #검색 성공
        if key == arr[middle]:
            # print('middle','key',key,'middle_idx',middle,'middle값',arr[middle])
            return True
        elif not left and key < arr[middle]:
            end = middle-1
            # print('left','key',key,'middle_idx',middle,'middle값',arr[middle])
            left = True
            right = False
        #arr[middle] < key
        elif not right and arr[middle] < key:
            start = middle + 1
            # print('right','key',key,'middle_idx',middle,'middle값',arr[middle])
            right = True
            left = False
        #같은곳에 또 갔으니까 끝!
        else:
            # print('key',key,'같은곳갔어!!')
            return False
    #검색실패
    return False

T = int(input())
for tc in range(1,T+1):
    #A,B에 속한 정수의 개수 N,M
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    # print('A',A,'B',B)
    #B에 속한 어떤 수가 A에 들어있는 값이면서, 양쪽구간 번갈아 나타나는 숫자 개수
    cnt = 0
    for b in range(M):
        if binarySearch(A,B[b]):
            cnt += 1
            # print(B[b],'cnt',cnt)
    print('#{} {}'.format(tc,cnt))