'''
2020-12-11 16:07-16:10
세자리수 x 세자리수 곱하기
1. 2번째 수의 1의자리와 1번째수의 곱하기
2. 10의자리와 1번쨰수곱하기
3. 백의 자리와 1번째수 곱하기
4. 1 + 10*2 + 100*3 한 값 구하기
'''
first = int(input())
second = input()

third = first * int(second[2])
fourth = first * int(second[1])
fifth = first * int(second[0])

sixth = third + fourth* 10 + fifth * 100
print(third)
print(fourth)
print(fifth)
print(sixth)
