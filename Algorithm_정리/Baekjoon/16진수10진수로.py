'''
01D06079861D79F99F
'''

def binary(num):
    global result,cnt
    if num == 0:
        return result
    result[3-cnt] = str(num%2)
    num //= 2
    cnt+=1
    binary(num)

alpha = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
bit = input()
#16진수는 각자리수를 2진수로 바꿔주면 2진수로 바뀜!!
nums = ''
for b in bit:
    result = ['0']*4
    cnt = 0
    #알파벳은 수로 변환
    if b.isalpha():
        for a in alpha:
            val = alpha[b]
        binary(val)
        nums += ''.join(result)
        continue
    binary(int(b))
    nums += ''.join(result)
for n in range(0,len(nums),7):
    words = nums[n:n+7]
    temp = 0
    for w in range(len(words)):
        word = words[len(words)-w-1]
        if int(word):
            temp += 2**w
    print(temp,end=' ')