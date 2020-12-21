def func():
    #값형은 global ans를 적지 않으면 그대로 print(ans)하면 0이 출력됨
    #global ans를 적으면 1이 출력됨
    ans = 1
    # global memo는 참조형이기 때문에 global 적지 않아도 수정가능하지만
    #memo = [1,2,3,4,5] 이렇게 할당을 해버리면 출력을 해도 [1,2,3,4]가 나옴, 이건 global memo를 적어줘야됨
    memo[2] = 10 #이런식으로 적혀있다면 global memo를 적지않아도 수정가능.
ans = 0
memo=[1,2,3,4]
func()

print(ans)