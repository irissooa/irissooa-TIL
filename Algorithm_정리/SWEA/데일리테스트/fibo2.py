def fibo2(n):
    # global memo #꼭써야되나요? 안써도됨!! why? memo가 전역변수인데 참조형이다
    if n >= 2 and len(memo) <= n: #len(memo)는 list가 구해졌나 아닌가를 확인하는 것, ㄱ계산되어 있으니 확인 안해도  된다는 것을 알려줌
        memo.append(fibo2(n-1)+fibo2(n-2))
    return memo[n]

memo = [0,1] #참조형, read, write 다 됨,
# ans = 0 #이런 값형은 read밖에 안됨, global 써야됨
print(fibo2(1000))