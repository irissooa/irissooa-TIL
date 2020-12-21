'''
N개의 숫자로 이루어진수열, 맨앞의 숫자를 맨 뒤로 보내는 작업 M번
수열의 맨 앞에 있는 숫자를 출력
'''
import sys
sys. stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #M은 최대 1000
    arr= list(map(int,input().split()))

    #선형큐일경우(파이썬제외) 뒤에 M번 만큼 추가할 리스트를 추가해줘야됨
    arr= list(map(int,input().split())) + ([0] * M)
    f,r = -1,N-1
    for _ in range(M):
        f += 1 #arr[f]
        r += 1
        arr[r] = arr[f]
    print(arr[f+1])

    #원형큐일경우
    arr= [0] +list(map(int,input().split()))
    f,r = 0,N
    SIZE = N+1
    for _ in range(M):
        f = (f+1) % SIZE
        r = (r+1) % SIZE
        arr[r] = arr[f]
    print(arr[(f+1) % SIZE])

    #아래 식을 안쓰고 M % N의 idx값을 넣어도 답을 구할 수 있음
    # print('#{} {}'.format(tc,arr[M % N]))

    #M번 작업을 진행, 맨앞의 숫자를 pop하고, 그 숫자를 제일 뒤에 붙임
    for i in range(M):
        arr.append(arr.pop(0))
    print('#{} {}'.format(tc,arr[0]))
