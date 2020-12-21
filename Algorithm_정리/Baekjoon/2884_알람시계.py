H=int(input("시 : "))
M=int(input("분 : "))
M=M-45
if M<0:
    M=M+60
    H=H-1
    if H<0:
        H=H+24
print(H,M)