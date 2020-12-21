N = int(input())
# for i in range(1,2*N):
#     if i <= (2*N)//2:#
#         print('*'*i)
#     else:
#         print('*'*(2*N-i))
star = N*2-1
for i in range(star):
    if i <= N-1:
        print(' '*i + '*'*(star-2*i)+ ' '*i)
    else:
        print(' '*(star-i-1) + '*'*(2*(i+1)-star) + ' '*(star-i-1))