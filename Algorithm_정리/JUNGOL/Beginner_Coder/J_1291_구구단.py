'''
구간의 처음과 끝을 입력받고
입력된 구간은 항상 처음이 작은건 아님
증가하거나 감소하는 순서 그대로 출력
'''
import sys
input = sys.stdin.readline

while True:
    s,e = map(int,input().split())
    if s <2 or s>9 or e <2 or e >9:
        print('INPUT ERROR!')
        continue
    else:
        break
if s <= e:
    for i in range(1,10):
        start = s
        while start<=e:
            if start*i<10:
                print('{} * {} =  {}'.format(start,i,start*i),end='   ')
            else:
                print('{} * {} = {}'.format(start,i,start*i),end='   ')
            start+=1
        print()
else:
    for i in range(1,10):
        start = s
        while start >= e:
            if start*i < 10:
                print('{} * {} =  {}'.format(start,i,start*i),end='   ')
            else:
                print('{} * {} = {}'.format(start,i,start*i),end='   ')
            start -=1
        print()