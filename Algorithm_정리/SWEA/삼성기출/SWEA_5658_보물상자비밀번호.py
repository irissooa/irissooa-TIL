'''
2020-12-03 18:10
각 변에 16진수 숫자가 적혀있는 보물상자가 있다
보물상자 뚜껑은 시계방향으로 돌릴 수 있고, 한번 돌릴 때마다 숫자가 시계방향으로 한칸씩 회전
각 변에 동일한 개수 숫자가 있고, 시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수를 나타냄
보물상자에 자물쇠가 걸려있는데
이 자물쇠의 비밀번호는 보물상자에 적힌 수로 만들 수 있는 모든 수 중 K번째로 큰 수->10진수로 만든 수
N개의 숫자가 입력으로 주어짐, 보물상자의 비밀번호 출력
서로 다른 회전 횟수에서 동일한 수가 중복으로 생성될 수 있다
크기 순서를 셀 떄 같은 수를 중복으로 세지 않기

N//4만큼 numbers를 자르는데 한칸씩 옮겨가며 계속 그 구간내에서 나올 수 있는 16진수를 10진수로 바꿔서 list에 저장(중복안됨)
N//4번 회전하면 같으니까 끝!
만든 list 큰수대로 정렬한 뒤, K번째 수 출력
'''
import sys
sys.stdin = open('input.txt','r')
alpha = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def calc(number):
    global numlist
    ans = 0
    nidx = 0
    for n in number[::-1]:
        if n.isalpha():
           ans += alpha[n]*(16**nidx)
        else:
            ans += int(n)*(16**nidx)
        # print(n,ans)
        nidx += 1
    for a,n in numlist:
        if num == n:
            return
    numlist.append([ans,num])
    # print(ans)
    return


T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    numbers = input()
    cnt = 0
    idx=0
    numlist = []
    # print(numbers)
    M = N//4
    while cnt < M:
        for i in range(0,N,M):
            if (i+idx+M)%N > (i+idx)%N:
                num = numbers[(i+idx)%N:(i+idx+M)%N]
            else:
                num = numbers[(i+idx)%N:]+numbers[:(i+idx+M)%N]
            # print(idx,i,N,(i+idx)%N,(i+idx+M)%N,num)
            # print(N,M,len(num),'길이이',num)
            calc(num)
        idx += 1
        cnt += 1
    numlist.sort(reverse=True)
    # print(numlist,K)
    print('#{} {}'.format(tc,numlist[K-1][0]))