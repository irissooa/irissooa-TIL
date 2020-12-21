def count():
    tmp = list(map(int,input().split()))
    grade = [0] * 5
    for i in range(1, len(tmp)):
        grade[tmp[i]] += 1

    return grade

def battle():
    if A[4]>B[4]:
        return "A"
    elif A[4] <B[4]:
        return "B"
    else:
        if A[3] >B[3]:
            return "A"
        elif A[3] < B[3]:
            return "B"
        else:
            if A[2] > B[2]:
                return "A"
            elif A[2] < B[2]:
                return "B"
            else:
                if A[1] > B[1]:
                    return "A"
                elif A[1] < B[1]:
                    return "B"
                else:
                    return "D"

N = int(input())

for i in range(N):
    A = count()
    B = count()
    print(battle())


