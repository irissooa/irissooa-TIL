def Counting_Sort(A,B,k): #k최대값
    C = [0] * k
    #카운팅
    for i in range(0,len(B)):
        C[A[i]] += 1
    #누적
    for i in range (1,len(C)):
        C[i] += C[i-1] #C[i] = C[i] +C[i-1]
    #소트
    for i in range(len(B)-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
#A[] 입력배열 DATA
#B[] 정렬된 배열 COUNTS
#C[] 카운트배열 TEMP
a = [0,4,1,3,1,2,4,1]#소스
b = [0] *len(a)#결과저장 배열
Counting_Sort(a,b,4+1)
print(a)
print(b)