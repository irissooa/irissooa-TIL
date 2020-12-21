def fact(n): # f(n) = n * f(n-1)
    if n == 1: #basic
        return 1
    else: #inductive(유도)
        return n * fact(n-1)


print(fact(4))

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)