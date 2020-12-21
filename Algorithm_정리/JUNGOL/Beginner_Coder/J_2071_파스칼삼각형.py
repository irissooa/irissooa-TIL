'''
2020-12-10 17:40-18-17
파스칼 삼각형 : 왼쪽 위와 오른쪽 위의 좌표 값을 더해서 값을 갱신해나가는 삼각형
1. 0으로 만든 2*n-1의 2차원배열
2.첫 행 n에 1넣음
3. 1행부터 n-1행까지 보는데 오른쪽 위, 왼쪽위를 더 한값으로 갱신(범위벗어나지않게 0 으로 오,왼 둘러쌈)
4. 출력은 종류에 따라 다름, 그전에 0이 아닌 것들만 따로 담아줌, 각행마다 0이아닌것만
종류 1
1.0이 아닌 그 리스트를 차례로 출력, 한칸 띄워서 출력하면 줄바꿈
종류2
1. 0이아닌 리스트 뒤에서부터 차례로 출력, blank도 1개씩 늘어남
종류3
1.0이아닌 리스트 뒤에서부터 새로운 배열을 만들어서 한 열씩 담아주고 출력
'''
n,m = map(int,input().split())
arr = [[0 for j in range(2*n+1)] for i in range(n)]
arr[0][n] = 1
pascal = [[1]]
for i in range(1,n):
    temp=[]
    for j in range(1,2*n):
        if arr[i-1][j-1] + arr[i-1][j+1]:
            temp.append(arr[i-1][j-1] + arr[i-1][j+1])
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
    pascal.append(temp)
if m ==1:
    for i in pascal:
        print(*i)
elif m ==2:
    blank = 0
    for i in pascal[::-1]:
        print(blank*' ',end='')
        print(*i)
        blank+=1
else:
    temp = [['' for j in range(n)] for i in range(n)]
    idx= 0
    for i in pascal[::-1]:
        # print(i,len(i))
        for j in range(len(i)):
            temp[n-j-1][idx] = i[j]
        idx+=1
    for x in range(n):
        for y in range(n):
            if temp[x][y]:
                print(temp[x][y],end=' ')
        print()