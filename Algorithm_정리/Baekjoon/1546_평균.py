N = int(input())
score = list(map(int,input().split()))
M = max(score)
result = []
for i in score:
    result.append(i/M*100)
print(sum(result)/len(result))
    