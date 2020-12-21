# #을 출력할건데 순서대로 #이 나오고 나머지는 +
s = ['+','+','+','+','+']
for i in range(len(s)):
    s[i] = '#'
    print(''.join(s))
    s[i] = '+'