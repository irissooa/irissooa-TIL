words = input()
words_upper = ''
for word in words:
    if word.islower():
        words_upper += word.upper() 
    else :
        words_upper += word
print(words_upper)