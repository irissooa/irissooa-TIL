import sys
sys.stdin = open("input.txt", "r")

#단어 10개만 공백없이 들어가는 공간이 있다
#입력되는 단어를 공백없이 개수만큼 이어지게 만들어라(10개단위로 끊어야됨)
#2차원 배열로 단어와 수를 str로 받기

for tc in range(1,int(input())+1):
    N = int(input())
    chars = [input().split() for _ in range(N)] #tc하나당 출력할 문자들과 개수 입력받음
    cnt = 0
    print(f'#{tc}')
    #10개씩 cnt를 세고 10개가 되면 print()를 해서 한칸 띄워주기
    for i in range(N): # chars에 들어있는 원소 수만큼 돌아가야됨
        for j in range(int(chars[i][1])): #수가 str로 돼있기 때문에 int를 해줌
            cnt += 1
            print(chars[i][0],end = '')
            if cnt == 10:#cnt가 10이 되면 print()로 한줄 띄우고cnt리셋
                print()
                cnt = 0
    print() #tc끼리는 구분돼야되기 때문


# #병훈
for t in range(1,int(input())+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    count = 0
    print(f'#{t}')
    for i in range(N):
        for j in range(int(arr[i][1])):
            print(arr[i][0],end='')
            count +=1
            if count==10:
                count =0
                print()
                continue
    print()

#의수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lists = [[str(x) for x in input().split()] for _ in
             range(N)]  # N개의 알파뱃을 2차원 배열 스트링형태로 저장 ex) [['A', '3'], ['B', '2']]
    tmp = []
    for i in range(N):
        tmp.extend(lists[i][0] * int(lists[i][1]))  # tmp = ['A', 'A', 'A', 'B', 'B']

    print(f'#{tc}')
    for x in range(len(tmp) // 10 + 1):  # tmp만들어진 것의 길이를 10로 나눈 몫의 수만큼 for문 반복
        res = tmp[10 * x:10 * (x + 1)]  # tmp를 10개씩 슬리이싱한다.
        res = ''.join(res)  # 리스트 10개를 join함수로 합친다
        print(res)  # 한줄 출력