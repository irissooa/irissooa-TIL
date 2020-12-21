'''
20-12-18 11:38-12
1~9까지ㅣ 서로 다른 숫자 세개
3개 물어봄, 동일한 자리, 스트라이크, 다른자리 볼
영수가 생각하고 있을 가능성이 있는 답의 개수
1. 1~9까지 3자리를 임의로 만들어서 확인하는데
2. 주어진 조건과 모두 맞는 것의 개수를 구해라
'''
import sys
sys.stdin = open('input.txt','r')
N = int(input())
infos=[]
for _ in range(N):
    infos.append(list(map(int,input().split())))
ans = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or i == k or j ==k :
                continue
            temp = str(100*i+10*j+k)
            for info in infos:
                num,s,b = info
                num = str(num)
                S,B = 0,0
                for n in range(3):
                    if num[n] == temp[n]:
                        S += 1
                    elif int(num[n]) in [i,j,k]:
                        B+= 1
                if S != s or B != b:
                    break
            else:
                ans += 1
                # print(temp,num)
print(ans)