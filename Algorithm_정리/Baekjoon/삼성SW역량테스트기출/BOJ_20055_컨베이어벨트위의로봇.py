'''
15:45
로봇이 어떤칸에 올라가거나 이동 -> 내구도 -1
내구도0 -> 로봇갈수 없음
N에 도착하면 로봇은 땅에 내려가야됨
#내구도가 0인것 개수가 K가 되면  stage를 print
#1단계
#arr원소들 한칸씩 미룸,  N번이되면 로봇내려감 오르고 이동하면 내구도-1
#로봇 한칸씩 이동할수있으면 이동 그 다음 장소가 0이거나 로봇이 있으면 안됨
#1번에 로봇이 없으면 올리고 내구도 -1,종료조건인지 확인
#종료조건이 아니라면 다시 단계반복, 몇번째 단계인지 확인
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def move(ans,robot,stage):
    global result
    while True:
        # ans = [0]*2*N
        # print('ans',ans)
        #arr원소를 한칸씩미룸
        # print('로봇이동전',robot)
        # print('벨트이동전',temp)
        # for i in range(2*N):
        #     ans[(i+1)%(2*N)] = temp[i]
        ans.insert(0,ans.pop())

        #로봇도 이동
        for i in range(N-1)[::-1]:
            if robot[i]:
                robot[i+1] = 1
                robot[i] = 0
        if robot[N-1]:
            robot[N-1] = 0
        # print('벨트이동후',ans)
        # print('벨트이동후로봇',robot)
        #로봇이 바뀐 배열이동가능한지 확인하고 1칸씩 이동시킴
        for i in range(N-1)[::-1]:
            if ans[i+1] > 0  and robot[i] and not robot[i+1]:
                robot[i] = 0
                robot[i+1] = 1
                ans[i+1] -=1
            if robot[N-1]:
                robot[N-1] = 0
        # print('로봇이동후',robot)
        # print('이동후벨트',ans)
        #첫번째가 올라갈수있고, 1번에 로봇이 없으면 올림 내구도-1
        if ans[0] and not robot[0]:
            ans[0] -= 1
            robot[0] = 1
            # print('로봇올라감',ans)
            # print('로봇올라감',robot)
        if robot[N-1]:
            robot[N-1] = 0
        cnt = 0
        #내구도 세어줌
        for i in range(2*N):
            if ans[i]<=0:
               cnt += 1
        if cnt >= K:
            result = stage
            return
        stage += 1
        # temp = ans[:]
        # print(stage,'다음단계',temp)




N,K = map(int,input().split())
arr = list(map(int,input().split()))
robotList = [0 for i in range(N)]
# robotList[0]=1
# print(arr)
result= 0
move(arr,robotList,1)
print(result)


