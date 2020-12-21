def fibo(n):
    if n < 2: #basic 기본파트
        return n
    else: #inductive 유도파트
        return fibo(n-1) + fibo(n-2)
    
print(fibo(8))