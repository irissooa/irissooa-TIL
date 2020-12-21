'''
1. 첫번째 수 양의 정수 주어짐
2. 두번째 수 양의 정수 중에서 하나를 선택
3. 세번째 이후에 나오는 모든 수 앞의 두 수를 순서대로 빼서 만듦 3=1-2, 4=2-3
4. 음의 정수가 만들어지면, 이 음의 정수를 버리고 더이상 수 만들지 않음
길이가 긴 것 중 하나만 출력
첫번째 부터 수를 a,b,c,d,e라고 했을 때
a-b = c, b-c=d c-d=e, 수를 가장 길게 이어지는 b의 범위를 구해보도록 하자
c>d 이어야 더 길게 이어지므로 a-b>b-c => a-b>b-(a-b)=>2a/3 > b
d>e 이어야 더 길게 이어지므로 b-c > c-d => b-(a-b) > (a-b)-(b-(a-b)) =>2b-a >2a-3b =>b>3a/5
그러므로 두번째 수인 b의 범위는 2a/3 > b > 3a/5이다.
'''
import sys
sys.stdin = open('input.txt','r')

#첫번째 수
F = int(input())
#두번째 수의 범위를 list에 담고 큰 순서대로 돌려서 다음 순서들을 stack에 넣고 가장 긴 것을 출력
# second=[]
# for s in range(2*F//3,3*F//5,-1):
#     second.append(s)
# # print(second)
# #while 문을 돌면서 stack에 수들을 넣을 건데 제일 긴것을 출력
# idx,i = 0,0#넘어갈 second의 idx
# #어떤 수든지 MAX_nums와 같이 4개까지는 나오기 떄문에 초기값으로 줌
# MAX=4#길이 최댓값
# MAX_nums=[F,F,0,F]
# if second:
#     stack=[F,second[0]]
# while idx<len(second):
#     #다음 수는 앞의 두 수를 뺀 것
#     num = stack[i]-stack[i+1]
#     if num >0:
#         stack.append(num)
#         i+=1
#         continue
#     else:
#         if len(stack) > MAX:
#             MAX = len(stack)
#             MAX_nums = [*stack]
#         idx += 1
#         # print(stack,i,idx)
#         if idx == len(second):
#             break
#         stack = [F,second[idx]]
#         i=0
# print(MAX)
# print(*MAX_nums)

#다시풀기.......
'''
내가 생각한 규칙이 틀린 것 같다.
완전탐색으로 다시 풀자
두번째 수는 첫번째수보다 작거나 같다
'''
second = F
MAX_list = []
MAX = 0
stack = [F,second]
i=0
while second >= 0:
    num = stack[i] - stack[i+1]
    if num >=0:
        stack.append(num)
        i+=1
        continue
    else:
        if len(stack) > MAX:
            MAX = len(stack)
            MAX_list = stack
        #다음 second로 넘어가고 초기화
        i = 0
        second -= 1
        stack = [F,second]
print(MAX)
print(*MAX_list)
