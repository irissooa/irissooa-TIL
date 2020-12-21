import sys
sys.stdin = open('input.txt','r')

words = input()
# print(len(words))
idx =0
q = []
ans = []

while True:
    if idx >= len(words):
        ans = ans + q[::-1]
        break
    #태그를 만나면 닫을때까지 q에담고 q를 그대로 ans에 담아줌
    if words[idx] == '<':
        if q:
            ans = ans + q[::-1]
            q= []
        while True:
            q.append(words[idx])
            if words[idx] == '>':
                ans += q
                q = []
                idx+=1
                break
            idx += 1
    #문자열
    else:
        if q == [' '] or words[idx] == ' ':
            ans = ans + q[::-1]
            q = []

        q.append(words[idx])
        idx+=1
print(''.join(ans))
print(len(ans))

## 다른사람코드....대박
a=input()
b=a.replace('>','<').split('<')
print(b)
s=""
for i in range(len(b)):
  if i%2:
      s+='<'+b[i]+'>'
  else:
    c=b[i].split()
    print('c',c)
    s+=' '.join([d[::-1] for d in c])
    print('s',s)
print(s)