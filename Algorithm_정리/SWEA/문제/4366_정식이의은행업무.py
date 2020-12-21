'''
#1. while문을 돌림,입력받은 2진수, 3진수의 값이 같아지면 break
#2. 2진수, 3진수 둘다 앞은 0이되면 안됨, 그럼 2진수는 2번쨰부터, 3진수는 1,2중 자신이 아닌수부터 바꾸고 확인
#3. 그렇게 계속 자신이 아닌수로 하나씩 바꿔보고 같아지면 끝!
'''
import sys
sys.stdin = open('input.txt','r')
import copy

#2진수 3진수가 같은지 확인하는 함수
def check(numList1,numList2):
    num1 = ''.join(numList1)
    num2 = ''.join(numList2)
    # print(num1,num2)
    if int(num1,2) == int(num2,3):
        return True
    return False


T = int(input())
for tc in range(1,T+1):
    binaryNum = list(input())
    ternaryNum = list(input())
    # print(int(binaryNum,2))
    # print(int(ternaryNum,3))
    BN = copy.deepcopy(binaryNum)
    TN = copy.deepcopy(ternaryNum)
    bidx = 0
    tidx = 0
    flag = False
    while not flag:
        for b in range(bidx,len(binaryNum)):
            if BN[b] == '0':
                BN[b] = '1'
            else:
                BN[b] = '0'
            #해당 idx는 봤으니 다음으로 넘김
            bidx += 1
            #3진수 숫자바꿈
            for t in range(len(ternaryNum)):
                #해당 값은 pop되고 계속 찾을거니까 리셋
                ternaryList=['0','1','2']
                ternaryList.pop(ternaryList.index(TN[t]))
                for tt in range(2):
                    TN[t] = ternaryList[tt]
                    if check(BN,TN):
                        result = ''.join(BN)
                        print('#{} {}'.format(tc, int(result, 2)))
                        flag = True
                        break
                #만약 못찾으면 원래값으로 돌려놓음
                TN[t] = ternaryNum[t]
                if flag:
                    break
            #BN도 만약에 값을 못찾으면 원래값으로 돌려놓음
            BN[b] = binaryNum[b]
            if flag:
                break

