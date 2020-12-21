#주어진 N길이의 숫자열을 오름차순으로 정렬하여 출력
#N을 입력받는다
#list로 받고, 정렬한 뒤 문자열로 바꿔줌

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr_sorted = sorted(arr)
    str_arr = ''
    for i in arr_sorted:
        str_arr += ' ' + str(i)
    print(f'#{tc}{str_arr}')

#병훈 버블정렬, 선택정렬 이용해서 품....대단해용..
#버블정렬로 푸는법
def bubble_sort():
    for i in range(N - 1):
        for j in range(i + 1, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

for t in range(1,int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    bubble_sort()
    print(f'#{t}',end=' ')
    [print(str(num),end=' ') for num in nums]
    print()

#선택정렬로 푸는법
def selection_sort():
    for i in range(N - 1):
        minIndex = i
        for j in range(i + 1, N):
            if nums[minIndex] > nums[j]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]


for t in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    selection_sort()
    print(f'#{t}', end=' ')
    [print(str(num), end=' ') for num in nums]
    print()