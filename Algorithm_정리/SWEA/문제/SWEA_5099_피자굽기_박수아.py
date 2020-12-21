'''
N개의 피자를 동시에 구울 수 있는 화덕이 있음
피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다
1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣음
치즈의 양에 따라 녹는 시간이 다름 꺼내지는 순서는 바뀔수 있음
화덕에 가장 마지막까지 남아있는 피자 번호를 알아내라

피자는 1번 위치에서 넣거나 뺄 수 없음
화덕 내부의 피자받침은 천천히 회전, 1번에서 잠시 꺼내
치즈를 확인하고 다시 같은 자리에 넣을 수 있음
M개의 피자에 처음 뿌려진 치즈의 양이 주어짐
화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어듦
이전 치즈의 양을 C라고 하면 다시

다시 풀어보기...
'''

for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) #N:화덕의 크기 M:피자수
    #피자번호와 idx번호를 맞추기 위해 앞에 0을 추가함
    pizza = [0] + list(map(int,input().split())) #치즈양
    #화덕(q처럼 사용할 예정), 피자번호를 저장함
    oven = [i for i in range(1,N+1)] #피자번호
    pos = N+1 #추가될 남은 피자 초기값(M개중에 오븐에 N개들어가고 남은 것 시작 점)

    while len(oven) > 1: #한개가 되면 pop해서 없앨거야
        num = oven.pop(0)
        pizza[num] = pizza[num] // 2 #치즈양 한바퀴,반으로 줄어듦
        if pizza[num]: #0이 아님
            oven.append(num)
        else: #0이면 새로운 피자 집어넣음
            if pos <= M: #M까지만 넣고 넘으면 추가안함
                oven.append(pos)
                pos += 1 #다음번호를 가리키게 함
    print('#{} {}'.format(tc,oven[0]))

#방법2
for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) #N:화덕의 크기 M:피자수
    #피자번호와 idx번호를 맞추기 위해 앞에 0을 추가함
    pizza = [0] + list(map(int,input().split())) #치즈양
    #번호랑 치즈양을 묶어서넣어줌
    oven = [[i,pizza[i]] for i in range(1,N+1)] #피자번호
    #남은 피자
    remain = [[i,pizza[i]] for i in range(N+1,M)]
    pos = N+1 #추가될 남은 피자 초기값(M개중에 오븐에 N개들어가고 남은 것 시작 점)

    while len(oven) > 1: #한개가 되면 pop해서 없앨거야
        num, cheeze = oven.pop(0)
        cheeze = cheeze // 2 #치즈양 한바퀴,반으로 줄어듦
        if cheeze: #0이 아님
            oven.append(num,cheeze)
        else: #0이면 새로운 피자 집어넣음
            if remain: #M까지만 넣고 넘으면 추가안함
                oven.append(remain.pop(0))
    print('#{} {}'.format(tc,oven[0]))
