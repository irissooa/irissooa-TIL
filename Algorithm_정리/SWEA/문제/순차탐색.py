#정렬되지 않은 경우
# def seq_search(a,n,key):
#     i = 0
#     while i < n and a[i] != key: #i는 n보다 작고 key값과 같지 않으면 끝남
#         i += 1
#     if i < n : return i
#     else : return -1 #못찾으면 -1 false를 의미
#
#
# arr = [4,9,11,23,2,19,7]
# key = 233
# print(seq_search(arr,len(arr),key))

#정렬된경우
def seq_search(a,n,key):
    i = 0
    while i < n and a[i] < key: #i는 n보다 작고 key값보다 작으면 끝남
        i += 1
    if i < n and a[i]==key : return i
    else : return -1 #못찾으면 -1 false를 의미


arr = [1,2,3,4,5,6,7,8,9]
key = 3
print(seq_search(arr,len(arr),key))