num = 456789 #Baby Gin 확인할 6자리 수
c = [0] * 12 #6자리수로부터 각 자리 수를 추출하여 개수를 누적할 리스트 idx넘어서면(+2까지 하는것이 있어서) 오류가 나기때문에 12개로 2개 idx더 첨가함
for i in range(6):
    c[num%10] += 1
    num //= 10
i = 0
tri = run = 0
while i<10:
    if c[i] >= 3: #triplete조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue # 같은것이 반복되면 두번 돌기 때문에 ex_123123 run,triplet둘다 확인하려고
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue

    i +=1

if tri + run == 2 : print('Baby Gin')
else : print('Lose')