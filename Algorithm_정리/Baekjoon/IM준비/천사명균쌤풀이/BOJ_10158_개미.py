def calc(pos, length):
    dir = (pos + t) // length
    idx = (pos + t) % length
    if dir % 2 == 0:
        return idx
    else:
        return length - idx


W, H = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

print(calc(p, W), calc(q, H))
