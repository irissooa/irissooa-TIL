#N을 입력받고 양세기를 N배수번 하는데 N배수의 자릿수를 한 set()에 넣고 그 set()이 0부터 9까지 들어가면 양세기를 멈추고 gop을 출력
#빈 set()을 만듦
#set()이 0,1,2,3,4,5,6,7,8,9가 되면 멈추는 while문을 만듦
#N배수의 각 자릿수를 set에 넣음
#다 넣으면 1씩 더해서 *1 *2 *3 ..을 해서 set에 0~9가 다 들어갈때까지 반복함

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    num_set = set()
    N = int(input())
    k = 0 #k배
    gop = 0
    sort_set = []
    while True:
        if sort_set == [0,1,2,3,4,5,6,7,8,9]:
            break
        else:
            k += 1
            gop = N * k
            for n in str(gop): #N을 문자로 받고 각 숫자들을 set에 넣는다
                num_set.add(int(n))
            sort_set = sorted(num_set)
    print(f'#{tc} {gop}')

#병훈
for t in range(1, int(input()) + 1):
    N = int(input())
    zero_to_nine = [False] * 10
    count = 1

    while sum(zero_to_nine) != 10:
        N_sheep = N * count
        str_N_sheep = str(N_sheep)

        for n in str_N_sheep:
            zero_to_nine[int(n)] = True

        count += 1

    print(f'#{t} {N_sheep}')
#의수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # str로 바로 받을까 생각했는데 숫자의 연산이 이루어져야 하기 때문에 우선 숫자로 받는다.

    index = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}  # 비교를 하기 위해 인덱스를 설정!
    temp = []  # 빈 리스트 초기화
    step = 0  # 단계 초기화

    while True:
        step += 1  # 몇단계 까지 갈까
        num = N * step  # num = 입력값 * 단계, 여기서 숫자의 연산이 이루어져야 하기 때문에 처음에 N을 인트로 받은것

        num_str = str(num)  # set이랑 비교하기 위해서는 int를  str로 바꿔줘야한다
        temp.extend(num_str)  # temp에 계속 추가하자

        res = set(temp)  # 중복제거하기위해 set을 사용
        if res == index:  # 중복제거한 결과와 인덱스 비교해서 같으면 와일문 탈출
            break
    print(f'#{tc} {num}')