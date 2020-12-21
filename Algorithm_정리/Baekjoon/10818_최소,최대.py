# N=int(input())
# arr = list(map(int,input().split()))
# print(min(arr), max(arr), end=' ')

temp = []
for i in range(9):
    temp.append(int(input()))
print(max(temp))
print(temp.index(max(temp))+1)
