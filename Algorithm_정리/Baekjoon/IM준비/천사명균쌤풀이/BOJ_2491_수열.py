def check(nums):
    global ans
    cnt = 1
    for i in range(1, N):
        if nums[i-1] <= nums[i]: cnt+=1
        else: cnt = 1

        if ans < cnt : ans = cnt


N = int(input())
arr = list(map(int, input().split()))

ans = 1

check(arr)
check(arr[::-1])
print(ans)
