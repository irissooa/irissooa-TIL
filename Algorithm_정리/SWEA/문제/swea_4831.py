import sys
sys.stdin = open("input.txt", "r")

T = int(input())#테스트케이스
for tc in range(1,T+1):
    #K최대이동가능정류장수, N종점정류장, M충전소 개수
    K, N, M = map(int,input().split())
    m_nums = list(map(int,input().split())) #충전소위치
    m_nums += [0,N] #0부터 시작하고 N에서끝남
    m_nums = sorted(m_nums) #정렬해줌
    # print(m_nums)
    cnt = 0
    loc = m_nums[0]

    while True: #위치가 종점
        if loc >= N-K:

            break
        elif loc + K in m_nums: #m_nums의 i위치에서K만큼 이동한 곳에 충전소가있다면 +1
            cnt += 1
            loc = loc +K #m_nums의 위치를 +K한 곳으로 옮겨줌
            # print(cnt)
        elif loc + K not in m_nums:
            #만약에 K만큼 움직인 곳에 충전소가없다면
            #그 움직인 사이 공간에 충전소가 있으면 가장 큰값으로
            #없다면 0을 출력하라
            bin = []
            for num in range(loc+1,loc+K): #idx i와 K만큼 움직인 곳 사이

                if num in m_nums:
                    # cnt += 1
                    # loc = num #위치를 해당 충전소
                    bin.append(num)
            if bin == []:
                cnt = 0
                break
            loc = max(bin)
            cnt += 1

    print(f'#{tc} {cnt}')
                    




