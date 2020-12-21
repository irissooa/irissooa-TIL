import sys
sys.stdin = open("input.txt", "r")
P,K=input().split()
password = int(P)-int(K)+1

print(password)