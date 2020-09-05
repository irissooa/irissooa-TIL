# Algorithm

## Magnetic

```python
'''
N극(1) S극(2) 교착상태 개수를 구해라 (1,2)가 붙어있는곳
1은 2를 향해 내려가고 2는 1을 향해 올라감
일단 0을 제외하고 2중배열에 저장
1이 2를 만나기전까지 감, 만약에 없다면 교착0
만난다면 cnt += 1을 해주고 다시 체크 리셋하고 다시감
만약 2가 1을 만나지 않는다면 이거도 교착0
'''
import sys
sys.stdin = open('input.txt','r')
for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    magnetic = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                magnetic.append(arr[i][j])
    # print(magnetic)
    #한 열씩 볼건데! 만약에 1을 만나면 check를 해줌, 그리고 2를 만나게 된다면 cnt += 1
    cnt = 0 # 교착점
    for j in range(N):
        flag = 0 #한열씩 볼거니까 열이 지나가면 flag 리셋
        for i in range(N):
            if arr[i][j] == 1:
                flag = 1
            #1을 만나지 않고 2라면 지나감
            elif flag == 0 and arr[i][j] == 2:
                continue
            #1을 만나고, 2를 만나면 cnt += 1 그리고 flag를 리셋
            elif flag == 1 and arr[i][j] == 2:
                cnt += 1
                flag = 0
    print('#{} {}'.format(tc,cnt))
```



## Contact

- BFS함수 만들 때 q는 선입선출이라 `pop(0)`을 해야되는데 그냥 `pop()`만 해줬다....하ㅠ

```python
'''
BFS로 풀기
연락인원 최대 100명
출발점으로부터 거리가 가장 먼것들 중 큰 숫자를 출력!
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint

def BFS(s):
    #방문표시
    dist[s] = 1
    q = []
    #출발점을 넣어줌
    q.append(s)
    while q:
        p = q.pop(0)
        # print(p,dist[p])
        for j in range(101):
            if contact[p][j] and not dist[j]: #연결되어있고 방문하지 않았다면!
                q.append(j)
                dist[j] = dist[p] + 1 #거리를 더해줌

for tc in range(1,11):
    #데이터의 길이와 시작점 입력받음
    L, S = map(int,input().split())
    #from to from to로 시작점 도착점이 입력받아짐
    arr = list(map(int,input().split()))
    # print(arr)
    #st와 ed를 인접행렬로 표시
    #100은 최대 연락 인원 수이기 때문, idx맞춰주기위해 +1
    contact = [[0]*101 for _ in range(101)]
    for i in range(0,len(arr),2):
        st,ed = arr[i],arr[i+1]
        # print(st,ed)
        contact[st][ed] = 1
    # print(contact[2][15],'컨텍트')
    # pprint(contact)
    #거리를 구함, 노드수만큼
    dist = [0 for j in range(101)]
    BFS(S)
    MAX_idx = 0#최대길이의 node값 저장
    MAX = 0#최대길이
    for d in range(101):
        # print('dist[{}]:{}'.format(d,dist[d]))
        if dist[d] >= MAX:
            MAX = dist[d]
            MAX_idx = d

    print('#{} {}'.format(tc,MAX_idx))
```

