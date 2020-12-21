n=int(input())
numbers = list(map(int,input().split())) #정수로 입력 된 것들을 모아서 리스트로 만듦
numbers.sort() # 정렬/ numbers자체가 바뀜
middle = len(numbers) // 2 #index는 0부터 시작이니 중간값의 idx는 2로 나눈 몫만큼
print(numbers[middle]) 


# T = int(input())

# for test_case in range(1, T + 1):
#     number = input().split() # 여기 EOF오류  Why? input이 반복문을 돌면서 T줄 만큼 있어야되는데 한줄밖에 없어서 에러가남 이럴떈 그냥 한줄자리 받는 코드로 input사용
#     numbers = []
#     for i in number:
#         numbers.append(int(i))
#     numbers.sort()
#     middle = len(numbers) // 2
#     print(numbers[middle]) 
#     Traceback (most recent call last):
#   File "swea_2063.py", line 53, in <module>
#     number = input().split() 
# EOFError: EOF when reading a line

    
    
    