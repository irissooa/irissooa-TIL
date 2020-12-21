def str_rev(str): #매개변수 str과 아래의 지역변수 str은 다른 것
#str->list
	arr = list(str)
#swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
#list->str
	str = "".join(arr)
    return str
 #  ___________
str = 'algorithm'
str1 = str_rev(str)
print(str1)

s='algorithm'
s=s[::-1]
print(S)