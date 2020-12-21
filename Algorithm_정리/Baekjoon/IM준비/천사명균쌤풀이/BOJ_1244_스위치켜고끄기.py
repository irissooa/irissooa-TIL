def man(num):
    for i in range(1, N + 1):
        if i % num == 0:
            if onoff[i]:
                onoff[i] = 0
            else:
                onoff[i] = 1


def woman(num):
    left = num
    right = num

    while True:
        left -= 1
        right += 1
        if left <= 0 or right > N or onoff[left] != onoff[right]:
            left += 1
            right -= 1
            break

    for i in range(left, right + 1):
        if onoff[i]:
            onoff[i] = 0
        else:
            onoff[i] = 1


N = int(input())

onoff = [0] + list(map(int, input().split()))

H = int(input())
for i in range(H):
    gender, num = map(int, input().split())
    if gender == 1:
        man(num)
    else:
        woman(num)

for i in range(1, N + 1):
    print(onoff[i], end=" ")
    if i % 20 == 0:
        print()
