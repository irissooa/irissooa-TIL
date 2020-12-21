from pprint import pprint
#2. insert,append사용
arr = [[1,1,1],[1,1,1],[1,1,1]]
#위, 아래 배열에 0으로 채워줌
arr.insert(0,[0]*len(arr[0])) #3을곱한 배열을 0idx에 삽입해서 앞에 0으로 채움
arr.append([0]*len(arr[0])) #뒤에도 마찬가지로 그만큼 삽입
#오른쪽, 왼쪽 idx에도 0으로 채워줌
#for문을 돌면서 각 배열에 앞 뒤로 0삽입
for x in arr:
    #x배열 0idx에 0채우기
    x.insert(0,0)
    #x배열 제일 뒤에 0채우기
    x.append(0)
pprint(arr)